import os
from dotenv import load_dotenv

load_dotenv()


class GlobalConstants:
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    ADMIN_ID = os.getenv('TELEGRAM_ADMIN_CHAT_ID')

    # db connection information

    # MongoDB
    MONGODB_URL = os.getenv('MONGODB_URL')

    # PostgresDB
    PG_HOST = os.getenv('POSTGRES_URL')
    PG_PORT = os.getenv('POSTGRES_PORT')
    PG_DB = os.getenv('POSTGRES_DB')
    PG_USER = os.getenv('POSTGRES_USER')
    PG_PASS = os.getenv('POSTGRES_PASSWORD')

    PG_URL = f'postgresql+asyncpg://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}'
