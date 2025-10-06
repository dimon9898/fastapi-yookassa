import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from keyboards import payment_kb 
from crud import generate_url

bot = Bot(token='8094950171:AAEDxkP4Gxl8QOD8Yb_qVVNX02GRkckD4CI')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    amount = 1200
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    course_id = 2
    return_url = 'https://t.me/basedbBot_bot'
    
    result = await generate_url(amount, user_id, user_name, course_id, return_url)
    
    link = result['confirmation']['confirmation_url']
    
    await message.answer('Кнопка для оплаты:', reply_markup=await payment_kb(link))




async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
 