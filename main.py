from flask import Flask, request
import telebot
import random
import os

TOKEN = os.environ.get("8242474574:AAHLjAgfU3NEmhjUIvNrDGjvkz98UYSxYG4", "")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['pick'])
def pick_numbers(message):
    try:
        parts = message.text.split()[1:]
        nums = list(map(int, parts))

        if len(nums) < 5:
            bot.reply_to(message, "حداقل ۵ عدد بده 😊")
            return

        selected = random.sample(nums, 5)
        bot.reply_to(message, "🎲 عددهای انتخاب‌شده:\n" + "، ".join(map(str, selected)))

    except:
        bot.reply_to(message, "فرمت درست:\n/pick عددها...\nمثال:\n/pick 3 7 11 14 22 33 41 50 60")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_data = request.get_data().decode("utf-8")
    bot.process_new_updates([telebot.types.Update.de_json(json_data)])
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is running!", 200

if __name__ == "__main__":
    app.run(port=5000)
