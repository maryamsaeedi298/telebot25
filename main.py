import os
import telebot
from fuzzywuzzy import process

# گرفتن توکن از متغیر محیطی
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# لیست سوالات و پاسخ‌ها (می‌تونی اینو تغییر بدی)
qa_pairs = {
    "سلام": "سلام! چطور میتونم کمکت کنم؟ 😊",
    "خداحافظ": "خدانگهدار! امیدوارم زودتر برگردی. 👋",
    "اسم تو چیه؟": "من یه ربات تلگرام هستم 🤖",
    "ساعت چنده؟": "متأسفم، من هنوز ساعت ندارم! ⏰",
    "چطور می‌توانم به ربات تو دستور بدم؟": "فقط سوالت رو بفرست، من سعی می‌کنم جواب بدم! 😊"
}

# تابعی برای پیدا کردن بهترین تطابق با استفاده از Fuzzy Matching
def get_best_match(user_message):
    best_match, score = process.extractOne(user_message, qa_pairs.keys())
    if score > 60:  # فقط اگه تشابه بالای ۶۰٪ بود جواب بده
        return qa_pairs[best_match]
    else:
        return "متوجه نشدم! لطفاً واضح‌تر بپرس. 🤔"

# هندلر پیام‌ها
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = get_best_match(message.text)
    bot.reply_to(message, response)

# شروع به دریافت پیام‌ها
print("ربات راه‌اندازی شد...")
bot.polling()