from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8966086459:AAEAfckT0-JEa1__yW_DVVMZznnlx6oNqSE"
ADMIN_ID = 5193764458
PHONE = "+7 916 496 18 50"

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("📲 Оплатить по СБП", callback_data='pay')]]
    await update.message.reply_text(
        "👋 Добро пожаловать в WoW!\nНажмите кнопку:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        f"📲 **Оплата по СБП**\n\nПереведите на номер:\n`{PHONE}`\n\n✅ После оплаты напишите /confirm"
    )

async def confirm(update: Update, context):
    user = update.effective_user
    await update.message.reply_text("✅ Заказ принят! Ожидайте.")
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"🛒 НОВЫЙ ЗАКАЗ!\nОт: @{user.username or user.first_name}\n💰 Оплата на {PHONE}"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("confirm", confirm))
app.add_handler(CallbackQueryHandler(button))

if __name__ == "__main__":
    print("✅ БОТ ЗАПУЩЕН 24/7!")
    app.run_polling() 
