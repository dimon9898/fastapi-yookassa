import asyncio
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



app = FastAPI()


@app.post('/webhook', status_code=status.HTTP_200_OK)
async def payment_webhook(request: Request):
    data = await request.json()
    
    if data.get('event') == 'payment.succeeded':
        payment = data.get('object')
        metadata = payment.get('metadata')
        
        user_id = metadata.get('user_id')
        
        if user_id:
            asyncio.create_task(send_notification(user_id, text='ВСЕ ОКЕЙ'))
    
    
    return {'ok': True}



async def send_notification(user_id: int, text: str):
    await bot.send_message(chat_id=user_id, text=text)


