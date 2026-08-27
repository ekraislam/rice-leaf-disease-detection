"""
RiceGuard Senior AI Agronomist & Botanical Intelligence Engine
Supports Live Google Gemini API Integration with a 50-Year Expert Fallback System.
Author: Designed & Developed by Ohi
"""

import os
import re
import json
import urllib.request
import urllib.parse
from src.disease_data import DISEASE_DATABASE
from src.tts_engine import clean_text_for_speech


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY", "").strip()


def is_meaningful_query(text: str) -> bool:
    if not text:
        return False
    cleaned = re.sub(r'[\s\.,\/#!$%\^&\*;:{}=\-_`~()?"\'<>+\|\\\[\]]', '', text)
    if len(cleaned) < 2:
        return False
    if len(set(cleaned)) == 1 and len(cleaned) > 2:
        return False
    return True


def call_gemini_api(message: str, lang: str = "bn", current_disease: str = None, current_confidence: float = None) -> dict:
    if not GEMINI_API_KEY:
        return None

    context_info = ""
    if current_disease:
        context_info = f"\n[DIAGNOSTIC CONTEXT]: The user currently uploaded a rice leaf photo. RiceGuard AI ResNet18 model diagnosed: '{current_disease}' with {current_confidence or 95}% confidence."

    system_instruction = (
        "You are 'RiceGuard AI Senior Agronomist' (রাইসগার্ড এআই ফসল বিশেষজ্ঞ), a world-class agricultural AI developed by Ohi. "
        "Your mission is to provide accurate, practical, and scientifically verified advice to rice farmers and agronomists in Bangladesh and worldwide. "
        "You have deep expertise in rice diseases (ব্লাস্ট, পাতা পোড়া, বাদামী দাগ, খোল পোড়া, ইত্যাদি), insect pests (মাজরা, পামরী, কারেন্ট পোকা), "
        "balanced fertilizers (ইউরিয়া, টিএসপি, এমওপি, জিংক), AWD irrigation, and Bangladesh Rice Research Institute (BRRI) & DAE guidelines.\n\n"
        "Guidelines:\n"
        "1. If the user asks in Bengali, reply in clear, professional, farmer-friendly Bengali. If in English, reply in English.\n"
        "2. Structure your reply nicely with emojis (🌾, 🧪, 🐛, 💧, 🌦️), bold headings, and clear bullet points for symptoms, chemical fungicides/insecticides with exact dosages, and field management.\n"
        "3. Provide exact dosages (e.g., 'ট্রাইসাইক্লাজল ৭৫ ডব্লিউপি প্রতি লিটার পানিতে ০.৭৫ গ্রাম' or 'Nativo @ 0.6 g/L').\n"
        "4. Always remind farmers to avoid spraying before rain and to suspend top-dressing Urea if blast or blight is active.\n"
        "5. Keep the total reply concise (around 100-180 words) so it is easy to read and listen to on mobile."
        + context_info
    )

    prompt = f"{system_instruction}\n\nUser Question: {message}\n\nPlease respond in {'Bengali (বাংলা)' if lang == 'bn' else 'English'}."

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 450,
            "topP": 0.95
        }
    }

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=req_data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            res_json = json.loads(response.read().decode("utf-8"))
            candidates = res_json.get("candidates", [])
            if candidates:
                raw_text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                if raw_text:
                    html_text = raw_text.replace("\n\n", "<br/><br/>").replace("\n", "<br/>")
                    html_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_text)
                    html_text = re.sub(r'\*\*(.*?)\*\*', r'<em>\1</em>', html_text)
                    html_text = re.sub(r'•\s*', r'• ', html_text)

                    clean_spoken = clean_text_for_speech(html_text, is_bn=(lang == "bn"))

                    return {
                        "source": "gemini",
                        "html": html_text,
                        "text_bn": clean_spoken if lang == "bn" else clean_text_for_speech(html_text, is_bn=True),
                        "text_en": clean_spoken if lang == "en" else clean_text_for_speech(html_text, is_bn=False)
                    }
    except Exception as e:
        print(f"[RiceGuard AI] Gemini API request failed ({e}), switching to 50-Year Expert Local Engine.")
        return None


