import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # 8808189144:AAG7pcZoC02SeLHBJKPYKPunDGzr6SuzS7k
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
ADMIN_IDS = list(set(map(int, os.getenv("ADMIN_IDS", str(OWNER_ID)).split(","))))
ADMIN_IDS = [OWNER_ID] + [i for i in ADMIN_IDS if i != OWNER_ID]

DB_NAME = os.getenv("DB_NAME", "bot.db")
