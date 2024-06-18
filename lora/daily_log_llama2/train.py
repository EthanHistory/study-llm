from huggingface_hub import login
from datasets import load_dataset

from pydantic import (
    BaseSettings,
    Field
)

from source import logger

class Settings(BaseSettings):
    huggingface_token: str = Field(..., env='HUGGINGFACE_TOKEN')

settings = Settings()

if __name__ == "__main__":
    logger.info("Login to huggingface...")
    login(token=settings.huggingface_token)

    logger.info("Load dailylog dataset...")
    dataset = load_dataset("li2017dailydialog/daily_dialog")