from aiogram.utils.keyboard import InlineKeyboardBuilder


async def payment_kb(link):
    kb = InlineKeyboardBuilder()
    
    kb.button(text='Оплатить', url=link)
    return kb.as_markup()