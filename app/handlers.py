from aiogram import F,Router,types
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext

import app.keybords as kb


router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'hello',reply_markup=kb.main)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer("hell")

@router.message(F.text == 'How are u)')
async def how_are_you(message: Message):
    await message.answer('ok!')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID photo: {message.photo[-1].file_id}')

@router.message(Command('give_photo'))
async def give_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAOsaBpI2ZwsS85H06UMJlbRVgZNIMoAAjL5MRvt99BIcR925H9_rpYBAAMCAAN5AAM2BA',
                               caption='its shark')

@router.message(Command('id'))
async def user_id(message: types.Message):
    await message.answer(f"your id: {message.from_user.id}")

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    
    await callback.answer('you chose') #callback to callback
    await callback.message.edit_text('Hello',reply_markup=kb.settings)

@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Your name:')

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Reg.number)
    await message.answer('phone number')

@router.message(Reg.number)
async def two_three(message: Message,state: FSMContext):
    await state.update_data(number = message.text)
    data = await state.get_data()
    await message.answer(f'cool.\n Your name: {data["name"]} \n Number: {data["number"]}')
    await state.clear()
