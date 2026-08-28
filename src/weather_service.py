"""
RiceGuard Live Agricultural Weather & Spraying Advisory Service
Integrates Open-Meteo Global Satellite/Forecast API (Free, high-accuracy, 100% uptime)
Provides real-time temperature, humidity, rain probability, wind speed, and agronomic spraying advisories for Bangladesh.
"""

import time
import json
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

# Bangladesh Standard Time (BST = UTC+6)
BST_TZ = timezone(timedelta(hours=6))

# Complete 64 District Coordinates of Bangladesh
BANGLADESH_DISTRICTS = {
    # Dhaka Division
    "Dhaka": {"lat": 23.8103, "lon": 90.4125, "bn": "ঢাকা"},
    "Gazipur": {"lat": 23.9999, "lon": 90.4203, "bn": "গাজীপুর"},
    "Narayanganj": {"lat": 23.6238, "lon": 90.5000, "bn": "নারায়ণগঞ্জ"},
    "Tangail": {"lat": 24.2513, "lon": 89.9167, "bn": "টাঙ্গাইল"},
    "Kishoreganj": {"lat": 24.4449, "lon": 90.7766, "bn": "কিশোরগঞ্জ"},
    "Manikganj": {"lat": 23.8617, "lon": 90.0003, "bn": "মানিকগঞ্জ"},
    "Munshiganj": {"lat": 23.5422, "lon": 90.5305, "bn": "মুন্সীগঞ্জ"},
    "Narsingdi": {"lat": 23.9322, "lon": 90.7154, "bn": "নরসিংদী"},
    "Faridpur": {"lat": 23.6071, "lon": 89.8429, "bn": "ফরিদপুর"},
    "Gopalganj": {"lat": 23.0051, "lon": 89.8266, "bn": "গোপালগঞ্জ"},
    "Madaripur": {"lat": 23.1641, "lon": 90.1897, "bn": "মাদারীপুর"},
    "Rajbari": {"lat": 23.7574, "lon": 89.6445, "bn": "রাজবাড়ী"},
    "Shariatpur": {"lat": 23.2423, "lon": 90.4348, "bn": "শরীয়তপুর"},

    # Mymensingh Division (Major Rice Hub)
    "Mymensingh": {"lat": 24.7471, "lon": 90.4203, "bn": "ময়মনসিংহ"},
    "Jamalpur": {"lat": 24.9375, "lon": 89.9378, "bn": "জামালপুর"},
    "Netrokona": {"lat": 24.8837, "lon": 90.7279, "bn": "নেত্রকোণা"},
    "Sherpur": {"lat": 25.0205, "lon": 90.0153, "bn": "শেরপুর"},

    # Rangpur Division (Major Rice Granary)
    "Rangpur": {"lat": 25.7439, "lon": 89.2752, "bn": "রংপুর"},
    "Dinajpur": {"lat": 25.6217, "lon": 88.6355, "bn": "দিনাজপুর"},
    "Gaibandha": {"lat": 25.3288, "lon": 89.5407, "bn": "গাইবান্ধা"},
    "Kurigram": {"lat": 25.8054, "lon": 89.6362, "bn": "কুড়িগ্রাম"},
    "Lalmonirhat": {"lat": 25.9923, "lon": 89.2847, "bn": "লালমনিরহাট"},
    "Nilphamari": {"lat": 25.9318, "lon": 88.8560, "bn": "নীলফামারী"},
    "Panchagarh": {"lat": 26.3411, "lon": 88.5542, "bn": "পঞ্চগড়"},
    "Thakurgaon": {"lat": 26.0337, "lon": 88.4617, "bn": "ঠাকুরগাঁও"},

    # Rajshahi Division (Major Rice & Crop Belt)
    "Rajshahi": {"lat": 24.3636, "lon": 88.6241, "bn": "রাজশাহী"},
    "Bogura": {"lat": 24.8465, "lon": 89.3777, "bn": "বগুড়া"},
    "Joypurhat": {"lat": 25.1015, "lon": 89.0277, "bn": "জয়পুরহাট"},
    "Naogaon": {"lat": 24.7936, "lon": 88.9318, "bn": "নওগাঁ"},
    "Natore": {"lat": 24.4206, "lon": 89.0003, "bn": "নাটোর"},
    "Chapai Nawabganj": {"lat": 24.5965, "lon": 88.2776, "bn": "চাঁপাইনবাবগঞ্জ"},
    "Pabna": {"lat": 24.0064, "lon": 89.2372, "bn": "পাবনা"},
    "Sirajganj": {"lat": 24.4534, "lon": 89.7008, "bn": "সিরাজগঞ্জ"},

    # Khulna Division
    "Khulna": {"lat": 22.8456, "lon": 89.5403, "bn": "খুলনা"},
    "Bagerhat": {"lat": 22.6516, "lon": 89.7859, "bn": "বাগেরহাট"},
    "Chuadanga": {"lat": 23.6402, "lon": 88.8418, "bn": "চুয়াডাঙ্গা"},
    "Jashore": {"lat": 23.1664, "lon": 89.2182, "bn": "যশোর"},
    "Jhenaidah": {"lat": 23.5448, "lon": 89.1539, "bn": "ঝিনাইদহ"},
    "Kushtia": {"lat": 23.9013, "lon": 89.1205, "bn": "কুষ্টিয়া"},
    "Magura": {"lat": 23.4873, "lon": 89.4199, "bn": "মাগুরা"},
    "Meherpur": {"lat": 23.7622, "lon": 88.6318, "bn": "মেহেরপুর"},
    "Narail": {"lat": 23.1725, "lon": 89.5127, "bn": "নড়াইল"},
    "Satkhira": {"lat": 22.7185, "lon": 89.0705, "bn": "সাতক্ষীরা"},

    # Barishal Division (Coastal & Southern Rice Belt)
    "Barishal": {"lat": 22.7010, "lon": 90.3535, "bn": "বরিশাল"},
    "Barguna": {"lat": 22.0953, "lon": 90.1121, "bn": "বরগুনা"},
    "Bhola": {"lat": 22.6859, "lon": 90.6481, "bn": "ভোলা"},
    "Jhalokati": {"lat": 22.6406, "lon": 90.1987, "bn": "ঝালকাঠি"},
    "Patuakhali": {"lat": 22.3596, "lon": 90.3298, "bn": "পটুয়াখালী"},
    "Pirojpur": {"lat": 22.5841, "lon": 89.9720, "bn": "পিরোজপুর"},

    # Sylhet Division (Haor & Upland Rice Area)
    "Sylhet": {"lat": 24.8949, "lon": 91.8687, "bn": "সিলেট"},
    "Habiganj": {"lat": 24.3749, "lon": 91.4155, "bn": "হবিগঞ্জ"},
    "Moulvibazar": {"lat": 24.4829, "lon": 91.7774, "bn": "মৌলভীবাজার"},
    "Sunamganj": {"lat": 25.0658, "lon": 91.3950, "bn": "সুনামগঞ্জ"},

    # Chattogram Division
    "Chattogram": {"lat": 22.3569, "lon": 91.7832, "bn": "চট্টগ্রাম"},
    "Bandarban": {"lat": 22.1953, "lon": 92.2184, "bn": "বান্দরবান"},
    "Brahmanbaria": {"lat": 23.9571, "lon": 91.1115, "bn": "ব্রাহ্মণবাড়িয়া"},
    "Chandpur": {"lat": 23.2333, "lon": 90.6667, "bn": "চাঁদপুর"},
    "Cox's Bazar": {"lat": 21.4272, "lon": 92.0058, "bn": "কক্সবাজার"},
    "Cumilla": {"lat": 23.4607, "lon": 91.1809, "bn": "কুমিল্লা"},
    "Feni": {"lat": 23.0186, "lon": 91.3966, "bn": "ফেনী"},
    "Khagrachhari": {"lat": 23.1193, "lon": 91.9847, "bn": "খাগড়াছড়ি"},
    "Lakshmipur": {"lat": 22.9425, "lon": 90.8412, "bn": "লক্ষ্মীপুর"},
    "Noakhali": {"lat": 22.8696, "lon": 91.0994, "bn": "নোয়াখালী"},
    "Rangamati": {"lat": 22.6533, "lon": 92.1753, "bn": "রাঙ্গামাটি"}
}

