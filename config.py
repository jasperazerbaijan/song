import os
API_ID = int(os.getenv("3588368"))
API_HASH = os.getenv("3d64c47cfe8d1cb0fc2cc06f5512298e")
BOT_TOKEN = os.getenv("1696209895:AAE_cnp_xuq_xj3OKDfGD34R7CTzhVVc_4U")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
