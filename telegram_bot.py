from download_comics import get_comic
from dotenv import load_dotenv
import telegram
import os


def main():
    load_dotenv()
    file_name = "comic_image.png"
    tg_bot_key = os.environ["TELEGRAM_BOT_TOKEN"]
    tg_chanal_name = os.environ["CHAT_ID"]

    bot = telegram.Bot(token=tg_bot_key)
    try:
        get_comic(file_name)

        with open(file_name, "rb") as f:
            bot.send_photo(chat_id=tg_chanal_name, photo=f)
    finally:
        os.remove(file_name)


if __name__ == "__main__":
    main()
