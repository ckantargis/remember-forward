#!/usr/bin/env python3
"""
build_site.py — Remember Forward site generator
Run from the project root: python build_site.py
Scans plates/ automatically and writes index.html
"""
import os
import re
from pathlib import Path

ROOT = Path(__file__).parent

# ── KNOWLEDGE PLATE METADATA ─────────────────────────────────────────────────
# filename → (short_title, description)
KNOWLEDGE_META = {
    "plate01_v3_rosetta.svg":            ("Plate 1 — Rosetta Index",         "Pictographic key · Mayan numbers · star map"),
    "plate02_v2_water_fire_shelter.svg": ("Plate 2 — Water · Fire · Shelter","Solar still · bow drill · debris hut"),
    "plate03_v2_agriculture_seeds.svg":  ("Plate 3 — Agriculture &amp; Seeds","Three Sisters · composting · seed saving"),
    "plate04_v2_technology.svg":         ("Plate 4 — Technology Re-foundation","Iron · glass · mathematics · printing"),
    "plate05_v2_governance.svg":         ("Plate 5 — Governance &amp; Ethics","Corruption sequence · golden rule · rights"),
    "plate06_v2_concords_stars.svg":     ("Plate 6 — Ten Concords &amp; Stars","Universal principles · star navigation"),
    "plate07_encoding_communication.svg":("Plate 7 — Encoding &amp; Communication","Binary · Morse · carrier wave · compression"),
    "plate08_physics_of_sound_v2.svg":   ("Plate 8 — Physics of Sound",      "The wave · resonance · the groove"),
    "plate09_audio_playback_guide.svg":  ("Plate 9 — Audio Playback Guide",  "Needle construction · tone arm · groove"),
    "plate10_electrical_phenomena.svg":  ("Plate 10 — Electrical Phenomena", "Charge · capacitor · arc · induction"),
    "plate11_energy_generation.svg":     ("Plate 11 — Energy Generation",    "Water wheel · wind · osmotic · capacitor"),
}

# ── LANGUAGE SERIES METADATA ─────────────────────────────────────────────────
# folder → display info + subseries list
# subseries: (series_num_str, display_name, badge_extra)
LANG_META = {
    "hebrew":   {
        "display": "Hebrew",
        "badge": "4 variants \u00b7 16 plates",
        "note": "right-to-left",
        "subseries": [
            ("09", "Biblical Hebrew"),
            ("10", "Mishnaic Hebrew"),
            ("11", "Yemenite Hebrew"),
            ("12", "Modern Hebrew"),
        ],
    },
    "arabic":        {"display": "Arabic",                   "badge": "4 plates", "note": "right-to-left",
                      "subseries": [("13", "Classical Arabic")]},
    "tamil":         {"display": "Tamil",                    "badge": "4 plates \u00b7 Dravidian",
                      "subseries": [("14", "Classical Tamil")]},
    "sanskrit":      {"display": "Sanskrit",                 "badge": "4 plates \u00b7 Devanagari",
                      "subseries": [("15", "Classical Sanskrit")]},
    "bengali":       {"display": "Bengali",                  "badge": "4 plates \u00b7 abugida",
                      "subseries": [("16", "Modern Bengali")]},
    "mandarin":      {"display": "Mandarin Chinese",         "badge": "4 plates \u00b7 logographic",
                      "subseries": [("17", "Mandarin Chinese")]},
    "japanese":      {"display": "Japanese",                 "badge": "4 plates \u00b7 kana + kanji",
                      "subseries": [("18", "Japanese")]},
    "malay":         {"display": "Malay / Indonesian",       "badge": "4 plates \u00b7 Austronesian",
                      "subseries": [("19", "Malay / Indonesian")]},
    "swahili":       {"display": "Swahili",                  "badge": "4 plates \u00b7 Bantu",
                      "subseries": [("20", "Swahili")]},
    "greek":         {"display": "Greek",                    "badge": "4 plates \u00b7 Hellenic",
                      "subseries": [("21", "Classical / Modern Greek")]},
    "latin":         {"display": "Latin",                    "badge": "4 plates \u00b7 Italic",
                      "subseries": [("22", "Classical Latin")]},
    "persian":       {"display": "Persian / Farsi",          "badge": "4 plates \u00b7 right-to-left", "note": "right-to-left",
                      "subseries": [("23", "Classical Persian")]},
    "russian":       {"display": "Russian",                  "badge": "4 plates \u00b7 Cyrillic",
                      "subseries": [("24", "Russian")]},
    "hindi":         {"display": "Hindi",                    "badge": "4 plates \u00b7 Devanagari",
                      "subseries": [("25", "Hindi")]},
    "spanish":       {"display": "Spanish",                  "badge": "4 plates \u00b7 Romance",
                      "subseries": [("26", "Spanish")]},
    "portuguese":    {"display": "Portuguese",               "badge": "4 plates \u00b7 Romance",
                      "subseries": [("27", "Portuguese")]},
    "french":        {"display": "French",                   "badge": "4 plates \u00b7 Romance",
                      "subseries": [("28", "French")]},
    "hausa":         {"display": "Hausa",                    "badge": "4 plates \u00b7 West Africa",
                      "subseries": [("29", "Hausa")]},
    "yoruba":        {"display": "Yoruba",                   "badge": "4 plates \u00b7 tonal \u00b7 West Africa",
                      "subseries": [("30", "Yoruba")]},
    "amharic":       {"display": "Amharic",                  "badge": "4 plates \u00b7 Ge\u2019ez script",
                      "subseries": [("31", "Amharic")]},
    "somali":        {"display": "Somali",                   "badge": "4 plates \u00b7 Cushitic",
                      "subseries": [("32", "Somali")]},
    "lingala":       {"display": "Lingala",                  "badge": "4 plates \u00b7 Bantu \u00b7 Central Africa",
                      "subseries": [("33", "Lingala")]},
    "tigrinya":      {"display": "Tigrinya",                 "badge": "4 plates \u00b7 Semitic \u00b7 Ge\u2019ez script",
                      "subseries": [("34", "Tigrinya")]},
    "igbo":          {"display": "Igbo",                     "badge": "4 plates \u00b7 Niger-Congo",
                      "subseries": [("35", "Igbo")]},
    "shona":         {"display": "Shona",                    "badge": "4 plates \u00b7 Bantu \u00b7 Southern Africa",
                      "subseries": [("36", "Shona")]},
    "zulu":          {"display": "Zulu",                     "badge": "4 plates \u00b7 Nguni Bantu",
                      "subseries": [("37", "Zulu")]},
    "vietnamese":    {"display": "Vietnamese",               "badge": "4 plates \u00b7 tonal",
                      "subseries": [("38", "Vietnamese")]},
    "thai":          {"display": "Thai",                     "badge": "4 plates \u00b7 tonal \u00b7 abugida",
                      "subseries": [("39", "Thai")]},
    "burmese":       {"display": "Burmese",                  "badge": "4 plates \u00b7 Mon-Khmer",
                      "subseries": [("40", "Burmese")]},
    "lao":           {"display": "Lao",                      "badge": "4 plates \u00b7 tonal \u00b7 Tai-Kadai",
                      "subseries": [("41", "Lao")]},
    "tagalog":       {"display": "Tagalog / Filipino",       "badge": "4 plates \u00b7 Austronesian",
                      "subseries": [("42", "Tagalog")]},
    "javanese":      {"display": "Javanese",                 "badge": "4 plates \u00b7 Austronesian",
                      "subseries": [("43", "Javanese")]},
    "sinhala":       {"display": "Sinhala",                  "badge": "4 plates \u00b7 Indo-Aryan",
                      "subseries": [("44", "Sinhala")]},
    "tok-pisin":     {"display": "Tok Pisin",                "badge": "4 plates \u00b7 Creole \u00b7 Pacific",
                      "subseries": [("45", "Tok Pisin")]},
    "quechua":       {"display": "Quechua",                  "badge": "4 plates \u00b7 Andean",
                      "subseries": [("46", "Quechua")]},
    "nahuatl":       {"display": "Nahuatl",                  "badge": "4 plates \u00b7 Mesoamerican",
                      "subseries": [("47", "Classical Nahuatl")]},
    "english":       {"display": "English",                  "badge": "4 plates \u00b7 Germanic",
                      "subseries": [("48", "English")]},
    "dutch":         {"display": "Dutch",                    "badge": "4 plates \u00b7 Germanic",
                      "subseries": [("49", "Dutch")]},
    "korean":        {"display": "Korean",                   "badge": "4 plates \u00b7 Hangul",
                      "subseries": [("50", "Korean")]},
    "turkish":       {"display": "Turkish",                  "badge": "4 plates \u00b7 Turkic",
                      "subseries": [("51", "Turkish")]},
    "german":        {"display": "German",                   "badge": "4 plates \u00b7 Germanic",
                      "subseries": [("52", "German")]},
    "punjabi":       {"display": "Punjabi",                  "badge": "4 plates \u00b7 Gurmukhi script",
                      "subseries": [("53", "Punjabi")]},
    "urdu":          {"display": "Urdu",                     "badge": "4 plates \u00b7 right-to-left", "note": "right-to-left",
                      "subseries": [("54", "Urdu")]},
    "pashto":        {"display": "Pashto",                   "badge": "4 plates \u00b7 right-to-left", "note": "right-to-left",
                      "subseries": [("55", "Pashto")]},
    "tibetan":       {"display": "Tibetan",                  "badge": "4 plates \u00b7 Tibetan script",
                      "subseries": [("56", "Classical Tibetan")]},
    "mongolian":     {"display": "Mongolian",                "badge": "4 plates \u00b7 traditional script",
                      "subseries": [("57", "Mongolian")]},
    "khmer":         {"display": "Khmer",                    "badge": "4 plates \u00b7 Austroasiatic",
                      "subseries": [("58", "Khmer")]},
    "hawaiian":      {"display": "Hawaiian",                 "badge": "4 plates \u00b7 Polynesian",
                      "subseries": [("59", "Hawaiian")]},
    "egyptian-arabic": {"display": "Egyptian Arabic",        "badge": "4 plates \u00b7 dialect", "note": "right-to-left",
                        "subseries": [("60", "Egyptian Arabic")]},
    "egyptian":      {"display": "Ancient Egyptian",         "badge": "4 plates \u00b7 hieroglyphs",
                      "subseries": [("61", "Classical Egyptian")]},
    "asl":           {"display": "ASL",                      "badge": "4 plates \u00b7 sign language",
                      "subseries": [("62", "American Sign Language")]},
    "bsl":           {"display": "BSL",                      "badge": "4 plates \u00b7 sign language",
                      "subseries": [("63", "British Sign Language")]},
    "lsf":           {"display": "LSF",                      "badge": "4 plates \u00b7 sign language \u00b7 France",
                      "subseries": [("64", "Langue des Signes Fran\u00e7aise")]},
    "csl":           {"display": "CSL",                      "badge": "4 plates \u00b7 sign language \u00b7 China",
                      "subseries": [("65", "Chinese Sign Language")]},
    "libras":        {"display": "LIBRAS",                   "badge": "4 plates \u00b7 sign language \u00b7 Brazil",
                      "subseries": [("66", "L\u00edngua Brasileira de Sinais")]},
}

