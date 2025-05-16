from telegram import Update, InputFile
 from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
 import os
 
 BOT_TOKEN = '8085650826:AAFrX8l90xyZ-9DL-TN3JthY5Vq4jx4Qne8'
 CHANNEL_USERNAME = '@DBMentor'  # без ссылки, только username
 PDF_PATH = 'guide.pdf'  # Путь к твоему PDF-файлу
 
 async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
     user_id = update.effective_user.id
    try:
         member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
         if member.status in ['member', 'administrator', 'creator']:
             await update.message.reply_text("Спасибо за подписку! Вот твой гайд:")
             with open(PDF_PATH, 'rb') as f:
                 await context.bot.send_document(chat_id=update.effective_chat.id, document=InputFile(f))
 else:
             await update.message.reply_text(f"Пожалуйста, подпишись на канал {CHANNEL_USERNAME} и снова напиши /start")
     except:
         await update.message.reply_text(f"Пожалуйста, подпишись на канал {CHANNEL_USERNAME} и снова напиши /start")
 
 if __name__ == '__main__':
     app = ApplicationBuilder().token(BOT_TOKEN).build()
     app.add_handler(CommandHandler('start', start))
     print("Бот запущен...")
     app.run_polling()
