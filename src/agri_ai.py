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


# Check for Google Gemini API Key from environment
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY", "").strip()


def is_meaningful_query(text: str) -> bool:
    """Checks if the user input contains actual words rather than just symbols or gibberish."""
    if not text:
        return False
    # Remove whitespace and common punctuation
    cleaned = re.sub(r'[\s\.,\/#!$%\^&\*;:{}=\-_`~()?"\'<>+\|\\\[\]]', '', text)
    if len(cleaned) < 2:
        return False
    # Check if it's only repeated single characters (e.g. 'aaaa', '.....')
    if len(set(cleaned)) == 1 and len(cleaned) > 2:
        return False
    return True


def call_gemini_api(message: str, lang: str = "bn", current_disease: str = None, current_confidence: float = None) -> dict:
    """
    Calls Google Gemini REST API (gemini-1.5-flash) for live generative agronomist consultation.
    """
    if not GEMINI_API_KEY:
        return None

    # Construct context-aware system prompt
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
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
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
                    # Convert markdown formatting to HTML
                    html_text = raw_text.replace("\n\n", "<br/><br/>").replace("\n", "<br/>")
                    html_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_text)
                    html_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_text)
                    html_text = re.sub(r'•\s*', r'• ', html_text)

                    # Spoken audio plain text
                    clean_spoken = re.sub(r'<[^>]+>', ' ', html_text)
                    clean_spoken = re.sub(r'[*#_]', '', clean_spoken)
                    clean_spoken = re.sub(r'\s+', ' ', clean_spoken).strip()

                    return {
                        "source": "gemini",
                        "html": html_text,
                        "text_bn": clean_spoken if lang == "bn" else "RiceGuard AI Agronomist consultation generated successfully.",
                        "text_en": clean_spoken if lang == "en" else "ধানের রোগ ও সার ব্যবস্থাপনার জন্য প্রস্তাবিত পরামর্শ।"
                    }
    except Exception as e:
        print(f"[RiceGuard AI] Gemini API request failed ({e}), switching to 50-Year Expert Local Engine.")
        return None


