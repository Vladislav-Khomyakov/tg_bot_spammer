## Telegram Bot: Автосообщение под постами канала

Бот автоматически отправляет сообщение под каждый новый пост в канале с кнопкой-ссылкой на чат.

### Требования
- Python 3.10+
- Токен бота из `@BotFather`

### Настройка
1. Создайте `.env` на основе примера:
```bash
cp .env.example .env
# отредактируйте .env и задайте BOT_TOKEN
```
2. Укажите ссылку на чат в `bot/constants.py` (`CHAT_LINK`).
3. Установите зависимости:
```bash
pip install -r requirements.txt
```

### Запуск
```bash
python -m bot.main
```

### Запуск в Docker
1. Собрать образ (через Makefile):
```bash
make docker-build IMAGE=tgbot-spammer TAG=latest
```
2. Запустить контейнер (передайте токен):
```bash
docker run --rm \
  -e BOT_TOKEN=your_token_here \
  tgbot-spammer:latest
```

> Вместо `your_token_here` укажите токен из `@BotFather`. Переменную можно прокинуть и через Docker secrets/compose.

### Настройки Telegram
- Добавьте бота в канал администратором с правом публиковать сообщения.
- Бот слушает посты канала и отвечает под каждым постом сообщением и кнопкой на чат.
