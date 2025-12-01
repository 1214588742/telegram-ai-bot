import os
import telebot, requests, urllib.parse

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

u = lambda p: "https://image.pollinations.ai/prompt/" + urllib.parse.quote_plus(p)

@bot.message_handler(func=lambda m: True)
def g(m):
    try:
        img = requests.get(u(m.text)).content
        bot.send_photo(m.chat.id, img, caption=m.text)
    except:
        bot.send_message(m.chat.id, "Xatolik yuz berdi, keyinroq urinib ko‘ring 🙂")

bot.infinity_polling()
