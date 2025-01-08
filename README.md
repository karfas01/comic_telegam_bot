# Мемный Telegram.

Программа создана для получения мемов и парсинг их через telegram-bot в telegram канал.

## Как установить / Требования для работы:

### Для работы требуется:

- Python версии [3.12.1](https://www.python.org/downloads/release/python-3121/) и выше должен быть уже установлен.
Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей воспользуйтель данной комндой:
```
pip install -r requirements.txt
```

- Для работы программы в дерриктории программы должен быть создан файл `.env`, с следующем содержимым:
```
TELEGRAM_BOT_TOKEN="token_telegram_bot"
CHAT_ID="@Telegram_Channel_Name"
```

Чтобы получить token от telegram_bot воспользуйтесь: [BotFather](https://t.me/BotFather) и добавте Telegram бота в telegram канал по [этим](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/) пунктам - настройкам (канала).

## Как пользоваться:

### Для скачивания и отправки комиксов:

- Запустить скрипт:
```
python telegram_bot.py
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).