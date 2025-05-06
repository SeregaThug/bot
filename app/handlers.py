from aiogram import F,Router,types
from aiogram.filters import CommandStart,Command
from aiogram.types import Message


router = Router()




@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("1")

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