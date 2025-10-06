import json
from aiogram import Bot
from fastapi import FastAPI, HTTPException, Request, status
import logging
from run import bot


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)


logger = logging.getLogger('fastapi')




app = FastAPI()


@app.post('/webhook')
async def payment_webhook(request: Request, bot: Bot):
    data = await request.json()
    result = json.dumps(data, indent=4, ensure_ascii=False)
    await bot.send_message(chat_id=7886074197, text=f'{result}')
    return {'ok': True}