# ── TRANSLATIONS ─────────────────────────────────────────────────────────────
# Top 5 languages by global speakers: English, Mandarin, Hindi, Spanish, Arabic
TRANSLATIONS = {
    "en": {
        "lang_name": "English",
        "dir": "ltr",
        "nav_plates":     "The Plates",
        "nav_containers": "Containers",
        "nav_concords":   "Ten Concords",
        "nav_downloads":  "Downloads",
        "nav_github":     "GitHub",
        "hero_eyebrow":   "Open Source · CC BY-SA 4.0 · Free Forever",
        "hero_subtitle":  "The Patient Message",
        "hero_body":      "A complete open-source system of laser-engraver-ready nickel plate designs for time capsules intended to preserve human knowledge through catastrophic events — readable by a finder 200 to 2,000 years from now with no shared language or cultural context.",
        "hero_tagline":   "Buy it · Build it · Bury it · For someone you will never meet",
        "btn_plates":     "View the Plates",
        "btn_downloads":  "Free Downloads",
        "mission_quote":  '"This was made for you, freely, by people who cared about the future. Use it together. Build something better. Make more capsules for others."',
        "mission_attr":   "The Bridge Phrase — engraved on every plate, in every language",
        "sec_plates":     "The Plates",
        "plates_h2":      "The Patient Message",
        "plates_p1":      "Each plate is a laser-engraver-ready SVG file, 480\u00d7680px portrait format, designed for nickel or stainless steel. Every plate uses only black strokes — no fills, no color — optimized for maximum legibility at any scale and any future reading technology from unaided eye to microscope.",
        "plates_p2":      "The complete set spans eleven knowledge plates covering survival through metaphysics, and four plates per language across fifty human languages — 214 plates total plus analog audio discs.",
        "sub_knowledge":  "Knowledge Plates",
        "sub_languages":  "Language Series",
        "plate_download": "Download SVG",
        "lang_plate_a":   "Script",
        "lang_plate_b":   "Phonology",
        "lang_plate_c":   "Grammar",
        "lang_plate_d":   "Text",
        "sec_containers": "The Capsule Designs",
        "containers_h2":  "Seven Container Tiers",
        "containers_p":   "Any plate set fits any container. The tiers describe survivability and cost, not content. From a clay jar fired with a wood fire to a lead-lined granite vault — every design is fully documented and free to build.",
        "sec_concords":   "The Ten Concords",
        "concords_h2":    "Universal Principles",
        "concords_p":     "Distilled from the convergence points of human civilizations across all recorded history. These are points of agreement, not imposition — discovered independently by people who had no contact with each other, across millennia. Their convergence is the evidence for their validity.",
        "concord_1":  "Every person has inherent worth.",
        "concord_2":  "Measure civilization by its most vulnerable.",
        "concord_3":  "The living world is not a resource.",
        "concord_4":  "Knowledge is a commons.",
        "concord_5":  "Power must be held lightly.",
        "concord_6":  "Cooperation is stronger than competition.",
        "concord_7":  "The future has no voice. Speak for it.",
        "concord_8":  "Beauty is not decoration.",
        "concord_9":  "Grief is the price of love. Pay it.",
        "concord_10": "You are not the first. You will not be the last.",
        "sec_downloads":  "Free Downloads",
        "downloads_h2":   "Everything Is Free",
        "downloads_p":    "Every file in this project is released under CC BY-SA 4.0. Copy them. Translate them. Improve them. Distribute them to everyone. No permission needed. No registration. No cost. The knowledge belongs to whoever finds it.",
        "dl_knowledge":   "Knowledge Plates (SVG)",
        "dl_languages":   "Language Series (SVG)",
        "dl_guides":      "Guides &amp; Documents",
        "dl_founders":    "Founder\u2019s Letter (DOCX)",
        "footer_sub":     "The Patient Message · 2026",
        "footer_copy":    "CC BY-SA 4.0 · Copy freely · Share freely · Improve freely · No permission needed",
        "scroll":         "Scroll",
        "of_plates":      "plates complete",
        "of_series":      "language series",
        "of_total":       "of",
    },
    "zh": {
        "lang_name": "中文",
        "dir": "ltr",
        "nav_plates":     "版片",
        "nav_containers": "容器",
        "nav_concords":   "十协约",
        "nav_downloads":  "下载",
        "nav_github":     "GitHub",
        "hero_eyebrow":   "开源 · CC BY-SA 4.0 · 永久免费",
        "hero_subtitle":  "患者的信息",
        "hero_body":      "一套完整的开源激光雕刻镍板设计系统，用于制作时间胶囊，旨在通过灾难性事件保存人类知识——在200至2000年后，无需共同语言或文化背景即可被发现者阅读。",
        "hero_tagline":   "购买它 · 建造它 · 埋藏它 · 为了一个你永远不会遇见的人",
        "btn_plates":     "查看版片",
        "btn_downloads":  "免费下载",
        "mission_quote":  '"这是为你而制作的，由关心未来的人们免费奉上。共同使用它。建造更好的东西。为他人制作更多胶囊。"',
        "mission_attr":   "桥接短语——刻在每块版片上，以每种语言书写",
        "sec_plates":     "版片",
        "plates_h2":      "患者的信息",
        "plates_p1":      "每块版片都是激光雕刻就绪的SVG文件，480×680px纵向格式，专为镍或不锈钢设计。每块版片仅使用黑色线条——无填充，无颜色——优化了在任何比例和任何未来阅读技术下的最大清晰度。",
        "plates_p2":      "完整套装涵盖十一块知识板，内容从生存技能到形而上学，以及五十种人类语言，每种语言四块版片——共214块版片加模拟音频碟片。",
        "sub_knowledge":  "知识板",
        "sub_languages":  "语言系列",
        "plate_download": "下载 SVG",
        "lang_plate_a":   "文字",
        "lang_plate_b":   "音系",
        "lang_plate_c":   "语法",
        "lang_plate_d":   "文本",
        "sec_containers": "胶囊设计",
        "containers_h2":  "七个容器等级",
        "containers_p":   "任何版片套装适合任何容器。等级描述的是耐用性和成本，而非内容。从用木火烧制的陶罐到铅衬花岗岩保险库——每种设计都有完整文档，可免费建造。",
        "sec_concords":   "十协约",
        "concords_h2":    "普世原则",
        "concords_p":     "从人类文明各文化的共同点中提炼而来，横跨有记录的全部历史。这些是共识点，而非强加——由彼此没有联系的人在数千年中独立发现。它们的汇合是其有效性的证据。",
        "concord_1":  "每个人都有固有的价值。",
        "concord_2":  "以最脆弱者衡量文明。",
        "concord_3":  "生命世界不是资源。",
        "concord_4":  "知识是公共财产。",
        "concord_5":  "权力必须轻持。",
        "concord_6":  "合作强于竞争。",
        "concord_7":  "未来没有声音。为它发声。",
        "concord_8":  "美不是装饰。",
        "concord_9":  "悲伤是爱的代价。付出它。",
        "concord_10": "你不是第一个。你不会是最后一个。",
        "sec_downloads":  "免费下载",
        "downloads_h2":   "一切免费",
        "downloads_p":    "本项目中的每个文件都在CC BY-SA 4.0下发布。复制它们。翻译它们。改进它们。向所有人分发它们。无需许可。无需注册。无需费用。知识属于发现它的人。",
        "dl_knowledge":   "知识版片（SVG）",
        "dl_languages":   "语言系列（SVG）",
        "dl_guides":      "指南与文件",
        "dl_founders":    "创始人信函（DOCX）",
        "footer_sub":     "患者的信息 · 2026",
        "footer_copy":    "CC BY-SA 4.0 · 自由复制 · 自由分享 · 自由改进 · 无需许可",
        "scroll":         "滚动",
        "of_plates":      "块版片已完成",
        "of_series":      "种语言系列",
        "of_total":       "共",
    },
    "hi": {
        "lang_name": "हिन्दी",
        "dir": "ltr",
        "nav_plates":     "प्लेटें",
        "nav_containers": "कंटेनर",
        "nav_concords":   "दस सहमतियाँ",
        "nav_downloads":  "डाउनलोड",
        "nav_github":     "GitHub",
        "hero_eyebrow":   "ओपन सोर्स · CC BY-SA 4.0 · सदा निःशुल्क",
        "hero_subtitle":  "धैर्यपूर्ण संदेश",
        "hero_body":      "लेज़र-एनग्रेवर के लिए तैयार निकेल प्लेट डिज़ाइन की एक पूर्ण ओपन-सोर्स प्रणाली, जो विनाशकारी घटनाओं के माध्यम से मानव ज्ञान को संरक्षित करने के लिए बनाई गई है — बिना किसी साझा भाषा या सांस्कृतिक संदर्भ के 200 से 2,000 वर्ष बाद खोजकर्ता द्वारा पढ़ने योग्य।",
        "hero_tagline":   "खरीदें · बनाएं · दफनाएं · किसी ऐसे व्यक्ति के लिए जिससे आप कभी नहीं मिलेंगे",
        "btn_plates":     "प्लेटें देखें",
        "btn_downloads":  "निःशुल्क डाउनलोड",
        "mission_quote":  '"यह आपके लिए बनाया गया था, उन लोगों द्वारा निःशुल्क जो भविष्य की परवाह करते थे। इसे मिलकर उपयोग करें। कुछ बेहतर बनाएं। दूसरों के लिए और कैप्सूल बनाएं।"',
        "mission_attr":   "सेतु वाक्यांश — हर प्लेट पर, हर भाषा में उत्कीर्ण",
        "sec_plates":     "प्लेटें",
        "plates_h2":      "धैर्यपूर्ण संदेश",
        "plates_p1":      "प्रत्येक प्लेट एक लेज़र-एनग्रेवर-तैयार SVG फ़ाइल है, 480×680px पोर्ट्रेट प्रारूप में, निकेल या स्टेनलेस स्टील के लिए डिज़ाइन की गई। हर प्लेट केवल काले स्ट्रोक का उपयोग करती है — कोई भराव नहीं, कोई रंग नहीं — किसी भी पैमाने और किसी भी भविष्य की पठन तकनीक में अधिकतम सुपाठ्यता के लिए अनुकूलित।",
        "plates_p2":      "पूर्ण सेट में जीवन रक्षा से आध्यात्मिकता तक के ग्यारह ज्ञान प्लेट और पचास मानव भाषाओं में प्रति भाषा चार प्लेट शामिल हैं — कुल 214 प्लेट और एनालॉग ऑडियो डिस्क।",
        "sub_knowledge":  "ज्ञान प्लेटें",
        "sub_languages":  "भाषा श्रृंखला",
        "plate_download": "SVG डाउनलोड करें",
        "lang_plate_a":   "लिपि",
        "lang_plate_b":   "स्वरविज्ञान",
        "lang_plate_c":   "व्याकरण",
        "lang_plate_d":   "पाठ",
        "sec_containers": "कैप्सूल डिज़ाइन",
        "containers_h2":  "सात कंटेनर स्तर",
        "containers_p":   "कोई भी प्लेट सेट किसी भी कंटेनर में फिट होता है। स्तर जीवित रहने की क्षमता और लागत का वर्णन करते हैं, सामग्री का नहीं। लकड़ी की आग में पकी मिट्टी की जार से लेकर सीसे से पंक्तिबद्ध ग्रेनाइट तिजोरी तक — हर डिज़ाइन पूरी तरह से दस्तावेज़ीकृत और निःशुल्क निर्माण योग्य है।",
        "sec_concords":   "दस सहमतियाँ",
        "concords_h2":    "सार्वभौमिक सिद्धांत",
        "concords_p":     "सभी दर्ज इतिहास में मानव सभ्यताओं के अभिसरण बिंदुओं से आसवित। ये सहमति के बिंदु हैं, थोपने के नहीं — सहस्राब्दियों में ऐसे लोगों द्वारा स्वतंत्र रूप से खोजे गए जिनका एक दूसरे से कोई संपर्क नहीं था। उनका अभिसरण उनकी वैधता का प्रमाण है।",
        "concord_1":  "प्रत्येक व्यक्ति में अंतर्निहित मूल्य है।",
        "concord_2":  "सभ्यता को उसके सबसे कमज़ोर से मापें।",
        "concord_3":  "जीवित संसार एक संसाधन नहीं है।",
        "concord_4":  "ज्ञान एक सार्वजनिक संपत्ति है।",
        "concord_5":  "शक्ति को हल्के से धारण करना चाहिए।",
        "concord_6":  "सहयोग प्रतिस्पर्धा से अधिक शक्तिशाली है।",
        "concord_7":  "भविष्य की कोई आवाज़ नहीं है। उसके लिए बोलो।",
        "concord_8":  "सौंदर्य सजावट नहीं है।",
        "concord_9":  "दुख प्यार की कीमत है। इसे चुकाओ।",
        "concord_10": "तुम पहले नहीं हो। तुम आखिरी नहीं होगे।",
        "sec_downloads":  "निःशुल्क डाउनलोड",
        "downloads_h2":   "सब कुछ निःशुल्क है",
        "downloads_p":    "इस प्रोजेक्ट की हर फ़ाइल CC BY-SA 4.0 के तहत जारी की गई है। उन्हें कॉपी करें। उनका अनुवाद करें। उन्हें बेहतर बनाएं। सभी को वितरित करें। कोई अनुमति नहीं चाहिए। कोई पंजीकरण नहीं। कोई शुल्क नहीं। ज्ञान उसका है जो इसे खोजे।",
        "dl_knowledge":   "ज्ञान प्लेटें (SVG)",
        "dl_languages":   "भाषा श्रृंखला (SVG)",
        "dl_guides":      "मार्गदर्शिकाएँ और दस्तावेज़",
        "dl_founders":    "संस्थापक का पत्र (DOCX)",
        "footer_sub":     "धैर्यपूर्ण संदेश · 2026",
        "footer_copy":    "CC BY-SA 4.0 · स्वतंत्र रूप से कॉपी करें · स्वतंत्र रूप से साझा करें · स्वतंत्र रूप से सुधारें · कोई अनुमति नहीं चाहिए",
        "scroll":         "स्क्रॉल",
        "of_plates":      "प्लेटें पूर्ण",
        "of_series":      "भाषा श्रृंखलाएँ",
        "of_total":       "में से",
    },
    "es": {
        "lang_name": "Español",
        "dir": "ltr",
        "nav_plates":     "Las Placas",
        "nav_containers": "Contenedores",
        "nav_concords":   "Los Diez Concordes",
        "nav_downloads":  "Descargas",
        "nav_github":     "GitHub",
        "hero_eyebrow":   "Código Abierto · CC BY-SA 4.0 · Gratis para Siempre",
        "hero_subtitle":  "El Mensaje Paciente",
        "hero_body":      "Un sistema completo de código abierto de diseños de placas de níquel listas para grabado láser, para cápsulas del tiempo destinadas a preservar el conocimiento humano a través de eventos catastróficos — legible por quien lo encuentre en 200 a 2,000 años sin ningún lenguaje o contexto cultural compartido.",
        "hero_tagline":   "Cómpralo · Constrúyelo · Entiérralo · Para alguien que nunca conocerás",
        "btn_plates":     "Ver las Placas",
        "btn_downloads":  "Descargas Gratuitas",
        "mission_quote":  '"Esto fue hecho para ti, gratuitamente, por personas que se preocuparon por el futuro. Úsalo juntos. Construye algo mejor. Haz más cápsulas para otros."',
        "mission_attr":   "La Frase Puente — grabada en cada placa, en cada idioma",
        "sec_plates":     "Las Placas",
        "plates_h2":      "El Mensaje Paciente",
        "plates_p1":      "Cada placa es un archivo SVG listo para grabado láser, formato vertical 480×680px, diseñado para níquel o acero inoxidable. Cada placa usa solo trazos negros — sin rellenos, sin color — optimizado para máxima legibilidad a cualquier escala y cualquier tecnología futura de lectura.",
        "plates_p2":      "El conjunto completo abarca once placas de conocimiento que cubren desde supervivencia hasta metafísica, y cuatro placas por idioma en cincuenta idiomas humanos — 214 placas en total más discos de audio analógico.",
        "sub_knowledge":  "Placas de Conocimiento",
        "sub_languages":  "Series de Idiomas",
        "plate_download": "Descargar SVG",
        "lang_plate_a":   "Escritura",
        "lang_plate_b":   "Fonología",
        "lang_plate_c":   "Gramática",
        "lang_plate_d":   "Texto",
        "sec_containers": "Los Diseños de Cápsulas",
        "containers_h2":  "Siete Niveles de Contenedor",
        "containers_p":   "Cualquier conjunto de placas cabe en cualquier contenedor. Los niveles describen durabilidad y costo, no contenido. Desde un jarro de arcilla cocida con fuego de madera hasta una bóveda de granito forrada de plomo — cada diseño está completamente documentado y es libre de construir.",
        "sec_concords":   "Los Diez Concordes",
        "concords_h2":    "Principios Universales",
        "concords_p":     "Destilados de los puntos de convergencia de las civilizaciones humanas a lo largo de toda la historia registrada. Son puntos de acuerdo, no de imposición — descubiertos de forma independiente por personas sin ningún contacto entre sí, a lo largo de milenios. Su convergencia es la evidencia de su validez.",
        "concord_1":  "Cada persona tiene un valor inherente.",
        "concord_2":  "Mide la civilización por sus más vulnerables.",
        "concord_3":  "El mundo vivo no es un recurso.",
        "concord_4":  "El conocimiento es un bien común.",
        "concord_5":  "El poder debe sostenerse con ligereza.",
        "concord_6":  "La cooperación es más fuerte que la competencia.",
        "concord_7":  "El futuro no tiene voz. Habla por él.",
        "concord_8":  "La belleza no es decoración.",
        "concord_9":  "El duelo es el precio del amor. Págalo.",
        "concord_10": "No eres el primero. No serás el último.",
        "sec_downloads":  "Descargas Gratuitas",
        "downloads_h2":   "Todo es Gratis",
        "downloads_p":    "Cada archivo de este proyecto está publicado bajo CC BY-SA 4.0. Cópialos. Tradúcelos. Mejóralos. Distribúyelos a todos. No se necesita permiso. No hay registro. Sin costo. El conocimiento pertenece a quien lo encuentre.",
        "dl_knowledge":   "Placas de Conocimiento (SVG)",
        "dl_languages":   "Series de Idiomas (SVG)",
        "dl_guides":      "Guías y Documentos",
        "dl_founders":    "Carta del Fundador (DOCX)",
        "footer_sub":     "El Mensaje Paciente · 2026",
        "footer_copy":    "CC BY-SA 4.0 · Copia libremente · Comparte libremente · Mejora libremente · Sin permiso necesario",
        "scroll":         "Desplazar",
        "of_plates":      "placas completas",
        "of_series":      "series de idiomas",
        "of_total":       "de",
    },
    "ar": {
        "lang_name": "العربية",
        "dir": "rtl",
        "nav_plates":     "اللوحات",
        "nav_containers": "الحاويات",
        "nav_concords":   "التوافقات العشر",
        "nav_downloads":  "التنزيلات",
        "nav_github":     "GitHub",
        "hero_eyebrow":   "مفتوح المصدر · CC BY-SA 4.0 · مجاني إلى الأبد",
        "hero_subtitle":  "الرسالة الصبورة",
        "hero_body":      "نظام متكامل مفتوح المصدر من تصاميم لوحات النيكل الجاهزة للنقش بالليزر، لكبسولات زمنية تهدف إلى الحفاظ على المعرفة البشرية عبر الكوارث — قابلة للقراءة من قِبل من يجدها بعد 200 إلى 2000 عام دون أي لغة مشتركة أو سياق ثقافي.",
        "hero_tagline":   "اشتره · ابنه · ادفنه · لشخص لن تلتقي به أبدًا",
        "btn_plates":     "عرض اللوحات",
        "btn_downloads":  "تنزيلات مجانية",
        "mission_quote":  '"صُنع هذا لأجلك، مجانًا، من قِبل أشخاص اهتموا بالمستقبل. استخدمه معًا. ابنِ شيئًا أفضل. اصنع المزيد من الكبسولات للآخرين."',
        "mission_attr":   "العبارة الجسر — منقوشة على كل لوحة، بكل لغة",
        "sec_plates":     "اللوحات",
        "plates_h2":      "الرسالة الصبورة",
        "plates_p1":      "كل لوحة هي ملف SVG جاهز للنقش بالليزر، بتنسيق عمودي 480×680 بكسل، مصمم للنيكل أو الفولاذ المقاوم للصدأ. تستخدم كل لوحة خطوطًا سوداء فقط — بلا تعبئة، بلا لون — محسّنة لأقصى قدر من الوضوح على أي مقياس وأي تقنية قراءة مستقبلية.",
        "plates_p2":      "تشمل المجموعة الكاملة إحدى عشرة لوحة معرفية تغطي من البقاء إلى الميتافيزيقا، وأربع لوحات لكل لغة عبر خمسين لغة بشرية — 214 لوحة إجمالًا بالإضافة إلى أقراص صوتية تناظرية.",
        "sub_knowledge":  "لوحات المعرفة",
        "sub_languages":  "سلاسل اللغات",
        "plate_download": "تنزيل SVG",
        "lang_plate_a":   "الكتابة",
        "lang_plate_b":   "الصوتيات",
        "lang_plate_c":   "القواعد",
        "lang_plate_d":   "النص",
        "sec_containers": "تصاميم الكبسولات",
        "containers_h2":  "سبعة مستويات من الحاويات",
        "containers_p":   "أي مجموعة لوحات تناسب أي حاوية. المستويات تصف المتانة والتكلفة، لا المحتوى. من جرة طينية محروقة بنار الحطب إلى قبو جرانيتي مبطن بالرصاص — كل تصميم موثق بالكامل ومجاني للبناء.",
        "sec_concords":   "التوافقات العشر",
        "concords_h2":    "مبادئ كونية",
        "concords_p":     "مقطّرة من نقاط التقاء الحضارات البشرية عبر كل التاريخ المسجّل. هذه نقاط اتفاق لا فرض — اكتشفها أشخاص لم يتواصلوا مع بعضهم بشكل مستقل عبر آلاف السنين. تقاطعها هو الدليل على صحتها.",
        "concord_1":  "لكل شخص قيمة متأصلة.",
        "concord_2":  "قِس الحضارة بأكثر ضعفائها.",
        "concord_3":  "العالم الحي ليس موردًا.",
        "concord_4":  "المعرفة ملك مشترك.",
        "concord_5":  "يجب أن تُحمل السلطة بخفة.",
        "concord_6":  "التعاون أقوى من التنافس.",
        "concord_7":  "المستقبل لا صوت له. تحدث عنه.",
        "concord_8":  "الجمال ليس زينة.",
        "concord_9":  "الحزن ثمن الحب. ادفعه.",
        "concord_10": "لست الأول. لن تكون الأخير.",
        "sec_downloads":  "تنزيلات مجانية",
        "downloads_h2":   "كل شيء مجاني",
        "downloads_p":    "كل ملف في هذا المشروع صادر تحت CC BY-SA 4.0. انسخها. ترجمها. حسّنها. وزّعها على الجميع. لا إذن مطلوب. لا تسجيل. بلا تكلفة. المعرفة تنتمي لمن يجدها.",
        "dl_knowledge":   "لوحات المعرفة (SVG)",
        "dl_languages":   "سلاسل اللغات (SVG)",
        "dl_guides":      "الأدلة والوثائق",
        "dl_founders":    "رسالة المؤسس (DOCX)",
        "footer_sub":     "الرسالة الصبورة · 2026",
        "footer_copy":    "CC BY-SA 4.0 · انسخ بحرية · شارك بحرية · حسّن بحرية · لا إذن مطلوب",
        "scroll":         "تمرير",
        "of_plates":      "لوحة مكتملة",
        "of_series":      "سلسلة لغوية",
        "of_total":       "من",
    },
}

