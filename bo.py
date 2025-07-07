🥰🥰🥰.[CRG]|SpaceHunters, [07/07/2025 21:53]
python-3.10.13

🥰🥰🥰.[CRG]|SpaceHunters, [07/07/2025 22:04]
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7771234555:AAHiQY8MtKVxu30VuQdxbNwmyna6E1UnET8'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🚀 Bienvenido a Metaplus. Invierte y gana 10% diario. Usa /menu para comenzar.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
