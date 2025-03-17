import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)
from typing import Final

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token
TOKEN: Final = '8169844151:AAH1MFP67grFhUMV78n0Fy2tmZpdzreIiwg'
BOT_USERNAME: Final = '@BravoSunEneegy_bot'

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    logger.info("Received /start command")
    keyboard = [
        [KeyboardButton("Mahsulotlar")],
        [KeyboardButton("Hisoblash")],
        [KeyboardButton("Servis")],
        [KeyboardButton("Biz haqimizda")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Iltimos, tanlang:", reply_markup=reply_markup)

# Message handler
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    logger.info(f"Button clicked with text: {text}")

    if text == "Mahsulotlar":
        keyboard = [
            [KeyboardButton("Invertorlar")],
            [KeyboardButton("Panellar")],
            [KeyboardButton("Akomulyatorlar")],
            [KeyboardButton("Aksesuarlar")],
            [KeyboardButton("Orqaga")],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Mahsulotlar:", reply_markup=reply_markup)

    elif text == "Invertorlar":
        try:
            await update.message.reply_photo(
                photo=open("C:/Users/O.Babakulov/Downloads/deye acc.jpg", "rb"),
                caption="""Deye on-grid 3kw = 5600000
Deye on-grid 5kw = 9200000
Deye on-grid 10kw = 12400000""",
            )
            await update.message.reply_photo(
                photo=open("C:/Users/O.Babakulov/Downloads/Solax acc.jpg", "rb"),
                caption="""Solax on-grid 3kw = 5770000
Solax on-grid 5kw = 7720000
Solax on-grid 10kw = 12480000""",
            )
            await update.message.reply_photo(photo=open("C:/Users/O.Babakulov/Downloads/Euronet acc.jpg", "rb"), caption="""Euronet 4.2kw = 5700000
Euronet 6.2kw = 6700000
Euronet 10.2kw = 11700000""",
            )
            await update.message.reply_photo(photo=open("C:/Users/O.Babakulov/Downloads/Huawei acc.jpg", "rb"), caption="""Huawei 5kw = 12480000
Huawei 10kw = 22620000""",
            )
        except FileNotFoundError:
            await update.message.reply_text("Invertorlar rasmlari topilmadi.")

    elif text == "Panellar":
        try:
            await update.message.reply_photo(
                photo=open("C:/Users/O.Babakulov/Downloads/Longi 620W 1365000 panel.jpg", "rb"),
                caption="Longi 620W = 1365000",
            )
            await update.message.reply_photo(photo=open("C:/Users/O.Babakulov/Downloads/Jinko 585W 1293000.jpg", "rb"), caption="Jinko 585W = 1293000")
            await update.message.reply_photo(photo=open("C:/Users/O.Babakulov/Downloads/panel.jpg", "rb"), caption="HY Solar 560W = 1092000")
        except FileNotFoundError:
            await update.message.reply_text("Panellar rasmlari topilmadi.")

    elif text == "Akomulyatorlar":
        try:
            await update.message.reply_photo(
                photo=open("C:/Users/O.Babakulov/Downloads/akomulyator.jpg", "rb"),
                caption="Akomulyatorlar haqida ma'lumot"
            )
        except FileNotFoundError:
            await update.message.reply_text("Akomulyatorlar rasmlari topilmadi.")

    elif text == "Aksesuarlar":
        try:
            await update.message.reply_photo(
                photo=open("C:/Users/O.Babakulov/Downloads/accessories.jpg", "rb"),
                caption="Aksesuarlar haqida ma'lumot"
            )
        except FileNotFoundError:
            await update.message.reply_text("Aksesuarlar rasmlari topilmadi.")

    elif text == "Hisoblash":
        await update.message.reply_photo(photo=open("C:/Users/O.Babakulov/Downloads/hisoblash 1.jpg", "rb"), caption="""Longi 620W x18ta = 24 570 000
Inverter SOLAX = 12 480 000
Aksesuvarlar = 3 950 000
O'rnatib berish bilan = 41 000 000""",
        )
        await update.message.reply_photo(photo=open("C:/Users/O.Babakulov/Downloads/hisoblash2.jpg", "rb"), caption="""HY Solar x9ta = 9 828 000
Inverter Solax = 7 720 000
Aksesuvarlar = 1 450 000
O'rnatib berish bilan = 19 000 000""",
        )
        await update.message.reply_photo(photo=open("C:/Users/O.Babakulov/Downloads/hisoblash3.jpg", "rb"), caption="""Jinko x9ta = 11 637 000
Inverter EuroNet = 6 700 000
Akomulyator Geliviy x4ta = 10 000 000
Aksesuvarlar = 1 663 000
O'rnatib berish bilan = 30 000 000""",
        )
    elif text == "Servis":
        await update.message.reply_photo(photo=open("C:/Users/O.Babakulov/Downloads/Quyosh panellariga texnik xizmat ko'rsatish.jpg", "rb"), caption="""🔧Quyosh panellariga texnik xizmat ko'rsatish""",)
        await update.message.reply_photo(photo=open("C:/Users/O.Babakulov/Downloads/Invertor hamda elektr energiyasi .jpg", "rb"), caption="""🔧Invertor hamda elektr energiyasi samaradorligi xizmatlari""",)
        

    elif text == "Biz haqimizda":
        await update.message.reply_text("""
         ☀️ Har xil turdagi quyosh panellari uchun 10 yildan 25 yilgacha kafolat!
         ✅ Panellarni o'rnatish davomida davlat subsidiyasi hamda YASHIL MAKON dasturining 19,5 foizli kreditlaridan foydalaning
         📞 Biz bilan bog'laning: +998 94 480-88-04 va +998 90 105-00-80
         📍Manzilimiz: Ziyovuddin shaharchasi Ichki Ishlar binosi yonida""")
        await update.message.reply_location(latitude=40.025846034252474, longitude=65.6673097927873)

    elif text == "Orqaga":
        keyboard = [
            [KeyboardButton("Mahsulotlar")],
            [KeyboardButton("Hisoblash")],
            [KeyboardButton("Servis")],
            [KeyboardButton("Biz haqimizda")],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Iltimos, tanlang:", reply_markup=reply_markup)

# Main function
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()