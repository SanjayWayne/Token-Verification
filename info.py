from os import environ

VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.

TOKEN_VERIFICATION_DURATION_SECONDS = int(os.environ.get("TOKEN_VERIFICATION_DURATION_SECONDS", 86400))  # Default: 24 hours (86400 seconds)
TOKEN_API = os.environ.get("TOKEN_API", "") # Shortlink API for token verification
TOKEN_URL = os.environ.get("TOKEN_URL", "") # Shortlink domain for token verification (without https://)
VERIFY_TUTORIAL = os.environ.get("VERIFY_TUTORIAL", "") # how to open link
BOT_USERNAME = os.environ.get("BOT_USERNAME", "") # bot username without @
