import logging
from fastapi import FastAPI, Request, BackgroundTasks
from aiogram import Bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

BOT_TOKEN = "8094950171:AAEDxkP4Gxl8QOD8Yb_qVVNX02GRkckD4CI"


@app.post("/webhook")
async def yookassa_webhook(request: Request, background: BackgroundTasks):
    data = await request.json()

    # ЛОГИРУЕМ ВСЁ — это важно
    logger.info(f"YooKassa webhook: {data}")

    # YooKassa присылает event
    if data.get("event") == "payment.succeeded":
        background.add_task(process_payment, data)

    # ОБЯЗАТЕЛЬНО сразу 200
    return {"ok": True}


async def process_payment(data: dict):
    try:
        payment = data.get("object", {})
        metadata = payment.get("metadata", {})
        user_id = metadata.get("user_id")

        if not user_id:
            logger.error("user_id not found in metadata")
            return

        bot = Bot(token=BOT_TOKEN)

        await bot.send_message(
            chat_id=int(user_id),
            text="✅ Оплата прошла успешно!"
        )

        await bot.session.close()

        logger.info(f"Message sent to user {user_id}")

    except Exception as e:
        logger.exception(f"Payment processing error: {e}")
