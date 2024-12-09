
from telethon import events
from JoKeRUB import l313l
import asyncio
import re
from telethon import events
    
import asyncio
import re
from JoKeRUB import l313l
import asyncio
import re
from JoKeRUB import l313l

plugin_category = "extra"
# تعريف المتغير global للتحكم في التكرار
its_Reham = False

@l313l.ar_cmd(pattern="كلمات(\s*(\d+))?$")
async def w3d_joker(event):
    global its_Reham

    # إذا كانت اللعبة لا تعمل، سيبدأ التكرار
    if not its_Reham:
        # التحقق من عدد مرات التكرار (إذا كان موجودًا)
        repetitions = 1  # افتراضيًا، يكون التكرار 1
        if event.pattern_match.group(2):
            repetitions = int(event.pattern_match.group(2))  # إذا كانت هناك قيمة، استخدمها
        
        await event.delete()  # حذف الأمر
        its_Reham = True

        # إرسال رسالة البداية
        start_message = await event.client.send_message(event.chat_id, f"تم بدء اللعبة! عدد التكرار: {repetitions}")

        for _ in range(repetitions):
            if not its_Reham:  # إذا تم إيقاف اللعبة، نخرج من الحلقة
                break
            if event.is_group:
                # إرسال "كلمات" للمجموعة
                await event.client.send_message(event.chat_id, "كلمات")
                await asyncio.sleep(1)

                # الحصول على آخر رسالة من المجموعة
                aljoker = await event.client.get_messages(event.chat_id, limit=1)
                aljoker = aljoker[0].message  # الرسالة الأولى (الأخيرة)

                try:
                    # استخدام تعبير نمطي لاستخراج الكلمة بين الأقواس
                    match = re.search(r"\((.*?)\)", aljoker)  # البحث عن الكلمة بين الأقواس
                    if match:
                        word = match.group(1).strip()  # الكلمة المستخرجة بين الأقواس (تجاهل المسافات)

                        # إرسال الكلمة الجديدة
                        await event.client.send_message(event.chat_id, f"{word}")
                        await asyncio.sleep(1)
                    else:
                        await event.client.send_message(event.chat_id, "⌔∮ لم أتمكن من استخراج الكلمة بين الأقواس ⚠️")
                
                except Exception as e:
                    # التعامل مع الأخطاء غير المتوقعة
                    await event.client.send_message(event.chat_id, f"⌔∮ حدث خطأ: {str(e)} ⚠️")
        
        # إرسال رسالة بعد الانتهاء من التكرار
        await event.client.send_message(event.chat_id, "تم الانتهاء من التكرار!")
        its_Reham = False  # إيقاف اللعبة بعد الانتهاء من التكرار
    else:
        await event.client.send_message(event.chat_id, "العب بالفعل تعمل!")

# أمر لإيقاف اللعبة
@l313l.ar_cmd(pattern="أوقف")
async def stop_game(event):
    global its_Reham
    its_Reham = False
    await event.client.send_message(event.chat_id, "تم إيقاف اللعبة!")
from JoKeRUB import l313l
import asyncio

plugin_category = "extra"


