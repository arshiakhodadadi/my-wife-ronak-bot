from email import message
from matplotlib import text
import telebot
import random
from config import RONAK_NUMBER

from rentedgirlfriend import RentedGirlfriend

class MyWife:
    def __init__(self):
        self.bot = telebot.TeleBot(token=RONAK_NUMBER)

        self.ai_enabled = False

        self.ai_engine = RentedGirlfriend()

        self.arshia_greetings =  [
            "سلام", "سلااام", "سلامی", "درود", "درود بر تو",
            "سلام چطوری", "سلام خوبی", "سلام حالت چطوره",
            "سلام چه خبر", "سلام چی کار می‌کنی", "سلام اوکی هستی",
            "چطوری", "چطورید", "چطوریی", "چطوری هستی",
            "خوبی", "خوبی؟", "خوبی عزیز",
        ]
        
        self.ronak_greetings = [
            "سلام عزیزم 🙂 خوبی؟",
            "سلام عشقم، حالت چطوره؟",
            "سلام 🙂 دلم برات تنگ شده بود",
        ]

        # 🔥 HANDLER
        @self.bot.message_handler(commands=["start"])
        @self.bot.message_handler(func=lambda message: message.content_type == "text")
        def greeting(message):
            text = message.text

            if not self.ai_enabled:
                if any(word in text for word in self.arshia_greetings):
                    reply = random.choice(self.ronak_greetings)
                    self.bot.reply_to(message, reply)

                self.ai_enabled = True
                return

            reply = self.ai_engine.chat(text)
            self.bot.reply_to(message, reply)

    def talk(self):
        print("It’s time to talk to your love, Ronak 🦥")
        self.bot.infinity_polling(timeout=120)

ronak = MyWife()
ronak.talk()