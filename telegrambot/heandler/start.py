from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import keyboard.keyboard as kb

startbot = Router()

startbot.message(Command("start"))
async def startanswer(message: Message):
    await message.answer("Привет! \nДля того чтобы пользоваться ботом нужно"
                         "\nзарегистрироваться или войти в"
                         "\nсвой аккаунт", reply_markup=kb.start())
    