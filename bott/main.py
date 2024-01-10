import asyncio
import io
import os
import logging
import sys
from aiogram import Bot, Dispatcher, Router, F, html
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from api import create_user, create_feedback, create_feedback1, create_feedback2, create_feedback3, create_feedback4, update_subscription_status, create_feedback5



load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()
form_router = Router()

class Form(StatesGroup):
    vid = State()
    vopros1 = State()
    vopros2 = State()
    vopros3 = State()
    vopros4 = State()
    itog = State()
    


@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer("Привет! Давай узнаем какой вид физической активности подойдет для тебя. Вы готовы начать опрос?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                KeyboardButton(text="Да"),
                ]
            ],
            resize_keyboard=True,
        ),
    )
    print(create_user(message.from_user.username, message.from_user.first_name, message.from_user.id))
    await state.set_state(Form.vid)
    

@form_router.message(Form.vid, F.text == "Да")
async def vopros1(message: Message, state: FSMContext) -> None:
    await message.answer("Начинаем! Тебе нравится заниматься спортом?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                KeyboardButton(text="Да"),
                KeyboardButton(text="Нет"),
                ]
            ],
            resize_keyboard=True,
        ),
    )
    await message.answer(create_feedback(message.from_user.id,  message.text))
    await state.set_state(Form.vopros1)


@form_router.message(Form.vopros1, F.text == "Да")
async def vopr1da(message: Message, state: FSMContext) -> None:
    await message.answer(f"""Отлично! Следующий вопрос: 
                         \nПредпочитаешь ли ты активности на свежем воздухе?""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                KeyboardButton(text="Да"),
                KeyboardButton(text="Нет"),
                ]
            ],
            resize_keyboard=True,
        ),
    )
    await message.answer(create_feedback1(message.from_user.id,  message.text))
    await state.set_state(Form.vopros2)

@form_router.message(Form.vopros1, F.text == "Нет")
async def vopr1no(message: Message, state: FSMContext) -> None:
    await message.answer(f"""Понял, спасибо за ответ. Если не твое, не беда! Давай перейдем ко второму вопросу:
                         \n Предпочитаешь ли ты активности на свежем воздухе?""",
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [
                                    KeyboardButton(text="Да"),
                                    KeyboardButton(text="Нет"),
                                    ]
                                ],
                                resize_keyboard=True,
                            ),
                        )
    await message.answer(create_feedback1(message.from_user.id,  message.text))
    await state.set_state(Form.vopros2) 

@form_router.message(Form.vopros2, F.text == "Да")
async def vopr2da(message: Message, state: FSMContext) -> None:
    await message.answer(f"""Прекрасно! Еще один вопрос:
                         \nТы предпочитаешь поездки на транспорте или пешие прогулки?""",
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [
                                    KeyboardButton(text="Транспорт"),
                                    KeyboardButton(text="Пешеход"),
                                    ]
                                ],
                                resize_keyboard=True,
                            ),
                        )
    await message.answer(create_feedback2(message.from_user.id,  message.text))
    await state.set_state(Form.vopros3)
    
@form_router.message(Form.vopros2, F.text == "Нет")
async def vopr2no(message: Message, state: FSMContext) -> None:
    await message.answer(f"""Понял, мы идем дальше. Еще один вопрос:
                         \nТы предпочитаешь поездки на транспорте или пешие прогулки?""",
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [
                                    KeyboardButton(text="Транспорт"),
                                    KeyboardButton(text="Пешеход"),
                                    ]
                                ],
                                resize_keyboard=True,
                            ),
                        )
    await message.answer(create_feedback2(message.from_user.id,  message.text))
    await state.set_state(Form.vopros3)

@form_router.message(Form.vopros3, F.text == "Пешеход")
async def vopr3da(message: Message, state: FSMContext) -> None:
    await message.answer(f"""Это здорово! И последний вопрос:
                         \nТы предпочтешь командные занятия спортом или индивидуальные?""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                KeyboardButton(text="Командные"),
                KeyboardButton(text="Индивидуальные"),
                ]
            ],
            resize_keyboard=True,
        ),
    )
    await message.answer(create_feedback3(message.from_user.id,  message.text))
    await state.set_state(Form.vopros4)
    