# ── CONTAINER TIER DATA ───────────────────────────────────────────────────────
TIERS = [
    ("Tier 0", "Fired Ceramic + Pitch",   "$10 – $30",     "500 – 2,000 years",
     ["Clay, fire, and pine pitch only", "No industrial materials required",
      "Buildable post-catastrophe", "Dead Sea Scroll precedent: 2,000 years"]),
    ("Tier A", "Schedule 80 PVC",         "$75 – $150",    "500 – 1,000 years",
     ["Hardware store build", "Teflon tape + marine epoxy seal",
      "Silica gel + oxygen absorbers", "Maximum household distribution"]),
    ("Tier B", "Titanium Sphere",         "$350 – $600",   "10,000+ years",
     ["Grade 5 Ti-6Al-4V alloy", "Argon atmosphere fill",
      "Viton O-rings, aerogel insulation", "Pyramid cavity at Giza angle"]),
    ("Tier C", "Ocean Capsule",           "$400 – $900",   "2,000+ years at depth",
     ["HDPE hull + zinc sacrificial anodes", "Titanium pressure vessel, 600 atm",
      "Gold-plated plates only", "Unreachable, unjurisdictable"]),
    ("Tier D", "Hastelloy C-276",         "$600 – $1,200", "10,000+ years",
     ["Superalloy for acid environments", "Volcanic, sulfurous, industrial soils",
      "Outperforms titanium in corrosive zones", "Nuclear-grade chemical resistance"]),
    ("Tier E", "Lead-Lined Granite",      "$500 – $1,500", "100,000+ years",
     ["Carved granite box, lead-poured seal", "Fixed institutional archive",
      "Nuclear industry permanence standard", "Inscribe the bridge phrase in the stone"]),
    ("Tier F", "Mountain Archive",        "$2,000+",       "Geological timescale",
     ["Dry cave or lava tube", "Natural environmental sealing",
      "Community maintenance agreement", "GPS + surface marker required"]),
]

