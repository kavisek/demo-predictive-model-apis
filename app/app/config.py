
from dotenv import load_dotenv

REDIS_HOST = os.getenv("REDIS_HOST","localhost")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD","docker")
REDIS_PORT = os.getenv("REDIS_PORT","6379")

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

