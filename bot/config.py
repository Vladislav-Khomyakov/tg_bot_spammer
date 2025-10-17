import os
from dotenv import load_dotenv


def load_bot_token() -> str:
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is not set in environment")
    return token
