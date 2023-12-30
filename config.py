import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","28687973"))
API_HASH = getenv("API_HASH","c377969d25dcee0a496a9c937897591d")
BOT_TOKEN = getenv("BOT_TOKEN","5528905227:AAGVGdhQvW4efvRngj6PBQh_hgYhCQrcgbM")
BOT_USERNAME = getenv("BOT_USERNAME","Music_RoboXBot")
USERNAME = getenv("USERNAME","Music_RoboXBot")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://MusicRoboXBot:3yDvdQqJfWkfQxXP@musicroboxbot.jbt7hzl.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002007767051"))
LOGS = int(getenv("LOGS", "-1001834089738"))
OWNER_ID = int(getenv("OWNER_ID", "5946148765"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","Music X Robot")
ASSUSERNAME = getenv("ASSUSERNAME" , "Mikashaa_Ai")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","mikasaakk")
DEEP_API = getenv("DEEP_API","c8e3d7fc-1f7e-455b-8019-5c1b7f21047a")
OPENAI_KEY = getenv("OPENAI_KEY",None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY","98eb5676-c157-4461-85e4-37f0a7547825")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AbhiMod/DCBOT",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
AM_CHAT = getenv("AM_CHAT","https://t.me/CoderXSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CodersXBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/CoderXSupport")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", "BQAGX0e2FSebtFMbQ75-HRmzpfY59dRDEYnxFdnt06h8wB5tZyMq4QiRAlItUKHggODDk-X6KuNXX_ToTltrkWswTVbT175MbgSEz5zNNUhGrLIPA0LJoFdMEqGFO5TEmFb4tHHQZDrFPmrvGZog3o6412wLiwors5KFoc4qzu7RisP2HUNMIVtb187CWR_b08kdwzvPyT29fbiM4k17t_YDRRwDAZRCMgeHE-SVCCHLVoJjz-apegb6d3YvYNPgS4EVzFBOCTPxIcVS6d6Y7LzYXuboGoi8iYNBHu8h1-8lPV4ao7OmUVrvT9wjzSPbhIN5X44EwEgNQgFE9P5GprmnAAAAAXibKDEA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = ["https://graph.org/file/04bc1c79ebdf6bbb15b05.jpg", "https://graph.org/file/d5da08b65b054e7183ae9.jpg", "https://graph.org/file/941558bfd46ee7f4c805b.jpg", "https://graph.org/file/4e07ecb0b1f68047fef51.jpg", "https://graph.org/file/2311d35739ca433f0b1c9.jpg", "https://graph.org/file/3ccbe5d1b2df1282afff8.jpg", "https://graph.org/file/13e35118f9db15f85d085.jpg"]
PING_IMG_URL = ["https://graph.org/file/04bc1c79ebdf6bbb15b05.jpg", "https://graph.org/file/d5da08b65b054e7183ae9.jpg", "https://graph.org/file/941558bfd46ee7f4c805b.jpg", "https://graph.org/file/4e07ecb0b1f68047fef51.jpg", "https://graph.org/file/2311d35739ca433f0b1c9.jpg", "https://graph.org/file/3ccbe5d1b2df1282afff8.jpg", "https://graph.org/file/13e35118f9db15f85d085.jpg"]
STATS_IMG_URL = ["https://graph.org/file/04bc1c79ebdf6bbb15b05.jpg", "https://graph.org/file/d5da08b65b054e7183ae9.jpg", "https://graph.org/file/941558bfd46ee7f4c805b.jpg", "https://graph.org/file/4e07ecb0b1f68047fef51.jpg", "https://graph.org/file/2311d35739ca433f0b1c9.jpg", "https://graph.org/file/3ccbe5d1b2df1282afff8.jpg", "https://graph.org/file/13e35118f9db15f85d085.jpg"]

PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/48f39202823b358203234.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/4eee6d4a7a1de179ff26d.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/04bc1c79ebdf6bbb15b05.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
