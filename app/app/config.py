import os
from dotenv import load_dotenv

REDIS_HOST = os.getenv("REDIS_HOST","localhost")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD","docker")
REDIS_PORT = os.getenv("REDIS_PORT","6379")
REDIS_EXPIRATION = os.getenv("REDIS_EXPIRATION",60)