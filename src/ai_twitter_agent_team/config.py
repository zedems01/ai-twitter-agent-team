from pathlib import Path
import os

from dotenv import load_dotenv
from loguru import logger




# Load environment variables from .env file if it exists
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")



AGENTS_DIR = PROJ_ROOT / "agents"
STORAGE_DIR = PROJ_ROOT / "storage"


