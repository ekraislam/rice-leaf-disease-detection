"""
RiceGuard Bangladesh Disease Outbreak Geo-Map Service
Tracks, aggregates, and renders real-time district-level rice leaf disease outbreaks on OpenStreetMap/Leaflet.
"""

import os
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "static", "outbreak_data.json")

# Baseline Active Outbreak Dataset across Bangladesh Rice Granaries (Total: 628 Baseline)
DEFAULT_OUTBREAKS = [
    {
        "id": "dinajpur",
        "district_en": "Dinajpur",
        "district_bn": "দিনাজপুর",
        "division": "Rangpur",
        "lat": 25.6217,
        "lon": 88.6355,
        "total_cases": 84,
        "primary_disease": "Leaf Blast",
        "primary_disease_bn": "ধানের ব্লাস্ট রোগ",
        "disease_slug": "leaf_blast",
        "severity": "high",
        "risk_label_bn": "উচ্চ সতর্কতা (High Alert)",
        "cases_breakdown": {
            "leaf_blast": 48,
            "bacterial_leaf_blight": 22,
            "brown_spot": 14
        },
        "advisory_bn": "আর্দ্রতা বৃদ্ধির কারণে ব্লাস্ট রোগ দ্রুত ছড়াচ্ছে। ট্রাইসাইক্লাজল ৭৫ ডব্লিউপি স্প্রে করুন।"
    },
    {
        "id": "mymensingh",
        "district_en": "Mymensingh",
        "district_bn": "ময়মনসিংহ",
        "division": "Mymensingh",
        "lat": 24.7471,
        "lon": 90.4203,
        "total_cases": 112,
        "primary_disease": "Bacterial Leaf Blight",
        "primary_disease_bn": "ব্যাকটেরিয়াল পাতা পোড়া",
        "disease_slug": "bacterial_leaf_blight",
        "severity": "high",
        "risk_label_bn": "উচ্চ সতর্কতা (High Alert)",
        "cases_breakdown": {
            "bacterial_leaf_blight": 62,
            "sheath_blight": 34,
            "leaf_blast": 16
        },
        "advisory_bn": "জমির পানি ৩-৪ দিন শুকিয়ে রাখুন এবং বিঘা প্রতি ৫ কেজি অতিরিক্ত পটাশ সার দিন।"
    },
    {
        "id": "bogura",
        "district_en": "Bogura",
        "district_bn": "বগুড়া",
        "division": "Rajshahi",
        "lat": 24.8465,
        "lon": 89.3777,
        "total_cases": 65,
        "primary_disease": "Brown Spot",
        "primary_disease_bn": "বাদামী দাগ রোগ",
        "disease_slug": "brown_spot",
        "severity": "medium",
        "risk_label_bn": "মাঝারি ঝুঁকি (Moderate Risk)",
        "cases_breakdown": {
            "brown_spot": 38,
            "leaf_blast": 18,
            "sheath_blight": 9
        },
        "advisory_bn": "মাটিতে পটাশ ও জিংকের ঘাটতি মেটান এবং ম্যানকোজেব ৭৫ ডব্লিউপি স্প্রে করুন।"
    },
    {
        "id": "naogaon",
        "district_en": "Naogaon",
        "district_bn": "নওগাঁ",
        "division": "Rajshahi",
        "lat": 24.7936,
        "lon": 88.9318,
        "total_cases": 78,
        "primary_disease": "Leaf Blast",
        "primary_disease_bn": "ধানের ব্লাস্ট রোগ",
        "disease_slug": "leaf_blast",
        "severity": "high",
        "risk_label_bn": "উচ্চ সতর্কতা (High Alert)",
        "cases_breakdown": {
            "leaf_blast": 45,
            "bacterial_leaf_blight": 20,
            "brown_spot": 13
        },
        "advisory_bn": "ইউরিয়া সারের উপরিপ্রয়োগ বন্ধ রেখে নেটিভো ০.৬ গ্রাম/লিটার বিকেলে স্প্রে করুন।"
    },
    {
        "id": "barishal",
        "district_en": "Barishal",
        "district_bn": "বরিশাল",
        "division": "Barishal",
        "lat": 22.7010,
        "lon": 90.3535,
        "total_cases": 52,
        "primary_disease": "Sheath Blight",
        "primary_disease_bn": "খোল পোড়া রোগ",
        "disease_slug": "sheath_blight",
        "severity": "medium",
        "risk_label_bn": "মাঝারি ঝুঁকি (Moderate Risk)",
        "cases_breakdown": {
            "sheath_blight": 32,
            "bacterial_leaf_blight": 12,
            "brown_spot": 8
        },
        "advisory_bn": "আক্রান্ত গাছের গোড়ায় হেক্সাকোনাজল ৫ ইসি বা ভ্যালিডামাইসিন ৩ এল স্প্রে করুন।"
    },
    {
        "id": "cumilla",
        "district_en": "Cumilla",
        "district_bn": "কুমিল্লা",
        "division": "Chattogram",
        "lat": 23.4607,
        "lon": 91.1809,
        "total_cases": 46,
        "primary_disease": "Rice Hispa",
        "primary_disease_bn": "ধানের পামরী পোকা",
        "disease_slug": "rice_hispa",
        "severity": "medium",
        "risk_label_bn": "মাঝারি ঝুঁকি (Moderate Risk)",
        "cases_breakdown": {
            "rice_hispa": 28,
            "brown_spot": 10,
            "bacterial_leaf_blight": 8
        },
        "advisory_bn": "মাঠে হাতজাল টেনে পামরী পোকা ধ্বংস করুন এবং ক্লোরপাইরিফস ২০ ইসি স্প্রে করুন।"
    },
    {
        "id": "sylhet",
        "district_en": "Sylhet",
        "district_bn": "সিলেট",
        "division": "Sylhet",
        "lat": 24.8949,
        "lon": 91.8687,
        "total_cases": 38,
        "primary_disease": "Brown Spot",
        "primary_disease_bn": "বাদামী দাগ রোগ",
        "disease_slug": "brown_spot",
        "severity": "low",
        "risk_label_bn": "নিয়ন্ত্রিত (Low Risk)",
        "cases_breakdown": {
            "brown_spot": 22,
            "leaf_blast": 10,
            "sheath_blight": 6
        },
        "advisory_bn": "হাওর অঞ্চলে বোরো ধানে ছত্রাকনাশক সিড-ট্রিটমেন্ট নিশ্চিত করুন।"
    },
    {
        "id": "jashore",
        "district_en": "Jashore",
        "district_bn": "যশোর",
        "division": "Khulna",
        "lat": 23.1664,
        "lon": 89.2081,
        "total_cases": 44,
        "primary_disease": "Bacterial Leaf Blight",
        "primary_disease_bn": "ব্যাকটেরিয়াল পাতা পোড়া",
        "disease_slug": "bacterial_leaf_blight",
        "severity": "medium",
        "risk_label_bn": "মাঝারি ঝুঁকি (Moderate Risk)",
        "cases_breakdown": {
            "bacterial_leaf_blight": 24,
            "sheath_blight": 12,
            "rice_hispa": 8
        },
        "advisory_bn": "কপার হাইড্রোক্সাইড বা কপার অক্সিক্লোরাইড স্প্রে করে রোগের বিস্তার রোধ করুন।"
    },
    {
        "id": "rangpur",
        "district_en": "Rangpur",
        "district_bn": "রংপুর",
        "division": "Rangpur",
        "lat": 25.7439,
        "lon": 89.2752,
        "total_cases": 74,
        "primary_disease": "Leaf Blast",
        "primary_disease_bn": "ধানের ব্লাস্ট রোগ",
        "disease_slug": "leaf_blast",
        "severity": "high",
        "risk_label_bn": "উচ্চ সতর্কতা (High Alert)",
        "cases_breakdown": {
            "leaf_blast": 44,
            "bacterial_leaf_blight": 18,
            "brown_spot": 12
        },
        "advisory_bn": "ভোরের কুয়াশা ও শিশির কাটলে বিকেলে ট্রাইসাইক্লাজল স্প্রে করুন।"
    },
    {
        "id": "tangail",
        "district_en": "Tangail",
        "district_bn": "টাঙ্গাইল",
        "division": "Dhaka",
        "lat": 24.2513,
        "lon": 89.9167,
        "total_cases": 35,
        "primary_disease": "Sheath Blight",
        "primary_disease_bn": "খোল পোড়া রোগ",
        "disease_slug": "sheath_blight",
        "severity": "low",
        "risk_label_bn": "নিয়ন্ত্রিত (Low Risk)",
        "cases_breakdown": {
            "sheath_blight": 18,
            "leaf_blast": 10,
            "bacterial_leaf_blight": 7
        },
        "advisory_bn": "গাছের ঘনত্ব ঠিক রাখুন এবং সুষম পটাশ সার ব্যবহার করুন।"
    }
]


