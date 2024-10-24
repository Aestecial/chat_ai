from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env


@dataclass
class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
