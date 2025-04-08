import os
from pyrogram import Client, filters
from yt_dlp import YoutubeDL

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("ytbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("أرسل رابط يوتيوب لتحميل الفيديو.")

@app.on_message(filters.text & ~filters.command(["start"]))
def download_video(client, message):
    url = message.text.strip()
    if "youtube.com" not in url and "youtu.be" not in url:
        message.reply("أرسل رابط يوتيوب فقط.")
        return

    msg = message.reply("جاري التحميل...")
    try:
        ydl_opts = {"outtmpl": "downloads/%(title)s.%(ext)s"}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        message.reply_video(video=filename, caption=info.get("title", ""))
        os.remove(filename)
        msg.delete()
    except Exception as e:
        msg.edit(f"حدث خطأ: {e}")

app.run()