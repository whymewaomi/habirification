from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start():
    menu = InlineKeyboardBuilder()
    menu.button(text="Войти", callback_data="login")
    menu.button(text="Зарегистрироваться", callback_data="reg")
    menu.adjust(1, 1)
    menu.as_markup()
    return menu