word_meanings = {
    "strong": "قوي",
    "near": "قريب",
    "car": "سيارة",
    "fix": "اصلاح",
    "flag": "علم",
    "dinner": "عشاء",
    "Leg": "ساق",
    "engineer": "مهندس",
    "nurse": "ممرضة",
    "power": "قوة",
    "lips": "شفاه",
    "head": "راس",
    "identity": "هوية",
    "necessary": "ضروري",
    "garbage": "نفايات",
    "custom": "مخصص",
    "beach": "شاطئ",
    "dress": "فستان",
    "long": "طويل",
    "director": "مخرج",
    "brave": "شجاع",
    "knee": "ركبة",
    "weather": "طقس",
    "mine": "ملكي",
    "worse": "اسوأ",
    "plane": "طائره",
    "finger": "اصبع",
    "wrong": "خطأ",
    "teacher": "معلم",
    "part": "جزء",
    "son": "ابن",
    "termination": "نهاية",
    "poster": "ملصق",
    "again": "مره اخرى",
    "judge": "قاضي",
    "kind": "حنون",
    "artist": "فنان",
    "shirt": "قميص",
    "most": "معظم",
    "inside": "داخل",
    "sour": "حامض",
    "common": "شائع",
    "airport": "مطار",
    "horse": "حصان",
    "Rice": "رز",
    "break": "استراحة",
    "empty": "فارغ",
    "town": "مدينة",
    "gloves": "قفازات",
    "Jeans": "جينز",
    "Cook": "طباخ",
    "bad": "سيء",
    "Funny": "مضحك",
    "early": "مبكر",
    "story": "قصة",
    "king": "ملك",
    "flower": "وردة",
    "hungry": "جائع",
    "feel": "شعور",
    "Tongue": "لسان",
    "Sugar": "سكر",
    "break": "استراحة",
    "Translator": "مترجم",
    "Honey": "عسل",
    "flat": "مسطح",
    "Shoes": "حذاء",
    "Hair": "شعر",
    "original": "الاصلي",
    "spicy": "حار",
    "impossible": "مستحيل",
    "hobby": "هواية",
    "Music": "موسيقى",
    "village": "قرية",
    "Eye": "عين",
    "high": "مرتفع",
    "Detective": "محقق",
    "easy": "سهل",
    "cow": "بقرة",
    "found": "وجد",
    "Programmer": "مبرمج",
    "flower": "زهره",
    "Eggs": "بيض",
    "Happy": "سعيد",
    "goal": "هدف",
    "Snake": "ثعبان",
    "host": "مضيف",
    "every": "كل",
    "dark": "مظلم",
    "end": "نهاية",    
    "earth": "ارض",
    "Leg": "ساق",
    "Disappointed": "خائب الامل",
    "Clerk": "كاتب",
    "dangerous": "خطر",
    "window": "نافذة",
    "bath": "حمام",
    "snow": "ثلج",
    "now": "الان",
    "voice": "صوت",
    "sell": "بيع",
    "Child": "طفل",
    "best": "الافضل",
    "character": "شخصيه",
    "holiday": "عطله",
    "Grandfather": "جد",
    "Actor": "ممثل",
    "sure": "متأكد",
    "Sad": "حزين",
    "salt": "ملح",
    "breakfast": "فطور",
    "key": "مفتاح",
    "Singer": "مغني",
    "door": "باب",
    "global": "عالمي",
    "writing": "كتابه",
    "bed": "سرير",
    "sofa": "كنبه",
    "cat": "قطة",
    "good": "جيد",
    "sun": "شمس",
    "summer": "صيف",
    "Car": "سيارة",
    "send": "ارسال",
    "clean": "نظيف",
    "quick": "سريع",
    "yet": "بعد",
    "Gloves": "قفازات",
    "enough": "يكفي",
    "life": "حياة",
    "situation": "موقف",
    "modern": "حديث",
    "Father": "اب",
    "Cook": "طباخ",
    "book": "كتاب",
    "Sensitive": "حساس",
    "ugly": "قبيح",
    "name": "اسم",
    "Crazy": "مجنون",
    "broken": "مكسور",    
    "Uncle": "عم",
    "hat": "قبعة",
    "solution": "حل",
    "future": "مستقبل",
    "Music": "موسيقى",
    "Producer": "منتج",
    "history": "تاريخ",
    "Sensitive": "حساس",
    "far": "بعيد",
    "Mechanic": "ميكانيكي",
    "mug": "كوب",
    "airport": "مطار",
    "season": "فصل",
    "student": "طالب",
    "simple": "بسيط",
    "different": "مختلف",
    "Designer": "مصمم",
    "grass": "عشب",
    "husband": "زوج",
    "correct": "صحيح",
    "Talented": "موهوب",
    "rich": "غني",
    "calm": "هدوء",
    "joke": "نكتة",
    "law": "قانون",
    "young": "صغير",
    "hotel": "فندق",
    "coat": "معطف",
    "how": "كيف",
    "donate": "تبرع",
    "angry": "غاضب",
    "tea": "شاي",
    "brake": "فرامل",
    "always": "دائما",
    "diet": "حمية",
    "common": "شائع",
    "because": "لان",
    "photograph": "صورة",
    "idea": "فكره",
    "rude": "وقح",
    "empty": "فارغ",
    "dirty": "وصخ",
    "anarchy": "فوضى",
    "carefully": "بحذر",
    "weak": "ضعيف",
    "lawyer": "محامي",
    "sheep": "خروف",
    "way": "طريق",
    "notebook": "دفتر ملاحظات",
    "embarrassed": "محرج",
    "scream": "صراخ",
    "live": "حي",
    "bored": "ملل",
    "free": "حر",
    "fact": "حقيقة",
    "face": "وجه",
    "place": "مكان",
    "happy": "سعيد",
    "worried": "قلق",
    "cap": "قبعة",
    "winter": "شتاء",
    "smart": "ذكي",
    "electric": "كهربائي",
    "under": "تحت",
    "round": "جولة",
    "sorry": "اسف",
    "actor": "ممثل",
    "social": "هنا",
    "newspaper": "جريدة",
    "fish": "سمكة",
    "outside": "خارج",
    "note": "ملاحظه",
    "behind": "خلف",
    "pretty": "جميل",
    "ice": "ثلج",
    "Mother": "ام",
    "Delighted": "مسرور",
    "bomb": "قنبله",
    "Chiken": "دجاج",
    "Father": "اب",
    "anything": "اي اشيء",
    "Shoes": "حذاء",
    "Butter": "زبده",
    "Uncle": "عم",
    "wear": "يرتدي",
    "piece": "قطعه",
    "body": "جسم",
    "doubt": "شك",
    "Crazy": "مجنون",
    "Singer": "مغني",
    "queen": "ملكة"    
    
    }