def get_expert_local_response(query: str, lang: str = "bn", current_disease: str = None, current_confidence: float = None) -> dict:
    """
    Comprehensive 50-Year Senior Agronomist Local Expert Engine.
    Handles diseases, pests, fertilization, water, weather, and gibberish filtering.
    """
    is_bn = (lang == "bn")
    q = query.lower().strip()

    # 0. Check for empty or gibberish non-meaningful queries
    if not is_meaningful_query(query):
        return {
            "html": (
                "🌾 <strong>নমস্কার/Hello!</strong><br/><br/>"
                "আপনার প্রশ্নটি স্পষ্ট বোঝা যায়নি। অনুগ্রহ করে ধানের কোনো নির্দিষ্ট রোগ (যেমন: <em>ব্লাস্ট, পাতা পোড়া, বাদামী দাগ, খোল পোড়া</em>), "
                "বালাইনাশকের নাম, সারের সঠিক ডোজ বা মাঠ পরিচর্যা নিয়ে প্রশ্ন লিখুন অথবা নিচের কুইক বাটনে চাপ দিন।"
                if is_bn else
                "🌾 <strong>Hello!</strong><br/><br/>"
                "Your query is not clear. Please type a specific question about rice diseases (e.g. <em>Blast, Blight, Brown Spot, Hispa</em>), "
                "fertilizer dosage, spraying weather, or field care."
            ),
            "text_bn": "আপনার প্রশ্নটি স্পষ্ট নয়। অনুগ্রহ করে ধানের রোগ, বালাইনাশক, সার বা পরিচর্যা নিয়ে প্রশ্ন লিখুন।",
            "text_en": "Your query is not clear. Please ask a specific question about rice diseases, fertilizers, or crop care."
        }

    # 1. Contextual Match: Questions about currently analyzed disease
    if current_disease and current_disease in DISEASE_DATABASE and any(w in q for w in ['বর্তমান', 'এই রোগ', 'প্রেসক্রিপশন', 'চিকিৎসা', 'ওষুধ', 'ডোজ', 'current', 'this disease', 'rx', 'treatment', 'medicine']):
        d_info = DISEASE_DATABASE[current_disease]
        d_name = d_info.get("name_bn" if is_bn else "name_en", current_disease)
        chem = d_info.get("management_bn" if is_bn else "management_en", {}).get("chemical", "প্রয়োজন নেই" if is_bn else "None required")
        cult = d_info.get("management_bn" if is_bn else "management_en", {}).get("cultural", "সুষম সেচ বজায় রাখুন।" if is_bn else "Maintain balanced irrigation.")
        sev = d_info.get("severity_bn" if is_bn else "severity_en", "সতর্কতা" if is_bn else "Caution")

        html = (
            f"🌿 <strong>শনাক্তকৃত রোগ: {d_name} ({sev})</strong><br/><br/>"
            f"💊 <strong>রাসায়নিক প্রতিকার:</strong> {chem}<br/><br/>"
            f"🌱 <strong>মাঠ পরিচর্যা:</strong> {cult}<br/><br/>"
            f"💡 <em>উপরের 'ডোজ ক্যালকুলেটর' দিয়ে আপনার জমির মাপ অনুযায়ী পানির ড্রাম হিসাব করে নিন।</em>"
            if is_bn else
            f"🌿 <strong>Diagnosed Condition: {d_name} ({sev})</strong><br/><br/>"
            f"💊 <strong>Chemical Prescription:</strong> {chem}<br/><br/>"
            f"🌱 <strong>Field Practice:</strong> {cult}<br/><br/>"
            f"💡 <em>Use the Dosage Calculator above to calculate water and knapsack tanks for your exact plot.</em>"
        )
        return {
            "html": html,
            "text_bn": f"ধানের পাতায় সনাক্তকৃত রোগ হলো {d_name}। প্রস্তাবিত বালাইনাশক চিকিৎসা: {chem}। মাঠ পরিচর্যা: {cult}",
            "text_en": f"Diagnosed condition is {d_name}. Recommended chemical treatment: {chem}. Cultural practice: {cult}"
        }

    # 2. Leaf Blast & Neck Blast (ব্লাস্ট রোগ)
    if any(w in q for w in ['ব্লাস্ট', 'শীষ ব্লাস্ট', 'blast', 'neck blast', 'pyricularia']):
        html = (
            "🌾 <strong>ধানের ব্লাস্ট রোগ (Pyricularia oryzae):</strong><br/><br/>"
            "• <strong>লক্ষণ:</strong> পাতায় চোখের মতো বা ডিম্বাকৃতি দাগ, যার কেন্দ্র ছাই রঙের এবং কিনারা বাদামী। শীষের গোড়ায় আক্রমণ হলে শীষ ভেঙে শুকিয়ে যায় (শীষ ব্লাস্ট)।<br/>"
            "• <strong>রাসায়নিক দমন:</strong> ট্রাইসাইক্লাজল ৭৫ ডব্লিউপি (যেমন: ট্রপার - ০.৭৫ গ্রাম/লিটার) অথবা ট্রাইফ্লক্সিস্ট্রবিন + টেবুকোনাজল (যেমন: নেটিভো - ০.৬ গ্রাম/লিটার) বিকেলে স্প্রে করুন।<br/>"
            "• <strong>জরুরি সতর্কতা:</strong> জমিতে ইউরিয়া সার প্রয়োগ সম্পূর্ণ বন্ধ রাখুন এবং বিঘা প্রতি ৫ কেজি অতিরিক্ত পটাশ সার দিন।"
            if is_bn else
            "🌾 <strong>Rice Leaf & Neck Blast (Pyricularia oryzae):</strong><br/><br/>"
            "• <strong>Symptoms:</strong> Spindle-shaped/eye-like lesions with grey centers and dark brown borders.<br/>"
            "• <strong>Chemical Control:</strong> Spray Tricyclazole 75 WP (Trooper @ 0.75 g/L) or Trifloxystrobin + Tebuconazole (Nativo @ 0.6 g/L) in late afternoon.<br/>"
            "• <strong>Crucial Warning:</strong> Immediately stop top-dressing Urea/Nitrogen and apply supplemental Muriate of Potash."
        )
        return {
            "html": html,
            "text_bn": "ধানের ব্লাস্ট রোগ একটি মারাত্মক ছত্রাকজনিত রোগ। পাতায় চোখের মতো ডিম্বাকৃতি দাগ দেখা যায়। প্রতিকারে ট্রাইসাইক্লাজল বা নেটিভো বিকেলে স্প্রে করুন এবং ইউরিয়া সার দেওয়া বন্ধ রাখুন।",
            "text_en": "Rice Leaf Blast causes eye-shaped lesions. Spray Tricyclazole or Nativo in late afternoon and stop top-dressing Urea fertilizer."
        }

    # 3. Bacterial Leaf Blight (ব্যাকটেরিয়াল পাতা পোড়া)
    if any(w in q for w in ['পাতা পোড়া', 'পোড়া', 'ব্যাকটেরিয়া', 'blight', 'xanthomonas', 'kresek']):
        html = (
            "🍂 <strong>ব্যাকটেরিয়াল পাতা পোড়া (Xanthomonas oryzae):</strong><br/><br/>"
            "• <strong>লক্ষণ:</strong> পাতার ডগা থেকে নিচের দিকে ঢেউ খেলানো হলুদ বা ধূসর হয়ে শুকিয়ে যায়। সকালে দাগের ওপর আঠালো রস দেখা যায়।<br/>"
            "• <strong>প্রতিকার:</strong> কপার অক্সিক্লোরাইড (প্রতি লিটারে ২ গ্রাম) অথবা থিওভিট স্প্রে করুন। প্রতি বিঘায় ৫ কেজি অতিরিক্ত পটাশ সার দিন।<br/>"
            "• <strong>পরিচর্যা:</strong> আক্রান্ত জমির পানি অন্য জমিতে প্রবাহিত হতে দেবেন না এবং জমি ৩-৪ দিন শুকিয়ে রাখুন।"
            if is_bn else
            "🍂 <strong>Bacterial Leaf Blight (Xanthomonas oryzae):</strong><br/><br/>"
            "• <strong>Symptoms:</strong> Water-soaked wavy lesions starting from leaf tips turning yellow-grey with bacterial ooze.<br/>"
            "• <strong>Control:</strong> Spray Copper Oxychloride 50 WP (2 g/L) or Streptocycline. Apply supplemental Potash (MOP) 5 kg/bigha.<br/>"
            "• <strong>Field Care:</strong> Prevent irrigation drainage from infected plots and drain water for 3–4 days."
        )
        return {
            "html": html,
            "text_bn": "ব্যাকটেরিয়াল পাতা পোড়া রোগে পাতার ডগা থেকে নিচের দিকে শুকিয়ে যায়। প্রতিকারে কপার অক্সিক্লোরাইড স্প্রে করুন এবং বিঘা প্রতি ৫ কেজি পটাশ সার দিন।",
            "text_en": "Bacterial Leaf Blight causes yellow drying from leaf tips. Spray Copper Oxychloride and apply supplemental Potash fertilizer."
        }

    # 4. Brown Spot & Narrow Brown Spot (বাদামী দাগ)
    if any(w in q for w in ['বাদামী দাগ', 'সরু বাদামী', 'brown spot', 'bipolaris', 'cercospora']):
        html = (
            "🟤 <strong>বাদামী দাগ রোগ (Bipolaris oryzae):</strong><br/><br/>"
            "• <strong>লক্ষণ:</strong> পাতায় তিলের দানার মতো অসংখ্য গোল বা ডিম্বাকৃতি বাদামী দাগ।<br/>"
            "• <strong>মূল কারণ:</strong> মাটিতে পুষ্টিহীনতা ও পটাশ বা সিলিকনের চরম ঘাটতি।<br/>"
            "• <strong>প্রতিকার:</strong> ম্যানকোজেব (ডাইথেন এম-৪৫ @ ২ গ্রাম/লিটার) বা কার্বেনডাজিম (১ গ্রাম/লিটার) স্প্রে করুন এবং সুষম সার প্রয়োগ করুন।"
            if is_bn else
            "🟤 <strong>Brown Spot (Bipolaris oryzae):</strong><br/><br/>"
            "• <strong>Symptoms:</strong> Small circular to oval sesame-seed shaped brown lesions.<br/>"
            "• <strong>Root Cause:</strong> Poor soil fertility, potassium or zinc deficiency.<br/>"
            "• <strong>Control:</strong> Spray Mancozeb 75 WP (2 g/L) or Carbendazim (1 g/L) and apply balanced NPK nutrients."
        )
        return {
            "html": html,
            "text_bn": "বাদামী দাগ রোগে পাতায় তিলের মতো বাদামী দাগ পড়ে। মাটিতে পুষ্টি ও পটাশ ঘাটতি এর মূল কারণ। প্রতিকারে ডাইথেন এম-৪৫ বা কার্বেনডাজিম স্প্রে করুন।",
            "text_en": "Brown Spot causes sesame-seed like lesions due to nutrient deficiency. Spray Mancozeb or Carbendazim and provide balanced fertilizers."
        }

    # 5. Sheath Blight & Sheath Rot (খোল পোড়া / খোল পচা)
    if any(w in q for w in ['খোল পোড়া', 'খোল পচা', 'sheath blight', 'rhizoctonia', 'sarocladium']):
        html = (
            "🌾 <strong>খোল পোড়া রোগ (Rhizoctonia solani):</strong><br/><br/>"
            "• <strong>লক্ষণ:</strong> পানির উপরিভাগে ধান গাছের খোলে সাপের চামড়ার মতো অনিয়মিত ধূসর-সবুজ দাগ।<br/>"
            "• <strong>প্রতিকার:</strong> হেক্সাকোনাজল (যেমন: কনটাফ ৫ ইসি @ ১ মিলি/লিটার) অথবা ভ্যালিডামাইসিন (২ মিলি/লিটার) গাছের গোড়ায় স্প্রে করুন।<br/>"
            "• <strong>পরিচর্যা:</strong> ঘন রোপণ এড়িয়ে চলুন এবং জমি থেকে অতিরিক্ত পানি নিষ্কাশন করুন।"
            if is_bn else
            "🌾 <strong>Sheath Blight (Rhizoctonia solani):</strong><br/><br/>"
            "• <strong>Symptoms:</strong> Snake-skin greenish-grey lesions near the waterline on leaf sheaths.<br/>"
            "• <strong>Control:</strong> Spray Hexaconazole 5 EC (1 ml/L) or Validamycin 3L (2 ml/L) directed at the plant base.<br/>"
            "• <strong>Field Care:</strong> Avoid high-density planting and improve sunlight penetration."
        )
        return {
            "html": html,
            "text_bn": "খোল পোড়া রোগে ধান গাছের গোড়ায় সাপের চামড়ার মতো দাগ হয়। প্রতিকারে হেক্সাকোনাজল বা ভ্যালিডামাইসিন গাছের গোড়ায় স্প্রে করুন।",
            "text_en": "Sheath Blight causes snake-skin lesions on leaf sheaths. Spray Hexaconazole or Validamycin targeted at the plant base."
        }

    # 6. Insects: Rice Hispa, Stem Borer, BPH, Gall Midge (পোকা-মাকড়)
    if any(w in q for w in ['পামরী', 'মাজরা', 'কারেন্ট পোকা', 'গান্ধী', 'লেদা', 'পোকা', 'hispa', 'borer', 'bph', 'planthopper', 'insect', 'pest']):
        html = (
            "🐛 <strong>ধানের প্রধান ক্ষতিকর পোকা ও দমন ব্যবস্থা:</strong><br/><br/>"
            "• <strong>পামরী পোকা (Hispa):</strong> পাতার সবুজ অংশ খেয়ে সাদা রেখা তৈরি করে। দমনে জমিতে পার্চিং (ডাল পোঁতা) করুন এবং আক্রমণ বেশি হলে ক্লোরপাইরিফস ২০ ইসি (২ মিলি/লিটার) স্প্রে করুন।<br/>"
            "• <strong>মাজরা পোকা (Stem Borer):</strong> কাণ্ড ফুটো করে মরা ডিগ বা সাদা শীষ বানায়। দমনে কার্বোফুরান (ফুরাডান) বা ভিরতাকো ব্যবহার করুন।<br/>"
            "• <strong>কারেন্ট পোকা (BPH):</strong> গাছের গোড়ার রস চুষে ক্ষেত পুড়িয়ে দেয় (হপার বার্ন)। দমনে পাইমেট্রোজিন (চেস) বা ডিনেটেফুরান গোড়ায় স্প্রে করুন।"
            if is_bn else
            "🐛 <strong>Major Rice Insect Pest Management:</strong><br/><br/>"
            "• <strong>Rice Hispa:</strong> Beetles scrape chlorophyll creating white streaks. Use field perching and spray Chlorpyrifos 20 EC (2 ml/L).<br/>"
            "• <strong>Stem Borer:</strong> Causes deadhearts and whiteheads. Apply Carbofuran or Virtako.<br/>"
            "• <strong>Brown Planthopper (BPH):</strong> Sucks plant sap causing hopperburn. Spray Pymetrozine (Chess) or Dinotefuran directed at plant base."
        )
        return {
            "html": html,
            "text_bn": "পামরী পোকা দমনে পার্চিং ও ক্লোরপাইরিফস দিন। মাজরা পোকা দমনে কার্বোফুরান এবং কারেন্ট পোকা দমনে পাইমেট্রোজিন গাছের গোড়ায় স্প্রে করুন।",
            "text_en": "Control Rice Hispa with perching and Chlorpyrifos. Control Stem Borer with Carbofuran and BPH with Pymetrozine."
        }

    # 7. Fertilizer, Urea, TSP, MOP, Zinc (সার ও পুষ্টি)
    if any(w in q for w in ['ইউরিয়া', 'টিএসপি', 'পটাশ', 'এমওপি', 'জিংক', 'দস্তা', 'সার', 'fertilizer', 'urea', 'npk', 'potash', 'zinc', 'dosage']):
        html = (
            "🧪 <strong>সুষম সার ও ইউরিয়া ব্যবহারের বৈজ্ঞানিক নিয়ম:</strong><br/><br/>"
            "• <strong>ইউরিয়া সতর্কবার্তা:</strong> জমিতে ব্লাস্ট বা ব্যাকটেরিয়াল পাতা পোড়া রোগ দেখা দিলে ইউরিয়া উপরিপ্রয়োগ সম্পূর্ণ বন্ধ রাখুন। ইউরিয়া দিলে রোগ দ্রুত ছড়িয়ে পড়ে।<br/>"
            "• <strong>ইউরিয়া কিস্তি:</strong> জমি থেকে পানি কমিয়ে সমান ৩ কিস্তিতে ইউরিয়া প্রয়োগ করুন (চারা রোপণের ১৫ দিন, ৩০ দিন ও থোর আসার ৫ দিন আগে)।<br/>"
            "• <strong>রোগ প্রতিরোধে পটাশ (MOP):</strong> রোগ প্রতিরোধ ক্ষমতা বাড়াতে শতক প্রতি ১৫০-২০০ গ্রাম পটাশ সার ব্যবহার করুন।"
            if is_bn else
            "🧪 <strong>Balanced Fertilizer & Urea Management:</strong><br/><br/>"
            "• <strong>Urea Warning:</strong> Immediately suspend top-dressing Urea if Blast or Bacterial Blight is present.<br/>"
            "• <strong>Split Nitrogen:</strong> Apply Urea in 3 equal splits (15 days, 30 days after transplanting, and 5 days before panicle initiation).<br/>"
            "• <strong>Potassium (MOP):</strong> Apply MOP @ 150–200 g/decimal to reinforce cell walls against fungal pathogens."
        )
        return {
            "html": html,
            "text_bn": "ব্লাস্ট বা পাতা পোড়া রোগে ইউরিয়া সার দেওয়া সম্পূর্ণ বন্ধ রাখুন। রোগ প্রতিরোধ ক্ষমতা বাড়াতে পটাশ সার দিন এবং ইউরিয়া ৩ কিস্তিতে প্রয়োগ করুন।",
            "text_en": "Stop top-dressing Urea if Blast or Blight is active. Apply Potash to strengthen plant immunity and split Urea into three doses."
        }

    # 8. Weather, Spray Timing, Rain rules (আবহাওয়া ও স্প্রে)
    if any(w in q for w in ['আবহাওয়া', 'কখন স্প্রে', 'সময়', 'বৃষ্টি', 'বাতাস', 'weather', 'when to spray', 'rain', 'wind']):
        html = (
            "🌦️ <strong>স্প্রে করার আদর্শ সময় ও আবহাওয়া নির্দেশিকা:</strong><br/><br/>"
            "• <strong>সেরা সময়:</strong> বিকেল ৩:৩০ থেকে ৫:০০ টার মিষ্টি রোদে স্প্রে করা সবচেয়ে কার্যকর। প্রখর রোদে বা সকালে শিশির ভেজা পাতায় স্প্রে করবেন না।<br/>"
            "• <strong>বৃষ্টির সতর্কতা:</strong> স্প্রে করার ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা থাকলে স্প্রে স্থগিত রাখুন।<br/>"
            "• <strong>বাতাস ও নিরাপত্তা:</strong> সর্বদা বাতাসের অনুকূলে স্প্রে করুন যাতে ওষুধ চোখে-মুখে না লাগে।"
            if is_bn else
            "🌦️ <strong>Weather & Spraying Advisory:</strong><br/><br/>"
            "• <strong>Best Timing:</strong> Late afternoon (3:30 PM - 5:00 PM) during mild sunlight.<br/>"
            "• <strong>Rain Advisory:</strong> Avoid spraying if rain is expected within 4 hours.<br/>"
            "• <strong>Wind:</strong> Always spray in the direction of the wind with protective eyewear and mask."
        )
        return {
            "html": html,
            "text_bn": "বিকেল ৩টা ৩০ থেকে ৫টার মিষ্টি রোদে স্প্রে করা সবচেয়ে ভালো। ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা থাকলে স্প্রে বন্ধ রাখুন এবং বাতাসের অনুকূলে স্প্রে করুন।",
            "text_en": "Late afternoon from 3:30 to 5 PM is ideal for spraying. Postpone spraying if rain is expected within 4 hours and spray along wind direction."
        }

    # 9. Irrigation, AWD, Water (সেচ ও পানি)
    if any(w in q for w in ['সেচ', 'পানি', 'এডব্লিউডি', 'water', 'irrigation', 'awd']):
        html = (
            "💧 <strong>সেচ ও এডব্লিউডি (AWD) পানি ব্যবস্থাপনা:</strong><br/><br/>"
            "• চারা রোপণের পর প্রথম ১০ দিন ২-৩ ইঞ্চি পানি রাখুন।<br/>"
            "• কুশি গজানোর সময় মাঝে মাঝে জমি শুকিয়ে বাতাস চলাচলের সুযোগ দিন (AWD পদ্ধতি)।<br/>"
            "• থোর ও ফুল ফোটার সময় জমিতে অবশ্যই পর্যাপ্ত পানি নিশ্চিত করুন।<br/>"
            "• ব্যাকটেরিয়াল পাতা পোড়া রোগ দেখা দিলে অতিরিক্ত পানি অবিলম্বে নিষ্কাশন করুন।"
            if is_bn else
            "💧 <strong>Irrigation & AWD Water Management:</strong><br/><br/>"
            "• Maintain 2–3 inches water for the first 10 days after transplanting.<br/>"
            "• Practice Alternate Wetting and Drying (AWD) during tillering to promote strong rooting.<br/>"
            "• Maintain continuous standing water during panicle initiation and flowering."
        )
        return {
            "html": html,
            "text_bn": "চারা রোপণের পর ২ থেকে ৩ ইঞ্চি পানি রাখুন। কুশি গজানোর সময় এডব্লিউডি পদ্ধতিতে মাঝে মাঝে জমি শুকান এবং ফুল ফোটার সময় পর্যাপ্ত পানি রাখুন।",
            "text_en": "Maintain 2 to 3 inches water after planting. Use Alternate Wetting and Drying during tillering and ensure continuous water during flowering."
        }

    # 10. Default General Consultation
    html = (
        f"🌾 <strong>RiceGuard AI পরামর্শক:</strong><br/><br/>"
        f"আপনার প্রশ্ন: <em>\"{query}\"</em><br/><br/>"
        f"ধানের রোগ (ব্লাস্ট, পাতা পোড়া, বাদামী দাগ, খোল পোড়া), ক্ষতিকর পোকা দমন, বালাইনাশক ও সারের মাত্রা বা সেচ ব্যবস্থাপনা নিয়ে নির্দিষ্ট যেকোনো প্রশ্ন করুন।<br/>"
        f"জরুরি প্রয়োজনে সরকারি কৃষি কল সেন্টারে সরাসরি কল করতে ডায়াল করুন <strong>১৬১২৩</strong>।"
        if is_bn else
        f"🌾 <strong>RiceGuard AI Agronomist:</strong><br/><br/>"
        f"Your query: <em>\"{query}\"</em><br/><br/>"
        f"Please ask about specific rice diseases (Blast, Blight, Brown Spot, Sheath Blight), pest control, fertilizer dosages, or field irrigation.<br/>"
        f"For urgent assistance, dial the National Agriculture Helpline <strong>16123</strong>."
    )
    return {
        "html": html,
        "text_bn": f"ধন্যবাদ আপনার প্রশ্নের জন্য। ধানের যেকোনো রোগ, সার বা সেচের নিয়ম জানতে লিখুন। জরুরি কৃষি পরামর্শের জন্য কল করুন ১৬১২৩।",
        "text_en": f"Thank you for your question. Ask about rice diseases, fertilizers, or spraying advice. For emergency assistance dial 16123."
    }


def query_agri_assistant(message: str, lang: str = "bn", current_disease: str = None, current_confidence: float = None) -> dict:
    """
    Main entrypoint: Attempts live Gemini API first, otherwise falls back to 50-Year Expert Local Engine.
    """
    if not is_meaningful_query(message):
        return get_expert_local_response(message, lang, current_disease, current_confidence)

    # 1. Try Live Gemini API if key is present
    if GEMINI_API_KEY:
        gemini_res = call_gemini_api(message, lang, current_disease, current_confidence)
        if gemini_res:
            return gemini_res

    # 2. Fallback to Senior Agronomist Expert System
    return get_expert_local_response(message, lang, current_disease, current_confidence)