def load_outbreak_data() -> list:
    """Loads outbreak records from disk or returns default baseline."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    return data
        except Exception:
            pass
    # Initialize default
    save_outbreak_data(DEFAULT_OUTBREAKS)
    return DEFAULT_OUTBREAKS


def save_outbreak_data(data: list):
    """Persists outbreak records to disk atomically."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        tmp_file = DATA_FILE + ".tmp"
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)
        os.rename(tmp_file, DATA_FILE)
    except Exception as e:
        print(f"[RiceGuard Outbreak] Save error: {e}")


def get_outbreak_map_data(disease_filter: str = "all") -> dict:
    """
    Returns filtered geo-data, stats, and markers for the Leaflet outbreak map.
    """
    data = load_outbreak_data()
    filtered_points = []
    total_national_cases = 0
    active_districts_count = len(data)

    slug_filter = disease_filter.lower().replace(" ", "_").strip() if disease_filter else "all"

    for item in data:
        total_national_cases += item.get("total_cases", 0)

        # Filter check
        if slug_filter != "all":
            cases_for_disease = item.get("cases_breakdown", {}).get(slug_filter, 0)
            if cases_for_disease <= 0 and item.get("disease_slug") != slug_filter:
                continue

        filtered_points.append(item)

    return {
        "success": True,
        "total_national_cases": total_national_cases,
        "total_active_districts": active_districts_count,
        "filter": slug_filter,
        "points": filtered_points,
        "last_updated": time.strftime("%d %b %Y, %I:%M %p")
    }