@l313l.ar_cmd(pattern="انقليزي(\s*(\d+))?$")
async def w3d_joker(event):
    global its_Reham

    # إذا كانت اللعبة لا تعمل، سيبدأ التكرار
    if not its_Reham:
        # التحقق من عدد مرات التكرار (إذا كان موجودًا)
        repetitions = 1  # افتراضيًا، يكون التكرار 1
        if event.pattern_match.group(2):
            repetitions = int(event.pattern_match.group(2))  # إذا كانت هناك قيمة، استخدمها
        
        await event.delete()  # حذف الأمر
        its_Reham = True

        # إرسال رسالة البداية
        start_message = await event.client.send_message(event.chat_id, f"تم بدء اللعبة! عدد التكرار: {repetitions}")

        # التكرار لإرسال كلمة "انقليزي"
        for _ in range(repetitions):
            if not its_Reham:  # إذا تم إيقاف اللعبة، نخرج من الحلقة
                break
            if event.is_group:
                # إرسال "انقليزي" للمجموعة
                await event.client.send_message(event.chat_id, "انقليزي")
                await asyncio.sleep(1)

                # الحصول على آخر رسالة من المجموعة (من المستخدم الذي سيرسل الكلمة)
                aljoker = await event.client.get_messages(event.chat_id, limit=1)
                aljoker = aljoker[0].message  # الرسالة الأولى (الأخيرة)

                try:
                    # استخدام تعبير نمطي لاستخراج الكلمة من الرسالة
                    match = re.search(r"\((.*?)\)", aljoker)  # البحث عن الكلمة بين الأقواس
                    if match:
                        word = match.group(1).strip()  # الكلمة المستخرجة بين الأقواس (تجاهل المسافات)

                        # البحث عن معنى الكلمة في القاموس
                        meaning = word_meanings.get(word.lower())

                        if meaning:
                            await event.client.send_message(event.chat_id, f"{meaning}")
                        else:
                            await event.client.send_message(event.chat_id, f"⌔∮ لم أتمكن من العثور على معنى الكلمة '{word}'")
                    else:
                        await event.client.send_message(event.chat_id, "⌔∮ لم أتمكن من استخراج الكلمة بين الأقواس ⚠️")
                except Exception as e:
                    # التعامل مع الأخطاء غير المتوقعة
                    await event.client.send_message(event.chat_id, f"⌔∮ حدث خطأ: {str(e)} ⚠️")
        
        # إرسال رسالة بعد الانتهاء من التكرار
        await event.client.send_message(event.chat_id, "تم الانتهاء من التكرار!")
        its_Reham = False  # إيقاف اللعبة بعد الانتهاء من التكرار
    else:
        await event.client.send_message(event.chat_id, "العب بالفعل تعمل!")

# أمر لإيقاف اللعبة
@l313l.ar_cmd(pattern="أوقف")
async def stop_game(event):
    global its_Reham
    its_Reham = False
    await event.client.send_message(event.chat_id, "تم إيقاف اللعبة!")

# متغير للتحكم في حالة اللعبة
its_Reham = False
