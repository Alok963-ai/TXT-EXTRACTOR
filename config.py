import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "20288951"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "e8cb5fb7a475b5f5eb3b0ef0e6ca03a8")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "7833842279"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "7833842279").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://kakabots2:dcaxq9OovneKdukM@cluster0.npttjwe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002548493129"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1004883878386")  # Optional here you'll get all logs
