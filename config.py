# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

import os
import re

# --- Telegram API Credentials from Heroku Config Vars ---
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# --- MongoDB URI from Heroku Config Vars ---
MONGO_URI = os.getenv("MONGO_URI")

# --- Default Settings ---
DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute"   # Options: "mute", "ban"
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex pattern to detect URLs in user bios
URL_PATTERN = re.compile(
    r'(https?://)([a-zA-Z0-9\.\-]+)(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9._%+-]*)?'
)