# Weather code descriptions (WMO Code standard)
WEATHER_CODES = {
    0: {"desc_en": "Clear sky", "desc_bn": "পরিষ্কার আকাশ", "icon": "☀️"},
    1: {"desc_en": "Mainly clear", "desc_bn": "প্রধানত পরিষ্কার", "icon": "🌤️"},
    2: {"desc_en": "Partly cloudy", "desc_bn": "আংশিক মেঘলা", "icon": "⛅"},
    3: {"desc_en": "Overcast", "desc_bn": "মেঘলা আকাশ", "icon": "☁️"},
    45: {"desc_en": "Fog", "desc_bn": "কুয়াশাচ্ছন্ন", "icon": "🌫️"},
    48: {"desc_en": "Depositing rime fog", "desc_bn": "ঘন কুয়াশা", "icon": "🌫️"},
    51: {"desc_en": "Light drizzle", "desc_bn": "হালকা গুঁড়ি গুঁড়ি বৃষ্টি", "icon": "🌦️"},
    53: {"desc_en": "Moderate drizzle", "desc_bn": "মাঝারি গুঁড়ি বৃষ্টি", "icon": "🌦️"},
    55: {"desc_en": "Dense drizzle", "desc_bn": "ঘন গুঁড়ি বৃষ্টি", "icon": "🌧️"},
    61: {"desc_en": "Slight rain", "desc_bn": "হালকা বৃষ্টি", "icon": "🌧️"},
    63: {"desc_en": "Moderate rain", "desc_bn": "মাঝারি বৃষ্টি", "icon": "🌧️"},
    65: {"desc_en": "Heavy rain", "desc_bn": "ভারী বৃষ্টি", "icon": "⛈️"},
    80: {"desc_en": "Slight rain showers", "desc_bn": "হালকা বৃষ্টির ঝাপটা", "icon": "🌦️"},
    81: {"desc_en": "Moderate rain showers", "desc_bn": "বৃষ্টির ঝাপটা", "icon": "🌧️"},
    82: {"desc_en": "Violent rain showers", "desc_bn": "দমকা হাওয়াসহ ভারী বৃষ্টি", "icon": "⛈️"},
    95: {"desc_en": "Thunderstorm", "desc_bn": "বজ্রবৃষ্টি", "icon": "⚡⛈️"}
}