def record_outbreak_case(district_name: str, disease_name: str) -> dict:
    """
    Increments real-time outbreak count for a district when any user anywhere diagnoses a disease.
    """
    if not disease_name or "healthy" in disease_name.lower():
        return get_outbreak_map_data("all")

    data = load_outbreak_data()
    d_slug = disease_name.lower().replace(" ", "_").strip()
    dist_clean = (district_name or "Dinajpur").strip().lower()

    matched = False
    target_item = None

    for item in data:
        if (item["district_en"].lower() == dist_clean or 
            item["district_bn"] == district_name or 
            dist_clean in item["district_en"].lower() or 
            item["id"] == dist_clean):
            target_item = item
            matched = True
            break

    # Fallback to Dinajpur or first granary if district name is arbitrary (e.g. Dhaka)
    if not matched and len(data) > 0:
        target_item = data[0]
        matched = True

    if target_item:
        target_item["total_cases"] = target_item.get("total_cases", 0) + 1
        breakdown = target_item.setdefault("cases_breakdown", {})
        breakdown[d_slug] = breakdown.get(d_slug, 0) + 1

        # Recalculate primary disease & severity
        if breakdown:
            top_dis = max(breakdown.items(), key=lambda x: x[1])[0]
            target_item["disease_slug"] = top_dis
        
        if target_item["total_cases"] >= 70:
            target_item["severity"] = "high"
            target_item["risk_label_bn"] = "উচ্চ সতর্কতা (High Alert)"
        elif target_item["total_cases"] >= 40:
            target_item["severity"] = "medium"
            target_item["risk_label_bn"] = "মাঝারি ঝুঁকি (Moderate Risk)"
        else:
            target_item["severity"] = "low"
            target_item["risk_label_bn"] = "নিয়ন্ত্রিত (Low Risk)"

        save_outbreak_data(data)

    return get_outbreak_map_data("all")
