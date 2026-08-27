"""
RiceGuard High-Fidelity Neural Text-to-Speech Engine
Powered by Microsoft Edge Neural Voices (Specialized for Authentic Bengali Agricultural Agronomist Persona)
Transforms raw agronomic data and prescriptions into 100% natural, conversational human speech.
Completely eliminates machine artifacts like 'ফুটকি', 'স্ল্যাশ', 'ড্যাশ', 'প্লাস'.
"""

import os
import re
import hashlib
import asyncio
import urllib.request
import urllib.parse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(BASE_DIR, "static", "audio")
CACHE_DIR = os.path.join(AUDIO_DIR, "cache")

os.makedirs(CACHE_DIR, exist_ok=True)

# Complete Neural Voice Registry
VOICE_ALIASES = {
    # Bengali Voices
    "pradeep": "bn-BD-PradeepNeural",        # 👨‍🌾 Male (Bangladesh - Deep & Authoritative)
    "tanishaa": "bn-IN-TanishaaNeural",      # 👩‍⚕️ Female (Expressive, Smooth & Melodic)
    "nabanita": "bn-BD-NabanitaNeural",      # 👩‍💼 Female (Bangladesh - Professional Doctor)
    "bashkar": "bn-IN-BashkarNeural",        # 👨‍💼 Male (Crisp & Energetic)
    # English Voices
    "guy": "en-US-GuyNeural",                # 👨‍💼 Male (US - Natural & Clear)
    "aria": "en-US-AriaNeural",              # 👩‍⚕️ Female (US - Expressive & Warm)
    "christopher": "en-US-ChristopherNeural",# 👨‍🌾 Male (US - Deep)
    "jenny": "en-US-JennyNeural",            # 👩‍💼 Female (US - Friendly)
}

VOICE_MAP = {
    "bn": {
        "male": "bn-BD-PradeepNeural",
        "female": "bn-BD-NabanitaNeural",
        "nabanita": "bn-BD-NabanitaNeural",
        "tanishaa": "bn-IN-TanishaaNeural",
        "pradeep": "bn-BD-PradeepNeural",
        "bashkar": "bn-IN-BashkarNeural",
        "default": "bn-BD-PradeepNeural"
    },
    "en": {
        "male": "en-US-GuyNeural",
        "female": "en-US-AriaNeural",
        "aria": "en-US-AriaNeural",
        "jenny": "en-US-JennyNeural",
        "guy": "en-US-GuyNeural",
        "christopher": "en-US-ChristopherNeural",
        "default": "en-US-GuyNeural"
    }
}

VOICE_RATES = {
    "bn-BD-PradeepNeural": "-2%",
    "bn-BD-NabanitaNeural": "-2%",
    "bn-IN-TanishaaNeural": "-2%",
    "bn-IN-BashkarNeural": "-2%",
    "en-US-GuyNeural": "-2%",
    "en-US-AriaNeural": "-2%",
    "en-US-ChristopherNeural": "-2%",
    "en-US-JennyNeural": "-2%"
}

DIGIT_MAP_BN = {
    '0': 'শূন্য', '1': 'এক', '2': 'দুই', '3': 'তিন', '4': 'চার',
    '5': 'পাঁচ', '6': 'ছয়', '7': 'সাত', '8': 'আট', '9': 'নয়',
    '০': 'শূন্য', '১': 'এক', '২': 'দুই', '৩': 'তিন', '৪': 'চার',
    '৫': 'পাঁচ', '৬': 'ছয়', '৭': 'সাত', '৮': 'আট', '৯': 'নয়'
}


