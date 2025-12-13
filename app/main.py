import json
import logging
from fastapi import FastAPI, Request, status
from aiogram import Bot
from run import bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi")

app = FastAPI()

@app.post("/webhook")
async def payment_webhook(request: Request):
    data = await request.json()
    logger.error(f"YOOKASSA WEBHOOK: {data}")
    return {"ok": True}