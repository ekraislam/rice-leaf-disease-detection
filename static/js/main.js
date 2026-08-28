/* ── Full i18n Translation Dictionary ── */
        const I18N = {
            bn: {
                page_title: 'RiceGuard AI — ধানের পাতার রোগ নির্ণয় ও বালাইনাশক প্রেসক্রিপশন',
                mode_single: 'একক পাতা বিশ্লেষণ',
                mode_batch: 'মাঠ ব্যাচ নিরীক্ষা',
                batch_drop_title: 'একসাথে একাধিক পাতার ছবি নির্বাচন বা ড্রপ করুন',
                batch_drop_sub: 'জমির বিভিন্ন কোণা থেকে ৩-২০টি পাতার ছবি দিন',
                batch_drop_meta: 'JPG · PNG · BMP (প্রতিটি সর্বোচ্চ ১০ মেগাবাইট)',
                btn_quick_batch: 'মাঠের ৪টি নমুনা টেস্ট করুন (Test 4 Samples)',
                batch_selected_label: 'নির্বাচিত পাতার নমুনাসমূহ:',
                btn_batch_analyze: 'মাঠের সকল নমুনা বিশ্লেষণ করুন',
                btn_batch_analyzing: 'মাঠের নমুনা বিশ্লেষণ চলছে…',
                batch_gauge_lbl: 'সুস্থ ফসল',
                batch_summary_title: 'সমগ্র মাঠ নিরীক্ষা ফলাফল',
                btn_batch_voice: 'মাঠ রিপোর্ট শুনুন',
                batch_dist_title: 'রোগের প্রাদুর্ভাব ও বিন্যাস (Prevalence Breakdown):',
                batch_rx_title: 'সমন্বিত বালাইনাশক ও মাঠ ব্যবস্থাপনা প্রেসক্রিপশন',
                batch_chem_title: '🧪 বালাইনাশক ও স্প্রে নির্দেশিকা',
                batch_cult_title: '🌱 মাঠ পরিচর্যা ও সেচ ব্যবস্থাপনা',
                batch_fert_title: '⚠️ সার প্রয়োগ ও নাইট্রোজেন সতর্কতা',
                batch_grid_title: 'পরীক্ষিত পাতার নমুনাসমূহ ও Grad-CAM দৃষ্টি',
                btn_batch_pdf: 'মাঠ অডিট PDF ডাউনলোড',

                brand_sub: 'ধানের পাতা রোগ নির্ণয় ও চিকিৎসা',
                dev_tag: 'Developed by',
                status_online: 'এআই অনলাইন',
                hero_eyebrow: 'কৃত্রিম বুদ্ধিমত্তা চালিত ফসল রোগ নির্ণয় ও প্রেসক্রিপশন',
                hero_title: 'কম্পিউটার ভিশন দিয়ে ধানের পাতার রোগ শনাক্তকরণ',
                hero_sub: 'ধানের পাতার ছবি আপলোড করুন এবং রেসনেট১৮ (ResNet18 + GAN) ডিপ লার্নিং মডেলের মাধ্যমে মুহূর্তেই সঠিক রোগ নির্ণয় ও বালাইনাশক পরামর্শ পান।',
                badge_classes: '৮টি বোটানিক্যাল শ্রেণি',
                samples_title: 'স্যাম্পল পাতা দিয়ে এক ক্লিকে টেস্ট',
                samples_hint: 'টেস্ট করতে নিচের যেকোনো স্যাম্পলে ক্লিক করুন',
                sample_brown_spot: 'বাদামী দাগ রোগ',
                sample_healthy: 'সুস্থ ধানের পাতা',
                sample_blast: 'পাতা ব্লাস্ট রোগ',
                sample_blight: 'ব্যাকটেরিয়াল পাতা পোড়া',
                card_upload_title: 'ধানের পাতা আপলোড ও পরীক্ষা',
                card_upload_sub: 'একটি পরিষ্কার, স্পষ্ট ধানের পাতার ছবি আপলোড করুন',
                drop_title: 'এখানে পাতার ছবি টেনে আনুন বা ড্রপ করুন',
                drop_sub: 'অথবা ডিভাইস থেকে ফাইল নির্বাচন করুন',
                drop_meta: 'JPG · PNG · BMP · TIFF (সর্বোচ্চ ১০ মেগাবাইট)',
                btn_live_cam: '📷 সরাসরি ক্যামেরা দিয়ে ছবি তুলুন',
                camera_title: 'লাইভ ক্যামেরা ভিউফাইন্ডার',
                camera_hint: 'ধানের পাতা ফ্রেমের ভেতরে রাখুন',
                btn_flip_cam: 'ক্যামেরা পাল্টান',
                ready_badge: 'বিশ্লেষণের জন্য প্রস্তুত',
                view_orig: 'আসল পাতা',
                view_cam: 'এআই হিটম্যাপ (Grad-CAM)',
                btn_zoom: 'জুম দেখুন',
                btn_remove: 'মুছুন',
                eval_mode_title: 'মূল্যায়ন মোড (ঐচ্ছিক গ্রাউন্ড-ট্রুথ যাচাই)',
                eval_label: 'প্রত্যাশিত পরিচিত শ্রেণি (Known Label)',
                select_class_prompt: '— শ্রেণি নির্বাচন করুন —',
                btn_analyze: 'পাতা বিশ্লেষণ ও রোগ শনাক্ত করুন',
                btn_analyzing: 'বিশ্লেষণ চলছে…',
                card_report_title: 'ডায়াগনস্টিক রিপোর্ট ও প্রেসক্রিপশন',
                card_report_sub: 'ResNet18 কম্পিউটার ভিশন ও কৃষিবিজ্ঞান আউটপুট',
                empty_title: 'আপনার রোগ নির্ণয়ের ফলাফল এখানে প্রদর্শিত হবে',
                empty_sub: 'একটি ধানের পাতার ছবি আপলোড করুন অথবা উপরের যেকোনো স্যাম্পল পাতায় ক্লিক করুন।',
                loading_sub: 'রেসনেট১৮ মডেলের মাধ্যমে বিশ্লেষণ চলছে',
                result_tag: 'শনাক্তকৃত রোগ (AI DIAGNOSIS)',
                btn_voice_read: 'প্রেসক্রিপশন শুনুন',
                voice_male: 'পুরুষ',
                voice_female: 'নারী',
                conf_label: 'মডেল কনফিডেন্স',
                top3_title: 'সম্ভাব্য রোগের তালিকা (Top-3)',
                tab_overview: '🌿 সারসংক্ষেপ',
                tab_symptoms: '🔍 লক্ষণসমূহ',
                tab_causes: '⚠️ কারণসমূহ',
                tab_mgmt: '💊 প্রতিকার',
                tab_calc: '🧪 ডোজ হিসাব',
                adv_title: 'মাঠ ও আবহাওয়া স্প্রে সতর্কতা গাইড',
                adv_1: 'স্প্রে করার ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা থাকলে স্প্রে স্থগিত রাখুন।',
                adv_2: 'মেঘলা দিনে বা শিশির ভেজা অবস্থায় বালাইনাশকের সাথে কৃষি আঠা (Sticker) মিশিয়ে নিন।',
                adv_3: 'সর্বদা বাতাসের অনুকূলে এবং বিকেল ৪টার পর মিষ্টি রোদে স্প্রে করুন।',
                calc_title: 'জমির পরিমাণ অনুযায়ী স্প্রে ও ওষুধ ডোজ ক্যালকুলেটর',
                calc_land_amount: 'জমির পরিমাণ',
                calc_land_unit: 'পরিমাপের একক',
                unit_decimal: 'শতক / ডেসিমল',
                unit_katha: 'কাঠা (১.৬৫ শতক)',
                unit_bigha: 'বিঘা (৩৩ শতক)',
                unit_acre: 'একর (১০০ শতক)',
                calc_water_label: 'প্রয়োজনীয় পানি',
                calc_chem_label: 'বালাইনাশক পরিমাণ',
                calc_tanks_label: '১৬ লিটার স্প্রে ড্রাম',
                btn_whatsapp: '💬 WhatsApp-এ পাঠান',
                btn_pdf_rx: '📄 প্রেসক্রিপশন ও PDF',
                btn_print: 'প্রিন্ট',
                btn_new_test: 'নতুন',
                btn_new_scan: '🌿 নতুন স্ক্যান',
                btn_analysis_done: '✓ বিশ্লেষণ সম্পন্ন',
                voice_stop: 'অডিও থামান',
                card_click_hint: 'বিস্তারিত জানুন ↗',
                rx_modal_title: 'ডিজিটাল প্রেসক্রিপশন প্রিভিউ (Live Report)',
                rx_modal_sub: 'ডাউনলোড বা প্রিন্ট করার আগে পুরো রিপোর্টটি যাচাই করুন',
                btn_modal_dl: '📥 PDF ডাউনলোড',
                btn_modal_print: '🖨️ প্রিন্ট',
                classes_sec_title: 'শনাক্তকরণযোগ্য ধানের ৮টি অবস্থা ও রোগ',
                classes_sec_sub: 'আমাদের কম্পিউটার ভিশন মডেল ধানের পাতার নিচের ৮টি অবস্থা নির্ভুলভাবে শনাক্ত করতে পারে।',
                class_1_name: 'ব্যাকটেরিয়াল পাতা পোড়া',
                class_1_sub: 'Xanthomonas oryzae',
                class_2_name: 'বাদামী দাগ রোগ',
                class_2_sub: 'Bipolaris oryzae',
                class_3_name: 'সুস্থ ধানের পাতা',
                class_3_sub: 'রোগমুক্ত স্বাস্থ্যকর পাতা',
                class_4_name: 'পাতা ব্লাস্ট রোগ',
                class_4_sub: 'Pyricularia oryzae',
                class_5_name: 'লিফ স্ক্যাল্ড (ঝলকানো)',
                class_5_sub: 'Microdochium oryzae',
                class_6_name: 'সরু বাদামী দাগ রোগ',
                class_6_sub: 'Cercospora janseana',
                class_7_name: 'ধানের পামরী পোকা',
                class_7_sub: 'Dicladispa armigera',
                class_8_name: 'খোল পোড়া রোগ',
                class_8_sub: 'Rhizoctonia solani',
                helpline_eyebrow: 'জরুরি কৃষি সহায়তা ও বিশেষজ্ঞ পরামর্শ',
                helpline_title: 'জাতীয় জরুরি কৃষি হেল্পলাইন ও বিজ্ঞানী সেল',
                helpline_sub: 'রোগের তীব্র আক্রমণ বা জরুরি প্রয়োজনে সরকারি কৃষি বিজ্ঞানী ও কর্মকর্তাদের সাথে সরাসরি কথা বলুন।',
                help_1_name: 'জাতীয় কৃষি কল সেন্টার',
                help_1_badge: 'সরকারি টোল-ফ্রি হটলাইন',
                help_1_desc: 'কৃষি, প্রাণিসম্পদ ও মৎস্য বিষয়ক তাৎক্ষণিক সরকারি বিশেষজ্ঞ পরামর্শ (সকাল ৯টা - বিকাল ৫টা)।',
                help_2_name: 'বাংলাদেশ ধান গবেষণা ইনস্টিটিউট (BRRI)',
                help_2_badge: 'ধান বিশেষজ্ঞ বিজ্ঞানী সেল',
                help_2_desc: 'ধানের জটিল ব্লাস্ট, পাতা ঝলসানো ও পামরী পোকার বিস্তার রোধে বিজ্ঞানীদের বিশেষ সহায়তা।',
                help_3_name: 'কৃষি সম্প্রসারণ অধিদপ্তর (DAE)',
                help_3_badge: 'মাঠ পর্যায়ের কর্মকর্তা ডিরেক্টরি',
                help_3_desc: 'আপনার উপজেলা ও ইউনিয়নের উপ-সহকারী কৃষি কর্মকর্তা (SAAO)-এর সাথে সরাসরি যোগাযোগ করুন।',
                help_dial_btn: '📞 ১-ট্যাপে কল করুন →',
                help_web_btn: '🌐 কর্মকর্তা পোর্টাল দেখুন →',
                help_1_num: '১৬১২৩',
                help_2_num: '০২-৪৯২৭২০০৫',
                stat_cases_val: '৬২৮+',
                stat_districts_val: '১০',
                footer_dev_label: 'Designed & Developed by',
                footer_brand: 'RiceGuard AI — ধানের রোগ নির্ণয় ও ফসল সুরক্ষা প্ল্যাটফর্ম',
                footer_desc: 'একটি কৃত্রিম বুদ্ধিমত্তা চালিত কম্পিউটার ভিশন সিস্টেম (ResNet18 + GAN-Augmented CNN)।<br/>কৃষক ও কৃষিবিদদের জন্য দ্রুত ও নির্ভুলভাবে ধানের রোগ শনাক্তকরণ ও প্রেসক্রিপশন প্রদানের লক্ষ্যে নির্মিত।',
                tag_agronomy: 'বালাইনাশক প্রেসক্রিপশন',
                footer_copy: '© 2026 RiceGuard AI Platform • Developed with ❤️ by',
                rx_chem: 'রাসায়নিক প্রতিকার ও বালাইনাশক',
                rx_cult: 'কৃষি ব্যবস্থাপনা ও পরিচর্যা',
                rx_bio: 'জৈব ও প্রাকৃতিক নিয়ন্ত্রণ',
                conf_high: 'উচ্চ নির্ভুলতা',
                conf_mod: 'মাঝারি নির্ভুলতা',
                conf_low: 'কম নির্ভুলতা',
                btn_install_pwa: 'অ্যাপ ইনস্টল',
                tool_enhance: '✨ অটো-এনহ্যান্স',
                tool_rotate: '🔄 ৯০° ঘোরান',
                tool_sharpen: '🔍 শার্প ফোকাস',
                chat_btn_text: 'এআই কৃষি বিশেষজ্ঞ',
                chat_bot_name: 'RiceGuard এআই কৃষি ডাক্তার',
                chat_bot_status: 'অনলাইনে সক্রিয় • ২৪/৭ সাপোর্ট',
                chat_welcome_title: 'RiceGuard AI ফসল সহকারীতে স্বাগতম!',
                chat_welcome_desc: 'ধানের রোগ শনাক্তকরণ, বালাইনাশক প্রেসক্রিপশন, সারের সঠিক মাত্রা ও মাঠ পরিচর্যা সংক্রান্ত যেকোনো প্রশ্ন করুন।',
                chat_welcome_msg: 'নমস্কার/সালাম! আমি <strong>RiceGuard AI</strong>-এর ডিজিটাল ফসল বিশেষজ্ঞ।<br/>ধানের রোগ, বালাইনাশক প্রয়োগ, সারের নিয়ম বা চাষাবাদ নিয়ে যেকোনো প্রশ্ন করুন।',
                chat_mic_title: 'ভয়েসে বাংলায় বলুন',
                chat_mic_listening: '🎙️ শুনছি... মুখে বাংলায় বলুন...',
                weather_widget_title: 'লাইভ আবহাওয়া ও স্প্রে পূর্বাভাস (Live Spray Advisory)',
                btn_gps_loc: 'আমার স্থান',
                w_lbl_temp: 'তাপমাত্রা',
                w_lbl_humidity: 'আর্দ্রতা',
                w_lbl_rain: 'বৃষ্টির ঝুঁকি',
                w_lbl_wind: 'বাতাসের গতি',
                map_badge: 'জাতীয় এপিডেমিওলজি ও লাইভ সার্ভিল্যান্স (Live Outbreak Surveillance)',
                map_heading: 'বাংলাদেশের ধানের রোগ বিস্তার লাইভ মানচিত্র',
                map_subtext: 'বিভিন্ন জেলা থেকে কৃষকদের সনাক্তকৃত রোগের রিয়েল-টাইম তথ্য ও আঞ্চলিক আগাম সতর্কতা।',
                stat_total_cases: 'মোট সনাক্তকরণ',
                stat_active_districts: 'সক্রিয় হটস্পট',
                filter_all: 'সকল রোগ (All)',
                filter_blast: 'ব্লাস্ট রোগ (Blast)',
                filter_blight: 'পাতা পোড়া (Blight)',
                filter_brown: 'বাদামী দাগ (Brown Spot)',
                filter_sheath: 'খোল পোড়া (Sheath Blight)',
                filter_hispa: 'পামরী পোকা (Rice Hispa)',
                legend_title: 'ঝুঁকির মাত্রা (Risk Level)',
                risk_high: 'উচ্চ সতর্কতা (>৭০ কেস)',
                risk_med: 'মাঝারি ঝুঁকি (৪০-৬৯ কেস)',
                risk_low: 'নিয়ন্ত্রিত (<৪০ কেস)',
                tool_reset: '↺ রিসেট',
                // --- Dynamic/JS-injected text strings (used via dict lookups in JS) ---
                loading_step: 'ইমেজ টেন্সর প্রস্তুত করা হচ্ছে (২২৪×২২৪)...',
                weather_loading: 'আপডেট: লোড হচ্ছে...',
                weather_analyzing: 'আবহাওয়া বিশ্লেষণ চলছে...',
                weather_loading_desc: 'লাইভ স্যাটেলাইট পূর্বাভাস লোড করা হচ্ছে।',
                overview_loading: 'বিবরণ লোড হচ্ছে...',
                error_generic: 'একটি ত্রুটি ঘটেছে।',
                batch_count_suffix: 'টি নমুনা',
                batch_loading_title: 'ফলাফল লোড হচ্ছে...',
                batch_default_risk: 'সুস্থ ও নিরাপদ',
                eval_banner_title: 'গ্রাউন্ড-ট্রুথ যাচাই ফলাফল',
                severity_default: 'উচ্চ ঝুঁকি',
                modal_sample_title: 'নমুনা বিশ্লেষণ',
                modal_orig_lbl: '১. মূল পাতা (Original Leaf)',
                modal_cam_lbl: '২. এআই দৃষ্টি (Grad-CAM XAI)',
                modal_pred_lbl: 'রোগের নাম',
                modal_close: 'বন্ধ করুন',
                encyclopedia_default_title: 'ধানের রোগকোষ ও নির্দেশিকা',
                encyclopedia_test_btn: '🔬 এই নমুনায় টেস্ট করুন',
                pdf_sub: 'ডিজিটাল ফসল চিকিৎসাপত্র ও প্রেসক্রিপশন',
                pdf_lbl_date: 'তারিখ:',
                pdf_lbl_case: 'কেস আইডি:',
                pdf_lbl_model: 'এআই মডেল: ResNet-18 (GAN-Augmented)',
                pdf_lbl_diag: 'নির্ণীত রোগ / শনাক্তকৃত অবস্থা',
                pdf_lbl_conf: 'মডেল কনফিডেন্স',
                pdf_lbl_orig: '১. মূল ধানের পাতা (Sample Image)',
                pdf_lbl_cam: '২. এআই দৃষ্টি হিটম্যাপ (Grad-CAM XAI)',
                pdf_lbl_sym: '🔍 প্রধান লক্ষণসমূহ (Symptoms)',
                pdf_lbl_causes: '⚠️ আক্রমণের কারণসমূহ (Causes)',
                pdf_rx_header: '💊 পূর্ণাঙ্গ বালাইনাশক ও প্রতিকার প্রেসক্রিপশন (Rx Treatment)',
                pdf_lbl_chem: '[রাসায়নিক প্রতিকার]',
                pdf_lbl_cult: '[কৃষি ও পরিচর্যা ব্যবস্থাপনা]',
                pdf_lbl_calc: '🧪 জমির ডোজ হিসাব',
                pdf_lbl_spray: '🌦️ স্প্রে সতর্কতা:',
                pdf_spray_rule1: '• ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা থাকলে স্প্রে স্থগিত রাখুন।',
                pdf_spray_rule2: '• বিকেলে মিষ্টি রোদে বাতাসের অনুকূলে স্প্রে করুন।',
                pdf_lbl_sys: 'সিস্টেম:',
                pdf_lbl_dev: 'কারিগরি বিকাশ ও ডিজাইন:',
                voice_pradeep: '👨‍🌾 প্রদীপ (পুরুষ)',
                voice_tanishaa: '👩‍⚕️ তানিশা (নারী)',
                voice_nabanita: '👩‍💼 নবনীতা (নারী)',
                voice_bashkar: '👨‍💼 ভাস্কর (পুরুষ)',
                chat_placeholder: 'ধানের রোগ বা চাষ নিয়ে প্রশ্ন লিখুন...',
                chat_topic_1_title: '🌾 ব্লাস্ট রোগ দমন',
                chat_topic_1_sub: 'লক্ষণ ও ওষুধ স্প্রে',
                chat_topic_2_title: '🧪 ইউরিয়া সারের নিয়ম',
                chat_topic_2_sub: 'প্রয়োগ সতর্কতা',
                chat_topic_3_title: '🐛 পামরী পোকা দমন',
                chat_topic_3_sub: 'পার্চিং ও রাসায়নিক',
                chat_topic_4_title: '🌦️ স্প্রে সতর্কতা',
                chat_topic_4_sub: 'আবহাওয়া ও সময়',
                chip_blast: '🌾 ব্লাস্ট রোগ',
                chip_blight: '🍂 পাতা পোড়া',
                chip_urea: '🧪 ইউরিয়া নিয়ম',
                chip_hispa: '🐛 পামরী পোকা',
                chip_sheath: '🌿 খোল পোড়া',
                chip_water: '💧 সেচ নিয়ম',
                footer_ai_desc: 'একটি কৃত্রিম বুদ্ধিমত্তা চালিত কম্পিউটার ভিশন সিস্টেম (ResNet18 + GAN-Augmented CNN)।<br/>কৃষক ও কৃষিবিদদের জন্য দ্রুত ও নির্ভুলভাবে ধানের রোগ শনাক্তকরণ ও প্রেসক্রিপশন প্রদানের লক্ষ্যে নির্মিত।'
            },
            en: {
                page_title: 'RiceGuard AI — Rice Leaf Disease Detection & Agronomy Prescription',
                brand_sub: 'Rice Leaf Intelligence & Diagnostics',
                dev_tag: 'Developed by',
                status_online: 'AI ONLINE',
                hero_eyebrow: 'AI-POWERED CROP DIAGNOSTICS & PRESCRIPTION',
                hero_title: 'Detect Rice Leaf Diseases with Computer Vision',
                hero_sub: 'Upload a clear rice leaf photo and let the trained ResNet18 model analyze visible disease patterns with agronomic treatment guidance in seconds.',
                badge_classes: '8 Botanical Classes',
                samples_title: 'Quick Test with Sample Leaves',
                samples_hint: 'Click any sample below to test immediately',
                sample_brown_spot: 'Brown Spot Leaf',
                sample_healthy: 'Healthy Rice Leaf',
                sample_blast: 'Leaf Blast Disease',
                sample_blight: 'Bacterial Leaf Blight',
                card_upload_title: 'Analyze Rice Leaf',
                card_upload_sub: 'Upload a clear, well-lit photo of a single rice leaf',
                drop_title: 'Drop your leaf image here',
                drop_sub: 'or browse from device (Click to browse)',
                drop_meta: 'JPG · PNG · BMP · TIFF (Max 10 MB)',
                btn_live_cam: '📷 Open Live Camera Scanner',
                camera_title: 'Live Camera Viewfinder',
                camera_hint: 'Position rice leaf inside frame',
                btn_flip_cam: 'Flip Camera',
                ready_badge: 'READY FOR ANALYSIS',
                view_orig: 'Original Leaf',
                view_cam: 'AI Heatmap (Grad-CAM)',
                btn_zoom: 'Zoom View',
                btn_remove: 'Remove',
                eval_mode_title: 'Evaluation Mode (Optional Ground-Truth)',
                eval_label: 'Expected Known Class Label',
                select_class_prompt: '— Select Class Label —',
                btn_analyze: 'Analyze Leaf & Detect Disease',
                btn_analyzing: 'Analyzing Leaf…',
                card_report_title: 'Diagnostic Report & Prescription',
                card_report_sub: 'ResNet18 computer vision & agronomy output',
                empty_title: 'Your diagnosis will appear here',
                empty_sub: 'Upload a rice leaf photo or click any quick sample above to start analysis.',
                loading_sub: 'Analyzing leaf features via ResNet18 deep neural network',
                result_tag: 'DIAGNOSED CONDITION (AI OUTPUT)',
                btn_voice_read: 'Listen Audio',
                voice_male: 'Male',
                voice_female: 'Female',
                conf_label: 'Model Confidence',
                top3_title: 'Top-3 Probability Distribution',
                tab_overview: '🌿 Overview',
                tab_symptoms: '🔍 Symptoms',
                tab_causes: '⚠️ Causes',
                tab_mgmt: '💊 Treatment',
                tab_calc: '🧪 Dosage Calc',
                adv_title: 'Weather & Spraying Advisory',
                adv_1: 'Postpone spraying if rain is expected within 4 hours.',
                adv_2: 'Mix an agricultural sticker/surfactant during humid or overcast conditions.',
                adv_3: 'Always spray along the wind direction in late afternoon.',
                calc_title: 'Field Spray & Chemical Dosage Calculator',
                calc_land_amount: 'Land Size',
                calc_land_unit: 'Unit of Measure',
                unit_decimal: 'Decimal / Cent',
                unit_katha: 'Katha (1.65 Decimals)',
                unit_bigha: 'Bigha (33 Decimals)',
                unit_acre: 'Acre (100 Decimals)',
                calc_water_label: 'Water Required',
                calc_chem_label: 'Chemical Dosage',
                calc_tanks_label: '16L Sprayer Tanks',
                btn_whatsapp: '💬 Share on WhatsApp',
                btn_pdf_rx: '📄 Prescription & PDF',
                btn_print: 'Print',
                btn_new_test: 'New',
                btn_new_scan: '🌿 New Scan',
                btn_analysis_done: '✓ Analysis Complete',
                voice_stop: 'Stop Audio',
                card_click_hint: 'View Details ↗',
                rx_modal_title: 'Digital Prescription Preview (Live Report)',
                rx_modal_sub: 'Review full diagnosis & dosage before downloading or printing',
                btn_modal_dl: '📥 Download PDF',
                btn_modal_print: '🖨️ Print',
                classes_sec_title: 'Supported Rice Conditions & Pathogens',
                classes_sec_sub: 'Our computer vision model classifies leaf imagery into eight distinct botanical categories.',
                class_1_name: 'Bacterial Leaf Blight',
                class_1_sub: 'Xanthomonas oryzae',
                class_2_name: 'Brown Spot',
                class_2_sub: 'Bipolaris oryzae',
                class_3_name: 'Healthy Rice Leaf',
                class_3_sub: 'Optimum Botanical Health',
                class_4_name: 'Leaf Blast',
                class_4_sub: 'Pyricularia oryzae',
                class_5_name: 'Leaf Scald',
                class_5_sub: 'Microdochium oryzae',
                class_6_name: 'Narrow Brown Leaf Spot',
                class_6_sub: 'Cercospora janseana',
                class_7_name: 'Rice Hispa',
                class_7_sub: 'Dicladispa armigera',
                class_8_name: 'Sheath Blight',
                class_8_sub: 'Rhizoctonia solani',
                helpline_eyebrow: 'EMERGENCY AGRI HELPLINE & SCIENTIST DESK',
                helpline_title: 'National Emergency Agri Helplines & Expert Cell',
                helpline_sub: 'Call national agronomists, BRRI scientists, and field extension officers directly for immediate support.',
                help_1_name: 'National Krishi Call Center',
                help_1_badge: 'Govt Toll-Free Hotline',
                help_1_desc: 'Instant advisory on crops, pests, and fertilizers by govt agronomists (9 AM - 5 PM).',
                help_2_name: 'Bangladesh Rice Research Institute (BRRI)',
                help_2_badge: 'Rice Scientist Taskforce',
                help_2_desc: 'Dedicated scientist helpdesk for epidemic blast, blights, and rice insect infestations.',
                help_3_name: 'Department of Agricultural Extension (DAE)',
                help_3_badge: 'Field Extension Officer Portal',
                help_3_desc: 'Locate and connect with your sub-district / union Sub-Assistant Agriculture Officer (SAAO).',
                help_dial_btn: '📞 1-Tap Direct Call →',
                help_web_btn: '🌐 View DAE Directory →',
                help_1_num: '16123',
                help_2_num: '02-49272005',
                stat_cases_val: '628+',
                stat_districts_val: '10',
                footer_dev_label: 'Designed & Developed by',
                footer_brand: 'RiceGuard AI — Rice Crop Protection Platform',
                footer_desc: 'An AI-powered computer vision system (ResNet18 + GAN-Augmented CNN).<br/>Built for farmers and agronomists to rapidly detect rice diseases and provide verified chemical and organic prescriptions.',
                tag_agronomy: 'Agronomy Prescriptions',
                footer_copy: '© 2026 RiceGuard AI Platform • Developed with ❤️ by',
                rx_chem: 'Chemical Fungicide / Bactericide',
                rx_cult: 'Cultural & Water Practices',
                rx_bio: 'Biological & Organic Control',
                conf_high: 'High Confidence',
                conf_mod: 'Moderate Confidence',
                conf_low: 'Low Confidence',
                btn_install_pwa: 'Install App',
                tool_enhance: '✨ Auto-Enhance',
                tool_rotate: '🔄 Rotate 90°',
                tool_sharpen: '🔍 Sharpen Focus',
                chat_btn_text: 'AI Agri Specialist',
                chat_bot_name: 'RiceGuard AI Agri Specialist',
                chat_bot_status: 'Online & Active • 24/7 Support',
                chat_welcome_title: 'Welcome to RiceGuard AI Assistant!',
                chat_welcome_desc: 'Ask any questions regarding rice leaf disease diagnosis, fungicide prescriptions, fertilizer dosages, or crop field care.',
                chat_welcome_msg: 'Hello! I am the <strong>RiceGuard AI</strong> Agronomy Assistant.<br/>Ask me any question about rice diseases, fungicides, fertilizers, or crop care.',
                chat_mic_title: 'Voice input in English',
                chat_mic_listening: '🎙️ Listening... Speak now...',
                weather_widget_title: 'Live Agricultural Weather & Spray Advisory',
                btn_gps_loc: 'My Location',
                w_lbl_temp: 'Temperature',
                w_lbl_humidity: 'Humidity',
                w_lbl_rain: 'Rain Risk',
                w_lbl_wind: 'Wind Speed',
                map_badge: 'National Epidemiology & Live Surveillance',
                map_heading: 'Bangladesh Rice Disease Outbreak Live Map',
                map_subtext: 'Real-time aggregated farmer diagnostic reports and district-level early warning advisories.',
                stat_total_cases: 'Total Diagnoses',
                stat_active_districts: 'Active Hotspots',
                filter_all: 'All Diseases',
                filter_blast: 'Leaf Blast',
                filter_blight: 'Bacterial Blight',
                filter_brown: 'Brown Spot',
                filter_sheath: 'Sheath Blight',
                filter_hispa: 'Rice Hispa',
                legend_title: 'Outbreak Severity',
                risk_high: 'High Alert (>70 cases)',
                risk_med: 'Moderate Risk (40-69 cases)',
                risk_low: 'Controlled (<40 cases)',
                tool_reset: '↺ Reset',
                // --- Batch UI keys missing from EN ---
                mode_single: 'Single Leaf Analysis',
                mode_batch: 'Field Batch Audit',
                batch_drop_title: 'Drop multiple leaf images or click to browse',
                batch_drop_sub: 'Sample 3–20 leaves from different corners of the field',
                batch_drop_meta: 'JPG · PNG · BMP (Max 10 MB each)',
                btn_quick_batch: '🧪 Load 4 Quick Field Samples',
                batch_selected_label: 'Selected leaf samples:',
                btn_batch_analyze: 'Analyze All Field Samples',
                btn_batch_analyzing: 'Analyzing field samples…',
                batch_gauge_lbl: 'Healthy Crop',
                batch_summary_title: 'Overall Field Audit Result',
                btn_batch_voice: 'Listen Field Report',
                batch_dist_title: 'Disease Prevalence Breakdown:',
                batch_rx_title: 'Integrated Pesticide & Field Management Prescription',
                batch_chem_title: '🧪 Fungicide & Spray Guidelines',
                batch_cult_title: '🌱 Field Care & Irrigation Management',
                batch_fert_title: '⚠️ Fertilizer & Nitrogen Restriction Advisory',
                batch_grid_title: 'Tested Leaf Samples & Grad-CAM Vision',
                btn_batch_pdf: 'Download Field Audit PDF',
                // --- Dynamic/JS-injected text strings ---
                loading_step: 'Preparing image tensor (224×224)...',
                weather_loading: 'Updated: Loading...',
                weather_analyzing: 'Analyzing weather conditions...',
                weather_loading_desc: 'Loading live satellite forecast data.',
                overview_loading: 'Loading description...',
                error_generic: 'An error occurred.',
                batch_count_suffix: 'samples',
                batch_loading_title: 'Loading results...',
                batch_default_risk: 'Healthy & Safe',
                eval_banner_title: 'Ground-Truth Verification Result',
                severity_default: 'High Risk',
                modal_sample_title: 'Sample Analysis',
                modal_orig_lbl: '1. Original Leaf',
                modal_cam_lbl: '2. AI Vision (Grad-CAM XAI)',
                modal_pred_lbl: 'Disease Name',
                modal_close: 'Close',
                encyclopedia_default_title: 'Rice Disease Encyclopedia',
                encyclopedia_test_btn: '🔬 Test With This Sample',
                pdf_sub: 'Digital Crop Prescription & Treatment Report',
                pdf_lbl_date: 'Date:',
                pdf_lbl_case: 'Case ID:',
                pdf_lbl_model: 'AI Model: ResNet-18 (GAN-Augmented)',
                pdf_lbl_diag: 'DIAGNOSED CONDITION',
                pdf_lbl_conf: 'Model Confidence',
                pdf_lbl_orig: '1. Original Rice Leaf (Sample Image)',
                pdf_lbl_cam: '2. AI Vision Heatmap (Grad-CAM XAI)',
                pdf_lbl_sym: '🔍 Key Symptoms',
                pdf_lbl_causes: '⚠️ Causes of Infection',
                pdf_rx_header: '💊 Full Pesticide & Treatment Prescription (Rx)',
                pdf_lbl_chem: '[Chemical Treatment]',
                pdf_lbl_cult: '[Cultural & Field Management]',
                pdf_lbl_calc: '🧪 Field Dosage Calculator',
                pdf_lbl_spray: '🌦️ Spray Advisory:',
                pdf_spray_rule1: '• Postpone spraying if rain is expected within 4 hours.',
                pdf_spray_rule2: '• Spray in late afternoon along wind direction.',
                pdf_lbl_sys: 'System:',
                pdf_lbl_dev: 'Technical Development & Design:',
                voice_pradeep: '👨‍🌾 Pradeep (Male)',
                voice_tanishaa: '👩‍⚕️ Tanisha (Female)',
                voice_nabanita: '👩‍💼 Nabanita (Female)',
                voice_bashkar: '👨‍💼 Bashkar (Male)',
                chat_placeholder: 'Ask about rice diseases, fertilizers, or crop care...',
                chat_topic_1_title: '🌾 Blast Disease Control',
                chat_topic_1_sub: 'Symptoms & spray',
                chat_topic_2_title: '🧪 Urea Fertilizer Rules',
                chat_topic_2_sub: 'Application caution',
                chat_topic_3_title: '🐛 Rice Hispa Control',
                chat_topic_3_sub: 'Perching & chemical',
                chat_topic_4_title: '🌦️ Spray Safety',
                chat_topic_4_sub: 'Weather & timing',
                chip_blast: '🌾 Leaf Blast',
                chip_blight: '🍂 Leaf Blight',
                chip_urea: '🧪 Urea Rules',
                chip_hispa: '🐛 Rice Hispa',
                chip_sheath: '🌿 Sheath Blight',
                chip_water: '💧 Irrigation',
                footer_ai_desc: 'An AI-powered computer vision system (ResNet18 + GAN-Augmented CNN).<br/>Built for farmers and agronomists to rapidly detect rice diseases and provide verified prescriptions.'
            }
        };

        const DISEASE_DB = window.DISEASE_DATABASE || {};
        let currentLang = localStorage.getItem('riceguard_lang') || 'bn';
        let currentDiseaseData = null;
        let currentTopPredictions = null;
        let currentConfidence = 0;
        let currentPredictionName = '';
        let originalImageSrc = '';
        let gradcamImageSrc = '';
        let currentViewMode = 'orig'; // 'orig' or 'cam'
        let rawOriginalDataUrl = '';
        let rawOriginalFile = null;

        /* ── Interactive Condition Encyclopedia Modal Functions ── */
        function openEncyclopedia(className) {
            if (!DISEASE_DB) return;
            
            let data = DISEASE_DB[className];
            if (!data) {
                const lower = className.toLowerCase();
                for (const k in DISEASE_DB) {
                    if (k.toLowerCase() === lower) {
                        data = DISEASE_DB[k];
                        className = k;
                        break;
                    }
                }
            }
            if (!data) return;

            const isBn = currentLang === 'bn';
            const title = isBn ? (data.name_bn || className) : (data.name_en || className);
            const pathogen = data.pathogen || 'N/A';
            const severity = isBn ? (data.severity_bn || 'সতর্কতা') : (data.severity_en || 'Caution');
            const overview = isBn ? (data.description_bn || '') : (data.description_en || '');
            
            const titleEl = document.getElementById('encyclopedia-title');
            const subEl = document.getElementById('encyclopedia-sub');
            if (titleEl) titleEl.textContent = title;
            if (subEl) subEl.textContent = pathogen;
            
            const sevBadge = document.getElementById('encyclopedia-severity');
            if (sevBadge) {
                sevBadge.textContent = (isBn ? 'ঝুঁকির মাত্রা: ' : 'Severity: ') + severity;
                sevBadge.style.background = data.severity_color || '#064E3B';
                sevBadge.style.color = '#FFFFFF';
            }

            const testBtn = document.getElementById('btn-encyclopedia-test-sample');
            if (testBtn) {
                testBtn.onclick = function() {
                    closeEncyclopedia();
                    const sampleMap = {
                        'brown spot': 'brown_spot',
                        'healthy rice leaf': 'healthy',
                        'leaf blast': 'blast',
                        'bacterial leaf blight': 'blight'
                    };
                    const sampleKey = sampleMap[className.toLowerCase()];
                    if (sampleKey && typeof loadSample === 'function') {
                        loadSample(sampleKey);
                    }
                    const formElem = document.getElementById('diagnostic-form');
                    if (formElem) {
                        formElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }
                };
            }

            const overviewEl = document.getElementById('encyclopedia-overview');
            if (overviewEl) overviewEl.textContent = overview;

            const symptomsEl = document.getElementById('encyclopedia-symptoms');
            if (symptomsEl) {
                const symptoms = (isBn ? data.symptoms_bn : data.symptoms_en) || [];
                symptomsEl.innerHTML = symptoms.map(s => `<li>${s}</li>`).join('');
            }

            const causesEl = document.getElementById('encyclopedia-causes');
            if (causesEl) {
                const causes = (isBn ? data.causes_bn : data.causes_en) || [];
                causesEl.innerHTML = causes.map(c => `<li>${c}</li>`).join('');
            }

            const treatmentEl = document.getElementById('encyclopedia-treatment');
            if (treatmentEl) {
                const mgmt = isBn ? data.management_bn : data.management_en;
                if (mgmt) {
                    treatmentEl.innerHTML = `
                        <div style="margin-bottom:0.4rem;"><strong>${isBn ? '• রাসায়নিক প্রতিকার:' : '• Chemical:'}</strong> ${mgmt.chemical || 'N/A'}</div>
                        <div style="margin-bottom:0.4rem;"><strong>${isBn ? '• মাঠ পরিচর্যা:' : '• Cultural:'}</strong> ${mgmt.cultural || 'N/A'}</div>
                        <div><strong>${isBn ? '• জৈব দমন:' : '• Biological:'}</strong> ${mgmt.biological || 'N/A'}</div>
                    `;
                } else {
                    treatmentEl.innerHTML = isBn ? 'কোনো রাসায়নিক প্রয়োজন নেই।' : 'No chemical required.';
                }
            }

            const modal = document.getElementById('modal-encyclopedia');
            if (modal) modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeEncyclopedia() {
            const modal = document.getElementById('modal-encyclopedia');
            if (modal) modal.classList.remove('active');
            document.body.style.overflow = '';
        }

        /* ── 1-Click Language Switcher Function ── */
        function setLanguage(lang) {
            const wasSpeaking = isSpeaking;
            if (isSpeaking) {
                stopAudioSpeech();
            }
            if (typeof stopChatAudio === 'function') {
                stopChatAudio();
            }

            currentLang = lang;
            localStorage.setItem('riceguard_lang', lang);
            document.documentElement.lang = lang;

            document.getElementById('lang-en').classList.toggle('active', lang === 'en');
            document.getElementById('lang-bn').classList.toggle('active', lang === 'bn');

            const dict = I18N[lang] || I18N.bn;
            document.title = dict.page_title;

            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dict[key]) {
                    el.innerHTML = dict[key];
                }
            });

            // Update Voice Selector tooltips based on active language
            const maleBtn = document.getElementById('voice-gender-male');
            const femaleBtn = document.getElementById('voice-gender-female');
            if (maleBtn) maleBtn.title = (lang === 'bn' ? 'পুরুষ কণ্ঠ (প্রদীপ)' : 'Male Voice (Guy)');
            if (femaleBtn) femaleBtn.title = (lang === 'bn' ? 'নারী কণ্ঠ (নবনীতা)' : 'Female Voice (Aria)');

            // Synchronize voice options in Chatbot
            if (typeof updateChatVoiceOptions === 'function') {
                updateChatVoiceOptions(lang);
            }

            // Translate Expected Class dropdown options
            const classSelect = document.getElementById('expected_class');
            if (classSelect) {
                const isBn = lang === 'bn';
                const classTranslations = {
                    "Bacterial Leaf Blight": { bn: "ব্যাকটেরিয়াল পাতা পোড়া রোগ (Bacterial Blight)", en: "Bacterial Leaf Blight" },
                    "Brown Spot": { bn: "বাদামী দাগ রোগ (Brown Spot)", en: "Brown Spot" },
                    "Healthy Rice Leaf": { bn: "সুস্থ ধানের পাতা (Healthy Leaf)", en: "Healthy Rice Leaf" },
                    "Leaf Blast": { bn: "পাতা ব্লাস্ট রোগ (Leaf Blast)", en: "Leaf Blast" },
                    "Leaf scald": { bn: "লিফ স্ক্যাল্ড (Leaf Scald)", en: "Leaf Scald" },
                    "Narrow Brown Leaf Spot": { bn: "সরু বাদামী দাগ রোগ (Narrow Brown Spot)", en: "Narrow Brown Leaf Spot" },
                    "Rice Hispa": { bn: "ধানের পামরী পোকা (Rice Hispa)", en: "Rice Hispa" },
                    "Sheath Blight": { bn: "খোল পোড়া রোগ (Sheath Blight)", en: "Sheath Blight" }
                };

                Array.from(classSelect.options).forEach(opt => {
                    if (!opt.value) return; // Prompt option handled by data-i18n
                    const trans = classTranslations[opt.value];
                    if (trans) {
                        opt.textContent = isBn ? trans.bn : trans.en;
                    }
                });
            }

            const micBtn = document.getElementById('btn-chat-mic');
            if (micBtn && !isChatListening) {
                micBtn.title = dict.chat_mic_title || (lang === 'bn' ? 'ভয়েসে বাংলায় বলুন' : 'Voice input in English');
            }
            const chatInput = document.getElementById('chat-input');
            if (chatInput && !isChatListening) {
                chatInput.placeholder = lang === 'bn' ? 'ধানের রোগ বা চাষ নিয়ে প্রশ্ন লিখুন...' : 'Ask about rice diseases, fertilizers, or care...';
            }

            populateDistrictDropdown();
            fetchLiveWeather(currentSelectedDistrict);
            if (typeof outbreakMap !== 'undefined' && outbreakMap) {
                loadOutbreakMapMarkers(currentOutbreakFilter);
            }

            if (currentDiseaseData) {
                updateResultLanguage(dict);
                calculateDosage();

                // Preload new language audio for 0ms playback
                if (typeof preloadPredictionAudio === 'function') {
                    preloadPredictionAudio(currentPredictionName, lang);
                }

                // If single voice was playing, auto-restart in new language seamlessly!
                if (wasSpeaking && typeof toggleVoiceSpeech === 'function') {
                    toggleVoiceSpeech();
                }
            }

            // Update Batch Results UI if active
            if (window.currentBatchData && typeof renderBatchResults === 'function') {
                const wasBatchSpeaking = window.isBatchSpeaking;
                if (wasBatchSpeaking && typeof stopBatchAudioSpeech === 'function') {
                    stopBatchAudioSpeech();
                }
                renderBatchResults(window.currentBatchData);
                if (wasBatchSpeaking && typeof toggleBatchAudioSpeech === 'function') {
                    toggleBatchAudioSpeech();
                }
            }

            // ─── Deep bilingual: update all hardcoded dynamic text elements ───

            // Loading step text
            const _loadStep = document.getElementById('loading-step-text');
            if (_loadStep) _loadStep.textContent = dict.loading_step || _loadStep.textContent;

            // Weather widget loading states
            const _weatherUpdated = document.getElementById('weather-updated-time');
            if (_weatherUpdated && (_weatherUpdated.textContent.includes('লোড') || _weatherUpdated.textContent.includes('Loading'))) {
                _weatherUpdated.textContent = dict.weather_loading || _weatherUpdated.textContent;
            }
            const _bWeatherUpdated = document.getElementById('batch-weather-updated-time');
            if (_bWeatherUpdated && (_bWeatherUpdated.textContent.includes('লোড') || _bWeatherUpdated.textContent.includes('Loading'))) {
                _bWeatherUpdated.textContent = dict.weather_loading || _bWeatherUpdated.textContent;
            }

            const _weatherAdvTitle = document.getElementById('weather-advisory-title');
            if (_weatherAdvTitle && (_weatherAdvTitle.textContent.includes('বিশ্লেষণ') || _weatherAdvTitle.textContent.includes('Analyzing'))) {
                _weatherAdvTitle.textContent = dict.weather_analyzing || _weatherAdvTitle.textContent;
            }
            const _bWeatherAdvTitle = document.getElementById('batch-weather-advisory-title');
            if (_bWeatherAdvTitle && (_bWeatherAdvTitle.textContent.includes('বিশ্লেষণ') || _bWeatherAdvTitle.textContent.includes('Analyzing'))) {
                _bWeatherAdvTitle.textContent = dict.weather_analyzing || _bWeatherAdvTitle.textContent;
            }

            const _weatherAdvDesc = document.getElementById('weather-advisory-desc');
            if (_weatherAdvDesc && (_weatherAdvDesc.textContent.includes('লোড') || _weatherAdvDesc.textContent.includes('Loading'))) {
                _weatherAdvDesc.textContent = dict.weather_loading_desc || _weatherAdvDesc.textContent;
            }
            const _bWeatherAdvDesc = document.getElementById('batch-weather-advisory-desc');
            if (_bWeatherAdvDesc && (_bWeatherAdvDesc.textContent.includes('লোড') || _bWeatherAdvDesc.textContent.includes('Loading'))) {
                _bWeatherAdvDesc.textContent = dict.weather_loading_desc || _bWeatherAdvDesc.textContent;
            }

            // Overview loading text
            const _overview = document.getElementById('text-overview');
            if (_overview && (_overview.textContent.includes('লোড') || _overview.textContent.includes('Loading'))) {
                _overview.textContent = dict.overview_loading || _overview.textContent;
            }

            // Client error text
            const _errEl = document.getElementById('client-error-text');
            if (_errEl) _errEl.textContent = dict.error_generic || _errEl.textContent;

            // Batch count badge
            const _batchBadge = document.getElementById('batch-count-badge');
            if (_batchBadge) {
                const n = _batchBadge.textContent.replace(/[^0-9]/g, '') || '0';
                const suffix = dict.batch_count_suffix || (lang === 'bn' ? 'টি নমুনা' : 'samples');
                _batchBadge.textContent = n + ' ' + suffix;
            }

            // Batch dominant title default when no data loaded
            const _batchDomTitle = document.getElementById('batch-dominant-title');
            if (_batchDomTitle && !window.currentBatchData) {
                _batchDomTitle.textContent = dict.batch_loading_title || _batchDomTitle.textContent;
            }

            // Batch default risk badge when no data
            const _batchRiskBadge = document.getElementById('batch-risk-badge');
            if (_batchRiskBadge && !window.currentBatchData) {
                _batchRiskBadge.textContent = dict.batch_default_risk || _batchRiskBadge.textContent;
            }

            // Eval banner title
            const _evalTitle = document.getElementById('eval-banner-title');
            if (_evalTitle) _evalTitle.textContent = dict.eval_banner_title || _evalTitle.textContent;

            // Modal inspect labels
            const _modalSampleTitle = document.getElementById('modal-sample-title');
            if (_modalSampleTitle) _modalSampleTitle.textContent = dict.modal_sample_title || _modalSampleTitle.textContent;

            // Inspect modal image labels (no id — use stable class pattern)
            document.querySelectorAll('.batch-inspect-modal').forEach(modal => {
                const divs = modal.querySelectorAll('div[style*="font-size:0.75rem"]');
                divs.forEach(d => {
                    if (d.textContent.includes('মূল পাতা') || d.textContent.includes('Original Leaf')) {
                        d.textContent = dict.modal_orig_lbl || d.textContent;
                    }
                    if (d.textContent.includes('এআই দৃষ্টি') || d.textContent.includes('AI Vision')) {
                        d.textContent = dict.modal_cam_lbl || d.textContent;
                    }
                });
                const closeSpan = modal.querySelector('button span');
                if (closeSpan) closeSpan.textContent = dict.modal_close || closeSpan.textContent;
            });

            // Encyclopedia default title
            const _encTitle = document.getElementById('encyclopedia-title');
            if (_encTitle && !document.getElementById('modal-encyclopedia')?.classList.contains('active')) {
                _encTitle.textContent = dict.encyclopedia_default_title || _encTitle.textContent;
            }

            // Encyclopedia test sample button
            const _encTestBtn = document.getElementById('btn-encyclopedia-test-sample');
            if (_encTestBtn) {
                const sp = _encTestBtn.querySelector('span');
                if (sp) sp.textContent = dict.encyclopedia_test_btn || sp.textContent;
            }

            // PDF template labels
            const _pdfMap = {
                'pdf-hdr-sub': dict.pdf_sub,
                'pdf-lbl-date': dict.pdf_lbl_date,
                'pdf-lbl-case': dict.pdf_lbl_case,
                'pdf-lbl-model': dict.pdf_lbl_model,
                'pdf-lbl-diag': dict.pdf_lbl_diag,
                'pdf-lbl-conf': dict.pdf_lbl_conf,
                'pdf-lbl-orig': dict.pdf_lbl_orig,
                'pdf-lbl-cam': dict.pdf_lbl_cam,
                'pdf-lbl-sym': dict.pdf_lbl_sym,
                'pdf-lbl-causes': dict.pdf_lbl_causes,
                'pdf-lbl-chem': dict.pdf_lbl_chem,
                'pdf-lbl-cult': dict.pdf_lbl_cult,
                'pdf-lbl-spray': dict.pdf_lbl_spray,
                'pdf-lbl-sys': dict.pdf_lbl_sys,
                'pdf-lbl-dev': dict.pdf_lbl_dev,
            };
            Object.entries(_pdfMap).forEach(([id, val]) => {
                if (!val) return;
                const el = document.getElementById(id);
                if (el) {
                    // For sys/dev, preserve nested strong tag
                    if (id === 'pdf-lbl-sys' || id === 'pdf-lbl-dev') {
                        const strong = el.querySelector('strong');
                        if (strong) {
                            const prefix = val;
                            el.childNodes[0].textContent = prefix + ' ';
                        } else {
                            el.textContent = val;
                        }
                    } else if (id === 'pdf-lbl-calc') {
                        const sp = el.querySelector('span');
                        if (sp) sp.textContent = val; else el.textContent = val;
                    } else {
                        el.textContent = val;
                    }
                }
            });

            // Chat voice select options
            const _voiceSelect = document.getElementById('chat-voice-select');
            if (_voiceSelect) {
                const _voiceMap = {
                    pradeep: dict.voice_pradeep,
                    tanishaa: dict.voice_tanishaa,
                    nabanita: dict.voice_nabanita,
                    bashkar: dict.voice_bashkar
                };
                Array.from(_voiceSelect.options).forEach(opt => {
                    if (_voiceMap[opt.value]) opt.textContent = _voiceMap[opt.value];
                });
            }

            // Chat welcome topic buttons
            const _topicBtns = document.querySelectorAll('.welcome-topic-btn');
            const _topicKeys = [
                ['chat_topic_1_title', 'chat_topic_1_sub'],
                ['chat_topic_2_title', 'chat_topic_2_sub'],
                ['chat_topic_3_title', 'chat_topic_3_sub'],
                ['chat_topic_4_title', 'chat_topic_4_sub'],
            ];
            _topicBtns.forEach((btn, idx) => {
                if (_topicKeys[idx]) {
                    const titleEl = btn.querySelector('.welcome-topic-title');
                    const subEl = btn.querySelector('.welcome-topic-sub');
                    if (titleEl && dict[_topicKeys[idx][0]]) titleEl.textContent = dict[_topicKeys[idx][0]];
                    if (subEl && dict[_topicKeys[idx][1]]) subEl.textContent = dict[_topicKeys[idx][1]];
                }
            });

            // Chat prompt chips
            const _chipKeys = ['chip_blast', 'chip_blight', 'chip_urea', 'chip_hispa', 'chip_sheath', 'chip_water'];
            document.querySelectorAll('.prompt-chip').forEach((chip, idx) => {
                if (_chipKeys[idx] && dict[_chipKeys[idx]]) chip.textContent = dict[_chipKeys[idx]];
            });

            // Footer description paragraph (hardcoded)
            document.querySelectorAll('.footer-desc p, .footer-desc').forEach(el => {
                if (el.innerHTML && (el.innerHTML.includes('ResNet18') || el.innerHTML.includes('কৃষক') || el.innerHTML.includes('farmers'))) {
                    if (dict.footer_ai_desc) el.innerHTML = dict.footer_ai_desc;
                }
            });
        }

        function updateResultLanguage(dict) {
            const isBn = currentLang === 'bn';
            const resultMain     = document.getElementById('result-prediction-main');
            const resultSeverity = document.getElementById('result-severity');
            const resultPathogen = document.getElementById('result-pathogen');
            const resultConfPill = document.getElementById('result-confidence-pill');
            const topPredList    = document.getElementById('top-predictions-list');

            if (!currentDiseaseData) return;

            // Main Disease Name
            resultMain.textContent = isBn ? (currentDiseaseData.name_bn || currentPredictionName) : (currentDiseaseData.name_en || currentPredictionName);
            
            // Pathogen
            resultPathogen.textContent = currentDiseaseData.pathogen 
                ? (isBn ? `জীবাণু: ${currentDiseaseData.pathogen}` : `Pathogen: ${currentDiseaseData.pathogen}`)
                : '';

            // Severity Badge
            if (currentDiseaseData.severity_color) {
                resultSeverity.style.backgroundColor = currentDiseaseData.severity_color + '33';
                resultSeverity.style.borderColor = currentDiseaseData.severity_color;
            }
            resultSeverity.textContent = isBn 
                ? (currentDiseaseData.severity_bn || currentDiseaseData.severity_en || 'ঝুঁকি')
                : (currentDiseaseData.severity_en || 'Risk Level');

            // Confidence Pill
            resultConfPill.className = 'confidence-pill';
            if (currentConfidence >= 85) {
                resultConfPill.textContent = dict.conf_high;
                resultConfPill.classList.add('pill-high');
            } else if (currentConfidence >= 65) {
                resultConfPill.textContent = dict.conf_mod;
                resultConfPill.classList.add('pill-mod');
            } else {
                resultConfPill.textContent = dict.conf_low;
                resultConfPill.classList.add('pill-low');
            }

            // Top-3 list
            if (currentTopPredictions && topPredList) {
                topPredList.innerHTML = '';
                currentTopPredictions.forEach(pred => {
                    const item = document.createElement('div');
                    item.className = 'top-pred-item';
                    const displayName = isBn ? (pred.class_bn || pred.class) : (pred.class || pred.class_bn);
                    item.innerHTML = `
                        <div class="top-pred-meta">
                            <span class="top-pred-name">${displayName}</span>
                            <span class="top-pred-percent">${pred.confidence}%</span>
                        </div>
                        <div class="top-pred-bar">
                            <div class="top-pred-bar-fill" style="width: ${pred.confidence}%;"></div>
                        </div>
                    `;
                    topPredList.appendChild(item);
                });
            }

            // Tabs Content
            renderDiseaseTabs(currentDiseaseData, dict);
        }

        /* ── Dynamic Tab Population ── */
        function renderDiseaseTabs(info, dict) {
            const isBn = currentLang === 'bn';
            const overviewText = document.getElementById('text-overview');
            const symptomsList = document.getElementById('list-symptoms');
            const causesList   = document.getElementById('list-causes');
            const mgmtGrid     = document.getElementById('grid-management');

            if (!info || !overviewText) return;

            // Overview
            overviewText.textContent = (isBn ? info.overview_bn : info.overview_en) || 'No details available.';

            // Symptoms
            symptomsList.innerHTML = '';
            const symptoms = (isBn ? info.symptoms_bn : info.symptoms_en) || [];
            symptoms.forEach(sym => {
                const li = document.createElement('li');
                li.className = 'bullet-item';
                li.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
                    <span>${sym}</span>
                `;
                symptomsList.appendChild(li);
            });

            // Causes
            causesList.innerHTML = '';
            const causes = (isBn ? info.causes_bn : info.causes_en) || [];
            causes.forEach(cause => {
                const li = document.createElement('li');
                li.className = 'bullet-item';
                li.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/></svg>
                    <span>${cause}</span>
                `;
                causesList.appendChild(li);
            });

            // Management / Treatment
            mgmtGrid.innerHTML = '';
            const mgmt = (isBn ? info.management_bn : info.management_en) || {};

            if (mgmt.chemical) {
                const cDiv = document.createElement('div');
                cDiv.className = 'rx-card';
                cDiv.innerHTML = `
                    <div class="rx-title rx-chemical">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m14 2-4 4-2-2-4 4 4 4"/><path d="m14 10 4 4"/><path d="m19 15-4-4"/></svg>
                        <span>${dict.rx_chem}</span>
                    </div>
                    <div class="rx-text">${mgmt.chemical}</div>
                `;
                mgmtGrid.appendChild(cDiv);
            }

            if (mgmt.cultural) {
                const cultDiv = document.createElement('div');
                cultDiv.className = 'rx-card';
                cultDiv.innerHTML = `
                    <div class="rx-title rx-cultural">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a2 2 0 0 1-2 2h-4a2 2 0 0 1-2-2v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7Z"/><line x1="9" x2="15" y1="22" y2="22"/></svg>
                        <span>${dict.rx_cult}</span>
                    </div>
                    <div class="rx-text">${mgmt.cultural}</div>
                `;
                mgmtGrid.appendChild(cultDiv);
            }

            if (mgmt.biological) {
                const bioDiv = document.createElement('div');
                bioDiv.className = 'rx-card';
                bioDiv.innerHTML = `
                    <div class="rx-title rx-bio">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.4 19 2c1 2 2 4.1 2 8 0 5.5-4.5 10-10 10Z"/></svg>
                        <span>${dict.rx_bio}</span>
                    </div>
                    <div class="rx-text">${mgmt.biological}</div>
                `;
                mgmtGrid.appendChild(bioDiv);
            }
        }

        /* ── Feature 1: Grad-CAM Toggle Mode ── */
        function toggleViewMode(mode) {
            currentViewMode = mode;
            const previewImg = document.getElementById('preview-img');
            const modalImg = document.getElementById('modal-img');
            const btnOrig = document.getElementById('btn-view-orig');
            const btnCam  = document.getElementById('btn-view-cam');

            if (mode === 'cam' && gradcamImageSrc) {
                previewImg.src = gradcamImageSrc;
                modalImg.src = gradcamImageSrc;
                btnCam.classList.add('active');
                btnOrig.classList.remove('active');
            } else {
                previewImg.src = originalImageSrc;
                modalImg.src = originalImageSrc;
                btnOrig.classList.add('active');
                btnCam.classList.remove('active');
            }
        }

        /* ── Feature 2: Spray Dosage Calculator ── */
        function calculateDosage() {
            const isBn = currentLang === 'bn';
            const amountInput = document.getElementById('land-amount');
            const unitSelect  = document.getElementById('land-unit');
            const waterVal    = document.getElementById('calc-water-val');
            const chemVal     = document.getElementById('calc-chem-val');
            const tanksVal    = document.getElementById('calc-tanks-val');
            const adviceText  = document.getElementById('calc-advice-text');

            if (!amountInput || !unitSelect) return;

            const amount = parseFloat(amountInput.value) || 0;
            const unit   = unitSelect.value;

            // Convert to decimals (1 acre = 100 decimals, 1 bigha = 33 decimals, 1 katha = 1.65 decimals)
            let decimals = amount;
            if (unit === 'katha') decimals = amount * 1.65;
            else if (unit === 'bigha') decimals = amount * 33;
            else if (unit === 'acre') decimals = amount * 100;

            // Standard foliar water rate: ~2 Liters per decimal (200L per acre)
            const totalWater = Math.max(1, Math.round(decimals * 2));
            const tanks = (totalWater / 16).toFixed(1);

            // Chemical dosage calculation
            const ratePerL = (currentDiseaseData && typeof currentDiseaseData.dosage_rate_per_liter === 'number') ? currentDiseaseData.dosage_rate_per_liter : 1.0;
            const chemUnit = (currentDiseaseData && currentDiseaseData.dosage_unit) ? currentDiseaseData.dosage_unit : 'ml';
            const totalChem = (totalWater * ratePerL).toFixed(1);
            const chemName  = isBn 
                ? (currentDiseaseData && currentDiseaseData.chemical_product_bn ? currentDiseaseData.chemical_product_bn : 'বালাইনাশক')
                : (currentDiseaseData && currentDiseaseData.chemical_product_en ? currentDiseaseData.chemical_product_en : 'Fungicide');

            if (ratePerL === 0) {
                waterVal.textContent = isBn ? `${totalWater} লিটার` : `${totalWater} L`;
                chemVal.textContent  = isBn ? 'প্রয়োজন নেই (০ মিলি)' : 'None (0 ml)';
                tanksVal.textContent = isBn ? `${tanks} ড্রাম` : `${tanks} Tanks`;
                adviceText.innerHTML = isBn 
                    ? '💡 পাতা সম্পূর্ণ সুস্থ। কোনো রাসায়নিক বালাইনাশক স্প্রে করার প্রয়োজন নেই।' 
                    : '💡 Leaf is completely healthy. No chemical spray is required.';
            } else {
                waterVal.textContent = isBn ? `${totalWater} লিটার` : `${totalWater} Liters`;
                chemVal.textContent  = isBn ? `${totalChem} ${chemUnit}` : `${totalChem} ${chemUnit}`;
                tanksVal.textContent = isBn ? `${tanks} ড্রাম` : `${tanks} Tanks`;
                adviceText.innerHTML = isBn
                    ? `💡 <strong>হিসাব:</strong> মোট <strong>${totalWater} লিটার</strong> পানিতে <strong>${totalChem} ${chemUnit}</strong> ${chemName} ভালোভাবে গুলিয়ে <strong>${tanks}টি</strong> ড্রামের সাহায্যে পুরো ক্ষেতে সমানভাবে স্প্রে করুন।`
                    : `💡 <strong>Mixing:</strong> Dissolve <strong>${totalChem} ${chemUnit}</strong> of ${chemName} in <strong>${totalWater} Liters</strong> of water and apply evenly using <strong>${tanks}</strong> knapsack tanks.`;
            }
        }

        /* ── Feature 2: Populate Official Doctor-Style Prescription Sheet ── */
        function populatePrescriptionData() {
            if (!currentDiseaseData) return null;

            const isBn = currentLang === 'bn';
            const dateStr = new Date().toLocaleDateString(isBn ? 'bn-BD' : 'en-US', {
                year: 'numeric', month: 'long', day: 'numeric'
            });
            const caseId = 'RX-' + Math.floor(100000 + Math.random() * 900000);

            // Dynamic Bilingual Labels in PDF Sheet
            const hdrSub = document.getElementById('pdf-hdr-sub');
            if (hdrSub) hdrSub.textContent = isBn 
                ? 'ডিজিটাল ফসল চিকিৎসাপত্র ও পূর্ণাঙ্গ রিপোর্ট (Digital Agronomy Prescription)' 
                : 'Digital Agronomy Prescription & Diagnostic Report';

            const lblDate = document.getElementById('pdf-lbl-date');
            if (lblDate) lblDate.textContent = isBn ? 'তারিখ:' : 'Date:';

            const lblCase = document.getElementById('pdf-lbl-case');
            if (lblCase) lblCase.textContent = isBn ? 'কেস আইডি:' : 'Case ID:';

            const lblModel = document.getElementById('pdf-lbl-model');
            if (lblModel) lblModel.textContent = isBn 
                ? 'এআই মডেল: ResNet-18 (GAN-Augmented)' 
                : 'AI Model: ResNet-18 (GAN-Augmented)';

            const lblDiag = document.getElementById('pdf-lbl-diag');
            if (lblDiag) lblDiag.textContent = isBn 
                ? 'শনাক্তকৃত রোগ (AI Diagnosis)' 
                : 'DIAGNOSED CONDITION (AI OUTPUT)';

            const lblConf = document.getElementById('pdf-lbl-conf');
            if (lblConf) lblConf.textContent = isBn ? 'মডেল কনফিডেন্স' : 'Model Confidence';

            const lblOrig = document.getElementById('pdf-lbl-orig');
            if (lblOrig) lblOrig.textContent = isBn 
                ? '১. মূল ধানের পাতা (Sample Leaf)' 
                : '1. Original Leaf Sample';

            const lblCam = document.getElementById('pdf-lbl-cam');
            if (lblCam) lblCam.textContent = isBn 
                ? '২. এআই দৃষ্টি হিটম্যাপ (Grad-CAM XAI)' 
                : '2. AI Attention Heatmap (Grad-CAM)';

            const lblSym = document.getElementById('pdf-lbl-sym');
            const lblCauses = document.getElementById('pdf-lbl-causes');
            if (lblCauses) lblCauses.textContent = isBn 
                ? '⚠️ আক্রমণের কারণসমূহ (Causes):' 
                : '⚠️ Disease Causes & Triggers:';

            

            const lblRx = document.getElementById('pdf-lbl-rx');
            if (lblRx) lblRx.textContent = isBn 
                ? '💊 পূর্ণাঙ্গ বালাইনাশক ও প্রতিকার প্রেসক্রিপশন (Rx Treatment)' 
                : '💊 Complete Agronomic Rx Prescription & Control';

            const lblChem = document.getElementById('pdf-lbl-chem');
            if (lblChem) lblChem.textContent = isBn ? '[রাসায়নিক প্রতিকার]' : '[Chemical Control]';

            const lblCult = document.getElementById('pdf-lbl-cult');
            if (lblCult) lblCult.textContent = isBn ? '[কৃষি ও পরিচর্যা ব্যবস্থাপনা]' : '[Cultural & Field Care]';

            const lblCalc = document.getElementById('pdf-lbl-calc');
            if (lblCalc) lblCalc.textContent = isBn ? '🧪 জমির ডোজ হিসাব:' : '🧪 Field Spray & Dosage:';

            const lblSpray = document.getElementById('pdf-lbl-spray');
            if (lblSpray) lblSpray.textContent = isBn ? '🌦️ স্প্রে সতর্কতা:' : '🌦️ Spraying Advisory:';

            const txtSpray = document.getElementById('pdf-txt-spray');
            if (txtSpray) txtSpray.innerHTML = isBn 
                ? '• ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা থাকলে স্প্রে স্থগিত রাখুন।<br/>• বিকেলে মিষ্টি রোদে বাতাসের অনুকূলে স্প্রে করুন।' 
                : '• Postpone spraying if rain is expected within 4 hours.<br/>• Always spray in late afternoon with mild sunlight along wind direction.';

            const lblSys = document.getElementById('pdf-lbl-sys');
            if (lblSys) lblSys.innerHTML = isBn 
                ? 'সিস্টেম: <strong>RiceGuard AI Autonomous Vision Platform</strong>' 
                : 'System: <strong>RiceGuard AI Autonomous Vision Platform</strong>';

            const lblDev = document.getElementById('pdf-lbl-dev');
            if (lblDev) lblDev.innerHTML = isBn 
                ? 'কারিগরি বিকাশ ও ডিজাইন: <strong class="notranslate" translate="no">Ohi</strong>' 
                : 'Designed & Developed by: <strong class="notranslate" translate="no">Ohi</strong>';

            // Diagnostic Values
            document.getElementById('pdf-date').textContent = dateStr;
            document.getElementById('pdf-case-id').textContent = caseId;
            document.getElementById('pdf-disease-name').textContent = isBn ? (currentDiseaseData.name_bn || currentPredictionName) : (currentDiseaseData.name_en || currentPredictionName);
            document.getElementById('pdf-pathogen').textContent = currentDiseaseData.pathogen 
                ? (isBn ? `জীবাণু: ${currentDiseaseData.pathogen}` : `Pathogen: ${currentDiseaseData.pathogen}`)
                : '';
            document.getElementById('pdf-confidence').textContent = currentConfidence + '%';
            
            const sevEl = document.getElementById('pdf-severity');
            sevEl.textContent = isBn ? (currentDiseaseData.severity_bn || 'ঝুঁকি') : (currentDiseaseData.severity_en || 'Risk');
            if (currentDiseaseData.severity_color) {
                sevEl.style.background = currentDiseaseData.severity_color;
            }

            document.getElementById('pdf-img-orig').src = originalImageSrc;
            document.getElementById('pdf-img-cam').src = gradcamImageSrc || originalImageSrc;

            // Symptoms List
            const symListEl = document.getElementById('pdf-list-symptoms');
            if (symListEl) {
                symListEl.innerHTML = '';
                const symptoms = (isBn ? currentDiseaseData.symptoms_bn : currentDiseaseData.symptoms_en) || [];
                symptoms.slice(0, 3).forEach(s => {
                    const li = document.createElement('li');
                    li.textContent = s;
                    symListEl.appendChild(li);
                });
            }

            // Causes List
            const causeListEl = document.getElementById('pdf-list-causes');
            if (causeListEl) {
                causeListEl.innerHTML = '';
                const causes = (isBn ? currentDiseaseData.causes_bn : currentDiseaseData.causes_en) || [];
                causes.slice(0, 3).forEach(c => {
                    const li = document.createElement('li');
                    li.textContent = c;
                    causeListEl.appendChild(li);
                });
            }

            const mgmt = isBn ? currentDiseaseData.management_bn : currentDiseaseData.management_en;
            document.getElementById('pdf-rx-chemical').textContent = mgmt?.chemical || (isBn ? 'প্রয়োজন নেই' : 'None required.');
            document.getElementById('pdf-rx-cultural').textContent = mgmt?.cultural || (isBn ? 'সুষম সেচ ও মাঠ পরিচর্যা বজায় রাখুন।' : 'Maintain proper crop care.');

            calculateDosage();

            const landAmt = document.getElementById('land-amount')?.value || '10';
            const landUnitSelect = document.getElementById('land-unit');
            const landUnitText = landUnitSelect ? landUnitSelect.options[landUnitSelect.selectedIndex].text : 'শতক';
            const water = document.getElementById('calc-water-val')?.textContent || '';
            const chem = document.getElementById('calc-chem-val')?.textContent || '';
            const tanks = document.getElementById('calc-tanks-val')?.textContent || '';

            document.getElementById('pdf-land-calc-text').textContent = `${landAmt} ${landUnitText}`;
            document.getElementById('pdf-calc-summary').textContent = isBn 
                ? `প্রয়োজনীয় পানি: ${water} | বালাইনাশক ডোজ: ${chem} | ১৬ লিটার স্প্রে ড্রাম: ${tanks}`
                : `Water Volume: ${water} | Chemical Dosage: ${chem} | 16L Tanks: ${tanks}`;

            return caseId;
        }

        /* ── Feature 2: Open / Close Doctor-Style Live Prescription Modal ── */
        function openPrescriptionModal() {
            if (!currentDiseaseData) {
                alert(currentLang === 'bn' ? 'অনুগ্রহ করে প্রথমে একটি পাতার ছবি আপলোড করে বিশ্লেষণ করুন।' : 'Please upload and analyze a rice leaf photo first.');
                return;
            }
            populatePrescriptionData();
            const modal = document.getElementById('modal-prescription');
            if (modal) {
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        }

        function closePrescriptionModal() {
            const modal = document.getElementById('modal-prescription');
            if (modal) {
                modal.classList.remove('active');
                document.body.style.overflow = '';
            }
        }

        function downloadPrescriptionPDF() {
            openPrescriptionModal();
        }

        /* ── Direct 1-Click PDF File Download (html2canvas + jsPDF) ── */
        async function executePdfDownload() {
            if (!currentDiseaseData) return;

            const caseId = populatePrescriptionData() || 'RX-REPORT';
            const btn = document.getElementById('btn-modal-pdf-download');
            const originalHtml = btn ? btn.innerHTML : '';
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = `<svg class="spin-svg" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="animation: spin 1s linear infinite;"><path d="M21 12a9 9 0 1 1-6.219-8.56"/></svg> <span>${currentLang === 'bn' ? 'PDF ডাউনলোড হচ্ছে…' : 'Downloading PDF…'}</span>`;
            }

            const source = document.getElementById('prescription-pdf-canvas');
            if (!source) {
                if (btn) { btn.disabled = false; btn.innerHTML = originalHtml; }
                return;
            }

            // Ensure images have source loaded
            const imgOrig = document.getElementById('pdf-img-orig');
            const imgCam = document.getElementById('pdf-img-cam');
            if (imgOrig && !imgOrig.src) imgOrig.src = originalImageSrc;
            if (imgCam && !imgCam.src) imgCam.src = gradcamImageSrc || originalImageSrc;

            try {
                // Use html2canvas directly on the styled prescription canvas
                if (typeof html2canvas !== 'undefined') {
                    const canvas = await html2canvas(source, {
                        scale: 2.5,
                        useCORS: true,
                        allowTaint: true,
                        backgroundColor: '#FFFFFF',
                        logging: false
                    });

                    const imgData = canvas.toDataURL('image/jpeg', 0.98);

                    // Determine jsPDF constructor
                    const jsPDFClass = (window.jspdf && window.jspdf.jsPDF) ? window.jspdf.jsPDF : (window.jsPDF || null);

                    if (jsPDFClass) {
                        const pdf = new jsPDFClass({
                            orientation: 'portrait',
                            unit: 'mm',
                            format: 'a4',
                            compress: true
                        });

                        const pdfWidth = pdf.internal.pageSize.getWidth();
                        const pdfHeight = pdf.internal.pageSize.getHeight();
                        const margin = 4;
                        const printWidth = pdfWidth - (margin * 2);
                        const printHeight = (canvas.height * printWidth) / canvas.width;

                        pdf.addImage(imgData, 'JPEG', margin, margin, printWidth, Math.min(printHeight, pdfHeight - (margin * 2)));
                        pdf.save(`RiceGuard_Prescription_${caseId}.pdf`);
                        return;
                    }
                }

                // Fallback to html2pdf if jsPDF object was not directly found
                if (typeof html2pdf !== 'undefined') {
                    const opt = {
                        margin: [4, 4, 4, 4],
                        filename: `RiceGuard_Prescription_${caseId}.pdf`,
                        image: { type: 'jpeg', quality: 0.98 },
                        html2canvas: { scale: 2, useCORS: true, backgroundColor: '#FFFFFF' },
                        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
                    };
                    await html2pdf().set(opt).from(source).save();
                } else {
                    printPrescription();
                }
            } catch (err) {
                console.error('PDF generation error, falling back:', err);
                printPrescription();
            } finally {
                if (btn) {
                    btn.disabled = false;
                    btn.innerHTML = originalHtml;
                }
            }
        }

        /* ── Direct Native Print / PDF Save via Dedicated Clean Window ── */
        function printPrescription() {
            if (!currentDiseaseData) {
                alert(currentLang === 'bn' ? 'অনুগ্রহ করে প্রথমে একটি পাতার ছবি আপলোড করে বিশ্লেষণ করুন।' : 'Please upload and analyze a rice leaf photo first.');
                return;
            }
            populatePrescriptionData();
            
            const source = document.getElementById('prescription-pdf-canvas');
            if (!source) {
                window.print();
                return;
            }

            const sheetHtml = source.innerHTML;
            const printWin = window.open('', '_blank', 'width=850,height=900');
            if (printWin) {
                printWin.document.write(`
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>RiceGuard_Prescription</title>
                        <meta charset="utf-8" />
                        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet" />
                        <style>
                            * { box-sizing: border-box; }
                            body {
                                margin: 0;
                                padding: 8mm 10mm;
                                background: #FFFFFF;
                                color: #0F291E;
                                font-family: 'Noto Sans Bengali', 'Plus Jakarta Sans', Arial, sans-serif;
                                -webkit-print-color-adjust: exact !important;
                                print-color-adjust: exact !important;
                            }
                            @page {
                                size: A4 portrait;
                                margin: 0;
                            }
                            .pr-sheet-box {
                                border: 2px solid #0F5132 !important;
                                border-radius: 8px !important;
                                padding: 1.15rem 1.35rem !important;
                                background: #FFFFFF !important;
                                width: 100% !important;
                            }
                        </style>
                    </head>
                    <body>
                        ${sheetHtml}
                        <script>
                            window.onload = function() {
                                setTimeout(function() {
                                    window.print();
                                }, 300);
                            };
                        <\/script>
                    </body>
                    </html>
                `);
                printWin.document.close();
            } else {
                window.print();
            }
        }

        /* ── 1-Click WhatsApp Direct Prescription Share ── */
        function sharePrescriptionWhatsApp() {
            if (!currentDiseaseData) {
                alert(currentLang === 'bn' ? 'অনুগ্রহ করে প্রথমে একটি পাতার ছবি আপলোড করে বিশ্লেষণ করুন।' : 'Please upload and analyze a rice leaf first.');
                return;
            }

            const isBn = currentLang === 'bn';
            const diseaseName = isBn ? (currentDiseaseData.name_bn || currentPredictionName) : (currentDiseaseData.name_en || currentPredictionName);
            const pathogen = currentDiseaseData.pathogen || 'N/A';
            const severity = isBn ? (currentDiseaseData.severity_bn || 'সতর্কতা') : (currentDiseaseData.severity_en || 'Caution');
            const mgmt = isBn ? currentDiseaseData.management_bn : currentDiseaseData.management_en;
            const chemical = mgmt?.chemical || (isBn ? 'প্রয়োজন নেই' : 'None required.');
            const cultural = mgmt?.cultural || (isBn ? 'সুষম সার ও সেচ ব্যবস্থাপনা।' : 'Proper water & fertilizer management.');

            calculateDosage();

            const landAmt = document.getElementById('land-amount')?.value || '10';
            const landUnitSelect = document.getElementById('land-unit');
            const landUnitText = landUnitSelect ? landUnitSelect.options[landUnitSelect.selectedIndex].text : 'শতক';
            const water = document.getElementById('calc-water-val')?.textContent || '';
            const chem = document.getElementById('calc-chem-val')?.textContent || '';
            const tanks = document.getElementById('calc-tanks-val')?.textContent || '';

            let message = '';
            if (isBn) {
                message = `🌾 *RiceGuard AI — ডিজিটাল ফসল প্রেসক্রিপশন*\n` +
                          `━━━━━━━━━━━━━━━━━━━━\n` +
                          `📋 *শনাক্তকৃত অবস্থা:* ${diseaseName}\n` +
                          `🔬 *জীবাণু/প্যাথোজেন:* ${pathogen}\n` +
                          `🎯 *মডেল কনফিডেন্স:* ${currentConfidence}%\n` +
                          `⚠️ *ঝুঁকির মাত্রা:* ${severity}\n\n` +
                          `💊 *বালাইনাশক ও চিকিৎসা পরামর্শ:*\n${chemical}\n\n` +
                          `🌱 *মাঠ পরিচর্যা:*\n${cultural}\n\n` +
                          `🧪 *জমির ডোজ হিসাব (${landAmt} ${landUnitText}):*\n` +
                          `• মোট পানি: ${water}\n` +
                          `• ওষুধের পরিমাণ: ${chem}\n` +
                          `• ১৬ লিটার ড্রাম: ${tanks}\n\n` +
                          `🌦️ *স্প্রে সতর্কতা:*\n` +
                          `• ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা থাকলে স্প্রে স্থগিত রাখুন।\n` +
                          `• বিকেলে মিষ্টি রোদে বাতাসের অনুকূলে স্প্রে করুন।\n\n` +
                          `📞 *জরুরি কৃষি হেল্পলাইন:* ১৬১২৩ (টোল-ফ্রি)\n` +
                          `👨‍🔬 *ডিজাইন ও বিকাশ:* Ohi\n` +
                          `🌐 *লাইভ প্ল্যাটফর্ম:* https://rice-leaf-disease-detection-1-1m1k.onrender.com/`;
            } else {
                message = `🌾 *RiceGuard AI — Digital Crop Prescription*\n` +
                          `━━━━━━━━━━━━━━━━━━━━\n` +
                          `📋 *Diagnosis:* ${diseaseName}\n` +
                          `🔬 *Pathogen:* ${pathogen}\n` +
                          `🎯 *AI Confidence:* ${currentConfidence}%\n` +
                          `⚠️ *Severity:* ${severity}\n\n` +
                          `💊 *Treatment & Rx:*\n${chemical}\n\n` +
                          `🌱 *Field Management:*\n${cultural}\n\n` +
                          `🧪 *Field Dosage (${landAmt} ${landUnitText}):*\n` +
                          `• Total Water: ${water}\n` +
                          `• Chemical Dosage: ${chem}\n` +
                          `• 16L Knapsack Tanks: ${tanks}\n\n` +
                          `🌦️ *Spraying Advisory:*\n` +
                          `• Postpone spraying if rain is expected within 4 hours.\n` +
                          `• Spray along wind direction in late afternoon.\n\n` +
                          `📞 *National Agri Hotline:* 16123\n` +
                          `👨‍🔬 *Developed by:* Ohi\n` +
                          `🌐 *Platform:* https://rice-leaf-disease-detection-1-1m1k.onrender.com/`;
            }

            const whatsappUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(message)}`;
            window.open(whatsappUrl, '_blank');
        }

        
        /* ── Batch Field Audit Controller & Multi-Image State ── */
        window.currentAnalysisMode = 'single';
        window.batchSelectedFiles = [];
        window.currentBatchData = null;
        window.activeBatchAudio = null;
        window.isBatchSpeaking = false;
        window.currentBatchVoiceGender = localStorage.getItem('riceguard_voice_gender') || 'male';

        function switchAnalysisMode(mode) {
            window.currentAnalysisMode = mode;
            const singleBtn = document.getElementById('btn-mode-single');
            const batchBtn = document.getElementById('btn-mode-batch');
            const singleContainer = document.getElementById('single-mode-container');
            const batchContainer = document.getElementById('batch-mode-container');
            const singleResults = document.getElementById('state-result');
            const batchResults = document.getElementById('batch-results-wrap');
            const emptyState = document.getElementById('state-empty');

            if (mode === 'batch') {
                if (singleBtn) singleBtn.classList.remove('active');
                if (batchBtn) batchBtn.classList.add('active');
                if (singleContainer) singleContainer.style.display = 'none';
                if (batchContainer) batchContainer.style.display = 'block';

                if (window.currentBatchData) {
                    if (singleResults) singleResults.style.display = 'none';
                    if (emptyState) emptyState.style.display = 'none';
                    if (batchResults) batchResults.classList.add('active');
                } else {
                    if (singleResults) singleResults.style.display = 'none';
                    if (batchResults) batchResults.classList.remove('active');
                    if (emptyState) emptyState.style.display = 'flex';
                }
            } else {
                if (batchBtn) batchBtn.classList.remove('active');
                if (singleBtn) singleBtn.classList.add('active');
                if (batchContainer) batchContainer.style.display = 'none';
                if (singleContainer) singleContainer.style.display = 'block';

                if (batchResults) batchResults.classList.remove('active');
                if (currentDiseaseData) {
                    if (emptyState) emptyState.style.display = 'none';
                    if (singleResults) singleResults.style.display = 'block';
                } else {
                    if (singleResults) singleResults.style.display = 'none';
                    if (emptyState) emptyState.style.display = 'flex';
                }
            }
        }

                /**
         * Fast client-side image compressor using HTML5 Canvas.
         * Downscales high-resolution mobile photos (12MP+, 4000x3000) to max 1024px, ~150-250KB JPEG.
         * Eliminates network timeouts and prevents 512MB RAM server crashes on cloud free tiers.
         */
        async function compressImageFile(file, maxWidth = 1024, maxHeight = 1024, quality = 0.82) {
            if (!file || !file.type || !file.type.startsWith('image/')) {
                return file;
            }
            if (file.size <= 250 * 1024 && file.type === 'image/jpeg') {
                return file;
            }

            return new Promise((resolve) => {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const img = new Image();
                    img.onload = () => {
                        let w = img.naturalWidth || img.width;
                        let h = img.naturalHeight || img.height;

                        if (w > maxWidth || h > maxHeight) {
                            if (w > h) {
                                h = Math.round((h * maxWidth) / w);
                                w = maxWidth;
                            } else {
                                w = Math.round((w * maxHeight) / h);
                                h = maxHeight;
                            }
                        }

                        const canvas = document.createElement('canvas');
                        canvas.width = Math.max(1, w);
                        canvas.height = Math.max(1, h);
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(img, 0, 0, w, h);

                        canvas.toBlob(
                            (blob) => {
                                if (blob && blob.size < file.size) {
                                    const safeName = (file.name || 'sample.jpg').replace(/\.[^.]+$/, '.jpg');
                                    const newFile = new File([blob], safeName, {
                                        type: 'image/jpeg',
                                        lastModified: Date.now()
                                    });
                                    resolve(newFile);
                                } else {
                                    resolve(file);
                                }
                            },
                            'image/jpeg',
                            quality
                        );
                    };
                    img.onerror = () => resolve(file);
                    img.src = e.target.result;
                };
                reader.onerror = () => resolve(file);
                reader.readAsDataURL(file);
            });
        }

        function handleBatchFileInput(files) {
            if (!files || files.length === 0) return;
            const validTypes = ['image/jpeg', 'image/png', 'image/bmp', 'image/webp', 'image/tiff'];
            
            for (let i = 0; i < files.length; i++) {
                const file = files[i];
                if (window.batchSelectedFiles.length >= 25) {
                    alert(currentLang === 'bn' ? 'সর্বোচ্চ ২৫টি ছবি একসাথে আপলোড করা যাবে।' : 'Maximum 25 images allowed per batch.');
                    break;
                }
                if (file.size > 10 * 1024 * 1024) {
                    alert(currentLang === 'bn' ? `${file.name} ফাইলটির সাইজ ১০ মেগাবাইটের বেশি!` : `File ${file.name} exceeds 10MB limit!`);
                    continue;
                }
                window.batchSelectedFiles.push(file);
            }

            renderBatchThumbnails();
        }

        function renderBatchThumbnails() {
            const tray = document.getElementById('batch-thumbnail-tray');
            const header = document.getElementById('batch-tray-header');
            const badge = document.getElementById('batch-count-badge');
            const submitBtn = document.getElementById('btn-batch-submit');

            if (!tray || !header) return;

            const count = window.batchSelectedFiles.length;
            if (badge) badge.textContent = currentLang === 'bn' ? `${count} টি পাতা নির্বাচিত` : `${count} samples selected`;

            if (count > 0) {
                tray.style.display = 'grid';
                header.style.display = 'flex';
                if (submitBtn) submitBtn.disabled = false;
            } else {
                tray.style.display = 'none';
                header.style.display = 'none';
                if (submitBtn) submitBtn.disabled = true;
                tray.innerHTML = '';
                return;
            }

            tray.innerHTML = '';
            window.batchSelectedFiles.forEach((file, index) => {
                const card = document.createElement('div');
                card.className = 'batch-thumb-card';
                
                const img = document.createElement('img');
                img.alt = file.name;
                const reader = new FileReader();
                reader.onload = (e) => { img.src = e.target.result; };
                reader.readAsDataURL(file);

                const removeBtn = document.createElement('button');
                removeBtn.type = 'button';
                removeBtn.className = 'batch-thumb-remove';
                removeBtn.title = currentLang === 'bn' ? 'মুছুন' : 'Remove';
                removeBtn.innerHTML = '✕';
                removeBtn.onclick = (e) => {
                    e.stopPropagation();
                    removeBatchFile(index);
                };

                card.appendChild(img);
                card.appendChild(removeBtn);
                tray.appendChild(card);
            });
        }

        function removeBatchFile(index) {
            window.batchSelectedFiles.splice(index, 1);
            renderBatchThumbnails();
        }

        async function loadQuickBatchSamples() {
            const sampleUrls = [
                { url: '/static/samples/healthy.jpg', name: 'Field_Sample_1_Healthy.jpg' },
                { url: '/static/samples/leaf_blast.jpg', name: 'Field_Sample_2_Blast.jpg' },
                { url: '/static/samples/brown_spot.jpg', name: 'Field_Sample_3_BrownSpot.jpg' },
                { url: '/static/samples/bacterial_blight.jpg', name: 'Field_Sample_4_Blight.jpg' }
            ];

            window.batchSelectedFiles = [];
            for (const s of sampleUrls) {
                try {
                    const res = await fetch(s.url);
                    const blob = await res.blob();
                    const file = new File([blob], s.name, { type: 'image/jpeg' });
                    window.batchSelectedFiles.push(file);
                } catch (e) {
                    console.warn('Failed to load sample:', s.name, e);
                }
            }
            renderBatchThumbnails();
        }

        async function submitBatchAnalysis() {
            if (!window.batchSelectedFiles || window.batchSelectedFiles.length === 0) {
                alert(currentLang === 'bn' ? 'অনুগ্রহ করে প্রথমে মাঠের পাতার ছবি নির্বাচন করুন।' : 'Please select leaf sample images first.');
                return;
            }

            const btn = document.getElementById('btn-batch-submit');
            const btnText = document.getElementById('btn-batch-text');
            const emptyState = document.getElementById('state-empty');
            const loadingState = document.getElementById('state-loading');
            const singleResults = document.getElementById('state-result');
            const batchResults = document.getElementById('batch-results-wrap');

            if (btn) btn.disabled = true;
            if (btnText) btnText.textContent = (I18N[currentLang] || I18N.bn).btn_batch_analyzing || 'মাঠের নমুনা বিশ্লেষণ চলছে…';

            if (emptyState) emptyState.style.display = 'none';
            if (singleResults) singleResults.style.display = 'none';
            if (batchResults) batchResults.classList.remove('active');
            if (loadingState) {
                loadingState.style.display = 'flex';
                const stepText = document.getElementById('loading-step-text');
                if (stepText) stepText.textContent = currentLang === 'bn' 
                    ? `মাঠের ${window.batchSelectedFiles.length}টি নমুনা অপ্টিমাইজ ও বিশ্লেষণ হচ্ছে…` 
                    : `Optimizing and analyzing ${window.batchSelectedFiles.length} field samples…`;
            }

            const formData = new FormData();
            try {
                for (let i = 0; i < window.batchSelectedFiles.length; i++) {
                    const originalF = window.batchSelectedFiles[i];
                    const compF = await compressImageFile(originalF);
                    formData.append('files', compF);
                }
            } catch (compErr) {
                console.warn('Compression fallback:', compErr);
                window.batchSelectedFiles.forEach(f => formData.append('files', f));
            }

            try {
                const response = await fetch('/api/batch-predict', {
                    method: 'POST',
                    body: formData
                });

                let data;
                try {
                    data = await response.json();
                } catch (parseErr) {
                    if (!response.ok) {
                        const is502 = response.status === 502 || response.status === 504;
                        const errMsg = is502
                            ? (currentLang === 'bn'
                                ? 'সার্ভার স্লিপ মোড থেকে চালু হচ্ছে বা মেমোরি রিফ্রেশ হচ্ছে (HTTP ' + response.status + ')। অনুগ্রহ করে ২০-৩০ সেকেন্ড অপেক্ষা করে আবার চেষ্টা করুন।'
                                : 'Server is waking up from sleep or refreshing memory (HTTP ' + response.status + '). Please wait 20-30 seconds and try again.')
                            : (currentLang === 'bn'
                                ? 'সার্ভার যোগাযোগে ত্রুটি (HTTP ' + response.status + ')। অনুগ্রহ করে পুনরায় চেষ্টা করুন।'
                                : 'Server communication error (HTTP ' + response.status + '). Please try again.');
                        throw new Error(errMsg);
                    }
                    throw parseErr;
                }

                if (!response.ok || !data.success) {
                    throw new Error(data.error || 'Batch analysis failed');
                }

                window.currentBatchData = data;
                if (loadingState) loadingState.style.display = 'none';
                renderBatchResults(data);

                // Scroll smoothly to results
                const outCard = document.getElementById('output-card');
                if (outCard) outCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

            } catch (err) {
                if (loadingState) loadingState.style.display = 'none';
                if (emptyState) emptyState.style.display = 'flex';
                alert((currentLang === 'bn' ? 'মাঠ নিরীক্ষা বিজ্ঞপ্তি: ' : 'Field audit notice: ') + err.message);
            } finally {
                if (btn) btn.disabled = false;
                if (btnText) btnText.textContent = (I18N[currentLang] || I18N.bn).btn_batch_analyze || 'মাঠের সকল নমুনা বিশ্লেষণ করুন';
            }
        }

        /* ── Check if browser has an authentic native Bengali TTS engine ── */
        function hasNativeBengaliSpeechSynthesisVoice() {
            if (!('speechSynthesis' in window)) return false;
            try {
                const voices = window.speechSynthesis.getVoices() || [];
                return voices.some(v => v.lang && (v.lang.toLowerCase().includes('bn') || v.lang.toLowerCase().includes('bengali')));
            } catch (e) {
                return false;
            }
        }

        /* ── Pre-cache Batch Summary Voice in Background for 0ms Instant Play ── */
        function preloadBatchAudio(data) {
            if (!data) return;
            window.batchPreloadedAudios = window.batchPreloadedAudios || {};
            const textBn = data.speech_text_bn;
            const textEn = data.speech_text_en;

            if (textBn) {
                try {
                    const mBn = new Audio(`/api/tts?lang=bn&gender=male&voice=pradeep&text=${encodeURIComponent(textBn)}`);
                    mBn.preload = 'auto';
                    const fBn = new Audio(`/api/tts?lang=bn&gender=female&voice=nabanita&text=${encodeURIComponent(textBn)}`);
                    fBn.preload = 'auto';
                    window.batchPreloadedAudios['bn_male'] = mBn;
                    window.batchPreloadedAudios['bn_female'] = fBn;
                } catch (e) {
                    console.warn('Batch audio preload bn notice:', e);
                }
            }

            if (textEn) {
                try {
                    const mEn = new Audio(`/api/tts?lang=en&gender=male&voice=guy&text=${encodeURIComponent(textEn)}`);
                    mEn.preload = 'auto';
                    const fEn = new Audio(`/api/tts?lang=en&gender=female&voice=aria&text=${encodeURIComponent(textEn)}`);
                    fEn.preload = 'auto';
                    window.batchPreloadedAudios['en_male'] = mEn;
                    window.batchPreloadedAudios['en_female'] = fEn;
                } catch (e) {
                    console.warn('Batch audio preload en notice:', e);
                }
            }
        }

        function renderBatchResults(data) {
            if (!data) return;
            preloadBatchAudio(data); // 🚀 Immediately pre-cache audio in background for 0ms play
            const isBn = currentLang === 'bn';
            const batchWrap = document.getElementById('batch-results-wrap');
            if (!batchWrap) return;

            batchWrap.classList.add('active');

            // 1. Health Gauge
            const gaugeVal = document.getElementById('batch-health-pct');
            if (gaugeVal) gaugeVal.textContent = `${data.healthy_pct}%`;

            const gaugeBox = document.getElementById('batch-health-gauge');
            if (gaugeBox) {
                if (data.healthy_pct >= 70) {
                    gaugeBox.style.background = 'radial-gradient(circle at 30% 30%, #34D399, #059669)';
                } else if (data.healthy_pct >= 40) {
                    gaugeBox.style.background = 'radial-gradient(circle at 30% 30%, #FBBF24, #D97706)';
                } else {
                    gaugeBox.style.background = 'radial-gradient(circle at 30% 30%, #F87171, #DC2626)';
                }
            }

            // 2. Dominant Disease Title & Risk Badge
            const domTitle = document.getElementById('batch-dominant-title');
            if (domTitle) {
                const dom = data.dominant_disease;
                domTitle.textContent = isBn 
                    ? `প্রধান লক্ষণ: ${dom.name_bn} (${dom.percentage}%)`
                    : `Dominant: ${dom.name_en} (${dom.percentage}%)`;
            }

            const riskBadge = document.getElementById('batch-risk-badge');
            if (riskBadge) {
                const risk = data.field_risk;
                riskBadge.className = `batch-risk-badge ${risk.badge_class}`;
                riskBadge.textContent = isBn ? risk.level_bn : risk.level_en;
            }

            const riskDesc = document.getElementById('batch-risk-desc');
            if (riskDesc) {
                riskDesc.textContent = isBn ? data.field_risk.desc_bn : data.field_risk.desc_en;
            }

            // 3. Disease Prevalence Stacked Progress Bar & Legend Pills
            const distBar = document.getElementById('batch-dist-bar');
            const distLegends = document.getElementById('batch-dist-legends');
            if (distBar && distLegends) {
                distBar.innerHTML = '';
                distLegends.innerHTML = '';

                const colors = {
                    'Healthy Rice Leaf': '#10B981',
                    'Leaf Blast': '#DC2626',
                    'Bacterial Leaf Blight': '#EA580C',
                    'Brown Spot': '#D97706',
                    'Sheath Blight': '#8B5CF6',
                    'Rice Hispa': '#EC4899',
                    'Leaf scald': '#06B6D4',
                    'Narrow Brown Leaf Spot': '#F59E0B'
                };

                data.disease_breakdown.forEach(item => {
                    const col = colors[item.class_name] || item.severity_color || '#10B981';
                    
                    // Bar Segment
                    const seg = document.createElement('div');
                    seg.className = 'batch-dist-seg';
                    seg.style.width = `${item.percentage}%`;
                    seg.style.background = col;
                    seg.title = `${isBn ? item.name_bn : item.name_en}: ${item.percentage}% (${item.count} leaves)`;
                    distBar.appendChild(seg);

                    // Legend Tag
                    const leg = document.createElement('span');
                    leg.className = 'batch-legend-tag';
                    leg.innerHTML = `<span class="legend-dot" style="background:${col};"></span> <span>${isBn ? item.name_bn : item.name_en}</span> <strong>${item.percentage}% (${item.count})</strong>`;
                    distLegends.appendChild(leg);
                });
            }

            // 4. Master Integrated Prescription
            const chemEl = document.getElementById('batch-chem-text');
            const cultEl = document.getElementById('batch-cult-text');
            const fertEl = document.getElementById('batch-fert-text');

            if (chemEl) chemEl.textContent = isBn ? data.master_prescription.chemical_bn : data.master_prescription.chemical_en;
            if (cultEl) cultEl.textContent = isBn ? data.master_prescription.cultural_bn : data.master_prescription.cultural_en;
            if (fertEl) fertEl.textContent = isBn ? data.master_prescription.fertilizer_advisory_bn : data.master_prescription.fertilizer_advisory_en;

            // 5. Multi-Sample Grid Gallery
            const grid = document.getElementById('batch-samples-grid');
            if (grid) {
                grid.innerHTML = '';
                data.samples.forEach(sample => {
                    const card = document.createElement('div');
                    card.className = 'batch-sample-card';
                    
                    const title = isBn ? sample.name_bn : sample.name_en;
                    const sev = isBn ? sample.severity_bn : sample.severity_en;

                    card.innerHTML = `
                        <div class="sample-card-media" id="media-sample-${sample.id}">
                            <img src="${sample.thumb_url}" id="img-sample-${sample.id}" alt="${sample.filename}" />
                            <span class="sample-id-pill">#${sample.id}</span>
                            ${sample.gradcam_url ? `
                                <button type="button" class="sample-cam-btn" onclick="toggleSampleCam(${sample.id})">
                                    <span>🔥</span> <span>Grad-CAM</span>
                                </button>
                            ` : ''}
                        </div>
                        <div class="sample-card-body">
                            <div class="sample-pred-title">${title}</div>
                            <div class="sample-meta-row">
                                <span>${isBn ? 'কনফিডেন্স:' : 'Confidence:'}</span>
                                <span class="sample-conf">${sample.confidence}%</span>
                            </div>
                            <button type="button" class="btn-sample-inspect" onclick="openBatchSampleModal(${sample.id})">
                                <span>🔍</span> <span>${isBn ? 'বিস্তারিত ও হিটম্যাপ দেখুন' : 'Inspect Sample & Heatmap'}</span>
                            </button>
                        </div>
                    `;
                    grid.appendChild(card);
                });
            }
        }

        function toggleSampleCam(sampleId) {
            if (!window.currentBatchData) return;
            const sample = window.currentBatchData.samples.find(s => s.id === sampleId);
            if (!sample || !sample.gradcam_url) return;

            const img = document.getElementById(`img-sample-${sampleId}`);
            if (!img) return;

            if (img.getAttribute('data-mode') === 'cam') {
                img.src = sample.thumb_url;
                img.setAttribute('data-mode', 'orig');
            } else {
                img.src = sample.gradcam_url;
                img.setAttribute('data-mode', 'cam');
            }
        }

        function openBatchSampleModal(sampleId) {
            if (!window.currentBatchData) return;
            const sample = window.currentBatchData.samples.find(s => s.id === sampleId);
            if (!sample) return;

            const modal = document.getElementById('batch-sample-modal');
            const isBn = currentLang === 'bn';

            document.getElementById('modal-sample-title').textContent = (isBn ? `নমুনা #${sample.id} — ` : `Sample #${sample.id} — `) + (isBn ? sample.name_bn : sample.name_en);
            document.getElementById('modal-sample-filename').textContent = sample.filename;
            document.getElementById('modal-sample-orig').src = sample.thumb_url;
            document.getElementById('modal-sample-cam').src = sample.gradcam_url || sample.thumb_url;
            document.getElementById('modal-sample-pred').textContent = isBn ? sample.name_bn : sample.name_en;
            document.getElementById('modal-sample-conf').textContent = `${sample.confidence}%`;

            const sympEl = document.getElementById('modal-sample-symptoms');
            if (sympEl) {
                const symps = (isBn ? sample.symptoms_bn : sample.symptoms_en) || [];
                sympEl.textContent = symps.length > 0 ? (isBn ? `লক্ষণ: ${symps.join(' • ')}` : `Symptoms: ${symps.join(' • ')}`) : '';
            }

            if (modal) modal.classList.add('active');
        }

        function closeBatchSampleModal() {
            const modal = document.getElementById('batch-sample-modal');
            if (modal) modal.classList.remove('active');
        }

        /* ── Batch Dual-Voice Audio Player (Male 👨‍🌾 / Female 👩‍⚕️) with 0ms Latency ── */
        let isBatchAudioLoading = false;

        function setBatchVoiceGender(gender) {
            window.currentBatchVoiceGender = gender;
            const maleBtn = document.getElementById('batch-voice-male');
            const femaleBtn = document.getElementById('batch-voice-female');
            if (maleBtn && femaleBtn) {
                if (gender === 'female') {
                    femaleBtn.classList.add('active');
                    maleBtn.classList.remove('active');
                } else {
                    maleBtn.classList.add('active');
                    femaleBtn.classList.remove('active');
                }
            }

            // Sync with global voice
            setVoiceGender(gender);

            if (window.isBatchSpeaking) {
                stopBatchAudioSpeech();
                toggleBatchAudioSpeech();
            }
        }

        function stopBatchAudioSpeech() {
            isBatchAudioLoading = false;
            if (window.activeBatchAudio) {
                window.activeBatchAudio.pause();
                window.activeBatchAudio.currentTime = 0;
                window.activeBatchAudio = null;
            }
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
            }
            window.isBatchSpeaking = false;
            const btn = document.getElementById('btn-batch-voice');
            const btnText = document.getElementById('batch-voice-text');
            if (btn) {
                btn.classList.remove('speaking');
                btn.classList.remove('loading');
            }
            if (btnText) btnText.textContent = currentLang === 'bn' ? 'মাঠ রিপোর্ট শুনুন' : 'Listen Field Summary';
        }

        function toggleBatchAudioSpeech() {
            const btn = document.getElementById('btn-batch-voice');
            const btnText = document.getElementById('batch-voice-text');

            if (window.isBatchSpeaking) {
                stopBatchAudioSpeech();
                return;
            }

            if (isBatchAudioLoading) return; // Prevent rapid click race conditions

            if (!window.currentBatchData) return;

            stopAudioSpeech(); // Stop single leaf audio if running
            if (typeof stopChatAudio === 'function') stopChatAudio();

            const isBn = currentLang === 'bn';
            const speechText = isBn ? window.currentBatchData.speech_text_bn : window.currentBatchData.speech_text_en;
            if (!speechText) return;

            const gender = window.currentBatchVoiceGender || 'male';
            const langCode = isBn ? 'bn' : 'en';

            let voiceName = 'pradeep';
            if (isBn) {
                voiceName = gender === 'female' ? 'nabanita' : 'pradeep';
            } else {
                voiceName = gender === 'female' ? 'aria' : 'guy';
            }

            isBatchAudioLoading = true;
            if (btn) btn.classList.add('loading');
            if (btnText) btnText.innerHTML = `<span style="display:inline-block;animation:spin 1s linear infinite;">⏳</span> ${isBn ? 'লোড হচ্ছে...' : 'Loading...'}`;

            const audioKey = `${langCode}_${gender}`;
            let audioToPlay = null;

            if (window.batchPreloadedAudios && window.batchPreloadedAudios[audioKey]) {
                audioToPlay = window.batchPreloadedAudios[audioKey];
                audioToPlay.currentTime = 0;
            } else {
                const audioUrl = `/api/tts?lang=${langCode}&gender=${gender}&voice=${encodeURIComponent(voiceName)}&text=${encodeURIComponent(speechText)}`;
                audioToPlay = new Audio(audioUrl);
            }

            window.activeBatchAudio = audioToPlay;

            const markPlaying = () => {
                isBatchAudioLoading = false;
                window.isBatchSpeaking = true;
                if (btn) {
                    btn.classList.remove('loading');
                    btn.classList.add('speaking');
                }
                if (btnText) btnText.textContent = isBn ? '⏸️ অডিও থামান' : '⏸️ Stop Audio';
            };

            audioToPlay.onplay = markPlaying;

            audioToPlay.onended = () => {
                stopBatchAudioSpeech();
            };

            audioToPlay.onerror = (e) => {
                console.warn('Batch TTS stream error:', e);
                isBatchAudioLoading = false;
                if (!isBn && 'speechSynthesis' in window) {
                    const utterance = new SpeechSynthesisUtterance(speechText);
                    utterance.lang = 'en-US';
                    utterance.rate = 0.95;
                    utterance.onend = stopBatchAudioSpeech;
                    utterance.onerror = stopBatchAudioSpeech;
                    window.speechSynthesis.speak(utterance);
                    markPlaying();
                } else if (isBn && hasNativeBengaliSpeechSynthesisVoice()) {
                    const utterance = new SpeechSynthesisUtterance(speechText);
                    utterance.lang = 'bn-BD';
                    utterance.rate = 0.9;
                    utterance.onend = stopBatchAudioSpeech;
                    utterance.onerror = stopBatchAudioSpeech;
                    window.speechSynthesis.speak(utterance);
                    markPlaying();
                } else {
                    stopBatchAudioSpeech();
                }
            };

            audioToPlay.play().then(() => {
                markPlaying();
            }).catch(err => {
                console.warn('Batch audio play error:', err);
                isBatchAudioLoading = false;
                if (!isBn && 'speechSynthesis' in window) {
                    const utterance = new SpeechSynthesisUtterance(speechText);
                    utterance.lang = 'en-US';
                    utterance.rate = 0.95;
                    utterance.onend = stopBatchAudioSpeech;
                    utterance.onerror = stopBatchAudioSpeech;
                    window.speechSynthesis.speak(utterance);
                    markPlaying();
                } else if (isBn && hasNativeBengaliSpeechSynthesisVoice()) {
                    const utterance = new SpeechSynthesisUtterance(speechText);
                    utterance.lang = 'bn-BD';
                    utterance.rate = 0.9;
                    utterance.onend = stopBatchAudioSpeech;
                    utterance.onerror = stopBatchAudioSpeech;
                    window.speechSynthesis.speak(utterance);
                    markPlaying();
                } else {
                    stopBatchAudioSpeech();
                }
            });
        }

        /* ── 1-Click Consolidated High-Definition Field Audit PDF Download (html2canvas + jsPDF) ── */
        async function executeBatchPdfDownload() {
            if (!window.currentBatchData) {
                alert(currentLang === 'bn' ? 'অনুগ্রহ করে প্রথমে মাঠের নমুনাগুলো বিশ্লেষণ করুন।' : 'Please run batch field analysis first.');
                return;
            }

            const btn = document.getElementById('btn-batch-pdf-main');
            const originalHtml = btn ? btn.innerHTML : '';
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = `<svg class="spin-svg" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="animation: spin 1s linear infinite;"><path d="M21 12a9 9 0 1 1-6.219-8.56"/></svg> <span>${currentLang === 'bn' ? 'অডিট PDF তৈরি হচ্ছে…' : 'Generating Audit PDF…'}</span>`;
            }

            const isBn = currentLang === 'bn';
            const data = window.currentBatchData;
            const caseId = 'BATCH-' + Math.floor(100000 + Math.random() * 900000);
            const dateStr = new Date().toLocaleDateString(isBn ? 'bn-BD' : 'en-US', { year: 'numeric', month: 'long', day: 'numeric' });
            const weather = window.currentWeatherData || {};
            const adv = weather.advisory || {};
            const activeDist = isBn ? (BD_DISTRICTS_LIST.find(d => d.en === currentSelectedDistrict)?.bn || currentSelectedDistrict) : currentSelectedDistrict;

            // Create temporary high-res offscreen rendering container
            const reportDiv = document.createElement('div');
            reportDiv.id = 'batch-pdf-export-container';
            reportDiv.style.cssText = 'position:fixed;left:-9999px;top:0;width:840px;background:#FFFFFF;padding:28px 32px;box-sizing:border-box;font-family:inherit;color:#0F172A;';

            // Build prevalence rows
            let prevRowsHtml = '';
            data.disease_breakdown.forEach((item, idx) => {
                const name = isBn ? item.name_bn : item.name_en;
                const sev = isBn ? item.severity_bn : item.severity_en;
                prevRowsHtml += `
                    <tr style="border-bottom:1px solid #E2E8F0;font-size:11px;">
                        <td style="padding:6px 8px;font-weight:700;">${idx + 1}</td>
                        <td style="padding:6px 8px;font-weight:700;color:#0F291E;">${name}</td>
                        <td style="padding:6px 8px;text-align:center;"><span style="background:${item.severity_color}22;color:${item.severity_color};font-weight:800;padding:2px 6px;border-radius:4px;">${sev}</span></td>
                        <td style="padding:6px 8px;text-align:center;font-weight:700;">${item.count} ${isBn ? 'টি' : 'leaves'}</td>
                        <td style="padding:6px 8px;text-align:right;font-weight:800;color:#065F46;">${item.percentage}%</td>
                    </tr>
                `;
            });

            // Build tested samples grid
            let samplesGridHtml = '';
            data.samples.forEach(s => {
                const sName = isBn ? s.name_bn : s.name_en;
                samplesGridHtml += `
                    <div style="background:#F8FAF9;border:1px solid #E2E8F0;border-radius:6px;padding:6px;display:flex;flex-direction:column;gap:4px;">
                        <div style="display:flex;gap:4px;height:75px;">
                            <img src="${s.thumb_url}" style="width:50%;height:100%;object-fit:cover;border-radius:4px;" crossOrigin="anonymous" />
                            <img src="${s.gradcam_url || s.thumb_url}" style="width:50%;height:100%;object-fit:cover;border-radius:4px;" crossOrigin="anonymous" />
                        </div>
                        <div style="font-size:10px;font-weight:800;color:#0F291E;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">#${s.id}. ${sName}</div>
                        <div style="display:flex;justify-content:space-between;font-size:9px;color:#64748B;">
                            <span>${isBn ? 'কনফিডেন্স' : 'Conf'}: <strong style="color:#059669;">${s.confidence}%</strong></span>
                            <span>${s.filename.slice(0, 14)}</span>
                        </div>
                    </div>
                `;
            });

            reportDiv.innerHTML = `
                <!-- Certificate Header -->
                <div style="display:flex;justify-content:space-between;align-items:flex-start;border-bottom:2.5px solid #059669;padding-bottom:12px;margin-bottom:14px;">
                    <div style="display:flex;align-items:center;gap:10px;">
                        <span style="font-size:32px;line-height:1;">🌾</span>
                        <div>
                            <h1 style="font-size:22px;color:#064E3B;font-weight:900;margin:0;letter-spacing:-0.02em;">RiceGuard AI</h1>
                            <p style="font-size:11.5px;color:#047857;font-weight:700;margin:2px 0 0;">
                                ${isBn ? 'মাঠ স্বাস্থ্য ও সমন্বিত বালাইনাশক অডিট সার্টিফিকেট' : 'Field Health Audit & Integrated Agronomic Certificate'}
                            </p>
                        </div>
                    </div>
                    <div style="text-align:right;font-size:10px;color:#475569;line-height:1.45;">
                        <div><strong style="color:#0F291E;">${isBn ? 'তারিখ:' : 'Date:'}</strong> ${dateStr}</div>
                        <div><strong style="color:#0F291E;">${isBn ? 'অডিট আইডি:' : 'Audit ID:'}</strong> <span style="font-family:monospace;font-weight:800;color:#065F46;">${caseId}</span></div>
                        <div><strong style="color:#0F291E;">${isBn ? 'অঞ্চল/জেলা:' : 'Location:'}</strong> 📍 ${activeDist}</div>
                        <div style="color:#059669;font-weight:700;">ResNet-18 (GAN-Augmented CNN)</div>
                    </div>
                </div>

                <!-- Field Overview Hero Card -->
                <div style="background:linear-gradient(135deg,#064E3B,#047857);border-radius:10px;padding:14px 18px;color:#FFFFFF;margin-bottom:14px;display:flex;justify-content:space-between;align-items:center;">
                    <div style="display:flex;align-items:center;gap:14px;">
                        <div style="width:68px;height:68px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#34D399,#059669);display:flex;flex-direction:column;align-items:center;justify-content:center;border:2.5px solid rgba(255,255,255,0.6);box-shadow:0 4px 12px rgba(0,0,0,0.3);">
                            <span style="font-size:19px;font-weight:900;line-height:1;">${data.healthy_pct}%</span>
                            <span style="font-size:7px;text-transform:uppercase;letter-spacing:0.06em;font-weight:700;opacity:0.9;">${isBn ? 'সুস্থ ফসল' : 'HEALTHY'}</span>
                        </div>
                        <div>
                            <div style="font-size:10px;text-transform:uppercase;letter-spacing:0.05em;opacity:0.85;font-weight:700;">${isBn ? 'সমগ্র মাঠ নিরীক্ষা ফলাফল' : 'OVERALL FIELD DIAGNOSIS'}</div>
                            <div style="font-size:16px;font-weight:900;margin:2px 0 4px;">
                                ${isBn ? `প্রধান লক্ষণ: ${data.dominant_disease.name_bn} (${data.dominant_disease.percentage}%)` : `Dominant: ${data.dominant_disease.name_en} (${data.dominant_disease.percentage}%)`}
                            </div>
                            <span style="background:${data.field_risk.color};color:#FFFFFF;font-size:10px;font-weight:800;padding:2px 8px;border-radius:12px;border:1px solid rgba(255,255,255,0.3);">
                                ${isBn ? data.field_risk.level_bn : data.field_risk.level_en}
                            </span>
                        </div>
                    </div>
                    <div style="text-align:right;max-width:240px;font-size:9.5px;line-height:1.4;opacity:0.92;background:rgba(0,0,0,0.2);padding:8px 10px;border-radius:6px;">
                        ${isBn ? data.field_risk.desc_bn : data.field_risk.desc_en}
                    </div>
                </div>

                <!-- 2-Column Row: Live Weather & Disease Prevalence Breakdown -->
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px;">
                    <!-- Weather Widget Box -->
                    <div style="border:1px solid #CBD5E1;border-radius:8px;padding:10px 12px;background:#F8FAFC;">
                        <div style="font-size:11px;font-weight:800;color:#0F5132;margin-bottom:6px;display:flex;align-items:center;gap:4px;">
                            <span>🌦️</span> <span>${isBn ? 'মাঠের লাইভ আবহাওয়া ও স্প্রে পূর্বাভাস' : 'Live Weather & Spraying Advisory'}</span>
                        </div>
                        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:4px;text-align:center;margin-bottom:8px;">
                            <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:4px;padding:4px 2px;">
                                <div style="font-size:11px;font-weight:800;color:#0F172A;">${weather.temperature || 28}°C</div>
                                <div style="font-size:8px;color:#64748B;">${isBn ? 'তাপমাত্রা' : 'Temp'}</div>
                            </div>
                            <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:4px;padding:4px 2px;">
                                <div style="font-size:11px;font-weight:800;color:#0284C7;">${weather.humidity || 72}%</div>
                                <div style="font-size:8px;color:#64748B;">${isBn ? 'আর্দ্রতা' : 'Humidity'}</div>
                            </div>
                            <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:4px;padding:4px 2px;">
                                <div style="font-size:11px;font-weight:800;color:#DC2626;">${weather.rain_prob_max || 10}%</div>
                                <div style="font-size:8px;color:#64748B;">${isBn ? 'বৃষ্টি ঝুঁকি' : 'Rain Risk'}</div>
                            </div>
                            <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:4px;padding:4px 2px;">
                                <div style="font-size:11px;font-weight:800;color:#475569;">${weather.wind_speed || 8} km/h</div>
                                <div style="font-size:8px;color:#64748B;">${isBn ? 'বাতাস' : 'Wind'}</div>
                            </div>
                        </div>
                        <div style="background:#ECFDF5;border-left:3px solid #059669;padding:5px 8px;border-radius:4px;font-size:9.5px;color:#065F46;font-weight:700;">
                            ${isBn ? (adv.tier_bn || 'স্প্রে করার অনুকূল আবহাওয়া') : (adv.tier_en || 'Optimal Spray Conditions')}: 
                            <span style="font-weight:500;color:#334155;">${isBn ? (adv.message_bn || 'পরবর্তী ৪ ঘণ্টায় বৃষ্টির সম্ভাবনা নেই।') : (adv.message_en || 'No immediate rain threat.')}</span>
                        </div>
                    </div>

                    <!-- Disease Prevalence Table -->
                    <div style="border:1px solid #CBD5E1;border-radius:8px;padding:10px 12px;background:#FFFFFF;">
                        <div style="font-size:11px;font-weight:800;color:#0F5132;margin-bottom:6px;display:flex;align-items:center;gap:4px;">
                            <span>📊</span> <span>${isBn ? 'রোগের প্রাদুর্ভাব ও বিন্যাস' : 'Disease Prevalence Breakdown'} (${data.total_samples} ${isBn ? 'নমুনা' : 'Samples'})</span>
                        </div>
                        <table style="width:100%;border-collapse:collapse;">
                            <thead>
                                <tr style="background:#F1F5F9;font-size:9px;color:#475569;border-bottom:1px solid #CBD5E1;">
                                    <th style="padding:4px;text-align:left;">#</th>
                                    <th style="padding:4px;text-align:left;">${isBn ? 'রোগের নাম' : 'Condition'}</th>
                                    <th style="padding:4px;text-align:center;">${isBn ? 'তীব্রতা' : 'Severity'}</th>
                                    <th style="padding:4px;text-align:center;">${isBn ? 'সংখ্যা' : 'Count'}</th>
                                    <th style="padding:4px;text-align:right;">${isBn ? 'শতাংশ' : 'Share'}</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${prevRowsHtml}
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Master Integrated Prescription Section -->
                <div style="border:1.5px solid #059669;border-radius:8px;padding:12px 14px;background:#F0FDF4;margin-bottom:14px;">
                    <div style="font-size:12px;font-weight:900;color:#065F46;margin-bottom:8px;display:flex;align-items:center;gap:5px;border-bottom:1px solid #BBF7D0;padding-bottom:5px;">
                        <span>💊</span> <span>${isBn ? 'সমন্বিত বালাইনাশক ও মাঠ ব্যবস্থাপনা প্রেসক্রিপশন' : 'Master Integrated Agronomic Prescription'}</span>
                    </div>
                    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:8px;">
                        <div style="background:#FFFFFF;border-left:3.5px solid #DC2626;border-radius:5px;padding:8px 10px;box-shadow:0 1px 2px rgba(0,0,0,0.05);">
                            <div style="font-size:10px;font-weight:800;color:#B91C1C;margin-bottom:3px;text-transform:uppercase;">
                                🧪 ${isBn ? 'বালাইনাশক ও স্প্রে নির্দেশিকা' : 'Chemical Control & Tank Mix'}
                            </div>
                            <div style="font-size:10px;line-height:1.45;color:#1E293B;white-space:pre-line;">
                                ${isBn ? data.master_prescription.chemical_bn : data.master_prescription.chemical_en}
                            </div>
                        </div>
                        <div style="background:#FFFFFF;border-left:3.5px solid #16A34A;border-radius:5px;padding:8px 10px;box-shadow:0 1px 2px rgba(0,0,0,0.05);">
                            <div style="font-size:10px;font-weight:800;color:#15803D;margin-bottom:3px;text-transform:uppercase;">
                                🌱 ${isBn ? 'মাঠ পরিচর্যা ও সেচ ব্যবস্থাপনা' : 'Field Care & Drainage'}
                            </div>
                            <div style="font-size:10px;line-height:1.45;color:#1E293B;white-space:pre-line;">
                                ${isBn ? data.master_prescription.cultural_bn : data.master_prescription.cultural_en}
                            </div>
                        </div>
                    </div>
                    <div style="background:#FFFBEB;border:1px solid #FDE68A;border-left:3.5px solid #D97706;border-radius:5px;padding:6px 10px;">
                        <div style="font-size:9.5px;font-weight:800;color:#B45309;margin-bottom:2px;">
                            ⚠️ ${isBn ? 'সার প্রয়োগ ও নাইট্রোজেন সতর্কতা' : 'Fertilizer Advisory & Nitrogen Warning'}
                        </div>
                        <div style="font-size:9.5px;color:#78350F;line-height:1.4;">
                            ${isBn ? data.master_prescription.fertilizer_advisory_bn : data.master_prescription.fertilizer_advisory_en}
                        </div>
                    </div>
                </div>

                <!-- Tested Samples Gallery Table with Grad-CAM -->
                <div style="margin-bottom:12px;">
                    <div style="font-size:11px;font-weight:800;color:#0F5132;margin-bottom:6px;display:flex;align-items:center;gap:4px;">
                        <span>🔬</span> <span>${isBn ? 'পরীক্ষিত পাতার নমুনাসমূহ ও Grad-CAM দৃষ্টি (Original & Heatmap)' : 'Tested Leaf Samples & Grad-CAM Visual XAI'}</span>
                    </div>
                    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;">
                        ${samplesGridHtml}
                    </div>
                </div>

                <!-- Official Seal & Helplines Footer -->
                <div style="border-top:1.5px solid #CBD5E1;padding-top:8px;display:flex;justify-content:space-between;align-items:center;font-size:9px;color:#64748B;">
                    <div>
                        <strong>RiceGuard AI Autonomous Platform</strong> • ${isBn ? 'কারিগরি বিকাশ ও ডিজাইন:' : 'Developed by:'} <strong style="color:#059669;">Ohi</strong>
                    </div>
                    <div style="font-weight:700;color:#0F291E;">
                        📞 ${isBn ? 'জাতীয় কৃষি কল সেন্টার: ১৬১২৩ | বিআরআরআই: ০২-৪৯২৭২০০৫' : 'Krishi Hotline: 16123 | BRRI: 02-49272005'}
                    </div>
                </div>
            `;

            document.body.appendChild(reportDiv);

            try {
                if (typeof html2canvas !== 'undefined') {
                    const canvas = await html2canvas(reportDiv, {
                        scale: 2.5,
                        useCORS: true,
                        allowTaint: true,
                        backgroundColor: '#FFFFFF',
                        logging: false
                    });

                    const imgData = canvas.toDataURL('image/jpeg', 0.98);
                    const jsPDFClass = (window.jspdf && window.jspdf.jsPDF) ? window.jspdf.jsPDF : (window.jsPDF || null);

                    if (jsPDFClass) {
                        const pdf = new jsPDFClass({ orientation: 'portrait', unit: 'mm', format: 'a4', compress: true });
                        const pdfWidth = pdf.internal.pageSize.getWidth();
                        const pdfHeight = pdf.internal.pageSize.getHeight();
                        const margin = 5;
                        const printWidth = pdfWidth - (margin * 2);
                        const printHeight = (canvas.height * printWidth) / canvas.width;

                        if (printHeight <= pdfHeight - (margin * 2)) {
                            pdf.addImage(imgData, 'JPEG', margin, margin, printWidth, printHeight);
                        } else {
                            // Multi-page handling
                            let heightLeft = printHeight;
                            let position = margin;
                            pdf.addImage(imgData, 'JPEG', margin, position, printWidth, printHeight);
                            heightLeft -= (pdfHeight - (margin * 2));

                            while (heightLeft > 0) {
                                position = heightLeft - printHeight + margin;
                                pdf.addPage();
                                pdf.addImage(imgData, 'JPEG', margin, position, printWidth, printHeight);
                                heightLeft -= pdfHeight;
                            }
                        }

                        pdf.save(`RiceGuard_Field_Audit_${caseId}.pdf`);
                    } else {
                        window.print();
                    }
                } else {
                    window.print();
                }
            } catch (err) {
                console.error('Batch PDF generation error:', err);
                window.print();
            } finally {
                document.body.removeChild(reportDiv);
                if (btn) {
                    btn.disabled = false;
                    btn.innerHTML = originalHtml;
                }
            }
        }


        /* ── Feature 3: Dual-Voice (Male 👨‍🌾 / Female 👩‍⚕️) Audio Prescription Speech ── */
        window.currentVoiceGender = localStorage.getItem('riceguard_voice_gender') || 'male';
        window.currentSelectedVoice = localStorage.getItem('riceguard_voice') || 'pradeep';
        window.preloadedAudios = { male: null, female: null };

        function updateChatVoiceOptions(lang) {
            const sel = document.getElementById('chat-voice-select');
            if (!sel) return;
            const currentGender = window.currentVoiceGender || 'male';
            if (lang === 'bn') {
                sel.innerHTML = `
                    <option value="pradeep">👨‍🌾 প্রদীপ (পুরুষ)</option>
                    <option value="nabanita">👩‍⚕️ নবনীতা (নারী)</option>
                    <option value="tanishaa">👩‍💼 তানিশা (নারী)</option>
                    <option value="bashkar">👨‍💼 ভাস্কর (পুরুষ)</option>
                `;
                const targetVoice = currentGender === 'female' ? 'nabanita' : 'pradeep';
                sel.value = targetVoice;
                window.currentSelectedVoice = targetVoice;
            } else {
                sel.innerHTML = `
                    <option value="guy">👨‍🌾 Guy (Male)</option>
                    <option value="aria">👩‍⚕️ Aria (Female)</option>
                    <option value="jenny">👩‍💼 Jenny (Female)</option>
                    <option value="christopher">👨‍💼 Christopher (Male)</option>
                `;
                const targetVoice = currentGender === 'female' ? 'aria' : 'guy';
                sel.value = targetVoice;
                window.currentSelectedVoice = targetVoice;
            }
            localStorage.setItem('riceguard_voice', window.currentSelectedVoice);
        }

        function setVoiceGender(gender) {
            window.currentVoiceGender = gender;
            localStorage.setItem('riceguard_voice_gender', gender);

            // Update UI toggle buttons
            const maleBtn = document.getElementById('voice-gender-male');
            const femaleBtn = document.getElementById('voice-gender-female');
            if (maleBtn && femaleBtn) {
                if (gender === 'female') {
                    femaleBtn.classList.add('active');
                    maleBtn.classList.remove('active');
                } else {
                    maleBtn.classList.add('active');
                    femaleBtn.classList.remove('active');
                }
            }

            // Sync with global voice & chat voice selector
            const isBn = currentLang === 'bn';
            let targetVoice = 'pradeep';
            if (isBn) {
                targetVoice = (gender === 'female') ? 'nabanita' : 'pradeep';
            } else {
                targetVoice = (gender === 'female') ? 'aria' : 'guy';
            }
            window.currentSelectedVoice = targetVoice;
            localStorage.setItem('riceguard_voice', targetVoice);
            const chatVoiceSel = document.getElementById('chat-voice-select');
            if (chatVoiceSel) chatVoiceSel.value = targetVoice;

            // If audio is currently playing, switch seamlessly to the selected voice!
            if (isSpeaking) {
                stopAudioSpeech();
                toggleVoiceSpeech();
            }
        }

        function setGlobalVoice(val) {
            window.currentSelectedVoice = val;
            localStorage.setItem('riceguard_voice', val);
            const isFem = (val === 'nabanita' || val === 'tanishaa' || val === 'aria' || val === 'jenny');
            setVoiceGender(isFem ? 'female' : 'male');
        }

        function preloadPredictionAudio(diseaseName, lang) {
            if (!diseaseName) return;
            const slug = diseaseName.toLowerCase().replace(/ /g, '_');
            const langCode = (lang || currentLang || 'bn').startsWith('bn') ? 'bn' : 'en';

            try {
                const maleUrl = `/api/tts?disease=${encodeURIComponent(slug)}&lang=${langCode}&gender=male`;
                const femaleUrl = `/api/tts?disease=${encodeURIComponent(slug)}&lang=${langCode}&gender=female`;

                const mAudio = new Audio(maleUrl);
                mAudio.preload = 'auto';
                const fAudio = new Audio(femaleUrl);
                fAudio.preload = 'auto';

                window.preloadedAudios = {
                    male: mAudio,
                    female: fAudio
                };
            } catch (e) {
                console.warn('Audio preload error:', e);
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            // Restore saved gender
            const savedGender = localStorage.getItem('riceguard_voice_gender') || 'male';
            const maleBtn = document.getElementById('voice-gender-male');
            const femaleBtn = document.getElementById('voice-gender-female');
            if (maleBtn && femaleBtn) {
                if (savedGender === 'female') {
                    femaleBtn.classList.add('active');
                    maleBtn.classList.remove('active');
                } else {
                    maleBtn.classList.add('active');
                    femaleBtn.classList.remove('active');
                }
            }
            updateChatVoiceOptions(currentLang);
        });

        let activeAudio = null;
        let isSpeaking = false;
        let isSingleAudioLoading = false;

        function cleanSpeechText(text, isBn) {
            if (!text) return '';
            let cleaned = text;
            if (isBn) {
                cleaned = cleaned.replace(/\([A-Za-z\s\.,\-]+\)/g, '');
                cleaned = cleaned.replace(/WP|EC|WG|SP|pv\./gi, '');
                cleaned = cleaned.replace(/[•\-\*\/]/g, ' ');
            } else {
                cleaned = cleaned.replace(/[•\-\*\/]/g, ' ');
            }
            return cleaned.replace(/\s+/g, ' ').trim();
        }

        function stopAudioSpeech() {
            isSingleAudioLoading = false;
            if (activeAudio) {
                activeAudio.pause();
                activeAudio.currentTime = 0;
                activeAudio = null;
            }
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
            }
            isSpeaking = false;
            const btn = document.getElementById('btn-voice-read');
            const btnText = document.getElementById('voice-btn-text');
            if (btn) {
                btn.classList.remove('speaking');
                btn.classList.remove('loading');
            }
            if (btnText) btnText.textContent = currentLang === 'bn' ? 'প্রেসক্রিপশন শুনুন' : 'Listen Audio';
        }

        function toggleVoiceSpeech() {
            const btn = document.getElementById('btn-voice-read');
            const btnText = document.getElementById('voice-btn-text');

            if (isSpeaking) {
                stopAudioSpeech();
                return;
            }

            if (isSingleAudioLoading) return; // Prevent race conditions

            if (!currentDiseaseData) return;

            const isBn = currentLang === 'bn';
            const diseaseName = isBn ? (currentDiseaseData.name_bn || currentPredictionName) : (currentDiseaseData.name_en || currentPredictionName);
            const severity = isBn ? (currentDiseaseData.severity_bn || 'সতর্কতা') : (currentDiseaseData.severity_en || 'Caution');
            const rawChemRx = (isBn ? currentDiseaseData.management_bn?.chemical : currentDiseaseData.management_en?.chemical) || '';
            const chemRx = cleanSpeechText(rawChemRx, isBn);

            let speechText = '';
            if (isBn) {
                if (diseaseName.includes('সুস্থ')) {
                    speechText = `ধানের পাতায় সনাক্তকৃত অবস্থা: ${diseaseName}। ঝুঁকির মাত্রা: ${severity}। ${(currentDiseaseData.overview_bn || '')} মাঠ নির্দেশিকা: ${(currentDiseaseData.management_bn?.cultural || '')} জমিতে কোনো রাসায়নিক বা কীটনাশক স্প্রে করার প্রয়োজন নেই।`;
                } else {
                    const symp = (currentDiseaseData.symptoms_bn || []).join('। ');
                    const causes = (currentDiseaseData.causes_bn || []).join('। ');
                    const cult = currentDiseaseData.management_bn?.cultural || '';
                    speechText = `ধানের পাতায় সনাক্তকৃত রোগ: ${cleanSpeechText(diseaseName, true)}। ঝুঁকির মাত্রা: ${severity}। ${(currentDiseaseData.overview_bn || '')} রোগের প্রধান লক্ষণসমূহ: ${symp}। রোগের মূল কারণ: ${causes}। চিকিৎসা ও বালাইনাশক প্রেসক্রিপশন: ${chemRx}। জরুরি মাঠ পরিচর্যা: ${cult}`;
                }
            } else {
                if (diseaseName.toLowerCase().includes('healthy')) {
                    speechText = `Diagnosed condition: ${diseaseName}. Risk level: ${severity}. ${(currentDiseaseData.overview_en || '')} Field practice: ${(currentDiseaseData.management_en?.cultural || '')} No chemical pesticide is required.`;
                } else {
                    const symp = (currentDiseaseData.symptoms_en || []).join('. ');
                    const causes = (currentDiseaseData.causes_en || []).join('. ');
                    const cult = currentDiseaseData.management_en?.cultural || '';
                    speechText = `Diagnosed condition: ${diseaseName}. Risk level: ${severity}. ${(currentDiseaseData.overview_en || '')} Key symptoms: ${symp}. Root causes: ${causes}. Recommended prescription: ${chemRx}. Essential field management: ${cult}`;
                }
            }

            isSingleAudioLoading = true;
            if (btn) btn.classList.add('loading');
            if (btnText) btnText.innerHTML = `<span style="display:inline-block;animation:spin 1s linear infinite;">⏳</span> ${isBn ? 'লোড হচ্ছে...' : 'Loading...'}`;

            const gender = window.currentVoiceGender || 'male';
            const langCode = isBn ? 'bn' : 'en';
            const slug = (currentPredictionName || '').toLowerCase().replace(/ /g, '_');
            const audioUrl = `/api/tts?disease=${encodeURIComponent(slug)}&lang=${langCode}&gender=${gender}&text=${encodeURIComponent(speechText)}`;

            // Use preloaded audio if available for zero-latency instant play
            if (window.preloadedAudios && window.preloadedAudios[gender]) {
                activeAudio = window.preloadedAudios[gender];
                activeAudio.currentTime = 0;
            } else {
                activeAudio = new Audio(audioUrl);
            }

            const markSinglePlaying = () => {
                isSingleAudioLoading = false;
                isSpeaking = true;
                if (btn) {
                    btn.classList.remove('loading');
                    btn.classList.add('speaking');
                }
                if (btnText) btnText.textContent = isBn ? '⏸️ অডিও থামান' : '⏸️ Stop Audio';
            };

            activeAudio.onplay = markSinglePlaying;

            activeAudio.onended = () => {
                stopAudioSpeech();
            };

            activeAudio.onerror = (e) => {
                console.warn('Backend audio failed:', e);
                isSingleAudioLoading = false;
                if (!isBn && 'speechSynthesis' in window) {
                    const utterance = new SpeechSynthesisUtterance(speechText);
                    utterance.lang = 'en-US';
                    utterance.rate = 0.95;
                    utterance.onend = stopAudioSpeech;
                    utterance.onerror = stopAudioSpeech;
                    window.speechSynthesis.speak(utterance);
                    markSinglePlaying();
                } else if (isBn && typeof hasNativeBengaliSpeechSynthesisVoice === 'function' && hasNativeBengaliSpeechSynthesisVoice()) {
                    const utterance = new SpeechSynthesisUtterance(speechText);
                    utterance.lang = 'bn-BD';
                    utterance.rate = 0.9;
                    utterance.onend = stopAudioSpeech;
                    utterance.onerror = stopAudioSpeech;
                    window.speechSynthesis.speak(utterance);
                    markSinglePlaying();
                } else {
                    stopAudioSpeech();
                }
            };

            activeAudio.play().then(() => {
                markSinglePlaying();
            }).catch(err => {
                console.warn('Audio play error:', err);
                isSingleAudioLoading = false;
                if (!isBn && 'speechSynthesis' in window) {
                    const utterance = new SpeechSynthesisUtterance(speechText);
                    utterance.lang = 'en-US';
                    utterance.rate = 0.95;
                    utterance.onend = stopAudioSpeech;
                    utterance.onerror = stopAudioSpeech;
                    window.speechSynthesis.speak(utterance);
                    markSinglePlaying();
                } else if (isBn && typeof hasNativeBengaliSpeechSynthesisVoice === 'function' && hasNativeBengaliSpeechSynthesisVoice()) {
                    const utterance = new SpeechSynthesisUtterance(speechText);
                    utterance.lang = 'bn-BD';
                    utterance.rate = 0.9;
                    utterance.onend = stopAudioSpeech;
                    utterance.onerror = stopAudioSpeech;
                    window.speechSynthesis.speak(utterance);
                    markSinglePlaying();
                } else {
                    stopAudioSpeech();
                }
            });
        }

        /* Helper to format bytes */
        function formatBytes(bytes) {
            if (bytes === 0) return '0 Bytes';
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
        }

        /* ── Load Quick Sample ── */
        function loadSample(url, filename) {
            fetch(url)
            .then(res => res.blob())
            .then(blob => {
                const file = new File([blob], filename, { type: 'image/jpeg' });
                rawOriginalFile = file;

                try {
                    const container = new DataTransfer();
                    container.items.add(file);
                    const fileInput = document.getElementById('image-input');
                    if (fileInput) fileInput.files = container.files;
                } catch (e) {
                    console.warn('DataTransfer fallback');
                }

                if (typeof handleFile === 'function') {
                    handleFile(file, true);
                }
            })
            .catch(err => {
                console.error('Failed to load sample', err);
            });
        }

        let handleFile = null;

        /* ── Feature 3: WebRTC Live Camera Capture Engine ── */
        let cameraStream = null;
        let facingMode = 'environment';

        async function startCamera() {
            const modalCamera = document.getElementById('modal-camera');
            const video = document.getElementById('camera-video');

            try {
                if (cameraStream) {
                    cameraStream.getTracks().forEach(track => track.stop());
                }
                cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { facingMode: facingMode, width: { ideal: 1280 }, height: { ideal: 720 } }
                });
                video.srcObject = cameraStream;
                modalCamera.classList.add('active');
            } catch (err) {
                console.warn('Camera access error:', err);
                alert(currentLang === 'bn' ? 'ক্যামেরা চালু করা যায়নি। অনুগ্রহ করে ব্রাউজার থেকে ক্যামেরার অনুমতি দিন।' : 'Could not access camera. Please allow camera permissions in your browser.');
            }
        }

        function stopCamera() {
            const modalCamera = document.getElementById('modal-camera');
            if (cameraStream) {
                cameraStream.getTracks().forEach(track => track.stop());
                cameraStream = null;
            }
            modalCamera.classList.remove('active');
        }

        function captureFromCamera() {
            const video = document.getElementById('camera-video');
            if (!video || !video.videoWidth) return;

            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

            canvas.toBlob((blob) => {
                const file = new File([blob], `Camera_Capture_${Date.now()}.jpg`, { type: 'image/jpeg' });
                rawOriginalFile = file;

                try {
                    const container = new DataTransfer();
                    container.items.add(file);
                    const fileInput = document.getElementById('image-input');
                    if (fileInput) fileInput.files = container.files;
                } catch (e) {}

                stopCamera();
                if (typeof handleFile === 'function') {
                    handleFile(file, true);
                }
            }, 'image/jpeg', 0.92);
        }

        function switchCamera() {
            facingMode = (facingMode === 'environment') ? 'user' : 'environment';
            startCamera();
        }

        /* ── Feature 3: Image Enhancement, Rotation & Sharpening Engine ── */
        function applyImageAutoEnhance() {
            const previewImg = document.getElementById('preview-img');
            if (!previewImg || !previewImg.src || previewImg.src.startsWith('data:image/svg')) return;

            const img = new Image();
            img.crossOrigin = 'anonymous';
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.naturalWidth || img.width;
                canvas.height = img.naturalHeight || img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);

                const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                const d = imgData.data;

                // Simple auto-level stretching + contrast boost
                const contrast = 1.20; // +20% contrast
                const brightness = 6;  // +6 brightness
                for (let i = 0; i < d.length; i += 4) {
                    d[i]   = Math.min(255, Math.max(0, (d[i] - 128) * contrast + 128 + brightness));
                    d[i+1] = Math.min(255, Math.max(0, (d[i+1] - 128) * contrast + 128 + brightness));
                    d[i+2] = Math.min(255, Math.max(0, (d[i+2] - 128) * contrast + 128 + brightness));
                }
                ctx.putImageData(imgData, 0, 0);

                canvas.toBlob((blob) => {
                    const newUrl = URL.createObjectURL(blob);
                    originalImageSrc = newUrl;
                    previewImg.src = newUrl;
                    document.getElementById('modal-img').src = newUrl;
                    updateFileInputWithBlob(blob, 'enhanced_leaf.jpg');
                    document.getElementById('btn-reset-filters').style.display = 'inline-flex';
                }, 'image/jpeg', 0.95);
            };
            img.src = previewImg.src;
        }

        function rotateImage90() {
            const previewImg = document.getElementById('preview-img');
            if (!previewImg || !previewImg.src) return;

            const img = new Image();
            img.crossOrigin = 'anonymous';
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.naturalHeight || img.height;
                canvas.height = img.naturalWidth || img.width;
                const ctx = canvas.getContext('2d');

                ctx.translate(canvas.width / 2, canvas.height / 2);
                ctx.rotate(Math.PI / 2);
                ctx.drawImage(img, -img.width / 2, -img.height / 2);

                canvas.toBlob((blob) => {
                    const newUrl = URL.createObjectURL(blob);
                    originalImageSrc = newUrl;
                    previewImg.src = newUrl;
                    document.getElementById('modal-img').src = newUrl;
                    updateFileInputWithBlob(blob, 'rotated_leaf.jpg');
                    document.getElementById('btn-reset-filters').style.display = 'inline-flex';
                }, 'image/jpeg', 0.95);
            };
            img.src = previewImg.src;
        }

        function applyImageSharpen() {
            const previewImg = document.getElementById('preview-img');
            if (!previewImg || !previewImg.src) return;

            const img = new Image();
            img.crossOrigin = 'anonymous';
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.naturalWidth || img.width;
                canvas.height = img.naturalHeight || img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);

                const srcData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                const dstData = ctx.createImageData(canvas.width, canvas.height);
                const src = srcData.data;
                const dst = dstData.data;
                const w = canvas.width;
                const h = canvas.height;

                // Sharpen convolution kernel [0, -0.6, 0, -0.6, 3.4, -0.6, 0, -0.6, 0]
                for (let y = 1; y < h - 1; y++) {
                    for (let x = 1; x < w - 1; x++) {
                        const idx = (y * w + x) * 4;
                        for (let c = 0; c < 3; c++) {
                            const val = 3.4 * src[idx + c]
                                      - 0.6 * src[((y - 1) * w + x) * 4 + c]
                                      - 0.6 * src[((y + 1) * w + x) * 4 + c]
                                      - 0.6 * src[(y * w + (x - 1)) * 4 + c]
                                      - 0.6 * src[(y * w + (x + 1)) * 4 + c];
                            dst[idx + c] = Math.min(255, Math.max(0, val));
                        }
                        dst[idx + 3] = src[idx + 3];
                    }
                }
                ctx.putImageData(dstData, 0, 0);

                canvas.toBlob((blob) => {
                    const newUrl = URL.createObjectURL(blob);
                    originalImageSrc = newUrl;
                    previewImg.src = newUrl;
                    document.getElementById('modal-img').src = newUrl;
                    updateFileInputWithBlob(blob, 'sharpened_leaf.jpg');
                    document.getElementById('btn-reset-filters').style.display = 'inline-flex';
                }, 'image/jpeg', 0.95);
            };
            img.src = previewImg.src;
        }

        function resetImageFilters() {
            if (rawOriginalDataUrl) {
                originalImageSrc = rawOriginalDataUrl;
                document.getElementById('preview-img').src = rawOriginalDataUrl;
                document.getElementById('modal-img').src = rawOriginalDataUrl;
                if (rawOriginalFile) {
                    const container = new DataTransfer();
                    container.items.add(rawOriginalFile);
                    document.getElementById('image-input').files = container.files;
                }
            }
            document.getElementById('btn-reset-filters').style.display = 'none';
        }

        function updateFileInputWithBlob(blob, filename) {
            const file = new File([blob], filename, { type: 'image/jpeg' });
            const container = new DataTransfer();
            container.items.add(file);
            document.getElementById('image-input').files = container.files;
        }

        /* ── Feature 1: Floating AI Agri-Assistant Chatbot Logic ── */
        let isChatOpen = false;

        function toggleAgriChat() {
            const chatBox = document.getElementById('chat-window-box');
            const widgetContainer = document.getElementById('chat-widget-container');
            if (!chatBox) return;
            isChatOpen = !isChatOpen;
            chatBox.classList.toggle('active', isChatOpen);
            if (widgetContainer) {
                widgetContainer.classList.toggle('chat-open', isChatOpen);
            }
            if (isChatOpen) {
                setTimeout(() => {
                    const input = document.getElementById('chat-input');
                    if (input) input.focus();
                }, 150);
            } else {
                stopChatAudio();
                stopChatVoiceInput();
            }
        }

        function clearChatHistory() {
            stopChatAudio();
            stopChatVoiceInput();
            const chatMsgs = document.getElementById('chat-messages');
            if (!chatMsgs) return;
            const dict = I18N[currentLang] || I18N.bn;
            chatMsgs.innerHTML = `
                <div class="chat-welcome-card" id="chat-welcome-card">
                    <div class="welcome-header">
                        <span>✨</span>
                        <span>${dict.chat_welcome_title}</span>
                    </div>
                    <p class="welcome-desc">${dict.chat_welcome_desc}</p>
                    <div class="welcome-topics-grid">
                        <button type="button" class="welcome-topic-btn" onclick="sendQuickPrompt('${currentLang === 'bn' ? 'ব্লাস্ট রোগের দ্রুত প্রতিকার কী?' : 'Quick remedy for Rice Blast?'}')">
                            <span class="welcome-topic-title">${currentLang === 'bn' ? '🌾 ব্লাস্ট রোগ দমন' : '🌾 Blast Disease Control'}</span>
                            <span class="welcome-topic-sub">${currentLang === 'bn' ? 'লক্ষণ ও ওষুধ স্প্রে' : 'Symptoms & Spray Rx'}</span>
                        </button>
                        <button type="button" class="welcome-topic-btn" onclick="sendQuickPrompt('${currentLang === 'bn' ? 'ইউরিয়া সার কখন দেওয়া উচিত নয়?' : 'When to avoid Urea fertilizer?'}')">
                            <span class="welcome-topic-title">${currentLang === 'bn' ? '🧪 ইউরিয়া সারের নিয়ম' : '🧪 Urea Fertilizer Rules'}</span>
                            <span class="welcome-topic-sub">${currentLang === 'bn' ? 'প্রয়োগ সতর্কতা' : 'Application Warnings'}</span>
                        </button>
                        <button type="button" class="welcome-topic-btn" onclick="sendQuickPrompt('${currentLang === 'bn' ? 'পামরী পোকা দমনের ঘরোয়া উপায় কী?' : 'How to manage Rice Hispa?'}')">
                            <span class="welcome-topic-title">${currentLang === 'bn' ? '🐛 পামরী পোকা দমন' : '🐛 Rice Hispa Control'}</span>
                            <span class="welcome-topic-sub">${currentLang === 'bn' ? 'পার্চিং ও রাসায়নিক' : 'Perching & Chemicals'}</span>
                        </button>
                        <button type="button" class="welcome-topic-btn" onclick="sendQuickPrompt('${currentLang === 'bn' ? 'স্প্রে করার সঠিক আবহাওয়া ও সময় কী?' : 'Best time and weather for spraying?'}')">
                            <span class="welcome-topic-title">${currentLang === 'bn' ? '🌦️ স্প্রে সতর্কতা' : '🌦️ Spray Weather Alert'}</span>
                            <span class="welcome-topic-sub">${currentLang === 'bn' ? 'আবহাওয়া ও সময়' : 'Wind & Rain Rules'}</span>
                        </button>
                    </div>
                </div>
            `;
        }

        function sendQuickPrompt(text) {
            const input = document.getElementById('chat-input');
            if (input) {
                input.value = text;
                handleChatSubmit(new Event('submit'));
            }
        }

        function getChatTimeString() {
            const now = new Date();
            let hours = now.getHours();
            let minutes = now.getMinutes();
            const ampm = hours >= 12 ? 'PM' : 'AM';
            hours = hours % 12;
            hours = hours ? hours : 12;
            const minStr = minutes < 10 ? '0' + minutes : minutes;
            const timeRaw = `${hours}:${minStr} ${ampm}`;
            if (currentLang === 'bn') {
                const bnNums = {'0':'০','1':'১','2':'২','3':'৩','4':'৪','5':'৫','6':'৬','7':'৭','8':'৮','9':'৯'};
                return timeRaw.replace(/[0-9]/g, w => bnNums[w] || w);
            }
            return timeRaw;
        }

        function escapeJsString(str) {
            return (str || '')
                .replace(/\\/g, '\\\\')
                .replace(/`/g, '\\`')
                .replace(/\$/g, '\\$')
                .replace(/"/g, '&quot;')
                .replace(/\n/g, ' ');
        }

        let activeChatAudio = null;
        let activeChatBtn = null;

        function stopChatAudio() {
            if (activeChatAudio) {
                activeChatAudio.pause();
                activeChatAudio.currentTime = 0;
                activeChatAudio = null;
            }
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
            }
            if (activeChatBtn) {
                activeChatBtn.classList.remove('playing');
                const orig = activeChatBtn.getAttribute('data-orig-text');
                if (orig) activeChatBtn.innerHTML = orig;
                activeChatBtn = null;
            }
        }

        function speakChatAudio(btn, lang, text) {
            if (activeChatBtn === btn) {
                stopChatAudio();
                return;
            }

            stopChatAudio();
            if (typeof stopAudioSpeech === 'function') stopAudioSpeech();
            if (typeof stopBatchAudioSpeech === 'function') stopBatchAudioSpeech();

            activeChatBtn = btn;
            const origHtml = btn.innerHTML;
            btn.setAttribute('data-orig-text', origHtml);
            btn.classList.add('playing');
            btn.innerHTML = `<span style="display:inline-block;animation:spin 1s linear infinite;">⏳</span> ${lang === 'bn' ? 'লোড হচ্ছে...' : 'Loading...'}`;

            // Clean text for speech
            const cleanText = text.replace(/<[^>]+>/g, ' ').replace(/[\*\_#\`\~>\|\[\]\(\)]/g, ' ').replace(/\s+/g, ' ').trim();

            const currentVoice = window.currentSelectedVoice || (lang === 'bn' ? 'pradeep' : 'guy');
            const audioUrl = '/api/tts?lang=' + encodeURIComponent(lang) + '&text=' + encodeURIComponent(cleanText) + '&voice=' + encodeURIComponent(currentVoice);
            activeChatAudio = new Audio(audioUrl);

            const markChatPlaying = () => {
                if (btn) btn.innerHTML = `⏸️ ${lang === 'bn' ? 'থামুন' : 'Stop'}`;
            };

            activeChatAudio.onplay = markChatPlaying;

            activeChatAudio.onended = () => {
                stopChatAudio();
            };

            activeChatAudio.onerror = (e) => {
                console.warn('Chat TTS audio stream error:', e);
                const isBn = lang === 'bn';
                if (!isBn && 'speechSynthesis' in window) {
                    const utterance = new SpeechSynthesisUtterance(cleanText);
                    utterance.lang = 'en-US';
                    utterance.rate = 0.95;
                    utterance.onend = stopChatAudio;
                    utterance.onerror = stopChatAudio;
                    window.speechSynthesis.speak(utterance);
                    markChatPlaying();
                } else if (isBn && typeof hasNativeBengaliSpeechSynthesisVoice === 'function' && hasNativeBengaliSpeechSynthesisVoice()) {
                    const utterance = new SpeechSynthesisUtterance(cleanText);
                    utterance.lang = 'bn-BD';
                    utterance.rate = 0.9;
                    utterance.onend = stopChatAudio;
                    utterance.onerror = stopChatAudio;
                    window.speechSynthesis.speak(utterance);
                    markChatPlaying();
                } else {
                    stopChatAudio();
                }
            };

            activeChatAudio.play().then(() => {
                markChatPlaying();
            }).catch(err => {
                console.warn('Chat audio play error:', err);
                const isBn = lang === 'bn';
                if (!isBn && 'speechSynthesis' in window) {
                    const utterance = new SpeechSynthesisUtterance(cleanText);
                    utterance.lang = 'en-US';
                    utterance.rate = 0.95;
                    utterance.onend = stopChatAudio;
                    utterance.onerror = stopChatAudio;
                    window.speechSynthesis.speak(utterance);
                    markChatPlaying();
                } else if (isBn && typeof hasNativeBengaliSpeechSynthesisVoice === 'function' && hasNativeBengaliSpeechSynthesisVoice()) {
                    const utterance = new SpeechSynthesisUtterance(cleanText);
                    utterance.lang = 'bn-BD';
                    utterance.rate = 0.9;
                    utterance.onend = stopChatAudio;
                    utterance.onerror = stopChatAudio;
                    window.speechSynthesis.speak(utterance);
                    markChatPlaying();
                } else {
                    stopChatAudio();
                }
            });
        }

        /* ── Bangla & English Voice Input (Web Speech Recognition API) ── */
        let chatRecognition = null;
        let isChatListening = false;
        let speechSilenceTimer = null;

        function normalizeBengaliVoiceText(text) {
            if (!text) return '';
            let t = text.trim();
            // Phonetic auto-corrections for common agricultural speech
            t = t.replace(/ব্লাষ্ট/g, 'ব্লাস্ট')
                 .replace(/পোড়া/g, 'পোড়া')
                 .replace(/মাজড়া/g, 'মাজরা')
                 .replace(/পামরি/g, 'পামরী')
                 .replace(/কারেন পোকা/g, 'কারেন্ট পোকা')
                 .replace(/ইউরিয়া/g, 'ইউরিয়া')
                 .replace(/পটাষ/g, 'পটাশ')
                 .replace(/কীট নাশক/g, 'কীটনাশক');
            return t;
        }

        function toggleChatVoiceInput() {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRecognition) {
                alert(currentLang === 'bn'
                    ? '🎙️ আপনার ব্রাউজারে সরাসরি ভয়েস রিকগনিশন সুবিধা পাওয়া যায়নি। অনুগ্রহ করে Google Chrome বা আধুনিক ব্রাউজারে চেষ্টা করুন।'
                    : '🎙️ Speech recognition is not supported in this browser. Please use Google Chrome or a modern browser.');
                return;
            }

            const micBtn = document.getElementById('btn-chat-mic');
            const chatInput = document.getElementById('chat-input');

            if (isChatListening) {
                stopChatVoiceInput(true);
                return;
            }

            try {
                if (chatRecognition) {
                    try { chatRecognition.abort(); } catch(e) {}
                }

                chatRecognition = new SpeechRecognition();
                chatRecognition.lang = (currentLang === 'bn') ? 'bn-BD' : 'en-US';
                chatRecognition.continuous = false; // Single-phrase mode to prevent word repetition on mobile
                chatRecognition.interimResults = true;
                chatRecognition.maxAlternatives = 1;

                chatRecognition.onstart = function() {
                    isChatListening = true;
                    if (micBtn) {
                        micBtn.classList.add('listening');
                        micBtn.title = currentLang === 'bn' ? 'শুনছি... মুখে বলুন (থামতে চাপুন)' : 'Listening... Speak now (Click to stop)';
                    }
                    if (chatInput) {
                        chatInput.classList.add('mic-active');
                        chatInput.placeholder = currentLang === 'bn' ? '🎙️ শুনছি... মুখে বাংলায় স্পষ্ট করে বলুন...' : '🎙️ Listening... Speak clearly in English...';
                        chatInput.focus();
                    }
                };

                chatRecognition.onresult = function(event) {
                    let transcript = '';
                    for (let i = 0; i < event.results.length; ++i) {
                        transcript += event.results[i][0].transcript;
                    }
                    transcript = transcript.trim();
                    if (chatInput && transcript) {
                        chatInput.value = transcript;
                    }

                    // Reset silence auto-submit timer (1.2s silence auto-submits)
                    if (speechSilenceTimer) clearTimeout(speechSilenceTimer);
                    speechSilenceTimer = setTimeout(() => {
                        if (isChatListening && chatInput && chatInput.value.trim().length >= 2) {
                            stopChatVoiceInput(true);
                        }
                    }, 1200);
                };

                chatRecognition.onerror = function(event) {
                    console.warn('Speech recognition status:', event.error);
                    if (event.error !== 'no-speech') {
                        stopChatVoiceInput(false);
                    }
                };

                chatRecognition.onend = function() {
                    if (isChatListening) {
                        stopChatVoiceInput(true);
                    }
                };

                chatRecognition.start();
            } catch (err) {
                console.error('Failed to start speech recognition:', err);
                stopChatVoiceInput(false);
            }
        }

        function stopChatVoiceInput(shouldSubmit = false) {
            if (speechSilenceTimer) {
                clearTimeout(speechSilenceTimer);
                speechSilenceTimer = null;
            }
            if (chatRecognition) {
                try { chatRecognition.stop(); } catch(e) {}
            }
            isChatListening = false;
            const micBtn = document.getElementById('btn-chat-mic');
            const chatInput = document.getElementById('chat-input');
            if (micBtn) {
                micBtn.classList.remove('listening');
                micBtn.title = currentLang === 'bn' ? 'ভয়েসে বাংলায় বলুন' : 'Voice input in English';
            }
            if (chatInput) {
                chatInput.classList.remove('mic-active');
                chatInput.placeholder = currentLang === 'bn' ? 'ধানের রোগ বা চাষ নিয়ে প্রশ্ন লিখুন...' : 'Ask about rice diseases, fertilizers, or care...';
            }

            if (shouldSubmit && chatInput) {
                const captured = normalizeBengaliVoiceText(chatInput.value.trim());
                if (captured.length >= 2) {
                    chatInput.value = captured;
                    handleChatSubmit({ preventDefault: () => {} });
                }
            }
        }

                window._chatSpeechStore = window._chatSpeechStore || {};

        function speakStoredChatAudio(btn, msgId, lang) {
            const store = window._chatSpeechStore || {};
            const item = store[msgId] || {};
            const text = (lang === 'bn') ? item.bn : item.en;
            if (typeof speakChatAudio === 'function') {
                speakChatAudio(btn, lang, text || '');
            }
        }

        async function handleChatSubmit(e) {
            if (e && e.preventDefault) e.preventDefault();
            const input = document.getElementById('chat-input');
            if (!input || !input.value.trim()) return;

            const userText = input.value.trim();
            input.value = '';

            const chatMsgs = document.getElementById('chat-messages');
            if (!chatMsgs) return;

            const timeStr = getChatTimeString();

            // Append user message bubble with wrap & time
            const userDiv = document.createElement('div');
            userDiv.className = 'chat-msg user';
            userDiv.innerHTML = `
                <div class="msg-bubble-wrap">
                    <div class="msg-bubble">${escapeHtml(userText)}</div>
                    <div class="msg-time">${timeStr}</div>
                </div>
            `;
            chatMsgs.appendChild(userDiv);
            chatMsgs.scrollTop = chatMsgs.scrollHeight;

            // Show typing indicator
            const typingDiv = document.createElement('div');
            typingDiv.className = 'chat-msg bot typing-temp';
            typingDiv.innerHTML = `
                <div class="msg-avatar">🌾</div>
                <div class="typing-indicator">
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                </div>
            `;
            chatMsgs.appendChild(typingDiv);
            chatMsgs.scrollTop = chatMsgs.scrollHeight;

            let botRes = null;
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify({
                        message: userText,
                        lang: currentLang,
                        current_disease: currentPredictionName || null,
                        current_confidence: currentConfidence || null
                    })
                });
                if (response.ok) {
                    const resJson = await response.json();
                    if (resJson && resJson.success) {
                        botRes = {
                            html: resJson.html,
                            text_bn: resJson.text_bn,
                            text_en: resJson.text_en
                        };
                    }
                }
            } catch (err) {
                console.warn('Backend /api/chat error, falling back to local engine:', err);
            }

            // Fallback if backend failed or offline
            if (!botRes) {
                botRes = getAgriBotResponse(userText);
            }

            const tempTyping = chatMsgs.querySelector('.typing-temp');
            if (tempTyping) tempTyping.remove();

            const botMsgId = 'msg_' + Date.now() + '_' + Math.floor(Math.random() * 10000);
            window._chatSpeechStore = window._chatSpeechStore || {};
            window._chatSpeechStore[botMsgId] = {
                bn: (botRes && botRes.text_bn) ? botRes.text_bn : '',
                en: (botRes && botRes.text_en) ? botRes.text_en : ''
            };

            const botTime = getChatTimeString();
            const botDiv = document.createElement('div');
            botDiv.className = 'chat-msg bot';

            botDiv.innerHTML = `
                <div class="msg-avatar">🌾</div>
                <div class="msg-bubble-wrap">
                    <div class="msg-bubble">
                        ${(botRes && botRes.html) ? botRes.html : '<p>উত্তর পাওয়া যায়নি।</p>'}
                        <div class="chat-voice-actions">
                            <button type="button" class="msg-listen-btn bn-btn" onclick="speakStoredChatAudio(this, '${botMsgId}', 'bn')">🔊 বাংলায় শুনুন</button>
                            <button type="button" class="msg-listen-btn en-btn" onclick="speakStoredChatAudio(this, '${botMsgId}', 'en')">🌐 Listen English</button>
                        </div>
                    </div>
                    <div class="msg-time">${botTime}</div>
                </div>
            `;
            chatMsgs.appendChild(botDiv);
            chatMsgs.scrollTop = chatMsgs.scrollHeight;

            // Background pre-warm audio for 0ms instant playback on click
            try {
                const curV = window.currentSelectedVoice || 'pradeep';
                if (botRes.text_bn) {
                    const cleanBn = botRes.text_bn.replace(/<[^>]+>/g, ' ').replace(/[\*\_#\`\~>\|\[\]\(\)]/g, ' ').replace(/\s+/g, ' ').trim();
                    fetch('/api/tts?lang=bn&text=' + encodeURIComponent(cleanBn) + '&voice=' + encodeURIComponent(curV)).catch(()=>{});
                }
            } catch (e) {}
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        function getAgriBotResponse(query) {
            const isBn = currentLang === 'bn';
            const q = query.toLowerCase().trim();

            // 1. Contextual match: if disease is currently diagnosed
            if (currentDiseaseData && (q.includes('বর্তমান') || q.includes('এই রোগ') || q.includes('প্রেসক্রিপশন') || q.includes('current') || q.includes('this disease') || q.includes('rx'))) {
                const dNameBn = currentDiseaseData.name_bn || currentPredictionName;
                const dNameEn = currentDiseaseData.name_en || currentPredictionName;
                const chemBn = currentDiseaseData.management_bn?.chemical || 'প্রয়োজন নেই';
                const chemEn = currentDiseaseData.management_en?.chemical || 'None required';
                const cultBn = currentDiseaseData.management_bn?.cultural || 'সুষম সেচ বজায় রাখুন।';
                const cultEn = currentDiseaseData.management_en?.cultural || 'Maintain proper irrigation.';

                const html = isBn 
                    ? `🌿 <strong>${dNameBn}</strong>-এর জন্য প্রস্তাবিত চিকিৎসা:<br/><br/>💊 <strong>বালাইনাশক:</strong> ${chemBn}<br/><br/>🌱 <strong>মাঠ পরিচর্যা:</strong> ${cultBn}<br/><br/>💡 <em>ডোজ ক্যালকুলেটর ব্যবহার করে আপনার জমির মাপ অনুযায়ী পানির পরিমাণ বের করে নিন।</em>`
                    : `🌿 Recommended management for <strong>${dNameEn}</strong>:<br/><br/>💊 <strong>Chemical Rx:</strong> ${chemEn}<br/><br/>🌱 <strong>Cultural Practice:</strong> ${cultEn}<br/><br/>💡 <em>Use the Dosage Calculator above to determine exact water & chemical mix for your plot.</em>`;

                return {
                    html: html,
                    text_bn: `ধানের পাতায় সনাক্তকৃত রোগ হলো ${dNameBn}। প্রস্তাবিত বালাইনাশক চিকিৎসা: ${chemBn}। মাঠ পরিচর্যা: ${cultBn}`,
                    text_en: `Diagnosed condition is ${dNameEn}. Recommended chemical treatment: ${chemEn}. Cultural practice: ${cultEn}`
                };
            }

            // 2. Blast Disease (পাতা ব্লাস্ট / শীষ ব্লাস্ট)
            if (q.includes('ব্লাস্ট') || q.includes('blast')) {
                const html = isBn 
                    ? `🌾 <strong>ধানের ব্লাস্ট রোগ (Pyricularia oryzae):</strong><br/><br/>• <strong>লক্ষণ:</strong> পাতায় চোখের মতো বা ডিম্বাকৃতি দাগ, যার কেন্দ্র ছাই রঙের এবং কিনারা বাদামী।<br/>• <strong>প্রতিকার:</strong> ট্রাইসাইক্লাজল (যেমন: ট্রপার ৭৫ ডব্লিউপি - ০.৭৫ গ্রাম/লিটার) অথবা ট্রাইফ্লক্সিস্ট্রবিন + টেবুকোনাজল (যেমন: নেটিভো - ০.৬ গ্রাম/লিটার) বিকেলে স্প্রে করুন।<br/>• <strong>সতর্কতা:</strong> জমিতে ইউরিয়া সার প্রয়োগ সাময়িক বন্ধ রাখুন এবং পটাশ সার ব্যবহার করুন।`
                    : `🌾 <strong>Rice Leaf Blast (Pyricularia oryzae):</strong><br/><br/>• <strong>Symptoms:</strong> Spindle-shaped/eye-like lesions with grey centers and brown borders.<br/>• <strong>Control:</strong> Spray Tricyclazole 75 WP (0.75 g/L) or Trifloxystrobin + Tebuconazole (Nativo @ 0.6 g/L) in late afternoon.<br/>• <strong>Advisory:</strong> Suspend top-dressing Nitrogen/Urea and maintain standing water in the plot.`;

                return {
                    html: html,
                    text_bn: `ধানের ব্লাস্ট রোগ একটি মারাত্মক ছত্রাকজনিত রোগ। পাতায় চোখের মতো ডিম্বাকৃতি দাগ দেখা যায়। প্রতিকারে ট্রাইসাইক্লাজল বা নেটিভো বিকেলে স্প্রে করুন এবং ইউরিয়া সার দেওয়া বন্ধ রাখুন।`,
                    text_en: `Rice Leaf Blast causes eye-shaped lesions. Spray Tricyclazole or Nativo in late afternoon and stop top-dressing Urea fertilizer.`
                };
            }

            // 3. Bacterial Leaf Blight (ব্যাকটেরিয়াল পাতা পোড়া)
            if (q.includes('পাতা পোড়া') || q.includes('পোড়া') || q.includes('blight') || q.includes('ব্যাকটেরিয়া')) {
                const html = isBn
                    ? `🍂 <strong>ব্যাকটেরিয়াল পাতা পোড়া (Xanthomonas oryzae):</strong><br/><br/>• <strong>লক্ষণ:</strong> পাতার ডগা থেকে নিচের দিকে ঢেউ খেলানো হলুদ বা ধূসর হয়ে শুকিয়ে যাওয়া।<br/>• <strong>প্রতিকার:</strong> কপার অক্সিক্লোরাইড (২ গ্রাম/লিটার) অথবা থিওভিট স্প্রে করুন। প্রতি বিঘায় ৫ কেজি অতিরিক্ত পটাশ সার দিন।<br/>• <strong>পরিচর্যা:</strong> আক্রান্ত জমির পানি অন্য জমিতে প্রবাহিত হতে দেবেন না।`
                    : `🍂 <strong>Bacterial Leaf Blight (Xanthomonas oryzae):</strong><br/><br/>• <strong>Symptoms:</strong> Water-soaked wavy lesions starting from leaf tips turning yellow-grey.<br/>• <strong>Control:</strong> Apply Copper Oxychloride (2 g/L) or Streptocycline. Apply supplemental Potash (MOP) 5 kg/bigha.<br/>• <strong>Field Care:</strong> Prevent irrigation drainage from infected plots to healthy ones.`;

                return {
                    html: html,
                    text_bn: `ব্যাকটেরিয়াল পাতা পোড়া রোগে পাতার ডগা থেকে নিচের দিকে শুকিয়ে যায়। প্রতিকারে কপার অক্সিক্লোরাইড স্প্রে করুন এবং বিঘা প্রতি ৫ কেজি পটাশ সার দিন।`,
                    text_en: `Bacterial Leaf Blight causes yellow drying from leaf tips. Spray Copper Oxychloride and apply supplemental Potash fertilizer.`
                };
            }

            // 4. Brown Spot (বাদামী দাগ)
            if (q.includes('বাদামী দাগ') || q.includes('brown spot')) {
                const html = isBn
                    ? `🟤 <strong>বাদামী দাগ রোগ (Bipolaris oryzae):</strong><br/><br/>• <strong>লক্ষণ:</strong> পাতায় তিলের দানার মতো অসংখ্য গোল বা ডিম্বাকৃতি বাদামী দাগ।<br/>• <strong>কারণ:</strong> মাটিতে পুষ্টিহীনতা (বিশেষ করে পটাশ ও সিলিকন ঘাটতি)।<br/>• <strong>প্রতিকার:</strong> ম্যানকোজেব (ডাইথেন এম-৪৫ @ ২ গ্রাম/লিটার) বা কার্বেনডাজিম (১ গ্রাম/লিটার) স্প্রে করুন এবং সুষম সার প্রয়োগ করুন।`
                    : `🟤 <strong>Brown Spot (Bipolaris oryzae):</strong><br/><br/>• <strong>Symptoms:</strong> Small circular to oval sesame-seed shaped brown lesions.<br/>• <strong>Cause:</strong> Poor soil nutrition, potassium or zinc deficiency.<br/>• <strong>Control:</strong> Spray Mancozeb 75 WP (2 g/L) or Carbendazim (1 g/L) and apply balanced NPK nutrients.`;

                return {
                    html: html,
                    text_bn: `বাদামী দাগ রোগে পাতায় তিলের মতো বাদামী দাগ পড়ে। মাটিতে পুষ্টি ও পটাশ ঘাটতি এর মূল কারণ। প্রতিকারে ডাইথেন এম-৪৫ বা কার্বেনডাজিম স্প্রে করুন।`,
                    text_en: `Brown Spot causes sesame-seed like lesions due to nutrient deficiency. Spray Mancozeb or Carbendazim and provide balanced fertilizers.`
                };
            }

            // 5. Sheath Blight (খোল পোড়া)
            if (q.includes('খোল পোড়া') || q.includes('sheath')) {
                const html = isBn
                    ? `🌾 <strong>খোল পোড়া রোগ (Rhizoctonia solani):</strong><br/><br/>• <strong>লক্ষণ:</strong> পানির উপরিভাগে ধান গাছের খোলে সাপের চামড়ার মতো অনিয়মিত ধূসর-সবুজ দাগ।<br/>• <strong>প্রতিকার:</strong> হেক্সাকোনাজল (যেমন: কনটাফ ৫ ইসি @ ১ মিলি/লিটার) অথবা ভ্যালিডামাইসিন (২ মিলি/লিটার) গাছের গোড়ায় স্প্রে করুন।`
                    : `🌾 <strong>Sheath Blight (Rhizoctonia solani):</strong><br/><br/>• <strong>Symptoms:</strong> Snake-skin greenish-grey lesions near the waterline on leaf sheaths.<br/>• <strong>Control:</strong> Spray Hexaconazole 5 EC (1 ml/L) or Validamycin 3L (2 ml/L) directed at the plant base.`;

                return {
                    html: html,
                    text_bn: `খোল পোড়া রোগে ধান গাছের গোড়ায় সাপের চামড়ার মতো দাগ হয়। প্রতিকারে হেক্সাকোনাজল বা ভ্যালিডামাইসিন গাছের গোড়ায় স্প্রে করুন।`,
                    text_en: `Sheath Blight causes snake-skin lesions on leaf sheaths. Spray Hexaconazole or Validamycin targeted at the plant base.`
                };
            }

            // 6. Rice Hispa (পামরী পোকা)
            if (q.includes('পামরী') || q.includes('পোকা') || q.includes('hispa') || q.includes('insect')) {
                const html = isBn
                    ? `🐛 <strong>ধানের পামরী পোকা (Dicladispa armigera):</strong><br/><br/>• <strong>লক্ষণ:</strong> পাতার সবুজ অংশ খেয়ে সাদা সমান্তরাল রেখা তৈরি করে।<br/>• <strong>ঘরোয়া দমন:</strong> জমিতে ডালপালা পুঁতে পাখি বসার ব্যবস্থা (পার্চিং) করুন এবং মশারি জাল দিয়ে পামরী পোকা টেনে ধ্বংস করুন।<br/>• <strong>রাসায়নিক দমন:</strong> আক্রমণ তীব্র হলে ক্লোরপাইরিফস (যেমন: ডারসবান ২০ ইসি @ ২ মিলি/লিটার) স্প্রে করুন।`
                    : `🐛 <strong>Rice Hispa (Dicladispa armigera):</strong><br/><br/>• <strong>Symptoms:</strong> Adult beetles scrape green leaf chlorophyll leaving parallel white streaks.<br/>• <strong>Organic/Eco Control:</strong> Field perching for insectivorous birds and light-trap netting.<br/>• <strong>Chemical Control:</strong> Spray Chlorpyrifos 20 EC (2 ml/L) if threshold exceeds 1-2 beetles/hill.`;

                return {
                    html: html,
                    text_bn: `পামরী পোকা পাতার সবুজ অংশ খেয়ে সাদা রেখা বানায়। দমনে জমিতে পার্চিং করুন এবং আক্রমণ বেশি হলে ক্লোরপাইরিফস স্প্রে করুন।`,
                    text_en: `Rice Hispa scrapes leaf chlorophyll creating white streaks. Use field perching and spray Chlorpyrifos for severe infestations.`
                };
            }

            // 7. Fertilizer & Urea Rules (ইউরিয়া / সার)
            if (q.includes('ইউরিয়া') || q.includes('সার') || q.includes('fertilizer') || q.includes('urea') || q.includes('npk')) {
                const html = isBn
                    ? `🧪 <strong>সারের ব্যবহার ও ইউরিয়া সতর্কবার্তা:</strong><br/><br/>• <strong>কখন ইউরিয়া নিষিদ্ধ:</strong> জমিতে ব্লাস্ট বা ব্যাকটেরিয়াল পাতা পোড়া রোগ দেখা দিলে ইউরিয়া উপরিপ্রয়োগ সম্পূর্ণ বন্ধ রাখুন। ইউরিয়া দিলে রোগ দ্রুত বাড়ে।<br/>• <strong>প্রয়োজনীয় সার:</strong> রোগ প্রতিরোধ ক্ষমতা বাড়াতে শতক প্রতি ১৫০-২০০ গ্রাম পটাশ (MOP) সার প্রয়োগ করুন।<br/>• <strong>ইউরিয়া প্রয়োগের সঠিক নিয়ম:</strong> জমি থেকে পানি কিছুটা কমিয়ে ৩ কিস্তিতে সমানভাবে ইউরিয়া প্রয়োগ করুন।`
                    : `🧪 <strong>Fertilizer & Urea Management:</strong><br/><br/>• <strong>When to Stop Urea:</strong> Immediately suspend top-dressing Urea if Blast or Bacterial Blight is present.<br/>• <strong>Potassium Boost:</strong> Apply additional MOP (Potash) @ 5 kg/acre to strengthen cell walls against fungal penetration.<br/>• <strong>Application:</strong> Apply nitrogen in 3 split doses under moist, non-flooded conditions.`;

                return {
                    html: html,
                    text_bn: `ব্লাস্ট বা পাতা পোড়া রোগে ইউরিয়া সার দেওয়া সম্পূর্ণ বন্ধ রাখুন। রোগ প্রতিরোধ ক্ষমতা বাড়াতে পটাশ সার দিন এবং ইউরিয়া ৩ কিস্তিতে প্রয়োগ করুন।`,
                    text_en: `Stop top-dressing Urea if Blast or Blight is active. Apply Potash to strengthen plant immunity and split Urea into three doses.`
                };
            }

            // 8. Weather & Spraying Time (আবহাওয়া / কখন স্প্রে করব)
            if (q.includes('আবহাওয়া') || q.includes('কখন') || q.includes('সময়') || q.includes('weather') || q.includes('when to spray') || q.includes('rain')) {
                const html = isBn
                    ? `🌦️ <strong>স্প্রে করার আদর্শ সময় ও আবহাওয়া নির্দেশিকা:</strong><br/><br/>• <strong>সঠিক সময়:</strong> বিকেল ৩:৩০ থেকে ৫:০০ টার মিষ্টি রোদে স্প্রে করা সবচেয়ে কার্যকর। প্রখর রোদে বা সকালে শিশির ভেজা পাতায় স্প্রে করবেন না।<br/>• <strong>বৃষ্টির সতর্কতা:</strong> স্প্রে করার ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা থাকলে স্প্রে স্থগিত রাখুন।<br/>• <strong>বাতাস:</strong> সর্বদা বাতাসের অনুকূলে স্প্রে করুন যাতে ওষুধ চোখে-মুখে না লাগে।`
                    : `🌦️ <strong>Weather & Spraying Advisory:</strong><br/><br/>• <strong>Best Timing:</strong> Late afternoon (3:30 PM - 5:00 PM) during mild sunlight.<br/>• <strong>Rain Advisory:</strong> Avoid spraying if rain is expected within 4 hours.<br/>• <strong>Wind:</strong> Always spray in the direction of the wind with appropriate protective gear.`;

                return {
                    html: html,
                    text_bn: `বিকেল ৩টা ৩০ থেকে ৫টার মিষ্টি রোদে স্প্রে করা সবচেয়ে ভালো। ৪ ঘণ্টার মধ্যে বৃষ্টির সম্ভাবনা থাকলে স্প্রে বন্ধ রাখুন এবং বাতাসের অনুকূলে স্প্রে করুন।`,
                    text_en: `Late afternoon from 3:30 to 5 PM is ideal for spraying. Postpone spraying if rain is expected within 4 hours and spray along wind direction.`
                };
            }

            // 9. Water & Irrigation (সেচ ও পানি)
            if (q.includes('সেচ') || q.includes('পানি') || q.includes('water') || q.includes('irrigation')) {
                const html = isBn
                    ? `💧 <strong>সেচ ও পানি ব্যবস্থাপনা:</strong><br/><br/>• চারা রোপণের পর ২-৩ ইঞ্চি পানি রাখুন।<br/>• কুশি গজানোর সময় মাঝে মাঝে জমি শুকিয়ে বাতাস চলাচলের সুযোগ দিন (AWD পদ্ধতি)।<br/>• থোর ও ফুল ফোটার সময় জমিতে অবশ্যই পর্যাপ্ত পানি নিশ্চিত করুন।<br/>• রোগ দেখা দিলে অতিরিক্ত পানি বের করে দিন।`
                    : `💧 <strong>Irrigation & Water Guidance:</strong><br/><br/>• Maintain 2-3 inches standing water during initial establishment.<br/>• Use Alternate Wetting and Drying (AWD) during tillering to promote root aeration.<br/>• Ensure continuous moisture during panicle initiation and flowering.`;

                return {
                    html: html,
                    text_bn: `চারা রোপণের পর ২ থেকে ৩ ইঞ্চি পানি রাখুন। কুশি গজানোর সময় এডব্লিউডি পদ্ধতিতে মাঝে মাঝে জমি শুকান এবং ফুল ফোটার সময় পর্যাপ্ত পানি রাখুন।`,
                    text_en: `Maintain 2 to 3 inches water after planting. Use Alternate Wetting and Drying during tillering and ensure continuous water during flowering.`
                };
            }

            // 10. Default Fallback
            const html = isBn
                ? `🌾 ধন্যবাদ আপনার প্রশ্নের জন্য! ধানের নির্দিষ্ট কোনো রোগ (যেমন: ব্লাস্ট, পাতা পোড়া, বাদামী দাগ, খোল পোড়া, পামরী পোকা) অথবা সার/সেচের নিয়ম জানতে লিখুন। অথবা উপরের কুইক বাটনে চাপ দিন। জরুরি পরামর্শের জন্য কল করুন <strong>১৬১২৩</strong>।`
                : `🌾 Thank you for your question! Ask about specific diseases (Blast, Blight, Brown Spot, Hispa), fertilizers, or spraying weather. For live emergency support, dial <strong>16123</strong>.`;

            return {
                html: html,
                text_bn: `ধন্যবাদ আপনার প্রশ্নের জন্য। ধানের যেকোনো রোগ, সার বা সেচের নিয়ম জানতে লিখুন। জরুরি কৃষি পরামর্শের জন্য কল করুন ১৬১২৩।`,
                text_en: `Thank you for your question. Ask about rice leaf diseases, fertilizers, or spraying advice. For emergency assistance dial 16123.`
            };
        }

        /* ── Progressive Web App (PWA) Service Worker & Install Logic ── */
        let deferredPrompt = null;

        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/sw.js', { scope: '/' })
                    .then((reg) => {
                        console.log('RiceGuard PWA Service Worker Registered! Scope:', reg.scope);
                    })
                    .catch((err) => {
                        console.warn('Service Worker registration failed:', err);
                    });
            });
        }

        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            const btnPwa = document.getElementById('btn-install-pwa');
            if (btnPwa) {
                btnPwa.style.display = 'inline-flex';
            }
        });

        window.addEventListener('appinstalled', () => {
            console.log('RiceGuard App was successfully installed!');
            const btnPwa = document.getElementById('btn-install-pwa');
            if (btnPwa) btnPwa.style.display = 'none';
            deferredPrompt = null;
        });

        function installPWA() {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then((choiceResult) => {
                    if (choiceResult.outcome === 'accepted') {
                        console.log('User accepted RiceGuard installation');
                        const btnPwa = document.getElementById('btn-install-pwa');
                        if (btnPwa) btnPwa.style.display = 'none';
                    }
                    deferredPrompt = null;
                });
            } else {
                alert(currentLang === 'bn' 
                    ? '📱 অ্যাপটি আপনার ফোনে ইনস্টল করতে ব্রাউজারের থ্রি-ডট (⋮) মেনুতে চাপ দিয়ে "Add to Home screen" বা "Install app" সিলেক্ট করুন।' 
                    : '📱 To install the app on your phone, open your browser menu (⋮) and tap "Add to Home screen" or "Install app".');
            }
        }

        /* ── Feature 1: Live Agricultural Weather & Spraying Advisory Engine ── */
        const BD_DISTRICTS_LIST = [
            { en: "Dinajpur", bn: "দিনাজপুর" },
            { en: "Mymensingh", bn: "ময়মনসিংহ" },
            { en: "Bogura", bn: "বগুড়া" },
            { en: "Naogaon", bn: "নওগাঁ" },
            { en: "Rangpur", bn: "রংপুর" },
            { en: "Rajshahi", bn: "রাজশাহী" },
            { en: "Dhaka", bn: "ঢাকা" },
            { en: "Gazipur", bn: "গাজীপুর" },
            { en: "Cumilla", bn: "কুমিল্লা" },
            { en: "Barishal", bn: "বরিশাল" },
            { en: "Sylhet", bn: "সিলেট" },
            { en: "Jashore", bn: "যশোর" },
            { en: "Khulna", bn: "খুলনা" },
            { en: "Tangail", bn: "টাঙ্গাইল" },
            { en: "Jamalpur", bn: "জামালপুর" },
            { en: "Netrokona", bn: "নেত্রকোণা" },
            { en: "Sherpur", bn: "শেরপুর" },
            { en: "Kishoreganj", bn: "কিশোরগঞ্জ" },
            { en: "Narayanganj", bn: "নারায়ণগঞ্জ" },
            { en: "Manikganj", bn: "মানিকগঞ্জ" },
            { en: "Munshiganj", bn: "মুন্সীগঞ্জ" },
            { en: "Narsingdi", bn: "নরসিংদী" },
            { en: "Faridpur", bn: "ফরিদপুর" },
            { en: "Gopalganj", bn: "গোপালগঞ্জ" },
            { en: "Madaripur", bn: "মাদারীপুর" },
            { en: "Rajbari", bn: "রাজবাড়ী" },
            { en: "Shariatpur", bn: "শরীয়তপুর" },
            { en: "Gaibandha", bn: "গাইবান্ধা" },
            { en: "Kurigram", bn: "কুড়িগ্রাম" },
            { en: "Lalmonirhat", bn: "লালমনিরহাট" },
            { en: "Nilphamari", bn: "নীলফামারী" },
            { en: "Panchagarh", bn: "পঞ্চগড়" },
            { en: "Thakurgaon", bn: "ঠাকুরগাঁও" },
            { en: "Joypurhat", bn: "জয়পুরহাট" },
            { en: "Natore", bn: "নাটোর" },
            { en: "Chapai Nawabganj", bn: "চাঁপাইনবাবগঞ্জ" },
            { en: "Pabna", bn: "পাবনা" },
            { en: "Sirajganj", bn: "সিরাজগঞ্জ" },
            { en: "Bagerhat", bn: "বাগেরহাট" },
            { en: "Chuadanga", bn: "চুয়াডাঙ্গা" },
            { en: "Jhenaidah", bn: "ঝিনাইদহ" },
            { en: "Kushtia", bn: "কুষ্টিয়া" },
            { en: "Magura", bn: "মাগুরা" },
            { en: "Meherpur", bn: "মেহেরপুর" },
            { en: "Narail", bn: "নড়াইল" },
            { en: "Satkhira", bn: "সাতক্ষীরা" },
            { en: "Barguna", bn: "বরগুনা" },
            { en: "Bhola", bn: "ভোলা" },
            { en: "Jhalokati", bn: "ঝালকাঠি" },
            { en: "Patuakhali", bn: "পটুয়াখালী" },
            { en: "Pirojpur", bn: "পিরোজপুর" },
            { en: "Habiganj", bn: "হবিগঞ্জ" },
            { en: "Moulvibazar", bn: "মৌলভীবাজার" },
            { en: "Sunamganj", bn: "সুনামগঞ্জ" },
            { en: "Chattogram", bn: "চট্টগ্রাম" },
            { en: "Bandarban", bn: "বান্দরবান" },
            { en: "Brahmanbaria", bn: "ব্রাহ্মণবাড়িয়া" },
            { en: "Chandpur", bn: "চাঁদপুর" },
            { en: "Cox's Bazar", bn: "কক্সবাজার" },
            { en: "Feni", bn: "ফেনী" },
            { en: "Khagrachhari", bn: "খাগড়াছড়ি" },
            { en: "Lakshmipur", bn: "লক্ষ্মীপুর" },
            { en: "Noakhali", bn: "নোয়াখালী" },
            { en: "Rangamati", bn: "রাঙ্গামাটি" }
        ];

        let currentSelectedDistrict = "Dinajpur";

        function populateDistrictDropdown() {
            const selects = [
                document.getElementById('weather-district-select'),
                document.getElementById('batch-weather-district-select')
            ];
            const isBn = (currentLang === 'bn');
            selects.forEach(select => {
                if (!select) return;
                select.innerHTML = '';
                BD_DISTRICTS_LIST.forEach(d => {
                    const opt = document.createElement('option');
                    opt.value = d.en;
                    opt.textContent = isBn ? `📍 ${d.bn}` : `📍 ${d.en}`;
                    if (d.en === currentSelectedDistrict) opt.selected = true;
                    select.appendChild(opt);
                });
            });
        }

        async function fetchLiveWeather(district = "Dinajpur", lat = null, lon = null) {
            // Single leaf weather elements
            const timeLbl = document.getElementById('weather-updated-time');
            const tempVal = document.getElementById('weather-val-temp');
            const humVal = document.getElementById('weather-val-humidity');
            const rainVal = document.getElementById('weather-val-rain');
            const windVal = document.getElementById('weather-val-wind');
            const iconElem = document.getElementById('weather-icon-temp');
            const banner = document.getElementById('weather-advisory-banner');
            const bannerIcon = document.getElementById('weather-advisory-icon');
            const bannerTitle = document.getElementById('weather-advisory-title');
            const bannerDesc = document.getElementById('weather-advisory-desc');

            // Batch mode weather elements
            const bTimeLbl = document.getElementById('batch-weather-updated-time');
            const bTempVal = document.getElementById('batch-weather-val-temp');
            const bHumVal = document.getElementById('batch-weather-val-humidity');
            const bRainVal = document.getElementById('batch-weather-val-rain');
            const bWindVal = document.getElementById('batch-weather-val-wind');
            const bIconElem = document.getElementById('batch-weather-icon-temp');
            const bBanner = document.getElementById('batch-weather-advisory-banner');
            const bBannerIcon = document.getElementById('batch-weather-advisory-icon');
            const bBannerTitle = document.getElementById('batch-weather-advisory-title');
            const bBannerDesc = document.getElementById('batch-weather-advisory-desc');

            const isBn = (currentLang === 'bn');
            const loadingMsg = isBn ? 'স্যাটেলাইট আবহাওয়া লোড হচ্ছে...' : 'Fetching Satellite Weather...';
            if (bannerTitle) bannerTitle.textContent = loadingMsg;
            if (bBannerTitle) bBannerTitle.textContent = loadingMsg;

            let url = '/api/weather?district=' + encodeURIComponent(district);
            if (lat !== null && lon !== null) {
                url = `/api/weather?lat=${lat}&lon=${lon}`;
            }

            try {
                const res = await fetch(url);
                const data = await res.json();
                if (data && data.success) {
                    window.currentWeatherData = data;
                    currentSelectedDistrict = data.district_en;

                    const selects = [
                        document.getElementById('weather-district-select'),
                        document.getElementById('batch-weather-district-select')
                    ];
                    selects.forEach(sel => { if (sel) sel.value = data.district_en; });

                    const updateStr = isBn ? `আপডেট: ${data.updated_at}` : `Updated: ${data.updated_at}`;
                    if (timeLbl) timeLbl.textContent = updateStr;
                    if (bTimeLbl) bTimeLbl.textContent = updateStr;

                    const tempStr = `${data.temperature}°C`;
                    if (tempVal) tempVal.textContent = tempStr;
                    if (bTempVal) bTempVal.textContent = tempStr;

                    const humStr = `${data.humidity}%`;
                    if (humVal) humVal.textContent = humStr;
                    if (bHumVal) bHumVal.textContent = humStr;

                    const rainStr = `${data.rain_prob_max}%`;
                    if (rainVal) rainVal.textContent = rainStr;
                    if (bRainVal) bRainVal.textContent = rainStr;

                    const windStr = `${data.wind_speed} km/h`;
                    if (windVal) windVal.textContent = windStr;
                    if (bWindVal) bWindVal.textContent = windStr;

                    const iconStr = data.icon || '☀️';
                    if (iconElem) iconElem.textContent = iconStr;
                    if (bIconElem) bIconElem.textContent = iconStr;

                    const adv = data.advisory || {};
                    const bannerClass = `spraying-alert-banner ${adv.status || 'optimal'}`;
                    if (banner) banner.className = bannerClass;
                    if (bBanner) bBanner.className = bannerClass;

                    const iconEmoji = adv.status === 'danger' ? '⚠️' : (adv.status === 'optimal' ? '✅' : '⛅');
                    if (bannerIcon) bannerIcon.textContent = iconEmoji;
                    if (bBannerIcon) bBannerIcon.textContent = iconEmoji;

                    const advTitleStr = isBn ? adv.tier_bn : adv.tier_en;
                    if (bannerTitle) bannerTitle.textContent = advTitleStr;
                    if (bBannerTitle) bBannerTitle.textContent = advTitleStr;

                    const advDescStr = isBn ? `${adv.message_bn} ${adv.recommendation_bn}` : `${adv.message_en} ${adv.recommendation_en}`;
                    if (bannerDesc) bannerDesc.textContent = advDescStr;
                    if (bBannerDesc) bBannerDesc.textContent = advDescStr;
                }
            } catch (err) {
                console.warn('Weather fetch warning:', err);
            }
        }

        function changeWeatherDistrict(districtName) {
            currentSelectedDistrict = districtName;
            fetchLiveWeather(districtName);
        }

        let userExactCoords = null;
        let isGpsAutoDetected = false;

        function detectGPSLocation(isSilent = false) {
            if (!navigator.geolocation) {
                if (!isSilent) alert(currentLang === 'bn' ? 'আপনার ব্রাউজারে জিপিএস সুবিধা নেই।' : 'Geolocation is not supported by your browser.');
                return;
            }
            const btn = document.querySelector('.weather-gps-btn');
            if (btn && !isSilent) btn.innerHTML = '<span>⏳</span> ' + (currentLang === 'bn' ? 'লোকেশন খুঁজছি...' : 'Locating...');

            navigator.geolocation.getCurrentPosition(
                (pos) => {
                    userExactCoords = { lat: pos.coords.latitude, lon: pos.coords.longitude };
                    isGpsAutoDetected = true;
                    if (btn) {
                        btn.innerHTML = '<span>📍</span> ' + (currentLang === 'bn' ? '✓ জিপিএস সক্রিয়' : '✓ GPS Active');
                        btn.style.background = '#10B981';
                        btn.style.color = '#FFFFFF';
                    }
                    fetchLiveWeather(null, pos.coords.latitude, pos.coords.longitude);
                },
                (err) => {
                    if (btn) btn.innerHTML = '<span>📍</span> ' + (currentLang === 'bn' ? 'আমার স্থান' : 'My Location');
                    if (!isSilent) {
                        alert(currentLang === 'bn' ? 'জিপিএস লোকেশন পাওয়া যায়নি। ড্রপডাউন থেকে আপনার জেলা নির্বাচন করুন।' : 'Could not detect GPS. Please select your district from dropdown.');
                    }
                },
                { timeout: 8000, maximumAge: 300000 }
            );
        }

        function autoDetectUserLocation() {
            // Silently try background GPS on page load or photo upload
            if (navigator.geolocation && !isGpsAutoDetected) {
                detectGPSLocation(true);
            }
        }

        /* ── Feature 2: Interactive Bangladesh Disease Outbreak Geo-Map Engine ── */
        const BASELINE_OUTBREAK_POINTS = [
            { id: "dinajpur", district_en: "Dinajpur", district_bn: "দিনাজপুর", division: "Rangpur", lat: 25.6217, lon: 88.6355, total_cases: 84, primary_disease: "Leaf Blast", primary_disease_bn: "ধানের ব্লাস্ট রোগ", disease_slug: "leaf_blast", severity: "high", risk_label_bn: "উচ্চ সতর্কতা (High Alert)", advisory_bn: "আর্দ্রতা বৃদ্ধির কারণে ব্লাস্ট রোগ দ্রুত ছড়াচ্ছে। ট্রাইসাইক্লাজল ৭৫ ডব্লিউপি স্প্রে করুন।" },
            { id: "mymensingh", district_en: "Mymensingh", district_bn: "ময়মনসিংহ", division: "Mymensingh", lat: 24.7471, lon: 90.4203, total_cases: 112, primary_disease: "Bacterial Leaf Blight", primary_disease_bn: "ব্যাকটেরিয়াল পাতা পোড়া", disease_slug: "bacterial_leaf_blight", severity: "high", risk_label_bn: "উচ্চ সতর্কতা (High Alert)", advisory_bn: "জমির পানি ৩-৪ দিন শুকিয়ে রাখুন এবং বিঘা প্রতি ৫ কেজি অতিরিক্ত পটাশ সার দিন।" },
            { id: "bogura", district_en: "Bogura", district_bn: "বগুড়া", division: "Rajshahi", lat: 24.8465, lon: 89.3777, total_cases: 65, primary_disease: "Brown Spot", primary_disease_bn: "বাদামী দাগ রোগ", disease_slug: "brown_spot", severity: "medium", risk_label_bn: "মাঝারি ঝুঁকি (Moderate Risk)", advisory_bn: "মাটিতে পটাশ ও জিংকের ঘাটতি মেটান এবং ম্যানকোজেব ৭৫ ডব্লিউপি স্প্রে করুন।" },
            { id: "naogaon", district_en: "Naogaon", district_bn: "নওগাঁ", division: "Rajshahi", lat: 24.7936, lon: 88.9318, total_cases: 78, primary_disease: "Leaf Blast", primary_disease_bn: "ধানের ব্লাস্ট রোগ", disease_slug: "leaf_blast", severity: "high", risk_label_bn: "উচ্চ সতর্কতা (High Alert)", advisory_bn: "ইউরিয়া সারের উপরিপ্রয়োগ বন্ধ রেখে নেটিভো ০.৬ গ্রাম/লিটার বিকেলে স্প্রে করুন।" },
            { id: "barishal", district_en: "Barishal", district_bn: "বরিশাল", division: "Barishal", lat: 22.7010, lon: 90.3535, total_cases: 52, primary_disease: "Rice Hispa", primary_disease_bn: "পামরী পোকা", disease_slug: "rice_hispa", severity: "medium", risk_label_bn: "মাঝারি ঝুঁকি (Moderate Risk)", advisory_bn: "জমিতে পার্চিং (ডাল পোঁতা) করুন এবং ক্লোরপাইরিফস ২০ ইসি ২ মিলি/লিটার স্প্রে করুন।" },
            { id: "cumilla", district_en: "Cumilla", district_bn: "কুমিল্লা", division: "Chattogram", lat: 23.4607, lon: 91.1809, total_cases: 46, primary_disease: "Sheath Blight", primary_disease_bn: "খোল পোড়া রোগ", disease_slug: "sheath_blight", severity: "medium", risk_label_bn: "মাঝারি ঝুঁকি (Moderate Risk)", advisory_bn: "গাছের গোড়ায় জমে থাকা পানি বের করে হেক্সাকোনাজল (কনটাফ ৫ ইসি) স্প্রে করুন।" },
            { id: "sylhet", district_en: "Sylhet", district_bn: "সিলেট", division: "Sylhet", lat: 24.8949, lon: 91.8687, total_cases: 38, primary_disease: "Leaf Scald", primary_disease_bn: "পাতা ঝলসানো রোগ", disease_slug: "leaf_scald", severity: "low", risk_label_bn: "নিয়ন্ত্রিত (Low Risk)", advisory_bn: "সুষম সার বজায় রাখুন ও আক্রান্ত জমিতে প্রপিকোনাজল স্প্রে করুন।" },
            { id: "jashore", district_en: "Jashore", district_bn: "যশোর", division: "Khulna", lat: 23.1664, lon: 89.2182, total_cases: 42, primary_disease: "Narrow Brown Leaf Spot", primary_disease_bn: "সরু বাদামী দাগ রোগ", disease_slug: "narrow_brown_leaf_spot", severity: "low", risk_label_bn: "নিয়ন্ত্রিত (Low Risk)", advisory_bn: "পটাশ সারের ঘাটতি দূর করুন এবং ছত্রাকনাশক স্প্রে করুন।" },
            { id: "rangpur", district_en: "Rangpur", district_bn: "রংপুর", division: "Rangpur", lat: 25.7439, lon: 89.2752, total_cases: 72, primary_disease: "Leaf Blast", primary_disease_bn: "ধানের ব্লাস্ট রোগ", disease_slug: "leaf_blast", severity: "high", risk_label_bn: "উচ্চ সতর্কতা (High Alert)", advisory_bn: "ভোরের কুয়াশা ও শিশির কাটলে বিকেলে ট্রাইসাইক্লাজল স্প্রে করুন।" },
            { id: "tangail", district_en: "Tangail", district_bn: "টাঙ্গাইল", division: "Dhaka", lat: 24.2513, lon: 89.9167, total_cases: 35, primary_disease: "Sheath Blight", primary_disease_bn: "খোল পোড়া রোগ", disease_slug: "sheath_blight", severity: "low", risk_label_bn: "নিয়ন্ত্রিত (Low Risk)", advisory_bn: "গাছের ঘনত্ব ঠিক রাখুন এবং সুষম পটাশ সার ব্যবহার করুন।" }
        ];

        let outbreakMap = null;
        let outbreakMarkersLayer = null;
        let currentOutbreakFilter = 'all';

        function initOutbreakMap() {
            const mapContainer = document.getElementById('outbreak-map');
            if (!mapContainer) return;

            if (typeof L === 'undefined') {
                console.warn('Leaflet.js not loaded yet, retrying in 150ms...');
                setTimeout(initOutbreakMap, 150);
                return;
            }

            if (outbreakMap) {
                try { outbreakMap.remove(); } catch(e) {}
                outbreakMap = null;
            }

            try {
                // Center precisely on Bangladesh (23.75° N, 90.35° E)
                outbreakMap = L.map('outbreak-map', {
                    center: [23.75, 90.35],
                    zoom: 7,
                    minZoom: 6,
                    maxZoom: 14,
                    scrollWheelZoom: false,
                    attributionControl: false,
                    zoomControl: true
                });

                // 1. Primary Professional Esri World Street Map (Ultra-Crisp, High-Speed, Zero Watermark, No API Key)
                const esriWorldStreet = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
                    maxZoom: 18,
                    crossOrigin: true
                });

                // 2. Secondary Fallback Tile Layer (OpenStreetMap Humanitarian)
                const osmHot = L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    crossOrigin: true
                });

                // 3. Tertiary Fallback Tile Layer (Standard OpenStreetMap)
                const osmLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    crossOrigin: true
                });

                esriWorldStreet.on('tileerror', function() {
                    console.warn('Primary Esri layer error, switching to OSM...');
                    if (outbreakMap && !outbreakMap.hasLayer(osmHot)) {
                        osmHot.addTo(outbreakMap);
                    }
                });

                esriWorldStreet.addTo(outbreakMap);

                outbreakMarkersLayer = L.layerGroup().addTo(outbreakMap);
                loadOutbreakMapMarkers(currentOutbreakFilter || 'all');

                // Force layout calculation multiple times to prevent blank grey box
                outbreakMap.invalidateSize(true);
                setTimeout(() => { if (outbreakMap) outbreakMap.invalidateSize(true); }, 150);
                setTimeout(() => { if (outbreakMap) outbreakMap.invalidateSize(true); }, 500);
                setTimeout(() => { if (outbreakMap) outbreakMap.invalidateSize(true); }, 1200);

                // Auto-refresh layout when map section scrolls into view
                if ('IntersectionObserver' in window) {
                    const mapObserver = new IntersectionObserver((entries) => {
                        entries.forEach(entry => {
                            if (entry.isIntersecting && outbreakMap) {
                                outbreakMap.invalidateSize(true);
                            }
                        });
                    }, { threshold: 0.05 });

                    const mapSection = document.getElementById('outbreak-map-section') || mapContainer;
                    if (mapSection) mapObserver.observe(mapSection);
                }

                window.addEventListener('resize', () => {
                    if (outbreakMap) outbreakMap.invalidateSize();
                });
            } catch (err) {
                console.error('Error initializing Outbreak Map:', err);
            }
        }

        async function loadOutbreakMapMarkers(filter = 'all') {
            if (!outbreakMap || !outbreakMarkersLayer) return;
            outbreakMarkersLayer.clearLayers();

            let pointsToRender = [];
            let totalCases = 628;
            let activeDistricts = 10;

            try {
                const res = await fetch('/api/outbreak-map?disease=' + encodeURIComponent(filter));
                if (res.ok) {
                    const data = await res.json();
                    if (data && data.success && Array.isArray(data.points) && data.points.length > 0) {
                        pointsToRender = data.points;
                        totalCases = data.total_national_cases || 628;
                        activeDistricts = data.total_active_districts || pointsToRender.length;
                    }
                }
            } catch (err) {
                console.warn('API fetch fallback to baseline:', err);
            }

            // Client-side fallback if API was sleeping or returned empty
            if (pointsToRender.length === 0) {
                const slug = (filter || 'all').toLowerCase().replace(' ', '_').trim();
                pointsToRender = BASELINE_OUTBREAK_POINTS.filter(p => {
                    if (slug === 'all') return true;
                    return p.disease_slug === slug;
                });
            }

            const isBn = (currentLang === 'bn');
            const statCases = document.getElementById('map-stat-cases');
            const statDists = document.getElementById('map-stat-districts');

            if (statCases) {
                const countStr = `${totalCases}+`;
                statCases.textContent = isBn ? countStr.replace(/[0-9]/g, d => ({'0':'০','1':'১','2':'২','3':'৩','4':'৪','5':'৫','6':'৬','7':'৭','8':'৮','9':'৯'}[d])) : countStr;
            }
            if (statDists) {
                const distStr = `${activeDistricts}`;
                statDists.textContent = isBn ? distStr.replace(/[0-9]/g, d => ({'0':'০','1':'১','2':'২','3':'৩','4':'৪','5':'৫','6':'৬','7':'৭','8':'৮','9':'৯'}[d])) : distStr;
            }

            const markerCoords = [];

            pointsToRender.forEach(pt => {
                markerCoords.push([pt.lat, pt.lon]);

                const iconHtml = `
                    <div class="glow-marker ${pt.severity}">
                        <div class="marker-pulse"></div>
                        <div class="marker-dot"></div>
                        <div class="marker-tag">${isBn ? pt.district_bn : pt.district_en}</div>
                    </div>
                `;

                const customIcon = L.divIcon({
                    className: 'glow-marker-wrap',
                    html: iconHtml,
                    iconSize: [36, 36],
                    iconAnchor: [18, 18],
                    popupAnchor: [0, -18]
                });

                const popupHtml = `
                    <div class="outbreak-popup-box">
                        <div class="outbreak-popup-title">
                            <span>📍 ${isBn ? pt.district_bn : pt.district_en}</span>
                            <span class="outbreak-popup-badge ${pt.severity}">${isBn ? pt.risk_label_bn : pt.severity.toUpperCase()}</span>
                        </div>
                        <div class="outbreak-popup-disease">
                            🌾 ${isBn ? 'প্রধান রোগ:' : 'Top Condition:'} <strong>${isBn ? pt.primary_disease_bn : pt.primary_disease}</strong>
                        </div>
                        <div class="outbreak-popup-cases">
                            📊 ${isBn ? 'মোট সনাক্তকরণ:' : 'Recorded Cases:'} <strong>${pt.total_cases} টি</strong> (${pt.division} বিভাগ)
                        </div>
                        <div class="outbreak-popup-adv">
                            💡 <strong>${isBn ? 'সতর্কতা ও পরামর্শ:' : 'Advisory:'}</strong> ${isBn ? pt.advisory_bn : 'Maintain balanced fertilization and spray recommended fungicide.'}
                        </div>
                    </div>
                `;

                const marker = L.marker([pt.lat, pt.lon], { icon: customIcon });
                marker.bindPopup(popupHtml, { maxWidth: 320 });
                outbreakMarkersLayer.addLayer(marker);
            });

            // Smoothly auto-fit and center on filtered active districts
            if (markerCoords.length > 0) {
                if (filter === 'all' || markerCoords.length >= 6) {
                    outbreakMap.flyTo([23.75, 90.35], 7, { duration: 0.8 });
                } else if (markerCoords.length === 1) {
                    outbreakMap.flyTo(markerCoords[0], 8.5, { duration: 0.8 });
                } else {
                    const bounds = L.latLngBounds(markerCoords);
                    outbreakMap.flyToBounds(bounds, { padding: [40, 40], maxZoom: 8.5, duration: 0.8 });
                }
            }
        }

        function openOutbreakDistrictModal(districtId) {
            const pt = BASELINE_OUTBREAK_POINTS.find(p => p.id === districtId);
            if (!pt) return;
            const isBn = (currentLang === 'bn');
            const title = isBn ? pt.district_bn : pt.district_en;
            const disease = isBn ? pt.primary_disease_bn : pt.primary_disease;
            const adv = isBn ? pt.advisory_bn : 'Maintain balanced fertilization and spray recommended fungicide.';
            const cases = isBn ? `${pt.total_cases} টি` : `${pt.total_cases} cases`;
            
            alert(`📍 ${title} — ${disease}\n\n📊 ${isBn ? 'মোট সনাক্তকরণ' : 'Total Cases'}: ${cases} (${pt.division} ${isBn ? 'বিভাগ' : 'Division'})\n\n💡 ${isBn ? 'সতর্কতা ও পরামর্শ' : 'Advisory'}: ${adv}`);
        }

        function filterOutbreakMap(diseaseSlug, btn) {
            currentOutbreakFilter = diseaseSlug;
            document.querySelectorAll('.outbreak-chip').forEach(c => c.classList.remove('active'));
            if (btn) btn.classList.add('active');

            // 1. Synchronize SVG Vector Hotspots
            const slug = (diseaseSlug || 'all').toLowerCase().replace(' ', '_').trim();
            document.querySelectorAll('.svg-hotspot-group').forEach(group => {
                const d = group.getAttribute('data-disease');
                if (slug === 'all' || d === slug) {
                    group.classList.remove('dimmed');
                } else {
                    group.classList.add('dimmed');
                }
            });

            // 2. Synchronize Leaflet Map Markers
            loadOutbreakMapMarkers(diseaseSlug);
        }

        document.addEventListener('DOMContentLoaded', function () {
            // Show install button on mobile browsers as fallback
            if (/Android|iPhone|iPad|iPod/i.test(navigator.userAgent)) {
                const btnPwa = document.getElementById('btn-install-pwa');
                if (btnPwa && !window.matchMedia('(display-mode: standalone)').matches) {
                    btnPwa.style.display = 'inline-flex';
                }
            }

            setLanguage(currentLang);
            populateDistrictDropdown();
            fetchLiveWeather(currentSelectedDistrict);
            setTimeout(() => {
                initOutbreakMap();
            }, 100);
            setTimeout(() => {
                autoDetectUserLocation();
            }, 600);

            const form             = document.getElementById('diagnostic-form');
            const fileInput        = document.getElementById('image-input');
            const dropzone         = document.getElementById('dropzone');
            const previewBox       = document.getElementById('preview-box');
            const previewImg       = document.getElementById('preview-img');
            const viewModePill     = document.getElementById('view-mode-pill');
            const scannerOverlay   = document.getElementById('scanner-overlay');
            const fileNameText     = document.getElementById('file-name-text');
            const fileSizeText     = document.getElementById('file-size-text');
            const btnRemoveImage   = document.getElementById('btn-remove-image');
            const btnSubmit        = document.getElementById('btn-submit');
            const btnIcon          = document.getElementById('btn-icon');
            const btnText          = document.getElementById('btn-text');
            const evalAccordion    = document.getElementById('eval-accordion');
            const accordionToggle  = document.getElementById('accordion-toggle');

            const stateEmpty       = document.getElementById('state-empty');
            const stateLoading     = document.getElementById('state-loading');
            const stateResult      = document.getElementById('state-result');
            const loadingStepText  = document.getElementById('loading-step-text');
            const resultConfNum    = document.getElementById('result-confidence-num');
            const resultProgressBar= document.getElementById('result-progress-bar');
            const btnReset         = document.getElementById('btn-reset');
            
            const clientErrorAlert = document.getElementById('client-error-alert');
            const clientErrorText  = document.getElementById('client-error-text');
            const modalZoom        = document.getElementById('modal-zoom');
            const modalImg         = document.getElementById('modal-img');
            const btnZoomPreview   = document.getElementById('btn-zoom-preview');
            const modalClose       = document.getElementById('modal-close');

            // Camera Elements
            const btnOpenCamera    = document.getElementById('btn-open-camera');
            const btnCloseCamera   = document.getElementById('btn-close-camera');
            const btnCapturePhoto  = document.getElementById('btn-capture-photo');
            const btnSwitchCam     = document.getElementById('btn-switch-cam');
            const modalCamera      = document.getElementById('modal-camera');
            const modalPrescription= document.getElementById('modal-prescription');

            if (btnOpenCamera) btnOpenCamera.addEventListener('click', startCamera);
            if (btnCloseCamera) btnCloseCamera.addEventListener('click', stopCamera);
            if (btnCapturePhoto) btnCapturePhoto.addEventListener('click', captureFromCamera);
            if (btnSwitchCam) btnSwitchCam.addEventListener('click', switchCamera);
            if (modalCamera) {
                modalCamera.addEventListener('click', (e) => {
                    if (e.target === modalCamera) stopCamera();
                });
            }
            if (modalPrescription) {
                modalPrescription.addEventListener('click', (e) => {
                    if (e.target === modalPrescription) closePrescriptionModal();
                });
            }
            if (modalZoom) {
                modalZoom.addEventListener('click', (e) => {
                    if (e.target === modalZoom) {
                        modalZoom.classList.remove('active');
                        document.body.style.overflow = '';
                    }
                });
            }
            if (modalClose) {
                modalClose.addEventListener('click', () => {
                    if (modalZoom) modalZoom.classList.remove('active');
                    document.body.style.overflow = '';
                });
            }
            if (btnZoomPreview) {
                btnZoomPreview.addEventListener('click', () => {
                    if (modalImg && previewImg && modalZoom) {
                        modalImg.src = previewImg.src;
                        modalZoom.classList.add('active');
                        document.body.style.overflow = 'hidden';
                    }
                });
            }

            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    closePrescriptionModal();
                    if (modalZoom) modalZoom.classList.remove('active');
                    if (modalCamera && modalCamera.classList.contains('active')) stopCamera();
                    document.body.style.overflow = '';
                }
            });

            function showError(msg) {
                clientErrorText.textContent = msg;
                clientErrorAlert.style.display = 'flex';
            }
            function clearErrors() {
                clientErrorAlert.style.display = 'none';
                const sAlert = document.getElementById('server-error-alert');
                if (sAlert) sAlert.style.display = 'none';
            }

            /* ── File Handling ── */
            handleFile = function(file, autoSubmit = false) {
                clearErrors();
                autoDetectUserLocation();
                if (!file) return;

                if (!file.type.startsWith('image/')) {
                    showError(currentLang === 'bn' ? 'দয়া করে একটি সঠিক JPG বা PNG ফরম্যাটের পাতার ছবি আপলোড করুন।' : 'Please upload a valid JPG or PNG image of a rice leaf.');
                    resetFileInput();
                    return;
                }

                if (file.size > 10 * 1024 * 1024) {
                    showError(currentLang === 'bn' ? 'ছবির সাইজ ১০ মেগাবাইটের বেশি হতে পারবে না।' : 'File size cannot exceed 10 MB.');
                    resetFileInput();
                    return;
                }

                rawOriginalFile = file;

                const reader = new FileReader();
                reader.onload = function (e) {
                    originalImageSrc = e.target.result;
                    rawOriginalDataUrl = e.target.result;
                    gradcamImageSrc = '';
                    previewImg.src = originalImageSrc;
                    if (modalImg) modalImg.src = originalImageSrc;
                    fileNameText.textContent = file.name;
                    fileSizeText.textContent = formatBytes(file.size);

                    const rBtn = document.getElementById('btn-reset-filters');
                    if (rBtn) rBtn.style.display = 'none';

                    dropzone.style.display = 'none';
                    const optBar = document.querySelector('.upload-options-bar');
                    if (optBar) optBar.style.display = 'none';
                    previewBox.classList.add('active');
                    viewModePill.classList.remove('active');
                    btnSubmit.disabled = false;

                    if (autoSubmit && form) {
                        form.dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
                    }
                };
                reader.readAsDataURL(file);
            };

            function resetFileInput() {
                fileInput.value = '';
                originalImageSrc = '';
                rawOriginalDataUrl = '';
                rawOriginalFile = null;
                gradcamImageSrc = '';
                previewImg.src = '';
                modalImg.src = '';
                const rBtn = document.getElementById('btn-reset-filters');
                if (rBtn) rBtn.style.display = 'none';
                previewBox.classList.remove('active');
                viewModePill.classList.remove('active');
                if (scannerOverlay) scannerOverlay.classList.remove('scanning');
                dropzone.style.display = 'block';
                const optBar = document.querySelector('.upload-options-bar');
                if (optBar) optBar.style.display = 'flex';
                btnSubmit.disabled = true;
                btnSubmit.classList.remove('analysis-done');
                btnIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/><line x1="11" x2="11" y1="8" y2="14"/><line x1="8" x2="14" y1="11" y2="11"/></svg>';
                btnText.textContent = (I18N[currentLang] || I18N.bn).btn_analyze;
                stopAudioSpeech();
                const evalB = document.getElementById('eval-verification-banner');
                if (evalB) evalB.style.display = 'none';
            }

            /* ── Drag & Drop ── */
            ['dragenter', 'dragover'].forEach(eventName => {
                dropzone.addEventListener(eventName, (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    dropzone.classList.add('dragover');
                });
            });

            ['dragleave', 'drop'].forEach(eventName => {
                dropzone.addEventListener(eventName, (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    dropzone.classList.remove('dragover');
                });
            });

            dropzone.addEventListener('drop', (e) => {
                const dt = e.dataTransfer;
                const files = dt.files;
                if (files && files.length > 0) {
                    fileInput.files = files;
                    handleFile(files[0]);
                }
            });

            fileInput.addEventListener('change', function () {
                if (this.files && this.files.length > 0) {
                    handleFile(this.files[0]);
                }
            });

            btnRemoveImage.addEventListener('click', function () {
                resetFileInput();
                clearErrors();
            });

            /* ── Accordion ── */
            if (accordionToggle && evalAccordion) {
                accordionToggle.addEventListener('click', function () {
                    const isExpanded = evalAccordion.classList.toggle('expanded');
                    accordionToggle.setAttribute('aria-expanded', isExpanded);
                });
            }

            /* ── Tabbed Navigation ── */
            const tabBtns = document.querySelectorAll('.tab-btn');
            const tabPanes = document.querySelectorAll('.tab-pane');
            tabBtns.forEach(btn => {
                btn.addEventListener('click', function () {
                    const targetId = this.getAttribute('aria-controls');
                    tabBtns.forEach(b => {
                        b.classList.remove('active');
                        b.setAttribute('aria-selected', 'false');
                    });
                    tabPanes.forEach(p => p.classList.remove('active'));

                    this.classList.add('active');
                    this.setAttribute('aria-selected', 'true');
                    const targetPane = document.getElementById(targetId);
                    if (targetPane) targetPane.classList.add('active');
                });
            });

            /* ── Lightbox Zoom ── */
            if (btnZoomPreview && modalZoom) {
                btnZoomPreview.addEventListener('click', () => modalZoom.classList.add('active'));
            }
            if (modalClose && modalZoom) {
                modalClose.addEventListener('click', () => modalZoom.classList.remove('active'));
            }
            if (modalZoom) {
                modalZoom.addEventListener('click', (e) => {
                    if (e.target === modalZoom) modalZoom.classList.remove('active');
                });
            }

            /* ── AJAX Form Submission ── */
            form.addEventListener('submit', async function (e) {
                e.preventDefault();
                clearErrors();

                // Abort any existing in-flight request to prevent parallel request spam & 429 rate-limits
                if (window.activeSingleAbortController) {
                    try { window.activeSingleAbortController.abort(); } catch(e) {}
                }
                window.activeSingleAbortController = new AbortController();

                const dict = I18N[currentLang] || I18N.bn;
                const formData = new FormData(form);

                // Resolve active file from input or memory
                let activeFile = (fileInput.files && fileInput.files.length > 0) ? fileInput.files[0] : rawOriginalFile;

                if (!activeFile) {
                    showError(currentLang === 'bn' ? 'দয়া করে প্রথমে একটি ধানের পাতার ছবি নির্বাচন করুন।' : 'Please select a rice leaf photo first.');
                    return;
                }

                // Explicitly set 'image' file field in FormData
                try {
                    activeFile = await compressImageFile(activeFile);
                } catch(compErr) {}
                formData.set('image', activeFile);

                if (scannerOverlay) scannerOverlay.classList.add('scanning');
                btnSubmit.disabled = true;
                btnSubmit.classList.remove('analysis-done');
                btnIcon.innerHTML = '<div class="spinner"></div>';
                btnText.textContent = dict.btn_analyzing;

                stateEmpty.style.display = 'none';
                stateResult.classList.remove('active');
                stateLoading.classList.add('active');

                const steps = currentLang === 'bn' ? [
                    'ইমেজ টেন্সর প্রস্তুত করা হচ্ছে (২২৪×২২৪ RGB)...',
                    'পাতার ক্ষত ও প্যাটার্ন বিশ্লেষণ চলছে...',
                    'Grad-CAM এআই দৃষ্টি হিটম্যাপ তৈরি হচ্ছে...',
                    'কৃষিবিজ্ঞান প্রেসক্রিপশন ও ডোজ হিসাব হচ্ছে...'
                ] : [
                    'Preparing image tensor (224×224 RGB)…',
                    'Extracting lesion & vascular features…',
                    'Generating Grad-CAM XAI activation maps…',
                    'Computing agronomic spray dosage…'
                ];
                let stepIdx = 0;
                const stepInterval = setInterval(() => {
                    stepIdx = (stepIdx + 1) % steps.length;
                    loadingStepText.textContent = steps[stepIdx];
                }, 600);

                const controller = new AbortController();
                const fetchTimeout = setTimeout(() => controller.abort(), 90000);

                const fetchPromise = fetch('/', {
                    method: 'POST',
                    body: formData,
                    signal: window.activeSingleAbortController.signal,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'Accept': 'application/json'
                    }
                }).then(async res => {
                    clearTimeout(fetchTimeout);
                    let data;
                    try {
                        data = await res.json();
                    } catch (parseErr) {
                        if (!res.ok) {
                            if (res.status === 429) {
                                throw new Error(currentLang === 'bn'
                                    ? 'একসাথে দ্রুত একাধিক রিকোয়েস্ট আসায় সার্ভার সাময়িক বিরতি নিয়েছে (HTTP 429)। অনুগ্রহ করে ৫-১০ সেকেন্ড অপেক্ষা করে আবার চেষ্টা করুন।'
                                    : 'Too many requests sent in quick succession (HTTP 429). Please wait 5-10 seconds before trying again.');
                            }
                            const is502 = res.status === 502 || res.status === 504;
                            if (is502) {
                                throw new Error(currentLang === 'bn'
                                    ? 'সার্ভার স্লিপ মোড থেকে চালু হচ্ছে বা মেমোরি রিফ্রেশ হচ্ছে (HTTP ' + res.status + ')। অনুগ্রহ করে ২০-৩০ সেকেন্ড অপেক্ষা করে আবার চেষ্টা করুন।'
                                    : 'Server is waking up from sleep or refreshing memory (HTTP ' + res.status + '). Please wait 20-30s and try again.');
                            }
                            throw new Error(currentLang === 'bn'
                                ? `সার্ভার ত্রুটি রিটার্ন করেছে: ${res.status}`
                                : `Server returned error: ${res.status}`);
                        }
                        throw new Error(currentLang === 'bn' ? 'সার্ভার থেকে সঠিক ফরম্যাটে তথ্য পাওয়া যায়নি।' : 'Server returned an invalid response format.');
                    }
                    return data;
                });

                fetchPromise
                .then((data) => {
                    clearInterval(stepInterval);
                    if (scannerOverlay) scannerOverlay.classList.remove('scanning');
                    stateLoading.classList.remove('active');

                    btnSubmit.disabled = false;
                    btnIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/><line x1="11" x2="11" y1="8" y2="14"/><line x1="8" x2="14" y1="11" y2="11"/></svg>';
                    btnText.textContent = dict.btn_analyze;

                    if (data && data.success) {
                        renderResults(data);
                    } else {
                        showError((data && data.error) ? data.error : (currentLang === 'bn' ? 'ছবিটি বিশ্লেষণ করা যায়নি। অন্য একটি পরিষ্কার ছবি দিয়ে চেষ্টা করুন।' : 'Could not analyze image. Please try another clear photo.'));
                        stateEmpty.style.display = 'flex';
                    }
                })
                .catch(err => {
                    clearInterval(stepInterval);
                    if (scannerOverlay) scannerOverlay.classList.remove('scanning');
                    stateLoading.classList.remove('active');
                    btnSubmit.disabled = false;
                    btnSubmit.classList.remove('analysis-done');
                    btnIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/><line x1="11" x2="11" y1="8" y2="14"/><line x1="8" x2="14" y1="11" y2="11"/></svg>';
                    btnText.textContent = dict.btn_analyze;
                    
                    showError(err.name === 'AbortError'
                        ? (currentLang === 'bn' ? 'অনুরোধের সময় শেষ হয়েছে — সার্ভার স্লিপ মোড থেকে চালু হচ্ছে। অনুগ্রহ করে আবার চেষ্টা করুন।' : 'Request timed out — server is waking up. Please try again.')
                        : (err.message || (currentLang === 'bn' ? 'সার্ভারে সংযোগ স্থাপন করা যায়নি।' : 'Could not connect to server.')));
                });
            });

            /* ── Render Diagnostic Results ── */
            function renderResults(data) {
                currentDiseaseData = data.disease_info || {};
                currentTopPredictions = data.top_predictions || [];
                currentConfidence = data.confidence;
                currentPredictionName = data.prediction;

                // Feature 1: GradCAM Heatmap Support
                if (data.gradcam_url) {
                    gradcamImageSrc = data.gradcam_url;
                    viewModePill.classList.add('active');
                    toggleViewMode('orig');
                } else {
                    viewModePill.classList.remove('active');
                }

                // Background preload prescription audio for 0ms instant playback (both male & female)
                try {
                    if (data.prediction && typeof preloadPredictionAudio === 'function') {
                        preloadPredictionAudio(data.prediction, currentLang);
                    }
                } catch (e) {}

                // Real-time report logging to Outbreak Surveillance Geo-Map
                try {
                    if (data.prediction && currentSelectedDistrict) {
                        fetch('/api/outbreak-report', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ district: currentSelectedDistrict, disease: data.prediction })
                        }).then(() => {
                            if (typeof loadOutbreakMapMarkers === 'function') {
                                loadOutbreakMapMarkers(currentOutbreakFilter);
                            }
                        }).catch(()=>{});
                    }
                } catch(e) {}

                const dict = I18N[currentLang] || I18N.bn;

                // Update Submit Button to Analysis Done state
                if (btnSubmit) {
                    btnSubmit.classList.add('analysis-done');
                    btnIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>';
                    btnText.textContent = dict.btn_analysis_done || (currentLang === 'bn' ? '✓ বিশ্লেষণ সম্পন্ন' : '✓ Analysis Complete');
                }

                // Ground-Truth Evaluation Verification
                const evalBanner = document.getElementById('eval-verification-banner');
                const evalTitle  = document.getElementById('eval-banner-title');
                const evalDesc   = document.getElementById('eval-banner-desc');
                const evalIcon   = document.getElementById('eval-banner-icon');

                if (evalBanner) {
                    const expected = data.expected_class || document.getElementById('expected_class')?.value;
                    if (expected && expected.trim() !== '') {
                        const isMatch = (data.prediction.toLowerCase().trim() === expected.toLowerCase().trim());
                        const isBn = currentLang === 'bn';
                        
                        let expName = expected;
                        let predName = isBn ? (currentDiseaseData.name_bn || data.prediction) : data.prediction;
                        
                        const diseaseDb = DISEASE_DB || {};
                        if (isBn && diseaseDb && diseaseDb[expected] && diseaseDb[expected].name_bn) {
                            expName = diseaseDb[expected].name_bn;
                        }

                        evalBanner.style.display = 'flex';
                        if (isMatch) {
                            evalBanner.className = 'eval-verification-banner eval-banner-match';
                            evalIcon.textContent = '✓';
                            evalTitle.textContent = isBn ? '✓ গ্রাউন্ড-ট্রুথ ফলাফল: সঠিক মিল (Match)' : '✓ Ground-Truth Match Confirmed';
                            evalDesc.innerHTML = isBn 
                                ? `আপনার দেওয়া পরিচিতি এবং এআই মডেলের ডায়াগনোসিস উভয়েই <strong>"${predName}"</strong> হিসেবে নির্ভুলভাবে মিলে গেছে।`
                                : `Your expected label and AI vision diagnosis both match: <strong>"${data.prediction}"</strong>.`;
                        } else {
                            evalBanner.className = 'eval-verification-banner eval-banner-mismatch';
                            evalIcon.textContent = '⚠️';
                            evalTitle.textContent = isBn ? '⚠️ গ্রাউন্ড-ট্রুথ ফলাফল: অনুমানে অমিল (Mismatch)' : '⚠️ Ground-Truth Mismatch Detected';
                            evalDesc.innerHTML = isBn
                                ? `আপনার নির্বাচিত অনুমান ছিল <strong>"${expName}"</strong>, কিন্তু এআই মডেলের কম্পিউটার ভিশন বিশ্লেষণ নিশ্চিত করেছে পাতাটি আসলে <strong>"${predName}"</strong> (${data.confidence}% নিশ্চিত)।`
                                : `You expected <strong>"${expName}"</strong>, but AI vision confirmed this leaf is <strong>"${data.prediction}"</strong> (${data.confidence}% confidence).`;
                        }
                    } else {
                        evalBanner.style.display = 'none';
                    }
                }

                resultConfNum.textContent = data.confidence + '%';
                resultProgressBar.style.width = '0%';
                setTimeout(() => {
                    resultProgressBar.style.width = data.confidence + '%';
                }, 80);

                updateResultLanguage(dict);
                calculateDosage();

                stateEmpty.style.display = 'none';
                stateResult.classList.add('active');
            }

            /* ── New Scan / Reset Handler with Smooth Scroll ── */
            if (btnReset) {
                btnReset.addEventListener('click', function () {
                    stateResult.classList.remove('active');
                    resetFileInput();
                    clearErrors();
                    stateEmpty.style.display = 'flex';
                    currentDiseaseData = null;
                    currentTopPredictions = null;
                    stopAudioSpeech();

                    // Smooth scroll up to diagnostic upload card
                    const formElem = document.getElementById('diagnostic-form');
                    if (formElem) {
                        formElem.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                });
            }
        });