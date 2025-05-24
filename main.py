import telegram
import time

# Замените на токен вашего бота и ID канала
import os
BOT_TOKEN = os.getenv("7972132060:AAEkAa7MQRFFy60fbEC6z6R2hV5Rfwq1JsA")
CHANNEL_ID = @molchaliviyhod
BOT_TOKEN=123456:ABCdefGhIjkLmNopQRStuvWxyZ
bot = telegram.Bot(token=BOT_TOKEN)
from dotenv import load_dotenv
load_dotenv()
# Пример поста
POSTS = [
    "Добро пожаловать на канал! Здесь будет автоматический постинг.",
    "Следите за обновлениями. Новый пост каждое утро!",
    "Знания — сила. Подписывайтесь, чтобы стать сильнее!"
]

def autopost():
    for post in POSTS:
        bot.send_message(chat_id=CHANNEL_ID, text=post)
        time.sleep(86400)  # Постить раз в 24 часа (86400 секунд)

if __name__ == "__main__":
    autopost()
  