# ── AUTO-DISCOVERY ────────────────────────────────────────────────────────────

def discover_knowledge_plates():
    """Return list of (filepath_rel, title, desc) for existing knowledge plates."""
    knowledge_dir = ROOT / "plates" / "knowledge"
    plates = []
    order = list(KNOWLEDGE_META.keys())
    found = {p.name: p for p in knowledge_dir.glob("*.svg")} if knowledge_dir.exists() else {}
    for fname in order:
        if fname in found:
            rel = f"plates/knowledge/{fname}"
            title, desc = KNOWLEDGE_META[fname]
            plates.append((rel, title, desc))
    # Any unknown SVGs not in KNOWLEDGE_META
    for fname, path in sorted(found.items()):
        if fname not in KNOWLEDGE_META:
            rel = f"plates/knowledge/{fname}"
            plates.append((rel, fname.replace(".svg","").replace("_"," ").title(), ""))
    return plates


def discover_language_series():
    """
    Return ordered list of language series dicts:
      { folder, display, badge, note, subseries: [(num, name, plates)] }
    where plates = {letter: filepath_rel}
    """
    lang_dir = ROOT / "plates" / "languages"
    if not lang_dir.exists():
        return []

    result = []
    seen_folders = []

    # Process known languages in order
    for folder, meta in LANG_META.items():
        folder_path = lang_dir / folder
        if not folder_path.exists():
            continue
        seen_folders.append(folder)
        svgs = sorted(folder_path.glob("*.svg"))
        # Group by subseries number
        series_plates = {}  # num_str → {letter → rel_path}
        for svg in svgs:
            if '_alt' in svg.name:
                continue
            m = re.match(r"plate(\d+)([a-d])", svg.name)
            if m:
                num, letter = m.group(1), m.group(2)
                series_plates.setdefault(num, {})[letter] = f"plates/languages/{folder}/{svg.name}"

        subseries_out = []
        for num, name in meta["subseries"]:
            num_str = num.split("-")[0].lstrip("0") or "0"  # first num
            # Find matching plates (num may be "09" or "09-12")
            matched = {}
            for snum, plates in series_plates.items():
                if snum == num.zfill(2) or snum == num:
                    matched = plates
                    break
            subseries_out.append({"num": num, "name": name, "plates": matched})

        result.append({
            "folder": folder,
            "display": meta["display"],
            "badge": meta["badge"],
            "note": meta.get("note", ""),
            "subseries": subseries_out,
        })

    # Any unknown language folders
    for folder_path in sorted(lang_dir.iterdir()):
        if not folder_path.is_dir():
            continue
        folder = folder_path.name
        if folder in seen_folders:
            continue
        svgs = sorted(folder_path.glob("*.svg"))
        series_plates = {}
        for svg in svgs:
            if '_alt' in svg.name:
                continue
            m = re.match(r"plate(\d+)([a-d])", svg.name)
            if m:
                num, letter = m.group(1), m.group(2)
                series_plates.setdefault(num, {})[letter] = f"plates/languages/{folder}/{svg.name}"
        subseries_out = [{"num": num, "name": folder.title(), "plates": plates}
                         for num, plates in sorted(series_plates.items())]
        total = sum(len(p) for p in series_plates.values())
        result.append({
            "folder": folder,
            "display": folder.title(),
            "badge": f"{total} plates",
            "note": "",
            "subseries": subseries_out,
        })

    return result


