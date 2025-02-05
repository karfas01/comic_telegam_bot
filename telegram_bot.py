from download_comics import get_comic
from dotenv import load_dotenv
import telegram
import os


def main():
    load_dotenv()

    try:
        tg_bot_key = os.environ["TELEGRAM_BOT_TOKEN"]
        tg_chanal_name = os.environ["CHAT_ID"]
    except KeyError as e:
        raise RuntimeError(f"Обязательная переменная окружения не установлена: {e}")

    bot = telegram.Bot(token=tg_bot_key)
    try:
        get_comic()

        with open("comic_image.png", "rb") as f:
            bot.send_photo(chat_id=tg_chanal_name, photo=f)
    finally:
        os.remove("comic_image.png")


if __name__ == "__main__":
    main()