def convert_decimals_to_spoken_bn(text: str) -> str:
    """Replaces decimal dots with pure formal Bengali 'দশমিক' and converts digits to words."""
    text = re.sub(r'(?:০\.৭৫|0\.75)', 'শূন্য দশমিক সাত পাঁচ', text)
    text = re.sub(r'(?:০\.৭|0\.7)', 'শূন্য দশমিক সাত', text)
    text = re.sub(r'(?:০\.৬|0\.6)', 'শূন্য দশমিক ছয়', text)
    text = re.sub(r'(?:০\.৫|0\.5)', 'শূন্য দশমিক পাঁচ', text)
    text = re.sub(r'(?:০\.২৫|0\.25)', 'শূন্য দশমিক দুই পাঁচ', text)
    text = re.sub(r'(?:০\.১|0\.1)', 'শূন্য দশমিক এক', text)
    text = re.sub(r'(?:০\.২|0\.2)', 'শূন্য দশমিক দুই', text)
    text = re.sub(r'(?:০\.৩|0\.3)', 'শূন্য দশমিক তিন', text)
    text = re.sub(r'(?:০\.৪|0\.4)', 'শূন্য দশমিক চার', text)
    text = re.sub(r'(?:০\.৮|0\.8)', 'শূন্য দশমিক আট', text)
    text = re.sub(r'(?:০\.৯|0\.9)', 'শূন্য দশমিক নয়', text)
    text = re.sub(r'(?:১\.৫|1\.5)', 'এক দশমিক পাঁচ', text)
    text = re.sub(r'(?:২\.৫|2\.5)', 'দুই দশমিক পাঁচ', text)
    text = re.sub(r'(?:৩\.৫|3\.5)', 'তিন দশমিক পাঁচ', text)

    def _to_words(match):
        int_part = match.group(1)
        dec_part = match.group(2)
        int_sp = ''.join(DIGIT_MAP_BN.get(d, d) for d in int_part)
        dec_sp = ' '.join(DIGIT_MAP_BN.get(d, d) for d in dec_part)
        return f'{int_sp} দশমিক {dec_sp}'

    text = re.sub(r'([0-9০-৯]+)\.([0-9০-৯]+)', _to_words, text)
    return text