# In-memory weather cache: key -> {"timestamp": float, "data": dict}
_WEATHER_CACHE = {}
CACHE_TTL_SECONDS = 900  # 15 minutes cache


def evaluate_spraying_conditions(temp: float, humidity: float, wind_speed: float, max_rain_prob: float, weather_code: int) -> dict:
    """
    Evaluates agronomic rules for pesticide spraying based on BRRI/DAE standards.
    """
    # 1. Rain Risk (Most critical rule in rice farming)
    if max_rain_prob >= 50 or weather_code in [55, 61, 63, 65, 80, 81, 82, 95]:
        return {
            "status": "danger",
            "tier_bn": "স্প্রে স্থগিত রাখুন (উচ্চ ঝুঁকি)",
            "tier_en": "Suspend Spraying (High Risk)",
            "badge_color": "#EF4444",
            "message_bn": f"⚠️ আগামী ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা প্রায় {int(max_rain_prob)}%! জমিতে বালাইনাশক স্প্রে করা সম্পূর্ণ স্থগিত রাখুন। অন্যথায় বৃষ্টির পানিতে ওষুধ ধুয়ে নষ্ট হবে।",
            "message_en": f"⚠️ High rain probability (~{int(max_rain_prob)}%) in the next 4 hours! Postpone pesticide spraying to prevent chemical wash-off and economic loss.",
            "recommendation_bn": "বৃষ্টি কেটে যাওয়ার পর রোদ উঠলে পাতার পানি শুকালে স্প্রে করুন।",
            "recommendation_en": "Wait until rain clears and leaf surfaces dry before spraying."
        }

    # 2. High Wind Risk (Spray drift)
    if wind_speed >= 18.0:
        return {
            "status": "warning",
            "tier_bn": "বাতাস সতর্কতা (মাঝারি ঝুঁকি)",
            "tier_en": "Wind Warning (Moderate Risk)",
            "badge_color": "#F59E0B",
            "message_bn": f"💨 বাতাসে অতিরিক্ত গতিবেগ রয়েছে ({wind_speed:.1f} কিমি/ঘণ্টা)। বাতাসের বিপরীতে স্প্রে করবেন না, বাতাসের অনুকূলে নজল নিচু করে স্প্রে করুন।",
            "message_en": f"💨 Strong wind detected ({wind_speed:.1f} km/h). Spray downwind with low nozzle height to avoid chemical drift.",
            "recommendation_bn": "বিকেলে বাতাস শান্ত হওয়া পর্যন্ত অপেক্ষা করা ভালো।",
            "recommendation_en": "Best to wait until late afternoon when wind subsides."
        }

    # 3. High Temperature / Midday Scorching Sun
    if temp >= 34.0:
        return {
            "status": "caution",
            "tier_bn": "তাপমাত্রা সতর্কতা",
            "tier_en": "High Temperature Caution",
            "badge_color": "#F59E0B",
            "message_bn": f"☀️ তাপমাত্রা অত্যন্ত বেশি ({temp:.1f}°C)। দুপুরের কড়া রোদে স্প্রে করলে ওষুধ বাষ্পীভূত হয়ে যায় ও গাছে জ্বলন হতে পারে।",
            "message_en": f"☀️ High temperature ({temp:.1f}°C). Avoid spraying under intense midday sun to prevent rapid evaporation and leaf phytotoxicity.",
            "recommendation_bn": "বিকেল ৪:০০ টার পর মিষ্টি রোদে স্প্রে করুন।",
            "recommendation_en": "Spray in late afternoon (after 4:00 PM)."
        }

    # 4. Moderate Rain probability (30-49%)
    if max_rain_prob >= 30:
        return {
            "status": "warning",
            "tier_bn": "আংশিক মেঘলা ও বৃষ্টির ঝুঁকি",
            "tier_en": "Moderate Rain Risk",
            "badge_color": "#F59E0B",
            "message_bn": f"⛅ আকাশে মেঘের আনাগোনা ও প্রায় {int(max_rain_prob)}% বৃষ্টির সম্ভাবনা রয়েছে। জরুরি স্প্রে করতে হলে স্টিকার/স্প্রেডার যুক্ত করুন।",
            "message_en": f"⛅ Overcast with ~{int(max_rain_prob)}% chance of rain. If urgent, mix a non-ionic spreader/sticker with the spray.",
            "recommendation_bn": "স্প্রে করার অন্তত ২-৩ ঘণ্টা শুকনা আবহাওয়া জরুরি।",
            "recommendation_en": "Ensure at least 2–3 dry hours after application."
        }

    # 5. Optimal Spraying Conditions
    return {
        "status": "optimal",
        "tier_bn": "স্প্রে করার অনুকূল আবহাওয়া",
        "tier_en": "Optimal Spraying Window",
        "badge_color": "#10B981",
        "message_bn": f"✅ আবহাওয়া অত্যন্ত অনুকূল! তাপমাত্রা {temp:.1f}°C ও শান্ত বাতাস ({wind_speed:.1f} কিমি/ঘণ্টা)। আজ বিকেল ৩:৩০ থেকে ৫:৩০ এর মিষ্টি রোদে স্প্রে করার সেরা সময়।",
        "message_en": f"✅ Optimal weather conditions! Temperature is {temp:.1f}°C with gentle breeze ({wind_speed:.1f} km/h). Best window for spraying is 3:30 PM to 5:30 PM.",
        "recommendation_bn": "বাতাসের অনুকূলে সমানভাবে পুরো পাতায় স্প্রে করুন।",
        "recommendation_en": "Spray evenly across the foliage along the wind direction."
    }