def get_expert_local_response(query: str, lang: str = "bn", current_disease: str = None, current_confidence: float = None) -> dict:
    is_bn = (lang == "bn")
    q = query.lower().strip()

    # 0. Check for empty or gibberish non-meaningful queries
    if not is_meaningful_query(query):
        html_bn = (
            "🌾 <strong>নমস্কার!</strong><br/><br/>"
            "আপনার প্রশ্নটি স্পষ্ট বোঝা যায়নি। অনুগ্রহ করে ধানের কোনো নির্দিষ্ট রোগ (যেমন: <em>ব্লাস্ট, পাতা পোড়া, বাদামী দাগ, খোল পোড়া</em>), "
            "বালাইনাশকের নাম, সারের সঠিক ডোজ বা মাঠ পরিচর্যা নিয়ে প্রশ্ন লিখুন অথবা নিচের কুইক বাটনে চাপ দিন।"
        )
        html_en = (
            "🌾 <strong>Hello!</strong><br/><br/>"
            "Your query is not clear. Please type a specific question about rice diseases (e.g. <em>Blast, Blight, Brown Spot, Hispa</em>), "
            "fertilizer dosage, spraying weather, or field care."
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 1. Contextual Match: Questions about currently analyzed disease
    if current_disease and current_disease in DISEASE_DATABASE and any(w in q for w in ['বর্তমান', 'এই রোগ', 'প্রেসক্রিপশন', 'চিকিৎসা', 'ওষুধ', 'ডোজ', 'current', 'this disease', 'rx', 'treatment', 'medicine']):
        d_info = DISEASE_DATABASE[current_disease]
        d_name_bn = d_info.get("name_bn", current_disease)
        d_name_en = d_info.get("name_en", current_disease)
        chem_bn = d_info.get("management_bn", {}).get("chemical", "প্রয়োজন নেই")
        chem_en = d_info.get("management_en", {}).get("chemical", "None required")
        cult_bn = d_info.get("management_bn", {}).get("cultural", "সুষম সেচ বজায় রাখুন।")
        cult_en = d_info.get("management_en", {}).get("cultural", "Maintain balanced irrigation.")
        sev_bn = d_info.get("severity_bn", "সতর্কতা")
        sev_en = d_info.get("severity_en", "Caution")

        html_bn = (
            f"🌿 <strong>শনাক্তকৃত রোগ: {d_name_bn} ({sev_bn})</strong><br/><br/>"
            f"💊 <strong>রাসায়নিক প্রতিকার:</strong> {chem_bn}<br/><br/>"
            f"🌱 <strong>মাঠ পরিচর্যা:</strong> {cult_bn}<br/><br/>"
            f"💡 <em>ডোজ ক্যালকুলেটর দিয়ে আপনার জমির মাপ অনুযায়ী পানির ড্রাম হিসাব করে নিন।</em>"
        )
        html_en = (
            f"🌿 <strong>Diagnosed Condition: {d_name_en} ({sev_en})</strong><br/><br/>"
            f"💊 <strong>Chemical Prescription:</strong> {chem_en}<br/><br/>"
            f"🌱 <strong>Field Practice:</strong> {cult_en}<br/><br/>"
            f"💡 <em>Use the Dosage Calculator above to calculate water and spray tanks for your plot.</em>"
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 2. Leaf Blast & Neck Blast (ব্লাস্ট রোগ)
    if any(w in q for w in ['ব্লাস্ট', 'শীষ ব্লাস্ট', 'blast', 'neck blast', 'pyricularia']):
        html_bn = (
            "🌾 <strong>ধানের ব্লাস্ট রোগ (Pyricularia oryzae):</strong><br/><br/>"
            "• <strong>লক্ষণ:</strong> পাতায় চোখের মতো বা ডিম্বাকৃতি দাগ, যার কেন্দ্র ছাই রঙের এবং কিনারা বাদামী। শীষের গোড়ায় আক্রমণ হলে শীষ ভেঙে শুকিয়ে যায়।<br/>"
            "• <strong>রাসায়নিক দমন:</strong> ট্রাইসাইক্লাজল ৭৫ ডব্লিউপি (যেমন: ট্রপার - ০.৭৫ গ্রাম/লিটার) অথবা ট্রাইফ্লক্সিস্ট্রবিন + টেবুকোনাজল (যেমন: নেটিভো - ০.৬ গ্রাম/লিটার) বিকেলে স্প্রে করুন।<br/>"
            "• <strong>জরুরি সতর্কতা:</strong> জমিতে ইউরিয়া সার প্রয়োগ সম্পূর্ণ বন্ধ রাখুন এবং বিঘা প্রতি ৫ কেজি অতিরিক্ত পটাশ সার দিন।"
        )
        html_en = (
            "🌾 <strong>Rice Leaf & Neck Blast (Pyricularia oryzae):</strong><br/><br/>"
            "• <strong>Symptoms:</strong> Spindle-shaped or eye-like lesions with grey centers and dark brown borders. At panicle stage, neck infection causes white drying.<br/>"
            "• <strong>Chemical Control:</strong> Spray Tricyclazole 75 WP (Trooper @ 0.75 g/L) or Trifloxystrobin + Tebuconazole (Nativo @ 0.6 g/L) in late afternoon.<br/>"
            "• <strong>Crucial Warning:</strong> Immediately suspend top-dressing Urea/Nitrogen and apply supplemental Muriate of Potash @ 5 kg per bigha to reinforce plant immunity."
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 3. Bacterial Leaf Blight (ব্যাকটেরিয়াল পাতা পোড়া)
    if any(w in q for w in ['পাতা পোড়া', 'পোড়া', 'ব্যাকটেরিয়া', 'blight', 'xanthomonas', 'kresek']):
        html_bn = (
            "🍂 <strong>ব্যাকটেরিয়াল পাতা পোড়া (Xanthomonas oryzae):</strong><br/><br/>"
            "• <strong>লক্ষণ:</strong> পাতার ডগা থেকে নিচের দিকে ঢেউ খেলানো হলুদ বা ধূসর হয়ে শুকিয়ে যায়। সকালে দাগের ওপর হলুদাভ আঠালো রস দেখা যায়।<br/>"
            "• <strong>প্রতিকার:</strong> কপার অক্সিক্লোরাইড ৫০ ডব্লিউপি (প্রতি লিটারে ২ গ্রাম) অথবা থিওভিট স্প্রে করুন। প্রতি বিঘায় ৫ কেজি অতিরিক্ত পটাশ সার দিন।<br/>"
            "• <strong>পরিচর্যা:</strong> আক্রান্ত জমির পানি অন্য জমিতে প্রবাহিত হতে দেবেন না এবং জমি ৩-৪ দিন শুকিয়ে রাখুন।"
        )
        html_en = (
            "🍂 <strong>Bacterial Leaf Blight (Xanthomonas oryzae):</strong><br/><br/>"
            "• <strong>Symptoms:</strong> Water-soaked wavy lesions starting from leaf tips turning yellow-grey with bacterial ooze visible in the morning.<br/>"
            "• <strong>Chemical Control:</strong> Spray Copper Oxychloride 50 WP (2 g/L) or Streptocycline. Apply supplemental Potash (MOP) @ 5 kg per bigha.<br/>"
            "• <strong>Field Care:</strong> Prevent irrigation drainage from infected plots to healthy fields and drain standing water for 3 to 4 days."
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 4. Brown Spot & Narrow Brown Spot (বাদামী দাগ)
    if any(w in q for w in ['বাদামী দাগ', 'সরু বাদামী', 'brown spot', 'bipolaris', 'cercospora']):
        html_bn = (
            "🟤 <strong>বাদামী দাগ রোগ (Bipolaris oryzae):</strong><br/><br/>"
            "• <strong>লক্ষণ:</strong> পাতায় তিলের দানার মতো অসংখ্য গোল বা ডিম্বাকৃতি বাদামী দাগ।<br/>"
            "• <strong>মূল কারণ:</strong> মাটিতে পুষ্টিহীনতা ও পটাশ বা সিলিকনের চরম ঘাটতি।<br/>"
            "• <strong>প্রতিকার:</strong> ম্যানকোজেব (ডাইথেন এম-৪৫ @ ২ গ্রাম/লিটার) বা কার্বেনডাজিম (১ গ্রাম/লিটার) স্প্রে করুন এবং সুষম সার প্রয়োগ করুন।"
        )
        html_en = (
            "🟤 <strong>Brown Spot (Bipolaris oryzae):</strong><br/><br/>"
            "• <strong>Symptoms:</strong> Small circular to oval sesame-seed shaped brown lesions on leaves and grains.<br/>"
            "• <strong>Root Cause:</strong> Poor soil fertility, potassium or zinc deficiency in sandy soils.<br/>"
            "• <strong>Control:</strong> Spray Mancozeb 75 WP (2 g/L) or Carbendazim (1 g/L) and apply balanced NPK nutrients."
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 5. Sheath Blight (খোল পোড়া)
    if any(w in q for w in ['খোল পোড়া', 'খোল পচা', 'sheath blight', 'rhizoctonia', 'sarocladium']):
        html_bn = (
            "🌾 <strong>খোল পোড়া রোগ (Rhizoctonia solani):</strong><br/><br/>"
            "• <strong>লক্ষণ:</strong> পানির উপরিভাগে ধান গাছের খোলে সাপের চামড়ার মতো অনিয়মিত ধূসর-সবুজ দাগ।<br/>"
            "• <strong>প্রতিকার:</strong> হেক্সাকোনাজল (যেমন: কনটাফ ৫ ইসি @ ১ মিলি/লিটার) অথবা ভ্যালিডামাইসিন (২ মিলি/লিটার) গাছের গোড়ায় স্প্রে করুন।<br/>"
            "• <strong>পরিচর্যা:</strong> ঘন রোপণ এড়িয়ে চলুন এবং জমি থেকে অতিরিক্ত পানি নিষ্কাশন করুন।"
        )
        html_en = (
            "🌾 <strong>Sheath Blight (Rhizoctonia solani):</strong><br/><br/>"
            "• <strong>Symptoms:</strong> Snake-skin greenish-grey lesions near the waterline on leaf sheaths, gradually moving upwards to upper leaves.<br/>"
            "• <strong>Control:</strong> Spray Hexaconazole 5 EC (1 ml/L) or Validamycin 3L (2 ml/L) directed at the plant base in early stages.<br/>"
            "• <strong>Field Care:</strong> Avoid high-density planting, weed field borders, and drain excess stagnant water."
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 6. Insects: Rice Hispa, Stem Borer, BPH (পোকা-মাকড়)
    if any(w in q for w in ['পামরী', 'মাজরা', 'কারেন্ট পোকা', 'গান্ধী', 'লেদা', 'পোকা', 'hispa', 'borer', 'bph', 'planthopper', 'insect', 'pest']):
        html_bn = (
            "🐛 <strong>ধানের প্রধান ক্ষতিকর পোকা ও দমন ব্যবস্থা:</strong><br/><br/>"
            "• <strong>পামরী পোকা (Hispa):</strong> পাতার সবুজ অংশ খেয়ে সাদা রেখা তৈরি করে। দমনে জমিতে পার্চিং (ডাল পোঁতা) করুন এবং আক্রমণ বেশি হলে ক্লোরপাইরিফস ২০ ইসি (২ মিলি/লিটার) স্প্রে করুন।<br/>"
            "• <strong>মাজরা পোকা (Stem Borer):</strong> কাণ্ড ফুটো করে মরা ডিগ বা সাদা শীষ বানায়। দমনে কার্বোফুরান (ফুরাডান) বা ভিরতাকো ব্যবহার করুন।<br/>"
            "• <strong>কারেন্ট পোকা (BPH):</strong> গাছের গোড়ার রস চুষে ক্ষেত পুড়িয়ে দেয় (হপার বার্ন)। দমনে পাইমেট্রোজিন (চেস) বা ডিনেটেফুরান গোড়ায় স্প্রে করুন।"
        )
        html_en = (
            "🐛 <strong>Major Rice Insect Pest Management:</strong><br/><br/>"
            "• <strong>Rice Hispa:</strong> Beetles scrape chlorophyll creating white parallel streaks. Use field perching and spray Chlorpyrifos 20 EC (2 ml/L).<br/>"
            "• <strong>Stem Borer:</strong> Caterpillars bore into stems causing deadhearts or whiteheads. Apply Carbofuran or Virtako.<br/>"
            "• <strong>Brown Planthopper (BPH):</strong> Sucks plant sap at base causing hopperburn. Spray Pymetrozine (Chess) or Dinotefuran directed at plant base."
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 7. Fertilizer, Urea, TSP, MOP, Zinc (সার ও পুষ্টি)
    if any(w in q for w in ['ইউরিয়া', 'টিএসপি', 'পটাশ', 'এমওপি', 'জিংক', 'দস্তা', 'সার', 'fertilizer', 'urea', 'npk', 'potash', 'zinc', 'dosage']):
        html_bn = (
            "🧪 <strong>সুষম সার ও ইউরিয়া ব্যবহারের বৈজ্ঞানিক নিয়ম:</strong><br/><br/>"
            "• <strong>ইউরিয়া সতর্কবার্তা:</strong> জমিতে ব্লাস্ট বা ব্যাকটেরিয়াল পাতা পোড়া রোগ দেখা দিলে ইউরিয়া উপরিপ্রয়োগ সম্পূর্ণ বন্ধ রাখুন। ইউরিয়া দিলে রোগ দ্রুত ছড়িয়ে পড়ে।<br/>"
            "• <strong>ইউরিয়া কিস্তি:</strong> জমি থেকে পানি কমিয়ে সমান ৩ কিস্তিতে ইউরিয়া প্রয়োগ করুন (চারা রোপণের ১৫ দিন, ৩০ দিন ও থোর আসার ৫ দিন আগে)।<br/>"
            "• <strong>রোগ প্রতিরোধে পটাশ (MOP):</strong> রোগ প্রতিরোধ ক্ষমতা বাড়াতে শতক প্রতি ১৫০-২০০ গ্রাম পটাশ সার ব্যবহার করুন।"
        )
        html_en = (
            "🧪 <strong>Balanced Fertilizer & Urea Management:</strong><br/><br/>"
            "• <strong>Urea Warning:</strong> Immediately suspend top-dressing Urea if Blast or Bacterial Blight is present. Excess nitrogen accelerates fungal growth.<br/>"
            "• <strong>Split Nitrogen:</strong> Apply Urea in 3 equal splits: 15 days, 30 days after transplanting, and 5 days before panicle initiation.<br/>"
            "• <strong>Potassium (MOP):</strong> Apply MOP @ 150 to 200 grams per decimal to reinforce cell walls against pathogen entry."
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 8. Weather, Spray Timing, Rain rules (আবহাওয়া ও স্প্রে)
    if any(w in q for w in ['আবহাওয়া', 'কখন স্প্রে', 'সময়', 'বৃষ্টি', 'বাতাস', 'weather', 'when to spray', 'rain', 'wind']):
        html_bn = (
            "🌦️ <strong>স্প্রে করার আদর্শ সময় ও আবহাওয়া নির্দেশিকা:</strong><br/><br/>"
            "• <strong>সেরা সময়:</strong> বিকেল ৩:৩০ থেকে ৫:০০ টার মিষ্টি রোদে স্প্রে করা সবচেয়ে কার্যকর। প্রখর রোদে বা সকালে শিশির ভেজা পাতায় স্প্রে করবেন না।<br/>"
            "• <strong>বৃষ্টির সতর্কতা:</strong> স্প্রে করার ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা থাকলে স্প্রে স্থগিত রাখুন।<br/>"
            "• <strong>বাতাস ও নিরাপত্তা:</strong> সর্বদা বাতাসের অনুকূলে স্প্রে করুন যাতে ওষুধ চোখে-মুখে না লাগে।"
        )
        html_en = (
            "🌦️ <strong>Weather & Spraying Advisory:</strong><br/><br/>"
            "• <strong>Best Timing:</strong> Late afternoon between 3:30 PM and 5:00 PM during mild sunlight. Avoid intense midday heat or morning dew.<br/>"
            "• <strong>Rain Advisory:</strong> Avoid spraying if rain is forecast within 4 hours to prevent pesticide runoff.<br/>"
            "• <strong>Wind Direction:</strong> Always spray along the wind direction with protective eyewear and face mask."
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 9. Irrigation, AWD, Water (সেচ ও পানি)
    if any(w in q for w in ['সেচ', 'পানি', 'এডব্লিউডি', 'water', 'irrigation', 'awd']):
        html_bn = (
            "💧 <strong>সেচ ও এডব্লিউডি (AWD) পানি ব্যবস্থাপনা:</strong><br/><br/>"
            "• চারা রোপণের পর প্রথম ১০ দিন ২-৩ ইঞ্চি পানি রাখুন।<br/>"
            "• কুশি গজানোর সময় মাঝে মাঝে জমি শুকিয়ে বাতাস চলাচলের সুযোগ দিন (AWD পদ্ধতি)।<br/>"
            "• থোর ও ফুল ফোটার সময় জমিতে অবশ্যই পর্যাপ্ত পানি নিশ্চিত করুন।<br/>"
            "• ব্যাকটেরিয়াল পাতা পোড়া রোগ দেখা দিলে অতিরিক্ত পানি অবিলম্বে নিষ্কাশন করুন।"
        )
        html_en = (
            "💧 <strong>Irrigation & AWD Water Management:</strong><br/><br/>"
            "• Maintain 2 to 3 inches standing water during the first 10 days after transplanting for seedling establishment.<br/>"
            "• Practice Alternate Wetting and Drying (AWD) during tillering stage to promote strong root aeration.<br/>"
            "• Maintain continuous standing water during panicle initiation and flowering stages.<br/>"
            "• If bacterial leaf blight appears, drain excess standing water immediately."
        )
        return {
            "html": html_bn if is_bn else html_en,
            "text_bn": clean_text_for_speech(html_bn, is_bn=True),
            "text_en": clean_text_for_speech(html_en, is_bn=False)
        }

    # 10. Default General Consultation
    html_bn = (
        f"🌾 <strong>RiceGuard AI পরামর্শক:</strong><br/><br/>"
        f"আপনার প্রশ্ন: <em>'{query}'</em><br/><br/>"
        f"ধানের রোগ (ব্লাস্ট, পাতা পোড়া, বাদামী দাগ, খোল পোড়া), ক্ষতিকর পোকা দমন, বালাইনাশক ও সারের মাত্রা বা সেচ ব্যবস্থাপনা নিয়ে নির্দিষ্ট যেকোনো প্রশ্ন করুন।<br/>"
        f"জরুরি প্রয়োজনে সরকারি কৃষি কল সেন্টারে সরাসরি কল করতে ডায়াল করুন <strong>১৬১২৩</strong>।"
    )
    html_en = (
        f"🌾 <strong>RiceGuard AI Agronomist:</strong><br/><br/>"
        f"Your query: <em>'{query}'</em><br/><br/>"
        f"Please ask about specific rice diseases (Blast, Blight, Brown Spot, Sheath Blight), pest control, fertilizer dosages, or field irrigation.<br/>"
        f"For urgent assistance, dial the National Agriculture Helpline <strong>16123</strong>."
    )
    return {
        "html": html_bn if is_bn else html_en,
        "text_bn": clean_text_for_speech(html_bn, is_bn=True),
        "text_en": clean_text_for_speech(html_en, is_bn=False)
    }


def query_agri_assistant(message: str, lang: str = "bn", current_disease: str = None, current_confidence: float = None) -> dict:
    if not is_meaningful_query(message):
        return get_expert_local_response(message, lang, current_disease, current_confidence)

    if GEMINI_API_KEY:
        gemini_res = call_gemini_api(message, lang, current_disease, current_confidence)
        if gemini_res:
            return gemini_res

    return get_expert_local_response(message, lang, current_disease, current_confidence)
