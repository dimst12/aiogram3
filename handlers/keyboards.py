from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')],
    [KeyboardButton(text='Shopping cart'), KeyboardButton(text='Contacts')]
],
    resize_keyboard=True, input_field_placeholder='Select a menu item.')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://youtube.com')]
])

cars = {
    "Badminton UA": "https://badminton.ua/",
    "Yonex": "https://yonex.ua/",
    "BWF": "https://bwfbadminton.com/",
    "Badminton Europe": "https://badmintoneurope.com"
}

def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car, url in cars.items():
        keyboard.add(InlineKeyboardButton(text=car, url=url))
    return keyboard.adjust(2).as_markup()