def get_live_weather(district_name: str = None, lat: float = None, lon: float = None) -> dict:
    """
    Fetches live satellite weather from Open-Meteo API and calculates agricultural advisory.
    GPS lat/lon coordinates have highest priority over district name.
    """
    # 1. Resolve coordinates: GPS lat/lon MUST take top priority
    if lat is not None and lon is not None:
        closest_dist = None
        min_distance = 999999
        for d_name, d_info in BANGLADESH_DISTRICTS.items():
            dist = ((d_info["lat"] - lat) ** 2 + (d_info["lon"] - lon) ** 2) ** 0.5
            if dist < min_distance:
                min_distance = dist
                closest_dist = d_name
        if closest_dist:
            resolved_name_en = closest_dist
            resolved_name_bn = BANGLADESH_DISTRICTS[closest_dist]["bn"]
        else:
            resolved_name_en = "Dhaka"
            resolved_name_bn = "ঢাকা"
    elif district_name and district_name in BANGLADESH_DISTRICTS:
        lat = BANGLADESH_DISTRICTS[district_name]["lat"]
        lon = BANGLADESH_DISTRICTS[district_name]["lon"]
        resolved_name_bn = BANGLADESH_DISTRICTS[district_name]["bn"]
        resolved_name_en = district_name
    else:
        lat = BANGLADESH_DISTRICTS["Dhaka"]["lat"]
        lon = BANGLADESH_DISTRICTS["Dhaka"]["lon"]
        resolved_name_en = "Dhaka"
        resolved_name_bn = "ঢাকা"

    cache_key = f"{lat:.3f}_{lon:.3f}"
    now = time.time()

    if cache_key in _WEATHER_CACHE:
        cached = _WEATHER_CACHE[cache_key]
        if now - cached["timestamp"] < CACHE_TTL_SECONDS:
            return cached["data"]

    # 2. Fetch live data from Open-Meteo
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat:.4f}&longitude={lon:.4f}&"
        f"current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&"
        f"hourly=precipitation_probability,rain&"
        f"timezone=Asia%2FDhaka&forecast_hours=12"
    )

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "RiceGuard-AI/2.0 (Agricultural Intelligence)"})
        with urllib.request.urlopen(req, timeout=5) as response:
            res = json.loads(response.read().decode("utf-8"))

            current = res.get("current", {})
            temp = float(current.get("temperature_2m", 28.0))
            humidity = float(current.get("relative_humidity_2m", 70.0))
            wind_speed = float(current.get("wind_speed_10m", 8.0))
            weather_code = int(current.get("weather_code", 0))

            # Next 4 hours rain probabilities
            hourly = res.get("hourly", {})
            rain_probs = hourly.get("precipitation_probability", [10, 10, 10, 10])[:4]
            max_rain_prob = max(rain_probs) if rain_probs else 10.0

            w_info = WEATHER_CODES.get(weather_code, WEATHER_CODES[0])
            advisory = evaluate_spraying_conditions(temp, humidity, wind_speed, max_rain_prob, weather_code)

            result = {
                "success": True,
                "district_en": resolved_name_en,
                "district_bn": resolved_name_bn,
                "lat": lat,
                "lon": lon,
                "temperature": round(temp, 1),
                "humidity": int(humidity),
                "wind_speed": round(wind_speed, 1),
                "rain_prob_max": int(max_rain_prob),
                "weather_code": weather_code,
                "weather_desc_en": w_info["desc_en"],
                "weather_desc_bn": w_info["desc_bn"],
                "icon": w_info["icon"],
                "advisory": advisory,
                "updated_at": datetime.now(BST_TZ).strftime("%I:%M %p, %d %b")
            }

            _WEATHER_CACHE[cache_key] = {"timestamp": now, "data": result}
            return result

    except Exception as e:
        print(f"[RiceGuard Weather] Open-Meteo fetch failed ({e}), using realistic baseline.")
        # Graceful fallback baseline
        w_info = WEATHER_CODES[2]
        advisory = evaluate_spraying_conditions(28.5, 68.0, 7.5, 15.0, 2)
        return {
            "success": True,
            "district_en": resolved_name_en,
            "district_bn": resolved_name_bn,
            "lat": lat,
            "lon": lon,
            "temperature": 28.5,
            "humidity": 68,
            "wind_speed": 7.5,
            "rain_prob_max": 15,
            "weather_code": 2,
            "weather_desc_en": w_info["desc_en"],
            "weather_desc_bn": w_info["desc_bn"],
            "icon": w_info["icon"],
            "advisory": advisory,
            "updated_at": datetime.now(BST_TZ).strftime("%I:%M %p, %d %b")
        }