@form_router.message(Form.vopros3, F.text == "Транспорт")
async def vopr3no(message: Message, state: FSMContext) -> None:
    await message.answer(f"""Хорошо. Последний вопрос:
                         \nТы предпочтешь командные занятия спортом или индивидуальные?""",
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [
                                    KeyboardButton(text="Командные"),
                                    KeyboardButton(text="Индивидуальные"),
                                    ]
                                ],
                                resize_keyboard=True,
                            ),
                        )
    await message.answer(create_feedback3(message.from_user.id,  message.text))
    await state.set_state(Form.vopros4)
    
@form_router.message(Form.vopros4, F.text == "Командные")
async def vopr4da(message: Message, state: FSMContext) -> None:
    await message.answer("Спасибо за ответы! ")
    await message.answer(f"""По результатам опроса, твои предпочтения указывают на то, что тебе мог бы понравиться футбол.
                         \nЭто командный вид спорта, который позволяет наслаждаться свежим воздухом и при этом требует коллективного взаимодействия.""")
    await message.answer(f"""Надеюсь, этот опрос помог тебе разобраться в подходящих видах физической активности.
                         \nТы бы хотел получать регулярные рассылки с тренировочными программами и статьями о здоровом образе жизни?""", 
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                KeyboardButton(text="Подписаться!"),
                KeyboardButton(text="Не подписываться."),
                ]
            ],
            resize_keyboard=True,
        ),
    )
    await message.answer(create_feedback4(message.from_user.id,  message.text))
    await state.set_state(Form.itog)


@form_router.message(Form.vopros4, F.text == "Индивидуальные")
async def vopr4no(message: Message, state: FSMContext) -> None:
    await message.answer("Спасибо за ответы! ")
    await message.answer(f"""По результатам опроса, твои предпочтения указывают на то, что тебе мог бы понравиться бег или велоспорт. 
                         \nЭто индивидуальные виды активности, которые позволяют наслаждаться свежим воздухом и одновременно развивать свои личные способности.""")
    await message.answer(f"""Надеюсь, этот опрос помог тебе разобраться в подходящих видах физической активности. 
                         \nТы бы хотел получать регулярные рассылки с тренировочными программами и статьями о здоровом образе жизни?""", 
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                KeyboardButton(text="Подписаться!"),
                KeyboardButton(text="Не подписываться."),
                ]
            ],
            resize_keyboard=True,
        ),
    )
    await message.answer(create_feedback4(message.from_user.id,  message.text))
    await state.set_state(Form.itog)

@form_router.message(Form.itog, F.text == "Подписаться!")
async def itogida(message: Message, state: FSMContext) -> None:
    await message.answer(create_feedback5(message.from_user.id,  message.text))
    await message.answer("Супер! Полезная информация будет приходить в этот чат, надеюсь, тебе будет интересно! ",
        reply_markup=ReplyKeyboardRemove(),
    )
    update_subscription_status(message.from_user.id, True)
    await state.clear()

@form_router.message(Form.itog, F.text == "Не подписываться.")
async def itogida(message: Message, state: FSMContext) -> None:
    await message.answer(create_feedback5(message.from_user.id,  message.text))
    await message.answer("Я рад, что ты уделил время для опроса. Успехов в твоих спортивных достижениях!",
        reply_markup=ReplyKeyboardRemove(),
    )
    update_subscription_status(message.from_user.id, True)
    await state.clear()

async def main():
   dp = Dispatcher()
   dp.include_router(form_router)
   await dp.start_polling(bot)

if __name__ == '__main__':
   logging.basicConfig(level=logging.INFO, stream=sys.stdout)
   asyncio.run(main())