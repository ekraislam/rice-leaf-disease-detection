"""
Botanical and Agronomic Disease Knowledge Base
Contains scientific descriptions, symptoms, causes, management plans, dosages, and translations
for all 8 rice leaf conditions classified by the ResNet18 model.
"""

DISEASE_DATABASE = {
    "Bacterial Leaf Blight": {
        "name_en": "Bacterial Leaf Blight",
        "name_bn": "ব্যাকটেরিয়াল পাতা পোড়া রোগ",
        "pathogen": "Xanthomonas oryzae pv. oryzae",
        "severity_en": "High Risk",
        "severity_bn": "উচ্চ ঝুঁকি",
        "severity_color": "#DC2626",
        "chemical_product_en": "Copper Oxychloride / Streptocycline",
        "chemical_product_bn": "কপার অক্সিক্লোরাইড / স্ট্রেপ্টোসাইক্লিন",
        "dosage_rate_per_liter": 2.0,
        "dosage_unit": "g",
        "overview_en": "A destructive bacterial disease affecting rice crops globally. It attacks leaf tissue leading to wilting, reduced tillering, and significant grain yield loss if unchecked during early growth stages.",
        "overview_bn": "একটি মারাত্মক ব্যাকটেরিয়াজনিত রোগ যা বিশ্বব্যাপী ধানের ব্যাপক ক্ষতি করে। এটি পাতার টিস্যু আক্রমণ করে পাতা শুকিয়ে ফেলে এবং ফলন মারাত্মকভাবে কমিয়ে দেয়।",
        "symptoms_en": [
            "Water-soaked yellowish-green stripes beginning from leaf tips and margins",
            "Lesions expand with wavy margins, turning milky-white to grayish-brown",
            "Bacterial ooze droplets (amber-colored beads) visible on young lesions in morning dew",
            "Severe infection causes 'kresek' (seedling wilting and systemic dying)"
        ],
        "symptoms_bn": [
            "পাতার ডগা ও ধার থেকে ভেজা হলুদাভ-সবুজ ডোরাকাটা দাগ শুরু হয়",
            "দাগগুলো ঢেউ খেলানো প্রান্তসহ প্রসারিত হয়ে সাদাটে-ধূসর বর্ণ ধারণ করে",
            "ভোরের শিশিরে দাগের ওপর আঠালো ব্যাকটেরিয়াল রস (অ্যাম্বার রঙ) দেখা যায়",
            "মারাত্মক সংক্রমণে চারা মারা যায় যাকে 'ক্রিসেক' অবস্থা বলে"
        ],
        "causes_en": [
            "Warm temperatures (25–34°C) with high relative humidity (>85%)",
            "Excessive nitrogen (Urea) fertilizer application without balanced Potassium",
            "Rainstorms, typhoon winds, and irrigation water facilitating bacterial spread",
            "Clipping seedling tips during transplanting"
        ],
        "causes_bn": [
            "উষ্ণ তাপমাত্রা (২৫-৩৪°সে) এবং অতিরিক্ত আর্দ্রতা (>৮৫%)",
            "পটাশ ছাড়া অতিরিক্ত ইউরিয়া সারের একপেশে ব্যবহার",
            "ঝড়-বৃষ্টি এবং সেচের পানির মাধ্যমে ব্যাকটেরিয়ার দ্রুত বিস্তার",
            "চারা রোপণের সময় পাতার ডগা কেটে ফেলা"
        ],
        "management_en": {
            "chemical": "Spray Copper Oxychloride 50 WP (2 g/L) or Streptocycline (0.1 g/L) + Copper Hydroxide (2 g/L) at early symptom appearance.",
            "cultural": "Drain stagnant field water for 3–4 days; balance nitrogen with extra Muriate of Potash (MOP); avoid clipping seedling tips.",
            "biological": "Seed treatment with biocontrol agent Pseudomonas fluorescens (10 g/kg seed)."
        },
        "management_bn": {
            "chemical": "লক্ষণ দেখা মাত্রই কপার অক্সিক্লোরাইড (প্রতি লিটারে ২ গ্রাম) অথবা স্ট্রেপ্টোসাইক্লিন + কপার হাইড্রোক্সাইড স্প্রে করুন।",
            "cultural": "জমির অতিরিক্ত পানি ৩-৪ দিন নিষ্কাশন করুন; ইউরিয়া কমিয়ে পটাশ সার প্রয়োগ বাড়ান; চারা রোপণের সময় ডগা কাটা বন্ধ করুন।",
            "biological": "সিউডোমোনাস ফ্লুরোসেন্স (১০ গ্রাম/কেজি বীজ) দিয়ে বীজ শোধন করুন।"
        }
    },

    "Brown Spot": {
        "name_en": "Brown Spot",
        "name_bn": "বাদামী দাগ রোগ",
        "pathogen": "Bipolaris oryzae (Helminthosporium oryzae)",
        "severity_en": "Moderate to High Risk",
        "severity_bn": "মাঝারি থেকে উচ্চ ঝুঁকি",
        "severity_color": "#D97706",
        "chemical_product_en": "Tilt 25 EC (Propiconazole) / Nativo 75 WG",
        "chemical_product_bn": "টিল্ট ২৫ ইসি (প্রপিকোনাজল) / নেটিভো ৭৫ ডব্লিউজি",
        "dosage_rate_per_liter": 1.0,
        "dosage_unit": "ml",
        "overview_en": "A widespread fungal disease historically linked to severe food crises. It primarily indicates nutrient deficiencies in the soil and attacks seedlings, leaves, and panicles.",
        "overview_bn": "একটি অতি পরিচিত ছত্রাকজনিত রোগ যা প্রধানত মাটিতে পুষ্টি উপাদানের অভাব থাকলে দেখা দেয়। এটি চারা, পাতা এবং ধানের শীষে আক্রমণ করে।",
        "symptoms_en": [
            "Small, oval to circular dark-brown spots uniformly scattered on leaf blades",
            "Fully developed spots have a grayish-white center with a prominent yellow halo",
            "Grains turn discolored, spotted, and poorly filled with reduced milling quality"
        ],
        "symptoms_bn": [
            "পাতার ওপর ছোট, ডিম্বাকৃতি বা গোলাকার গাঢ় বাদামী দাগ ছড়িয়ে থাকে",
            "বড় দাগের কেন্দ্র ধূসর-সাদা এবং চারপাশে সুস্পষ্ট হলুদ বলয় দেখা যায়",
            "ধানের দানায় কালো দাগ পড়ে এবং চাল চিটা বা অপুষ্ট হয়"
        ],
        "causes_en": [
            "Nutrient-deficient soils (lack of Potassium, Silicon, Manganese, Zinc)",
            "Drought stress, irregular irrigation, or poor soil organic matter",
            "Infected seed sources and humid cloud conditions"
        ],
        "causes_bn": [
            "মাটিতে পটাশিয়াম, সিলিকন, জিংক ও জৈব সারের তীব্র ঘাটতি",
            "খরা বা অনিয়মিত সেচ এবং পানির সংকট",
            "সংক্রমিত বীজ এবং মেঘলা আর্দ্র আবহাওয়া"
        ],
        "management_en": {
            "chemical": "Foliar spray with Propiconazole 25 EC (Tilt - 1 ml/L) or Nativo 75 WG (0.6 g/L) or Mancozeb 75 WP (2.5 g/L).",
            "cultural": "Apply balanced fertilizer with split Potash (MOP) and Zinc Sulphate; maintain proper water level in field.",
            "biological": "Seed treatment with Trichoderma harzianum or hot water treatment (52–54°C for 15 mins)."
        },
        "management_bn": {
            "chemical": "প্রপিকোনাজল ২৫ ইসি (টিল্ট - ১ মিলি/লিটার) অথবা নেটিভো (০.৬ গ্রাম/লিটার) স্প্রে করুন।",
            "cultural": "সুষম সার ব্যবহার করুন, বিশেষ করে পটাশ ও দস্তা সার কিস্তিতে দিন; জমিতে পর্যাপ্ত সেচ নিশ্চিত করুন।",
            "biological": "ট্রাইকোডার্মা দিয়ে বীজ শোধন করুন অথবা কুসুম গরম পানিতে (৫২-৫৪°সে) ১৫ মিনিট বীজ ভিজিয়ে রাখুন।"
        }
    },

    "Healthy Rice Leaf": {
        "name_en": "Healthy Rice Leaf",
        "name_bn": "সুস্থ ধানের পাতা",
        "pathogen": "None (Optimum Botanical Health)",
        "severity_en": "Normal / Healthy",
        "severity_bn": "সুস্থ ও স্বাভাবিক",
        "severity_color": "#10B981",
        "chemical_product_en": "No pesticide needed",
        "chemical_product_bn": "কোনো বালাইনাশকের প্রয়োজন নেই",
        "dosage_rate_per_liter": 0.0,
        "dosage_unit": "ml",
        "overview_en": "The analyzed sample displays no detectable pathogenic lesions, discolorations, or pest feeding streaks. The leaf lamina exhibits vibrant chlorophyll distribution and vigorous physiological posture.",
        "overview_bn": "পরীক্ষিত পাতায় কোনো রোগজীবাণু বা পোকার আক্রমণের লক্ষণ পাওয়া যায়নি। পাতাটি স্বাস্থ্যকর ও সতেজ রয়েছে।",
        "symptoms_en": [
            "Uniform green leaf pigmentation with clear vascular venation",
            "No necrotic lesions, chlorotic halos, or mycelial mats",
            "Normal turgidity and healthy leaf sheath attachments"
        ],
        "symptoms_bn": [
            "সুস্পষ্ট শিরাসহ পাতার গাঢ় সবুজ ও সতেজ বর্ণ",
            "কোনো প্রকার পচা দাগ, হলুদ বলয় বা পোকার ক্ষত নেই",
            "স্বাভাবিক বৃদ্ধি ও সুস্থ খোল"
        ],
        "causes_en": [
            "Balanced soil fertility and optimal NPK management",
            "Effective preventative weed and water management practices"
        ],
        "causes_bn": [
            "মাটির সুষম উর্বরতা ও সঠিক সময়ে সার প্রয়োগ",
            "সঠিক সেচ ও রোগমুক্ত পরিবেশ"
        ],
        "management_en": {
            "chemical": "No chemical pesticide required. Avoid prophylactic pesticide overuse to preserve beneficial predatory insects.",
            "cultural": "Maintain alternate wetting and drying (AWD) irrigation; monitor weekly for early symptom emergence.",
            "biological": "Promote beneficial predators like dragonflies, spiders, and ladybird beetles."
        },
        "management_bn": {
            "chemical": "কোনো কীটনাশক বা ছত্রাকনাশক স্প্রে করার প্রয়োজন নেই। অপ্রয়োজনীয় ওষুধ ব্যবহার এড়িয়ে চলুন।",
            "cultural": "পরিমিত সেচ দিন এবং নিয়মিত ক্ষেত পরিদর্শন করুন।",
            "biological": "উপকারী পোকা ও মাকড়সা সংরক্ষণ করুন।"
        }
    },

    "Leaf Blast": {
        "name_en": "Leaf Blast",
        "name_bn": "পাতা ব্লাস্ট রোগ",
        "pathogen": "Pyricularia oryzae (Magnaporthe oryzae)",
        "severity_en": "Critical Emergency",
        "severity_bn": "জরুরী মারাত্মক ঝুঁকি",
        "severity_color": "#EF4444",
        "chemical_product_en": "Trooper 75 WP (Tricyclazole) / Amistar Top",
        "chemical_product_bn": "ট্রুপার ৭৫ ডব্লিউপি (ট্রাইসাইক্লাজল) / অ্যামিস্টার টপ",
        "dosage_rate_per_liter": 0.75,
        "dosage_unit": "g",
        "overview_en": "The most catastrophic fungal disease of rice. It spreads rapidly via airborne conidia and can destroy entire fields within days under favorable weather if not intervened immediately.",
        "overview_bn": "ধানের সবচেয়ে মারাত্মক ছত্রাকজনিত রোগ। বাতাসের মাধ্যমে ছত্রাকের স্পোর ছড়িয়ে পড়ে এবং অনুকূল আবহাওয়ায় কয়েক দিনের মধ্যে পুরো ক্ষেত ছারখার করতে পারে।",
        "symptoms_en": [
            "Classic diamond or spindle-shaped (eye-like) lesions with pointed ends",
            "Centers of spots are grayish-white with dark brown or reddish borders",
            "Lesions coalesce causing rapid leaf desiccation and field 'burnt' appearance"
        ],
        "symptoms_bn": [
            "পাতায় চোখের মতো বা তীরের ফলার মতো দুই প্রান্ত সরু বাদামী দাগ",
            "দাগের কেন্দ্র ধূসর-সাদা এবং চারপাশ গাঢ় লালচে-বাদামী বর্ণের হয়",
            "একাধিক দাগ একত্রিত হয়ে পুরো পাতা পুড়ে যাওয়ার মতো শুকিয়ে যায়"
        ],
        "causes_en": [
            "Excessive urea top-dressing creating succulent leaf tissues",
            "Extended leaf wetness (>10 hours) and high relative humidity (>90%)",
            "Cool night temperatures (17–22°C) combined with warm overcast daytime"
        ],
        "causes_bn": [
            "অতিরিক্ত মাত্রায় ইউরিয়া সার প্রয়োগ",
            "টানা শিশিরভেজা পাতা (>১০ ঘণ্টা) এবং উচ্চ আর্দ্রতা (>৯০%)",
            "দিনের বেলা গরম ও রাতে ঠান্ডা আবহাওয়া এবং গুঁড়ি গুঁড়ি বৃষ্টি"
        ],
        "management_en": {
            "chemical": "Emergency foliar spray with Tricyclazole 75 WP (Trooper / Beam - 0.75 g/L) or Isoprothiolane 40 EC (2 ml/L) or Amistar Top (1 ml/L).",
            "cultural": "Immediately withhold urea application; maintain 2–3 inches standing water in field; burn infected stubble.",
            "biological": "Grow certified blast-tolerant varieties; apply silicon amendments to strengthen epidermal silica cells."
        },
        "management_bn": {
            "chemical": "জরুরী ভিত্তিতে ট্রাইসাইক্লাজল ৭৫ ডব্লিউপি (ট্রুপার/বীম - ০.৭৫ গ্রাম/লিটার) অথবা অ্যামিস্টার টপ (১ মিলি/লিটার) বিকেলে স্প্রে করুন।",
            "cultural": "ইউরিয়া সারের উপরিপ্রয়োগ অবিলম্বে বন্ধ রাখুন; জমিতে ২-৩ ইঞ্চি পানি ধরে রাখুন।",
            "biological": "ব্লাস্ট সহনশীল জাত চাষ করুন এবং জমিতে সিলিকন সমৃদ্ধ সার প্রয়োগ করুন।"
        }
    },

    "Leaf scald": {
        "name_en": "Leaf Scald",
        "name_bn": "লিফ স্ক্যাল্ড (পাতা ঝলকানো)",
        "pathogen": "Microdochium oryzae (Rhynchosporium oryzae)",
        "severity_en": "Moderate Risk",
        "severity_bn": "মাঝারি ঝুঁকি",
        "severity_color": "#EA580C",
        "chemical_product_en": "Carbendazim 50 WP / Propiconazole",
        "chemical_product_bn": "কার্বেনডাজিম ৫০ ডব্লিউপি / প্রপিকোনাজল",
        "dosage_rate_per_liter": 1.5,
        "dosage_unit": "g",
        "overview_en": "A fungal foliar disease that causes blighting from leaf tips and margins. It impairs photosynthetic capacity and causes premature senescence.",
        "overview_bn": "একটি পাতা ঝলকানো ছত্রাকজনিত রোগ যা পাতার ডগা ও ধার থেকে শুরু হয়। এটি গাছের সালোকসংশ্লেষণ কমিয়ে দেয় এবং পাতা দ্রুত শুকিয়ে ফেলে।",
        "symptoms_en": [
            "Starts as water-soaked lesions from leaf tip or margin expanding downward",
            "Distinct chevron-shaped zonate patterns with alternating light and dark brown bands",
            "Infected area dries out with bleached, scalded appearance"
        ],
        "symptoms_bn": [
            "পাতার ডগা বা প্রান্ত থেকে ভেজা দাগ শুরু হয়ে নিচের দিকে বাড়ে",
            "ব্যান্ডের মতো হালকা ও গাঢ় বাদামী স্তরে স্তরে দাগ (Chevron pattern) সৃষ্টি হয়",
            "আক্রান্ত অংশ রোদে পুড়ে যাওয়ার মতো ঝলসে শুকিয়ে যায়"
        ],
        "causes_en": [
            "Dense canopy planting with restricted airflow",
            "High nitrogen rates combined with frequent rain or heavy dew"
        ],
        "causes_bn": [
            "গাছ খুব ঘন করে রোপণ করা এবং আলো-বাতাসের অভাব",
            "অতিরিক্ত নাইট্রোজেন সার এবং মেঘলা ভেজা আবহাওয়া"
        ],
        "management_en": {
            "chemical": "Spray Carbendazim 50 WP (1.5 g/L) or Propiconazole (1 ml/L) or Copper Hydroxide (2 g/L).",
            "cultural": "Maintain optimal seedling spacing (20 × 15 cm); balance nitrogen with potassium; clear weed hosts.",
            "biological": "Use hot water seed sanitation before sowing."
        },
        "management_bn": {
            "chemical": "কার্বেনডাজিম (১.৫ গ্রাম/লিটার) অথবা প্রপিকোনাজল (১ মিলি/লিটার) স্প্রে করুন।",
            "cultural": "চারা রোপণের সঠিক দূরত্ব (২০ × ১৫ সেমি) বজায় রাখুন; সুষম পটাশ সার দিন।",
            "biological": "বীজ বপনের আগে গরম পানি দিয়ে বীজ শোধন করে নিন।"
        }
    },

    "Narrow Brown Leaf Spot": {
        "name_en": "Narrow Brown Leaf Spot",
        "name_bn": "সরু বাদামী দাগ রোগ",
        "pathogen": "Cercospora janseana (Passalora janseana)",
        "severity_en": "Moderate Risk",
        "severity_bn": "মাঝারি ঝুঁকি",
        "severity_color": "#B45309",
        "chemical_product_en": "Propiconazole 25 EC (Tilt) / Azoxystrobin",
        "chemical_product_bn": "প্রপিকোনাজল ২৫ ইসি (টিল্ট) / অ্যাজোক্সিস্ট্রবিন",
        "dosage_rate_per_liter": 1.0,
        "dosage_unit": "ml",
        "overview_en": "A late-season fungal disease prevalent during ripening stages. It accelerates premature leaf death and reduces grain filling efficiency.",
        "overview_bn": "ধানের জীবনকালের শেষের দিকে (দুধ বা পাকা পর্যায়ে) দেখা যাওয়া একটি ছত্রাকজনিত রোগ। এটি অকালে পাতা মেরে ফেলে এবং ধানের দানা অপুষ্ট করে।",
        "symptoms_en": [
            "Short, narrow, linear reddish-brown to dark brown streaks (2–10 mm long, 1 mm wide)",
            "Lesions run strictly parallel to leaf veins",
            "Severe cases cause premature lodging and sheath discoloration"
        ],
        "symptoms_bn": [
            "পাতার শিরা বরাবর খাটো, চিকন, লম্বাটে লালচে-বাদামী রেখা (২-১০ মিমি লম্বা)",
            "দাগগুলো পাতার শিরার সমান্তরালে অবস্থান করে",
            "তীব্র হলে পাতা অকালে শুকিয়ে গাছ হেলে পড়ে"
        ],
        "causes_en": [
            "Nutrient depletion in aging soil during panicle filling",
            "Warm days with high relative humidity and low potassium levels"
        ],
        "causes_bn": [
            "গাছের বয়স বাড়ার সাথে সাথে মাটিতে পুষ্টি ও পটাশের ঘাটতি",
            "উষ্ণ আবহাওয়া এবং বাতাসে অতিরিক্ত জলীয় বাষ্প"
        ],
        "management_en": {
            "chemical": "Spray Propiconazole 25 EC (1 ml/L) or Azoxystrobin (1 ml/L) at boot stage or early panicle emergence.",
            "cultural": "Ensure top-dressing of Potash (MOP) at panicle initiation stage; avoid late-stage moisture stress.",
            "biological": "Rotate crops and incorporate rice straw into soil with microbial decomposers."
        },
        "management_bn": {
            "chemical": "থোড় আসার সময় প্রপিকোনাজল (১ মিলি/লিটার) অথবা অ্যাজোক্সিস্ট্রবিন স্প্রে করুন।",
            "cultural": "কাইচ থোড় আসার সময় শেষ কিস্তির পটাশ সার নিশ্চিত করুন; জমিতে পানির অভাব হতে দেবেন না।",
            "biological": "ফসল কাটার পর ট্রাইকোডার্মা দিয়ে নাড়া পচিয়ে মাটির উর্বরতা বাড়ান।"
        }
    },

    "Rice Hispa": {
        "name_en": "Rice Hispa",
        "name_bn": "ধানের পামরী পোকা",
        "pathogen": "Dicladispa armigera (Insect Pest)",
        "severity_en": "High Infestation Risk",
        "severity_bn": "উচ্চ পোকার আক্রমণ",
        "severity_color": "#C2410C",
        "chemical_product_en": "Cartap Hydrochloride 50 SP (Suntap) / Chlorpyrifos",
        "chemical_product_bn": "কার্টাপ হাইড্রোক্লোরাইড ৫০ এসপি (সানট্যাপ) / ক্লোরপাইরিফস",
        "dosage_rate_per_liter": 1.5,
        "dosage_unit": "g",
        "overview_en": "A major coleopteran insect pest of rice in South Asia. Both spiny adult beetles and tunneling larvae feed aggressively on leaf chlorophyll.",
        "overview_bn": "দক্ষিণ এশিয়ার অন্যতম ক্ষতিকর ধানের পোকা। কাঁটাযুক্ত পূর্ণাঙ্গ পোকা এবং পাতার ভেতর থাকা কীড়া উভয়েই পাতার সবুজ অংশ খেয়ে সাদা করে ফেলে।",
        "symptoms_en": [
            "White parallel streaks and transparent blisters on leaf surface",
            "Adults scrape upper epidermis leaving only lower translucent skin",
            "Leaf tips wither and infected fields look whitish-burnt from a distance"
        ],
        "symptoms_bn": [
            "পাতার ওপর সমান্তরাল সাদা দাগ এবং ফোসকার মতো সুড়ঙ্গ",
            "পূর্ণাঙ্গ পোকা পাতার সবুজ অংশ কুরে কুরে খায় ফলে পাতা সাদা পর্দার মতো হয়ে যায়",
            "দূর থেকে দেখলে পুরো ক্ষেত ঝলসে বা রোদে শুকিয়ে যাওয়ার মতো সাদা দেখায়"
        ],
        "causes_en": [
            "Warm humid cloudy weather with dense lush crop growth",
            "Heavy unmetered urea application attracting pest populations",
            "Grassy weeds along field levees harboring overwintering beetles"
        ],
        "causes_bn": [
            "উষ্ণ ও মেঘলা আবহাওয়া এবং অতিরিক্ত ইউরিয়া ব্যবহারের ফলে কচি পাতার আধিক্য",
            "আইলে বা জমিতে ঘাসজাতীয় আগাছার উপস্থিতি যেখানে পোকা আশ্রয় নেয়"
        ],
        "management_en": {
            "chemical": "Spray Chlorpyrifos 20 EC (2 ml/L) or Cartap Hydrochloride 50 SP (Suntap - 1.5 g/L) or Thiamethoxam (0.3 g/L) when pest threshold exceeds 4–5 adults/hill.",
            "cultural": "Sweep-netting to catch and destroy adult beetles; clip and burn leaf tips before seedling transplanting.",
            "biological": "Encourage natural parasitoids like Trichogramma and entomopathogenic fungi Beauveria bassiana."
        },
        "management_bn": {
            "chemical": "প্রতি গোছায় ৪-৫টি পোকা দেখা গেলে কার্টাপ (সানট্যাপ - ১.৫ গ্রাম/লিটার) অথবা ক্লোরপাইরিফস (২ মিলি/লিটার) স্প্রে করুন।",
            "cultural": "সুইপ নেট (হাতা জাল) দিয়ে পোকা ধরে মেরে ফেলুন; চারা রোপণের আগে আক্রান্ত ডগা কেটে ধ্বংস করুন।",
            "biological": "বিউভেরিয়া ব্যাসিয়ানা জাতীয় উপকারী জৈব ছত্রাক স্প্রে করুন।"
        }
    },

    "Sheath Blight": {
        "name_en": "Sheath Blight",
        "name_bn": "খোল পোড়া রোগ",
        "pathogen": "Rhizoctonia solani (Soil-borne Fungus)",
        "severity_en": "High Risk",
        "severity_bn": "উচ্চ ঝুঁকি",
        "severity_color": "#B91C1C",
        "chemical_product_en": "Hexaconazole 5 EC (Contaf) / Validamycin 3L",
        "chemical_product_bn": "হেক্সাকোনাজল ৫ ইসি (কনটাফ) / ভ্যালিডামাইসিন ৩এল",
        "dosage_rate_per_liter": 2.0,
        "dosage_unit": "ml",
        "overview_en": "A soil-borne and water-borne fungal disease that attacks leaf sheaths near the water line, creating snake-skin patterns that climb up into the crop canopy.",
        "overview_bn": "মাটি ও পানির মাধ্যমে ছড়ানো মারাত্মক ছত্রাকজনিত রোগ। এটি পানির কাছাকাছি কাণ্ডের খোলে সাপের চামড়ার মতো দাগ সৃষ্টি করে উপরের দিকে ছড়িয়ে পড়ে।",
        "symptoms_en": [
            "Greenish-gray oval or irregular water-soaked spots on lower leaf sheaths near water line",
            "Spots enlarge with dark reddish-brown borders and grayish-white bleached centers",
            "Sclerotia (small brown mustard-seed-like grains) form on infected tissue"
        ],
        "symptoms_bn": [
            "পানির সামান্য উপরে কাণ্ডের খোলে ডিম্বাকৃতি ধূসর-সবুজ ভেজা দাগ",
            "দাগগুলো সাপের খোলসের মতো গাঢ় বাদামী বর্ডারসহ প্রসারিত হয়",
            "আক্রান্ত অংশে সরিষার দানার মতো ছোট ছোট বাদামী স্কেলেরোসিয়া দেখা যায়"
        ],
        "causes_en": [
            "High temperature (28–32°C) combined with high canopy humidity (>85%)",
            "Dense plant spacing and excessive nitrogen application",
            "Sclerotia survival in soil and flood water from previous seasons"
        ],
        "causes_bn": [
            "উচ্চ তাপমাত্রা (২৮-৩২°সে) এবং গাছের গোড়ায় অতিরিক্ত আর্দ্রতা (>৮৫%)",
            "গাছ অতিরিক্ত ঘন করে লাগানো এবং মাত্রাতিরিক্ত ইউরিয়া প্রয়োগ",
            "মাটিতে পূর্ববর্তী ফসলের ছত্রাক বীজ (স্কেলেরোসিয়া) টিকে থাকা"
        ],
        "management_en": {
            "chemical": "Spray Hexaconazole 5 EC (Contaf - 2 ml/L) or Validamycin 3L (2 ml/L) or Azoxystrobin + Difenoconazole (1 ml/L) directed at the plant base.",
            "cultural": "Drain field water to reduce humidity around tillers; widen spacing between hills; remove floating weed debris.",
            "biological": "Apply Trichoderma-enriched compost to soil at last land preparation."
        },
        "management_bn": {
            "chemical": "গাছের গোড়া ভিজিয়ে হেক্সাকোনাজল (কনটাফ - ২ মিলি/লিটার) অথবা ভ্যালিডামাইসিন (২ মিলি/লিটার) স্প্রে করুন।",
            "cultural": "জমির অতিরিক্ত পানি নিষ্কাশন করে গোড়ায় বাতাস চলাচলের ব্যবস্থা করুন; আগাছা পরিষ্কার রাখুন।",
            "biological": "জমি তৈরির সময় ট্রাইকোডার্মা মিশ্রিত জৈব সার প্রয়োগ করুন।"
        }
    }
}