def clean_text_for_speech(text: str, is_bn: bool = True) -> str:
    """
    Transforms mechanical AI/report text into warm, natural, conversational human speech.
    Removes raw symbols, dashes, colons, and expands chemical dosages into fluent Bengali or English.
    """
    if not text:
        return ""

    cleaned = text

    # Strip HTML tags
    cleaned = re.sub(r'<br\s*/?>', ' । ', cleaned)
    cleaned = re.sub(r'</p>', ' । ', cleaned)
    cleaned = re.sub(r'<[^>]+>', ' ', cleaned)
    cleaned = re.sub(r'https?://\S+', '', cleaned)

    emoji_pattern = re.compile(
        "["
        "\U00010000-\U0010ffff"
        "\U00002600-\U000027BF"
        "\U00002300-\U000023FF"
        "\U00002B50-\U00002B55"
        "\U0001F000-\U0001F9FF"
        "]+",
        flags=re.UNICODE
    )
    cleaned = emoji_pattern.sub(' ', cleaned)

    if is_bn:
        cleaned = re.sub(r'\(শীষ ব্লাস্ট\)', ', যাকে শীষ ব্লাস্ট বলে', cleaned)
        cleaned = re.sub(r'\(হপার বার্ন\)', ', যাকে হপার বার্ন বলে', cleaned)
        cleaned = re.sub(r'\(ক্রিসেক\)', ', যাকে ক্রিসেক বলে', cleaned)
        cleaned = re.sub(r'\(AWD পদ্ধতি\)', ', অর্থাৎ পর্যায়ক্রমে জমি ভেজানো ও শুকানো পদ্ধতি', cleaned)
        cleaned = re.sub(r'\(যেমন\s*:\s*([^\)]+)\)', r'যেমন ', cleaned)

        cleaned = re.sub(r'([\d\.]+)\s*গ্রাম\s*/\s*লিটার', r'প্রতি লিটার পানিতে  গ্রাম', cleaned)
        cleaned = re.sub(r'([\d\.]+)\s*মিলি\s*/\s*লিটার', r'প্রতি লিটার পানিতে  মিলি', cleaned)
        cleaned = re.sub(r'([\d\.]+)\s*গ্রাম\s*/\s*কেজি', r'প্রতি কেজি বীজে  গ্রাম', cleaned)
        cleaned = re.sub(r'([\d\.]+)\s*কেজি\s*/\s*বিঘা', r'বিঘা প্রতি  কেজি', cleaned)
        cleaned = re.sub(r'@\s*([\d\.]+)\s*গ্রাম', r'প্রতি লিটারে  গ্রাম', cleaned)
        cleaned = re.sub(r'@\s*([\d\.]+)\s*মিলি', r'প্রতি লিটারে  মিলি', cleaned)
        cleaned = re.sub(r'\s*\+\s*', ' এবং ', cleaned)

        cleaned = re.sub(r'•\s*লক্ষণ\s*:\s*', 'রোগের লক্ষণ হলো, ', cleaned)
        cleaned = re.sub(r'•\s*রাসায়নিক দমন\s*:\s*', 'রাসায়নিক চিকিৎসায়, ', cleaned)
        cleaned = re.sub(r'•\s*প্রতিকার\s*:\s*', 'প্রতিকার হিসেবে, ', cleaned)
        cleaned = re.sub(r'•\s*জরুরি সতর্কতা\s*:\s*', 'বিশেষ সতর্কতা হিসেবে, ', cleaned)
        cleaned = re.sub(r'•\s*পরিচর্যা\s*:\s*', 'মাঠ পরিচর্যার ক্ষেত্রে, ', cleaned)
        cleaned = re.sub(r'•\s*মূল কারণ\s*:\s*', 'রোগের মূল কারণ হলো, ', cleaned)
        cleaned = re.sub(r'•\s*পামরী পোকা\s*:\s*', 'পামরী পোকা দমনে, ', cleaned)
        cleaned = re.sub(r'•\s*মাজরা পোকা\s*:\s*', 'মাজরা পোকা দমনে, ', cleaned)
        cleaned = re.sub(r'•\s*কারেন্ট পোকা\s*:\s*', 'কারেন্ট পোকা দমনে, ', cleaned)
        cleaned = re.sub(r'•\s*ইউরিয়া সতর্কবার্তা\s*:\s*', 'ইউরিয়া ব্যবহারের ক্ষেত্রে, ', cleaned)
        cleaned = re.sub(r'•\s*ইউরিয়া কিস্তি\s*:\s*', 'ইউরিয়া প্রয়োগের কিস্তিতে, ', cleaned)
        cleaned = re.sub(r'•\s*রোগ প্রতিরোধে পটাশ\s*:\s*', 'রোগ প্রতিরোধে পটাশ সারের ক্ষেত্রে, ', cleaned)
        cleaned = re.sub(r'•\s*সেরা সময়\s*:\s*', 'স্প্রে করার সেরা সময় হলো, ', cleaned)
        cleaned = re.sub(r'•\s*বৃষ্টির সতর্কতা\s*:\s*', 'বৃষ্টি সংক্রান্ত সতর্কতা হলো, ', cleaned)
        cleaned = re.sub(r'•\s*বাতাস ও নিরাপত্তা\s*:\s*', 'বাতাস ও নিরাপত্তা নির্দেশিকায়, ', cleaned)
        cleaned = re.sub(r'•\s*', ' ', cleaned)

        cleaned = re.sub(r'\([A-Za-z\s\.,\-]+\)', '', cleaned)
        cleaned = re.sub(r'[\(\)\[\]\*\_\#\`\~]', '', cleaned)
        cleaned = re.sub(r'\s*-\s*', ', ', cleaned)
        cleaned = re.sub(r'[:—]', ', ', cleaned)
        cleaned = re.sub(r'/', ' অথবা ', cleaned)
        cleaned = convert_decimals_to_spoken_bn(cleaned)
    else:
        cleaned = re.sub(r'•\s*Symptoms\s*:\s*', 'As for symptoms, ', cleaned)
        cleaned = re.sub(r'•\s*Chemical Control\s*:\s*', 'Chemical control: ', cleaned)
        cleaned = re.sub(r'•\s*Control\s*:\s*', 'Recommended control: ', cleaned)
        cleaned = re.sub(r'•\s*Crucial Warning\s*:\s*', 'Important warning: ', cleaned)
        cleaned = re.sub(r'•\s*Field Care\s*:\s*', 'Field care: ', cleaned)
        cleaned = re.sub(r'•\s*Root Cause\s*:\s*', 'Root cause: ', cleaned)
        cleaned = re.sub(r'•\s*', ' ', cleaned)
        cleaned = re.sub(r'@', 'at ', cleaned)
        cleaned = re.sub(r'/', ' or ', cleaned)
        cleaned = re.sub(r'[\(\)\[\]\*\_\#\`\~]', '', cleaned)
        cleaned = re.sub(r'[:—\-]', ', ', cleaned)

    cleaned = re.sub(r',\s*,', ',', cleaned)
    cleaned = re.sub(r'।\s*।', '।', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned


async def _synthesize_edge_tts(text: str, voice: str, output_path: str):
    import edge_tts
    rate = VOICE_RATES.get(voice, "-2%")
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch="+0Hz")
    await communicate.save(output_path)


