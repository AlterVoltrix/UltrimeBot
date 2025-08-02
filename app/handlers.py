from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                          InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
router = Router()



# Главное меню
# Главное меню
@router.message(CommandStart())
async def cmd_start(message: Message):
    # Создаем клавиатуру главного меню
    main_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Типичные вопросы FAQ')],
            [KeyboardButton(text='Руководства'), KeyboardButton(text='Об устройствах')]
        ],
        resize_keyboard=True,
        input_field_placeholder='Выберите раздел...'
    )
    
    # Отправляем приветственное сообщение с клавиатурой
    await message.answer(
        'Приветствую, я UltrimeBot. Помогаю с вопросами по устройствам, прошивкам и документаций.\n\n'
        'Выберите нужный раздел:',
        reply_markup=main_kb
    )

# Обработка кнопки "Назад" - теперь удаляет предыдущее сообщение
@router.callback_query(F.data == "back_to_main")
async def back_handler(callback: CallbackQuery):
    try:
        # Удаляем сообщение с кнопками
        await callback.message.delete()
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")
    
    # Отправляем новое сообщение с главным меню
    await callback.message.answer(
        "",
        reply_markup=kb.main
    )
    await callback.answer()
# Раздел FAQ
@router.message(F.text == 'Типичные вопросы FAQ')
async def faq_menu(message: Message):
    await message.answer("Частые вопросы:", reply_markup=kb.catalog)

# Раздел "Руководства" (ссылки)
@router.message(F.text == 'Руководства')
async def guides_menu(message: Message):
    await message.answer("📚 Доступные руководства:", reply_markup=kb.guides)

# Раздел "Об устройствах"
@router.message(F.text == 'Об устройствах')
async def devices_menu(message: Message):
    await message.answer("📱 Выберите модель устройства:", reply_markup=kb.devices)

# Обработчики для устройств (шаблоны)
@router.callback_query(F.data.startswith('device_'))
async def device_info(callback: CallbackQuery):
    model = callback.data.split('_')[1].upper()
    info = {
        'mrxxx': "MRXXX:\n\n• Характеристика 1\n• Характеристика 2\n• Совместимость: ...",
        'cs21xx': "CS21XX:\n",
        'cs41xx': "CS41XX:\n",
        'cs61xx': "CS61XX:\n",
        'cs62xx': "CS62XX:\n",
        'cs63xx': "CS63XX:\n",
        'cs71xx': "CS71XX:\n",
        # Добавьте описание для других моделей
    }.get(model.lower(), "Информация об этом устройстве скоро появится!")
    
    await callback.message.answer(info)
    await callback.answer()

# Обработчики FAQ (оставьте ваши текущие, например)
@router.callback_query(F.data == 'WordUltrime')
async def WordUltrime(callback: CallbackQuery):
    await callback.message.answer(
   """
   План работы Ultrime: \n
   1. Нажмите два раза ЛКМ на значок Ultrime \n
   2. Напишите в адресной строке браузера '127.0.0.1:8080' \n
   3. После загрузки страницы выберите интересующее вас устройство \n
   4. Выберите желаемый способ прошивки \n
   5. Подключите устройство и выберите COM-порт подключен к устройству \n
   6. Нажмите кнопку 'Старт' \n
"""

   )
    
@router.callback_query(F.data == "TwoDevices")
async def TwoDevices(callback : CallbackQuery):
    await callback.message.answer(
   """
Можно ли прошивать 2 устройства одновременно?

Да, это возможно при соблюдении следующих условий:
- На компьютере должно быть не менее 2 COM-портов
- Каждое устройство должно быть подключено к отдельному COM-порту
- Рекомендуется проверить COM-проты
- Не рекомендуется во время прошивки одного устройства начинать прошивку одного с связи с возможномы ошибками
"""
    )


@router.callback_query(F.data == "Error")
async def Error(callback: CallbackQuery):
    await callback.message.answer(
        """
Что делать если прошивка сбилась на полпути?

1. Не паникуйте и не отключайте устройство.
2. Попробуйте начать прошивку с того этапе на котором все сбилось.
3. Если проблема повторяется, начинайте прошивку заново.
4. Проверьте целостность COM-порта.
5. Попробуйте другой COM-порт.
6. Если ничего не помогает, обратитесь к создателям Ultrime.
"""
    )
    await callback.answer()



@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Справка по боту:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="FAQ", callback_data="help_faq"),
             InlineKeyboardButton(text="Поддержка", url="t.me/AlterVoltrix")]
        ])
    )

