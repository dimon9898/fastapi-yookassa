import asyncio
import json
from fastapi import FastAPI, Request, status
from run import bot  # ← импортируем готовый экземпляр!

app = FastAPI()


@app.post("/webhook", status_code=status.HTTP_200_OK)
async def payment_webhook(request: Request):
    data = await request.json()

    if data.get("event") == "payment.succeeded":
        payment = data.get("object", {})
        metadata = payment.get("metadata", {})
        user_id = metadata.get("user_id")

        if user_id:
            # создаём задачу на фоновую отправку
            asyncio.create_task(send_notification(user_id, text="✅ Оплата прошла успешно!"))

    return {"ok": True}


async def send_notification(user_id: int, text: str):
    """Безопасная отправка уведомления пользователю"""
    try:
        await bot.send_message(chat_id=user_id, text=text)
    except Exception as e:
        print(f"⚠️ Ошибка при отправке пользователю {user_id}: {e}")