def _google_tts_fallback(text: str, lang: str = "bn") -> bytes:
    words = text.split(" ")
    chunks = []
    curr = ""
    for w in words:
        if len(curr) + len(w) + 1 <= 80:
            curr += (" " + w if curr else w)
        else:
            if curr:
                chunks.append(curr)
            curr = w
    if curr:
        chunks.append(curr)

    combined = b""
    for c in chunks:
        encoded = urllib.parse.quote(c.strip())
        tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded}&tl={lang}&client=tw-ob"
        req = urllib.request.Request(
            tts_url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        )
        with urllib.request.urlopen(req, timeout=6) as response:
            combined += response.read()
    return combined


def generate_speech_audio(text: str, lang: str = "bn", voice: str = None, gender: str = None) -> bytes:
    lang_key = "bn" if (lang and lang.startswith("bn")) else "en"
    clean_text = clean_text_for_speech(text, is_bn=(lang_key == "bn"))
    if not clean_text:
        return b""

    bn_voices = {"pradeep", "tanishaa", "nabanita", "bashkar"}
    en_voices = {"guy", "aria", "christopher", "jenny"}

    if lang_key == "bn":
        if voice and voice.lower() in bn_voices:
            resolved_key = voice.lower()
        elif gender == "female" or (voice and voice.lower() in {"aria", "jenny", "female"}):
            resolved_key = "nabanita"
        else:
            resolved_key = "pradeep"
    else:
        if voice and voice.lower() in en_voices:
            resolved_key = voice.lower()
        elif gender == "female" or (voice and voice.lower() in {"nabanita", "tanishaa", "female"}):
            resolved_key = "aria"
        else:
            resolved_key = "guy"

    selected_voice = VOICE_ALIASES.get(resolved_key, "bn-BD-PradeepNeural" if lang_key == "bn" else "en-US-GuyNeural")

    cache_hash = hashlib.md5(f"{selected_voice}_{clean_text}".encode("utf-8")).hexdigest()
    cache_file = os.path.join(CACHE_DIR, f"{cache_hash}.mp3")

    if os.path.exists(cache_file) and os.path.getsize(cache_file) > 500:
        try:
            with open(cache_file, "rb") as f:
                return f.read()
        except Exception:
            pass

    temp_file = os.path.join(CACHE_DIR, f"temp_{cache_hash}.mp3")
    try:
        try:
            loop = asyncio.get_event_loop()
            if loop.is_closed():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        if loop.is_running():
            import nest_asyncio
            nest_asyncio.apply()
            loop.run_until_complete(_synthesize_edge_tts(clean_text, selected_voice, temp_file))
        else:
            loop.run_until_complete(_synthesize_edge_tts(clean_text, selected_voice, temp_file))

        if os.path.exists(temp_file) and os.path.getsize(temp_file) > 500:
            if os.path.exists(cache_file):
                os.remove(cache_file)
            os.replace(temp_file, cache_file)
            with open(cache_file, "rb") as f:
                return f.read()
    except Exception as edge_err:
        print(f"[RiceGuard TTS] Edge Neural TTS warning ({edge_err}), using fallback.")
        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except Exception:
                pass

    try:
        audio_bytes = _google_tts_fallback(clean_text, lang=lang_key)
        if audio_bytes and len(audio_bytes) > 200:
            with open(cache_file, "wb") as f:
                f.write(audio_bytes)
            return audio_bytes
    except Exception as fallback_err:
        print(f"[RiceGuard TTS] Fallback TTS error: {fallback_err}")

    return b""


def prewarm_common_audio():
    try:
        from src.agri_ai import get_expert_local_response
        topics = ['ব্লাস্ট রোগ', 'পাতা পোড়া', 'বাদামী দাগ', 'খোল পোড়া', 'পামরী পোকা', 'ইউরিয়া নিয়ম', 'স্প্রে সতর্কতা', 'সেচ']
        for t in topics:
            res = get_expert_local_response(t, lang='bn')
            text_bn = res.get('text_bn', '')
            if text_bn:
                generate_speech_audio(text_bn, lang='bn', voice='pradeep')
                generate_speech_audio(text_bn, lang='bn', voice='nabanita')
    except Exception as e:
        print(f"[RiceGuard TTS] Pre-warm notice: {e}")


def start_background_cache_prewarm():
    import threading
    t = threading.Thread(target=prewarm_common_audio, daemon=True)
    t.start()
