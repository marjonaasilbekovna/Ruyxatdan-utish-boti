import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Registor

TOKEN = "7181305178:AAEVp764bS7csy8A7lcAXUrNkj7Z9x--2hE"
ADMIN_ID = [7241341727, 7376235983]

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Ro'yxatdan o'tish botga hush kelibsiz"
    await message.answer(text)

@dp.message(Command("reg"))
async def register(message: Message, state:FSMContext):
    await message.answer("Ro'yxatdan o'tish uchun ma'limotlarni kiriting !  \nIsmingizni kiriting ")
    await state.set_state(Registor.ism)

@dp.message(F.text, Registor.ism)
async def register_ism(message: Message, state:FSMContext):
    ism = message.text 
    await state.update_data(name = ism)
    await state.set_state(Registor.familiya)
    await message.answer("Familiyani kiriting")

@dp.message(Registor.ism)
async def register_ism_del(message:Message, state:FSMContext):
    await message.answer(text= "Ismimgizni to'g'ri kiriting ❗️")
    await message.delete()

@dp.message(F.text, Registor.familiya)
async def register_familiya(message: Message, state:FSMContext):
    familiya = message.text  
    await state.update_data(surname = familiya)
    await state.set_state(Registor.yosh)
    await message.answer("Yoshingizni kiriting")

@dp.message(Registor.familiya)
async def register_familiya_del(message: Message, state:FSMContext):
    await message.answer(text= "Familiyngizni tug'ri kiriting ❗️")
    await message.delete()

@dp.message(F.text, Registor.yosh)
async def register_yosh(message: Message, state:FSMContext):
    yosh = message.text  
    await state.update_data(age = yosh)
    await state.set_state(Registor.tel)
    await message.answer("Telefon raqamni kiriting")

@dp.message(Registor.yosh)
async def register_yosh_del(message: Message, state:FSMContext):
    await message.answer(text= "Yoshingizni tug'ri kiriting ❗️")
    await message.delete()

@dp.message(F.text.regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"), Registor.tel)
async def register_tel(message: Message, state:FSMContext):
    tel = message.text  
    await state.update_data(tel = tel)
    await state.set_state(Registor.email)
    await message.answer("Emailingizni kiriting")

@dp.message(Registor.tel)
async def register_tel_del(message: Message, state:FSMContext):
    await message.answer(text= "Telefon raqamingizni tug'ri kiriting ❗️")
    await message.delete()   

@dp.message(F.text.regexp(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"), Registor.email)
async def register_email(message: Message, state:FSMContext):
    email = message.text
    await state.update_data(email = email)
    await state.set_state(Registor.rasm)
    await message.answer("Biror bir rasm kiriting")

@dp.message(Registor.email)
async def register_email_del(message: Message, state:FSMContext):
    await message.answer(text= "Emailingizni tug'ri kiriting ❗️")
    await message.delete()

@dp.message(F.photo, Registor.rasm)
async def photo_message(message: Message, state:FSMContext):
    photo = message.photo[-1]
    await state.update_data(rasm_id=photo.file_id)
    await state.set_state(Registor.kurs)
    await message.answer("Kurs nomini kiriting ")

@dp.message(Registor.rasm)
async def invalid_photo_message(message: Message, state: FSMContext):
    await message.answer(text= " Iltimos rasm yuboring ❗️")
    await message.delete() 

@dp.message(F.text, Registor.kurs)
async def register_kurs(message: Message, state:FSMContext):
    kurs = message.text
    await state.update_data(kurs = kurs)
    await state.set_state(Registor.viloyat)
    await message.answer("Viloyat nomini kiriting")

@dp.message(Registor.kurs)
async def register_kurs_del(message: Message, state:FSMContext):
    await message.answer(text= "Kursingizni tug'ri kiriting ❗️")
    await message.delete()

@dp.message(F.text, Registor.viloyat)
async def register_viloyat(message: Message, state:FSMContext):
    viloyat = message.text
    await state.update_data(viloyat = viloyat)
    await state.set_state(Registor.tuman)
    await message.answer("Tuman nomini kiriting")

@dp.message(Registor.viloyat)
async def register_viloyat_del(message: Message, state:FSMContext):
    await message.answer(text= "Viloyatni tug'ri kiriting ❗️")
    await message.delete()

@dp.message(F.text, Registor.tuman)
async def register_tuman(message: Message, state:FSMContext):
    tuman = message.text
    await state.update_data(tuman = tuman)
    await state.set_state(Registor.kocha)
    await message.answer("Kocha nomini kiriting")

@dp.message(Registor.tuman)
async def register_tuman_del(message: Message, state:FSMContext):
    await message.answer(text= "Tumaningizni tug'ri kiriting ❗️")
    await message.delete()

@dp.message(F.text, Registor.kocha)
async def register_kocha(message: Message, state:FSMContext):
    kocha = message.text
    await state.update_data(kocha = kocha)
    await state.set_state(Registor.maktab)
    await message.answer("Maktabingizni kiriting")

@dp.message(Registor.kocha)
async def register_kocha_del(message: Message, state:FSMContext):
    await message.answer(text= "Ko'changizni tug'ri kiriting ❗️")
    await message.delete()

@dp.message(F.text, Registor.maktab)
async def register_maktab(message: Message, state:FSMContext):
    data = await state.get_data()

@dp.message(Registor.maktab)
async def register_maktab_del(message: Message, state:FSMContext):
    await message.answer(text= "Maktabingizni tug'ri kiriting ❗️")
    await message.delete()

    data = await state.get_data()

    ism = data.get("name")
    familiya = data.get("surname")
    yosh = data.get("age")
    tel = data.get("tel")
    email = data.get("email")
    kurs = data.get("kurs") 
    viloyat = data.get("viloyat")
    tuman = data.get("tuman")
    kocha = data.get("kocha")
    rasm = data.get("rasm_id")
    maktab = message.text

    text = f"Ism : {ism} \nFamiliya : {familiya} \nYosh : {yosh} \nTel : {tel} \nEmail: {email} \nKurs : {kurs} \nViloyat: {viloyat} viloyati \nTuman: {tuman} tumani \nKo'cha: {kocha} ko'chasi \nMaktab: {maktab}"
    await message.answer("Siz ro'yxatdan o'tdingiz!")

    for admin in ADMIN_ID:
        await bot.send_message(chat_id= admin, text=text)
        await bot.send_photo(chat_id= admin, photo=rasm)
    await state.clear()


@dp.startup()
async def bot_start(bot: Bot):
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Tabriklaymiz 🎉 \nBotimiz ishga tushdi ")

@dp.shutdown()
async def bot_stop(bot: Bot):
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Bot to'xtadi ❗️")
    
async def main():
    global bot
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
