import json
from aiogram import Bot
from fastapi import FastAPI, HTTPException, Request, status, Depends
import logging
from run import bot


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)


logger = logging.getLogger('fastapi')

async def get_bot():
    return bot


app = FastAPI()


@app.post('/webhook', status_code=status.HTTP_200_OK)
async def payment_webhook(request: Request, bot: Bot = Depends(get_bot)):
    data = await request.json()
    await bot.send_message(chat_id=7886074197, text=f'ОК')
    return {'ok': True}


