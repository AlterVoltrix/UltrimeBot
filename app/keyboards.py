from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                          InlineKeyboardMarkup, InlineKeyboardButton)

# Главное меню
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Типичные вопросы FAQ')],
        [KeyboardButton(text='Руководства'), KeyboardButton(text='Об устройствах')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите раздел...'
)

# Кнопка "Назад" для инлайн-клавиатур
back_button = InlineKeyboardButton(text="⬅ Назад", callback_data="back_to_main")

# Меню FAQ
catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Как работать с Ultrime?', callback_data='WordUltrime')],
    [InlineKeyboardButton(text='Можно ли прошивать 2 устройства?', callback_data='TwoDevices')],
    [InlineKeyboardButton(text='Прошивка сбилась на полпути', callback_data='Error')],
    [back_button]
])

# Меню "Руководства" (шаблон для ссылок)
guides = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инструкция по работе с Ultrime', url='https://vostok.b4com.tech/Products/Files/DocEditor.aspx?fileid=72017')],  # Замените ссылку
    [InlineKeyboardButton(text='Обновления', url='https://vostok.b4com.tech/Products/Files/DocEditor.aspx?fileid=89589')],
    [InlineKeyboardButton(text='Тестирование', url='https://vostok.b4com.tech/Products/Files/DocEditor.aspx?fileid=96329')],
    [InlineKeyboardButton(text='Документация', url='https://vostok.b4com.tech/Products/Files/DocEditor.aspx?fileid=65489')],

    [back_button]
])

# Меню "Об устройствах" (модели)
devices = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='MRXXX', callback_data='device_mrxxx')],
    [InlineKeyboardButton(text='CS21XX', callback_data='device_cs21xx')],
    [InlineKeyboardButton(text='CS41XX', callback_data='device_cs41xx')],
    [InlineKeyboardButton(text='CS61XX', callback_data='device_cs61xx')],
    [InlineKeyboardButton(text='CS62XX', callback_data='device_cs62xx')],
    [InlineKeyboardButton(text='CS63XX', callback_data='device_cs63xx')],
    [InlineKeyboardButton(text='CS71XX', callback_data='device_cs71xx')],
    [back_button]
])