def discover_alt_series():
    """
    Return ordered list of alt series dicts:
      { folder, num, display, pairing, plates: {letter: filepath_rel} }
    """
    plate_types = {"script", "phonology", "grammar", "history", "text", "notation", "cherology"}
    lang_dir = ROOT / "plates" / "languages"
    if not lang_dir.exists():
        return []
    result = []
    for folder_path in sorted(lang_dir.iterdir()):
        if not folder_path.is_dir():
            continue
        folder = folder_path.name
        alts = sorted(folder_path.glob("*_alt.svg"))
        if not alts:
            continue
        series_dict = {}
        for svg in alts:
            m = re.match(r"plate(\d+)([a-d])_(.+)_alt\.svg$", svg.name)
            if not m:
                continue
            num, letter, middle = m.group(1), m.group(2), m.group(3)
            parts = middle.split("_")
            while parts and parts[-1] in plate_types:
                parts.pop()
            folder_norm = folder.replace("-", "_")
            joined = "_".join(parts)
            if joined.startswith(folder_norm + "_"):
                raw_secondary = joined[len(folder_norm) + 1:].replace("_", " ")
                secondary = raw_secondary.upper() if len(raw_secondary.replace(" ", "")) <= 4 else raw_secondary.title()
                primary = LANG_META.get(folder, {}).get("display", folder_norm.replace("_", " ").title())
            else:
                secondary = parts[-1].upper() if len(parts[-1]) <= 4 else parts[-1].replace("_", " ").title()
                primary = " ".join(parts[:-1]).replace("_", " ").title() or LANG_META.get(folder, {}).get("display", "")
            pairing = f"{primary} / {secondary}"
            if num not in series_dict:
                series_dict[num] = {"pairing": pairing, "plates": {}}
            series_dict[num]["plates"][letter] = f"plates/languages/{folder}/{svg.name}"
        meta = LANG_META.get(folder, {})
        display = meta.get("display", folder.replace("-", " ").title())
        for num, data in sorted(series_dict.items()):
            result.append({
                "folder": folder,
                "num": num,
                "display": display,
                "pairing": data["pairing"],
                "plates": data["plates"],
            })
    return result


def count_plates(knowledge, languages):
    k_count = len(knowledge)
    l_count = sum(
        sum(len(sub["plates"]) for sub in series["subseries"])
        for series in languages
    )
    series_count = len(languages)
    # Count each complete subseries as a language series
    subseries_count = sum(len(s["subseries"]) for s in languages)
    return k_count, l_count, k_count + l_count, series_count


# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
  :root {
    --gold: #c8a96e;
    --gold-light: #e8c98a;
    --gold-pale: #f5eacc;
    --dark: #0d0d0b;
    --dark-mid: #161610;
    --dark-surface: #1e1e17;
    --dark-raised: #252520;
    --text: #ddd3b4;
    --text-dim: #b0a080;
    --text-faint: #7a7060;
    --rule: #2a2920;
    --accent: #9b7c3a;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }

  body {
    background: var(--dark);
    color: var(--text);
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 18px;
    line-height: 1.75;
    overflow-x: hidden;
  }

  /* Noise texture */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 1000;
    opacity: 0.5;
  }

  /* ── NAV ── */
  nav {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 500;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 2rem;
    background: rgba(13,13,11,0.92);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid rgba(200,169,110,0.10);
    gap: 1rem;
  }
  .nav-brand {
    font-family: 'Cinzel', serif;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    color: var(--gold);
    text-decoration: none;
    text-transform: uppercase;
    white-space: nowrap;
  }
  .nav-links {
    display: flex;
    gap: 1.5rem;
    list-style: none;
    flex-wrap: wrap;
  }
  .nav-links a {
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--text-dim);
    text-decoration: none;
    text-transform: uppercase;
    transition: color 0.2s;
  }
  .nav-links a:hover { color: var(--gold); }

  /* ── LANGUAGE SWITCHER ── */
  .lang-switcher {
    display: flex;
    gap: 0.4rem;
    align-items: center;
    flex-shrink: 0;
  }
  .lang-btn {
    font-family: 'Cinzel', serif;
    font-size: 0.58rem;
    letter-spacing: 0.1em;
    padding: 0.3em 0.6em;
    background: transparent;
    border: 1px solid var(--text-faint);
    color: var(--text-faint);
    cursor: pointer;
    transition: all 0.2s;
    text-transform: uppercase;
  }
  .lang-btn:hover, .lang-btn.active {
    border-color: var(--gold);
    color: var(--gold);
    background: rgba(200,169,110,0.07);
  }

  /* ── HERO ── */
  .hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 8rem 2rem 5rem;
    position: relative;
    background:
      radial-gradient(ellipse 80% 60% at 50% 30%, rgba(200,169,110,0.07) 0%, transparent 70%),
      radial-gradient(ellipse 40% 40% at 20% 80%, rgba(155,124,58,0.04) 0%, transparent 60%),
      var(--dark);
  }
  .hero::before {
    content: '';
    position: absolute;
    inset: 24px;
    border: 1px solid rgba(200,169,110,0.12);
    pointer-events: none;
  }
  .hero::after {
    content: '';
    position: absolute;
    inset: 30px;
    border: 1px solid rgba(200,169,110,0.05);
    pointer-events: none;
  }

  .hero-eyebrow {
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    letter-spacing: 0.28em;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 2.5rem;
    opacity: 0;
    animation: fadeUp 1s ease 0.2s forwards;
  }
  .hero-title {
    font-family: 'Cinzel', serif;
    font-weight: 900;
    font-size: clamp(3rem, 9vw, 7rem);
    line-height: 1.0;
    letter-spacing: 0.08em;
    color: var(--gold-light);
    text-shadow: 0 0 80px rgba(200,169,110,0.18), 0 2px 4px rgba(0,0,0,0.8);
    margin-bottom: 0.3em;
    opacity: 0;
    animation: fadeUp 1.2s ease 0.4s forwards;
  }
  .hero-subtitle {
    font-family: 'Cinzel', serif;
    font-size: clamp(0.75rem, 1.8vw, 1rem);
    letter-spacing: 0.25em;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 3rem;
    opacity: 0;
    animation: fadeUp 1s ease 0.6s forwards;
  }
  .hero-rule {
    width: 120px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 0 auto 3rem;
    opacity: 0;
    animation: fadeUp 1s ease 0.7s forwards;
  }
  .hero-body {
    max-width: 640px;
    font-size: clamp(1.05rem, 2vw, 1.2rem);
    color: var(--text);
    line-height: 1.85;
    margin-bottom: 3rem;
    opacity: 0;
    animation: fadeUp 1s ease 0.9s forwards;
  }
  .hero-tagline {
    font-family: 'Cinzel', serif;
    font-size: clamp(0.75rem, 1.5vw, 0.9rem);
    letter-spacing: 0.18em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin-bottom: 3rem;
    opacity: 0;
    animation: fadeUp 1s ease 1.0s forwards;
  }
  .hero-cta {
    display: flex;
    gap: 1.2rem;
    flex-wrap: wrap;
    justify-content: center;
    opacity: 0;
    animation: fadeUp 1s ease 1.1s forwards;
  }
  .scroll-hint {
    position: absolute;
    bottom: 2.5rem;
    left: 50%;
    transform: translateX(-50%);
    font-family: 'Cinzel', serif;
    font-size: 0.6rem;
    letter-spacing: 0.3em;
    color: var(--text-faint);
    text-transform: uppercase;
    opacity: 0;
    animation: fadeUp 1s ease 1.4s forwards;
  }
  .scroll-hint::after {
    content: '';
    display: block;
    width: 1px;
    height: 40px;
    background: linear-gradient(to bottom, var(--text-faint), transparent);
    margin: 0.5rem auto 0;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* ── BUTTONS ── */
  .btn {
    font-family: 'Cinzel', serif;
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    padding: 0.9em 2.2em;
    text-decoration: none;
    transition: all 0.3s ease;
  }
  .btn-primary {
    background: transparent;
    color: var(--gold-light);
    border: 1px solid var(--gold);
  }
  .btn-primary:hover {
    background: rgba(200,169,110,0.1);
    box-shadow: 0 0 24px rgba(200,169,110,0.18);
    color: var(--gold-pale);
  }
  .btn-secondary {
    background: transparent;
    color: var(--text-dim);
    border: 1px solid var(--text-faint);
  }
  .btn-secondary:hover {
    color: var(--text);
    border-color: var(--text-dim);
  }

  /* ── MISSION BANNER ── */
  .mission {
    background: var(--dark-surface);
    border-top: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
    padding: 3.5rem 2rem;
    text-align: center;
  }
  .mission-quote {
    font-size: clamp(1.1rem, 2vw, 1.4rem);
    font-style: italic;
    color: var(--text);
    max-width: 720px;
    margin: 0 auto 1rem;
    line-height: 1.75;
  }
  .mission-attr {
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    letter-spacing: 0.22em;
    color: var(--text-dim);
    text-transform: uppercase;
  }

  /* ── SECTIONS ── */
  section {
    max-width: 1100px;
    margin: 0 auto;
    padding: 6rem 2rem;
  }
  .section-label {
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    letter-spacing: 0.32em;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  .section-label::before, .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--rule);
  }
  .section-label::before { max-width: 40px; }

  h2 {
    font-family: 'Cinzel', serif;
    font-size: clamp(1.6rem, 3vw, 2.4rem);
    font-weight: 600;
    color: var(--gold-light);
    letter-spacing: 0.05em;
    margin-bottom: 1.5rem;
    line-height: 1.2;
  }
  h3 {
    font-family: 'Cinzel', serif;
    font-size: 1rem;
    font-weight: 600;
    color: var(--gold);
    letter-spacing: 0.1em;
    margin-bottom: 0.75rem;
    text-transform: uppercase;
  }
  p { margin-bottom: 1.2rem; color: var(--text); }
  p:last-child { margin-bottom: 0; }

  .divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--rule) 20%, var(--gold) 50%, var(--rule) 80%, transparent);
    margin: 0;
  }
  .divider-section {
    text-align: center;
    font-size: 0.8rem;
    letter-spacing: 0.5em;
    color: var(--text-faint);
    padding: 2rem 0;
  }

  /* Scroll reveal */
  .reveal { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }
  .reveal.visible { opacity: 1; transform: translateY(0); }

  /* ── PROGRESS ── */
  .progress-notice {
    font-family: 'Cinzel', serif;
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin: 2.5rem 0 0.75rem;
  }
  .progress-track {
    height: 2px;
    background: var(--dark-raised);
    margin-bottom: 3rem;
    position: relative;
  }
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--accent), var(--gold));
  }
  .subsection-label {
    font-family: 'Cinzel', serif;
    font-size: 0.68rem;
    letter-spacing: 0.2em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin: 3rem 0 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--rule);
  }

  /* ── PLATE CARDS ── */
  .plates-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-bottom: 1rem;
  }
  .plate-card {
    background: var(--dark-surface);
    border: 1px solid var(--rule);
    padding: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    transition: border-color 0.3s;
  }
  .plate-card:hover { border-color: rgba(200,169,110,0.3); }
  .plate-card img {
    width: 100%;
    aspect-ratio: 480/680;
    object-fit: contain;
    background: #fff;
    display: block;
  }
  .plate-card-title {
    font-family: 'Cinzel', serif;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    color: var(--gold);
    text-transform: uppercase;
    margin: 0;
  }
  .plate-card-desc {
    font-size: 0.88rem;
    color: var(--text);
    line-height: 1.5;
    flex: 1;
    margin: 0;
  }
  .plate-card-link {
    font-family: 'Cinzel', serif;
    font-size: 0.62rem;
    letter-spacing: 0.15em;
    color: var(--gold);
    text-decoration: none;
    text-transform: uppercase;
    border-top: 1px solid var(--rule);
    padding-top: 0.5rem;
    margin-top: auto;
    transition: color 0.2s;
  }
  .plate-card-link:hover { color: var(--gold-pale); }

  /* ── LANGUAGE SERIES ── */
  .lang-series-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
  }
  .lang-block {
    background: var(--dark-surface);
    border: 1px solid var(--rule);
    padding: 1.25rem 1.25rem 1rem;
  }
  .lang-block-header {
    display: flex;
    align-items: baseline;
    gap: 0.75rem;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--rule);
  }
  .lang-series-num {
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    color: var(--text-dim);
    letter-spacing: 0.1em;
  }
  .lang-series-name {
    font-family: 'Cinzel', serif;
    font-size: 0.9rem;
    color: var(--gold-light);
    letter-spacing: 0.08em;
    font-weight: 600;
    flex: 1;
  }
  .lang-series-badge {
    font-size: 0.72rem;
    color: var(--text-dim);
    font-style: italic;
  }
  .lang-plate-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.35rem 0;
    border-bottom: 1px solid rgba(42,41,32,0.6);
  }
  .lang-plate-row:last-child { border-bottom: none; }
  .lang-sub-name {
    font-size: 0.82rem;
    color: var(--text);
    flex: 1;
  }
  .lang-plate-link {
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    color: var(--text-dim);
    text-decoration: none;
    border: 1px solid var(--rule);
    padding: 0.25em 0.55em;
    transition: all 0.2s;
  }
  .lang-plate-link:hover { color: var(--gold); border-color: var(--gold); }

  /* ── CONTAINER TIERS ── */
  .tiers-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1.25rem;
    margin-top: 2.5rem;
  }
  .tier-card {
    background: var(--dark-surface);
    border: 1px solid var(--rule);
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  .tier-label {
    font-family: 'Cinzel', serif;
    font-size: 0.62rem;
    letter-spacing: 0.2em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin: 0;
  }
  .tier-name {
    font-family: 'Cinzel', serif;
    font-size: 0.95rem;
    color: var(--gold-light);
    font-weight: 600;
    margin: 0;
    line-height: 1.3;
  }
  .tier-price {
    font-size: 0.85rem;
    color: var(--text-dim);
    margin: 0;
  }
  .tier-list {
    list-style: none;
    margin: 0.5rem 0 0;
    padding: 0;
    flex: 1;
  }
  .tier-list li {
    font-size: 0.85rem;
    color: var(--text);
    padding: 0.2rem 0 0.2rem 1rem;
    position: relative;
    line-height: 1.5;
  }
  .tier-list li::before {
    content: '·';
    position: absolute;
    left: 0;
    color: var(--gold);
  }
  .tier-lifespan {
    font-family: 'Cinzel', serif;
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    color: var(--gold);
    text-transform: uppercase;
    margin: 0.75rem 0 0;
    padding-top: 0.75rem;
    border-top: 1px solid var(--rule);
  }

  /* ── CONCORDS ── */
  .concords-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1rem;
    margin-top: 2.5rem;
  }
  .concord-item {
    background: var(--dark-surface);
    border: 1px solid var(--rule);
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
  .concord-num {
    font-family: 'Cinzel', serif;
    font-size: 1rem;
    color: var(--gold);
    letter-spacing: 0.1em;
    margin: 0;
  }
  .concord-text {
    font-size: 1rem;
    color: var(--text);
    line-height: 1.55;
    margin: 0;
  }

  /* ── DOWNLOADS ── */
  .downloads-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2.5rem;
  }
  .download-group-title {
    font-family: 'Cinzel', serif;
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--rule);
  }
  .download-item {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 0.5rem;
    padding: 0.45rem 0;
    border-bottom: 1px solid rgba(42,41,32,0.5);
  }
  .download-item:last-child { border-bottom: none; }
  .download-name {
    font-size: 0.88rem;
    color: var(--text);
  }
  .download-link {
    font-family: 'Cinzel', serif;
    font-size: 0.62rem;
    letter-spacing: 0.12em;
    color: var(--gold);
    text-decoration: none;
    text-transform: uppercase;
    flex-shrink: 0;
    transition: color 0.2s;
  }
  .download-link:hover { color: var(--gold-pale); }

  /* ── FOOTER ── */
  footer {
    background: var(--dark-mid);
    border-top: 1px solid var(--rule);
    text-align: center;
    padding: 4rem 2rem;
  }
  .footer-title {
    font-family: 'Cinzel', serif;
    font-size: 1.1rem;
    letter-spacing: 0.18em;
    color: var(--gold-light);
    text-transform: uppercase;
    margin-bottom: 0.5rem;
  }
  .footer-sub {
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin-bottom: 1.5rem;
  }
  .footer-links {
    display: flex;
    gap: 1.5rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 1.5rem;
  }
  .footer-links a {
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    color: var(--text-dim);
    text-decoration: none;
    text-transform: uppercase;
    transition: color 0.2s;
  }
  .footer-links a:hover { color: var(--gold); }
  .footer-copy {
    font-size: 0.82rem;
    color: var(--text-faint);
    margin: 0;
  }

  /* ── RESPONSIVE ── */
  @media (max-width: 600px) {
    nav { padding: 0.75rem 1rem; }
    .nav-links { display: none; }
    section { padding: 4rem 1.25rem; }
    .plates-grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); }
    .lang-series-grid { grid-template-columns: 1fr; }
  }
