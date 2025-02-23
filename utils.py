import pytz, random, string
from datetime import date, datetime, timedelta
from config import TOKEN_API, TOKEN_URL, TOKEN_VERIFICATION_DURATION_SECONDS
from shortzy import Shortzy

TOKENS = {}
VERIFIED = {}

async def get_verify_shorted_link(link):
    shortzy = Shortzy(api_key=TOKEN_API, base_site=TOKEN_URL)
    link = await shortzy.convert(link)
    return link

async def check_token(bot, userid, token):
    user = await bot.get_users(userid)
    if user.id in TOKENS.keys():
        TKN = TOKENS[user.id]
        if token in TKN.keys():
            is_used = TKN[token]
            if is_used == True:
                return False
            else:
                return True
    else:
        return False

async def get_token(bot, userid, link):
    user = await bot.get_users(userid)
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    TOKENS[user.id] = {token: False}
    link = f"{link}verify-{user.id}-{token}"
    shortened_verify_url = await get_verify_shorted_link(link)
    return str(shortened_verify_url)

async def verify_user(bot, userid, token):
    user = await bot.get_users(userid)
    TOKENS[user.id] = {token: True}
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    expiration = now + timedelta(seconds=TOKEN_VERIFICATION_DURATION_SECONDS)
    VERIFIED[user.id] = expiration.isoformat()

async def check_verification(bot, userid):
    user = await bot.get_users(userid)
    if user.id in VERIFIED.keys():
        expiration_iso = VERIFIED[user.id]
        expiration = datetime.fromisoformat(expiration_iso)
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        if now > expiration:
            return False
        else:
            return True
    else:
        return False
