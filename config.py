#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import environ
from requests import get as rget

CONFIG_FILE_URL = environ.get('CONFIG_FILE_URL')
try:
    if len(CONFIG_FILE_URL) == 0:
        raise TypeError
    try:
        res = rget(CONFIG_FILE_URL)
        if res.status_code == 200:
            with open('.env', 'wb+') as f:
                f.write(res.content)
        else:
            log_error(f"Failed to download config.env {res.status_code}")
    except Exception as e:
        log_error(f"CONFIG_FILE_URL: {e}")
except:
    pass

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = environ.get("BOT_TOKEN")

# SUDO USERS
SUDO_USER = list(
    map(int, environ.get("SUDO_USER", "").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = environ.get(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to my Personal Assistant Bot",
)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = environ.get("MONGO_DB_URI", None)