"""

# ── JS ────────────────────────────────────────────────────────────────────────

def build_js(translations):
    """Build the inline JavaScript block."""
    import json
    t_json = json.dumps(translations, ensure_ascii=False, indent=2)
    return f"""
  const TRANSLATIONS = {t_json};

  let currentLang = localStorage.getItem('rf-lang') || 'en';

  function setLang(lang) {{
    if (!TRANSLATIONS[lang]) return;
    currentLang = lang;
    localStorage.setItem('rf-lang', lang);
    const t = TRANSLATIONS[lang];

    // Direction
    document.documentElement.lang = lang;
    document.documentElement.dir = t.dir || 'ltr';

    // All i18n elements
    document.querySelectorAll('[data-i18n]').forEach(el => {{
      const key = el.dataset.i18n;
      if (t[key] !== undefined) el.innerHTML = t[key];
    }});

    // Active button
    document.querySelectorAll('.lang-btn').forEach(btn => {{
      btn.classList.toggle('active', btn.dataset.lang === lang);
    }});
  }}

  // Init
  document.querySelectorAll('.lang-btn').forEach(btn => {{
    btn.addEventListener('click', () => setLang(btn.dataset.lang));
  }});
  setLang(currentLang);

  // Scroll reveal
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {{
    entries.forEach((entry, i) => {{
      if (entry.isIntersecting) {{
        setTimeout(() => entry.target.classList.add('visible'), i * 60);
        observer.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold: 0.08, rootMargin: '0px 0px -30px 0px' }});
  reveals.forEach(el => observer.observe(el));
"""

# ── HTML SECTIONS ─────────────────────────────────────────────────────────────

def nav_html(langs):
    lang_btns = "\n      ".join(
        f'<button class="lang-btn" data-lang="{code}">{t["lang_name"]}</button>'
        for code, t in langs.items()
    )
    return f"""
<nav>
  <a href="#top" class="nav-brand">Remember Forward</a>
  <ul class="nav-links">
    <li><a href="#plates" data-i18n="nav_plates">The Plates</a></li>
    <li><a href="#containers" data-i18n="nav_containers">Containers</a></li>
    <li><a href="#concords" data-i18n="nav_concords">Ten Concords</a></li>
    <li><a href="#downloads" data-i18n="nav_downloads">Downloads</a></li>
    <li><a href="https://github.com/ckantargis/remember-forward" data-i18n="nav_github">GitHub</a></li>
  </ul>
  <div class="lang-switcher">
    {lang_btns}
  </div>
</nav>"""


def hero_html():
    return """
<section class="hero" id="top">
  <p class="hero-eyebrow" data-i18n="hero_eyebrow">Open Source · CC BY-SA 4.0 · Free Forever</p>
  <h1 class="hero-title">Remember<br>Forward</h1>
  <p class="hero-subtitle" data-i18n="hero_subtitle">The Patient Message</p>
  <div class="hero-rule"></div>
  <p class="hero-body" data-i18n="hero_body">A complete open-source system of laser-engraver-ready nickel plate designs for time capsules intended to preserve human knowledge through catastrophic events — readable by a finder 200 to 2,000 years from now with no shared language or cultural context.</p>
  <p class="hero-tagline" data-i18n="hero_tagline">Buy it · Build it · Bury it · For someone you will never meet</p>
  <div class="hero-cta">
    <a href="#plates" class="btn btn-primary" data-i18n="btn_plates">View the Plates</a>
    <a href="#downloads" class="btn btn-secondary" data-i18n="btn_downloads">Free Downloads</a>
  </div>
  <span class="scroll-hint" data-i18n="scroll">Scroll</span>
</section>

<div class="mission">
  <p class="mission-quote" data-i18n="mission_quote">"This was made for you, freely, by people who cared about the future. Use it together. Build something better. Make more capsules for others."</p>
  <p class="mission-attr" data-i18n="mission_attr">The Bridge Phrase — engraved on every plate, in every language</p>
</div>"""


def _alt_blocks_html(alt_series):
    if not alt_series:
        return ""
    blocks = []
    labels = {"a": "Script/Notation", "b": "Phonology/Cherology", "c": "Grammar", "d": "History/Text"}
    for entry in alt_series:
        links = []
        for letter in ["a", "b", "c", "d"]:
            href = entry["plates"].get(letter, "")
            if href:
                links.append(
                    f'<a href="{href}" download class="lang-plate-link" title="{labels[letter]}">'
                    f'{letter.upper()}</a>'
                )
        blocks.append(f"""
    <div class="lang-block reveal">
      <div class="lang-block-header">
        <span class="lang-series-num">{entry["num"]}</span>
        <span class="lang-series-name">{entry["pairing"]}</span>
        <span class="lang-series-badge">alt · 4 plates</span>
      </div>
      <div class="lang-plate-row">
        <span class="lang-sub-name">alternate pairing</span>
        {"".join(links)}
      </div>
    </div>""")
    return "".join(blocks)


def plates_html(knowledge, languages, alt_series=None):
    if alt_series is None:
        alt_series = []
    k_count, l_count, total, series_count = count_plates(knowledge, languages)
    plates_done = k_count + l_count
    pct = round(plates_done / 214 * 100, 1)

    # Knowledge plate cards
    cards = []
    for rel, title, desc in knowledge:
        cards.append(f"""
    <div class="plate-card reveal">
      <img src="{rel}" alt="{title}" loading="lazy">
      <p class="plate-card-title">{title}</p>
      <p class="plate-card-desc">{desc}</p>
      <a href="{rel}" download class="plate-card-link" data-i18n="plate_download">Download SVG</a>
    </div>""")

    # Language blocks
    lang_blocks = []
    for series in languages:
        rows = []
        for sub in series["subseries"]:
            links = []
            for letter in ["a", "b", "c", "d"]:
                href = sub["plates"].get(letter, "")
                if href:
                    title_keys = {"a": "lang_plate_a", "b": "lang_plate_b",
                                  "c": "lang_plate_c", "d": "lang_plate_d"}
                    labels = {"a": "Script", "b": "Phonology", "c": "Grammar", "d": "Text"}
                    links.append(
                        f'<a href="{href}" download class="lang-plate-link" '
                        f'data-i18n-title="{title_keys[letter]}" title="{labels[letter]}">'
                        f'{letter.upper()}</a>'
                    )
            rows.append(f"""
        <div class="lang-plate-row">
          <span class="lang-sub-name">{sub["num"]} · {sub["name"]}</span>
          {"".join(links)}
        </div>""")

        note_html = f' <span class="lang-series-badge">{series["note"]}</span>' if series.get("note") else ""
        lang_blocks.append(f"""
    <div class="lang-block reveal">
      <div class="lang-block-header">
        <span class="lang-series-num">{series["subseries"][0]["num"] if series["subseries"] else ""}</span>
        <span class="lang-series-name">{series["display"]}</span>
        <span class="lang-series-badge">{series["badge"]}</span>
        {note_html}
      </div>
      {"".join(rows)}
    </div>""")

    return f"""
<div class="divider"></div>

<section id="plates">
  <p class="section-label" data-i18n="sec_plates">The Plates</p>
  <h2 data-i18n="plates_h2">The Patient Message</h2>
  <p data-i18n="plates_p1">Each plate is a laser-engraver-ready SVG file, 480×680px portrait format, designed for nickel or stainless steel. Every plate uses only black strokes — no fills, no color — optimized for maximum legibility at any scale and any future reading technology from unaided eye to microscope.</p>
  <p data-i18n="plates_p2">The complete set spans eleven knowledge plates covering survival through metaphysics, and four plates per language across fifty human languages — 214 plates total plus analog audio discs.</p>

  <p class="progress-notice">{plates_done} of 214 plates complete · {series_count} of 50 language series</p>
  <div class="progress-track"><div class="progress-fill" style="width:{pct}%"></div></div>

  <p class="subsection-label" data-i18n="sub_knowledge">Knowledge Plates</p>
  <div class="plates-grid">{"".join(cards)}
  </div>

  <p class="subsection-label" data-i18n="sub_languages">Language Series</p>
  <div class="lang-series-grid">{"".join(lang_blocks)}
  </div>

  <p class="subsection-label">Alternate Language Pairings</p>
  <p style="max-width:680px;margin:0 auto 1.5rem;font-size:0.9rem;opacity:0.75;">Each language series also has four alternate draft plates pairing it with a geographically nearby secondary language (~500 mi radius), showing structural contrast between neighboring writing traditions.</p>
  <div class="lang-series-grid">{_alt_blocks_html(alt_series)}
  </div>
</section>"""


def containers_html():
    cards = []
    for label, name, price, lifespan, items in TIERS:
        lis = "\n".join(f"        <li>{item}</li>" for item in items)
        cards.append(f"""
    <div class="tier-card reveal">
      <p class="tier-label">{label}</p>
      <p class="tier-name">{name}</p>
      <p class="tier-price">{price}</p>
      <ul class="tier-list">
{lis}
      </ul>
      <p class="tier-lifespan">{lifespan}</p>
    </div>""")

    return f"""
<div class="divider-section">· · ·</div>

<section id="containers">
  <p class="section-label" data-i18n="sec_containers">The Capsule Designs</p>
  <h2 data-i18n="containers_h2">Seven Container Tiers</h2>
  <p data-i18n="containers_p">Any plate set fits any container. The tiers describe survivability and cost, not content. From a clay jar fired with a wood fire to a lead-lined granite vault — every design is fully documented and free to build.</p>
  <div class="tiers-grid">{"".join(cards)}
  </div>
</section>"""


def concords_html():
    concords_en = [
        "Every person has inherent worth.",
        "Measure civilization by its most vulnerable.",
        "The living world is not a resource.",
        "Knowledge is a commons.",
        "Power must be held lightly.",
        "Cooperation is stronger than competition.",
        "The future has no voice. Speak for it.",
        "Beauty is not decoration.",
        "Grief is the price of love. Pay it.",
        "You are not the first. You will not be the last.",
    ]
    numerals = ["I","II","III","IV","V","VI","VII","VIII","IX","X"]
    items = []
    for i, (num, text) in enumerate(zip(numerals, concords_en), 1):
        items.append(f"""
    <div class="concord-item reveal">
      <p class="concord-num">{num}</p>
      <p class="concord-text" data-i18n="concord_{i}">{text}</p>
    </div>""")

    return f"""
<div class="divider-section">· · ·</div>

<section id="concords">
  <p class="section-label" data-i18n="sec_concords">The Ten Concords</p>
  <h2 data-i18n="concords_h2">Universal Principles</h2>
  <p data-i18n="concords_p">Distilled from the convergence points of human civilizations across all recorded history. These are points of agreement, not imposition — discovered independently by people who had no contact with each other, across millennia. Their convergence is the evidence for their validity.</p>
  <div class="concords-grid">{"".join(items)}
  </div>
</section>"""


def downloads_html(knowledge, languages):
    # Knowledge downloads
    k_items = []
    for rel, title, _ in knowledge:
        k_items.append(f"""
      <div class="download-item">
        <span class="download-name">{title}</span>
        <a href="{rel}" download class="download-link">SVG</a>
      </div>""")

    # Language downloads
    lang_items = []
    for series in languages:
        for sub in series["subseries"]:
            for letter in ["a","b","c","d"]:
                href = sub["plates"].get(letter, "")
                if href:
                    fname = href.split("/")[-1].replace(".svg","").replace("_"," ")
                    label = {"a":"Script","b":"Phonology","c":"Grammar","d":"Text"}[letter]
                    lang_items.append(f"""
      <div class="download-item">
        <span class="download-name">{series["display"]} — {label}</span>
        <a href="{href}" download class="download-link">SVG</a>
      </div>""")

    return f"""
<div class="divider-section">· · ·</div>

<section id="downloads">
  <p class="section-label" data-i18n="sec_downloads">Free Downloads</p>
  <h2 data-i18n="downloads_h2">Everything Is Free</h2>
  <p data-i18n="downloads_p">Every file in this project is released under CC BY-SA 4.0. Copy them. Translate them. Improve them. Distribute them to everyone. No permission needed. No registration. No cost. The knowledge belongs to whoever finds it.</p>

  <div class="downloads-grid">
    <div class="download-group reveal">
      <p class="download-group-title" data-i18n="dl_knowledge">Knowledge Plates (SVG)</p>
      {"".join(k_items)}
    </div>

    <div class="download-group reveal">
      <p class="download-group-title" data-i18n="dl_languages">Language Series (SVG)</p>
      {"".join(lang_items)}
    </div>

    <div class="download-group reveal">
      <p class="download-group-title" data-i18n="dl_guides">Guides &amp; Documents</p>
      <div class="download-item">
        <span class="download-name" data-i18n="dl_founders">Founder's Letter (DOCX)</span>
        <a href="guides/gd_02_founders_letter.docx" download class="download-link">DOCX</a>
      </div>
    </div>
  </div>
</section>"""


def footer_html():
    return """
<footer>
  <p class="footer-title">Remember Forward</p>
  <p class="footer-sub" data-i18n="footer_sub">The Patient Message · 2026</p>
  <div class="footer-links">
    <a href="#top">Home</a>
    <a href="#plates" data-i18n="nav_plates">The Plates</a>
    <a href="#containers" data-i18n="nav_containers">Containers</a>
    <a href="#downloads" data-i18n="nav_downloads">Downloads</a>
    <a href="https://github.com/ckantargis/remember-forward" data-i18n="nav_github">GitHub</a>
    <a href="guides/gd_02_founders_letter.docx" data-i18n="dl_founders">Founder's Letter</a>
  </div>
  <p class="footer-copy" data-i18n="footer_copy">CC BY-SA 4.0 · Copy freely · Share freely · Improve freely · No permission needed</p>
</footer>"""


# ── MAIN BUILD ────────────────────────────────────────────────────────────────

def build():
    knowledge = discover_knowledge_plates()
    languages = discover_language_series()
    alts = discover_alt_series()
    k_count, l_count, total, series_count = count_plates(knowledge, languages)
    print(f"  Knowledge plates: {k_count}")
    print(f"  Language plates:  {l_count} across {series_count} series")
    print(f"  Alt series:       {len(alts)}")
    print(f"  Total plates:     {total}")

    html = f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Remember Forward — The Patient Message</title>
<meta name="description" content="An open-source system of laser-engraver-ready nickel plate designs for time capsules. Preserve human knowledge through catastrophic events. Buy it. Build it. Bury it.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;900&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
{nav_html(TRANSLATIONS)}
{hero_html()}
{plates_html(knowledge, languages, alts)}
{containers_html()}
{concords_html()}
{downloads_html(knowledge, languages)}
{footer_html()}
<script>
{build_js(TRANSLATIONS)}
</script>
</body>
</html>"""

    out = ROOT / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"\nWrote {out}")
    print(f"Size: {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    print("Building Remember Forward site...")
    build()
    print("Done.")
