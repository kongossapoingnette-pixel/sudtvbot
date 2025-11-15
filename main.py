import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler

TOKEN = os.getenv("7972198993:AAGjX-JkKB8Ho_XKj2y0Yb9lVEC1zBJoiiw")
LIENS_CHAINES = [
    "https://t.me/urbainetendances",
    "https://t.me/tech_et_pouvoir",
    "https://t.me/raissa_vente_en_ligne"
]
CHAT_ID = os.getenv("https://t.me/sudinfotv")  

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Salut Ndongo, ton bot est prêt à publier et partager !")

def partager_liens(update: Update, context: CallbackContext):
    message = "📢 Voici mes autres chaînes Telegram :\n" + "\n".join(LIENS_CHAINES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def envoyer_liens_quotidiens():
    bot = Bot(token=7972198993:AAGjX-JkKB8Ho_XKj2y0Yb9lVEC1zBJoiiw)
    message = "📢 Mes autres chaînes Telegram :\n" + "\n".join(LIENS_CHAINES)
    bot.send_message(chat_id=CHAT_ID, text=message)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("liens", partager_liens))

scheduler = BackgroundScheduler()
scheduler.add_job(envoyer_liens_quotidiens, 'cron', hour=9, minute=0)
scheduler.start()

updater.start_polling()
