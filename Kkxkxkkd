from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pytube import YouTube

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ابعث رابط تاع يوتيوب باش نعطيك فيديوا.")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    if "youtube.com" not in url and "youtu.be" not in url:
        await update.message.reply_text("ابعث رابط قدقد ولا اخرج عليا.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download(filename="video.mp4")
        await update.message.reply_video(video=open("video.mp4", "rb"), caption=yt.title)
        os.remove("video.mp4")
    except Exception as e:
        await update.message.reply_text(f"خطأ : {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("اصبر شوي", download))

    app.run_polling()
