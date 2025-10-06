import json
import logging
from fastapi import FastAPI, Request, status
from aiogram import Bot
from run import bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi")

app = FastAPI()

@app.post("/webhook", status_code=status.HTTP_200_OK)
async def payment_webhook(request: Request):
    data = await request.json()

    if data.get("event") == "payment.succeeded":
        payment = data.get("object", {})
        metadata = payment.get("metadata", {})
        user_id = metadata.get("user_id")

        if user_id:
            try:
                user_id = int(user_id)
                await bot.send_message(chat_id=user_id, text="✅ Оплата прошла успешно!")
                logger.info(f"Сообщение отправлено пользователю {user_id}")
            except Exception as e:
                logger.error(f"Ошибка при отправке пользователю {user_id}: {e}")

    return {"ok": True}
