
import logging

from aiogram import Bot, Dispatcher, executor, types
from config import *
from buttons import *
from aiogram.types import Message,CallbackQuery

logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


######  Salomlashish va klaviyatura pasi knopka yonalishi  ########

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    info = f"*Mualif: Alikuziyev Anvar \nAssalomu alekum 🤝 {message.from_user.first_name}*"
    info += "*\nbizning online FasFood Magazinimzga \nxush kelibsiz iltimos tilni tanlang🥳*"
    await message.reply_photo(photo=open('images/fastfood.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=til_uz)
    await call.message.delete()


################  UZB TILDAGI KOD  #######################
##############  Til va song yonalshi  ##########################

'''Til ni bosa rayon knopkaga otsin'''

@dp.message_handler(text="🇸🇱 Uzbek")
async def echo(message: types.Message):
    info = f"*Iltimos Tumaningizni tanlang📍*"
    await message.answer(info,parse_mode='markdown',reply_markup=rayon_uz)
    await call.message.delete()

@dp.message_handler(text="🇷🇺 Русский")
async def echo(message: types.Message):
    info = f"*Пожалуйста выберите свой регион📍*"
    await message.answer(info,parse_mode='markdown', reply_markup=rayon_ru)
    await call.message.delete()



################## UZ Tuman va song yonalshi #####################

# UZ Tuman
'''Tumanlarni bosgandan song teli soriydi'''

@dp.message_handler(text="📍Yunusobot")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()


@dp.message_handler(text="📍Mirobod")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()

@dp.message_handler(text="📍Uchtepa")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()

@dp.message_handler(text="📍Olmazor")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()

@dp.message_handler(text="📍Bektimir")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()

@dp.message_handler(text="📍Mirzo-Ulugbek")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()

@dp.message_handler(text="📍Chilonzor")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()

@dp.message_handler(text="📍Yakkasaroy")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()

@dp.message_handler(text="📍Sergili")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()

@dp.message_handler(text="📍Shayxontoxur")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()

@dp.message_handler(text="📍Yashnobot")
async def echo(message: types.Message):
    info = f"*Raqamingizni jonatasizmi📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=uz_tel)
    await call.message.delete()







################## RU Tuman va song yonalshi #####################

# RU Туман

@dp.message_handler(text="📍Юнусабать")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Мирабать")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Учтепа")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Алмазар")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Бектемир")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Мирзо-Улугбек")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Чиланзар")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Яккасарай")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Сергили")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Шайхантахур")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()

@dp.message_handler(text="📍Яшнабать")
async def echo(message: types.Message):
    info = f"*Можешь прислать мне свой номер?📞*"
    await message.answer(info,parse_mode='markdown',reply_markup=ru_tel)
    await call.message.delete()








########### UZ,RU  Buyirtma berish knopkasi va song yonalshi  ###########
'''Telefon nomer jonatilgandan song Buyurtma berishga otadi'''

@dp.message_handler(content_types=['contact'])
async def echo(message):
    info = f"*Buyurtma beramizmi😉 / Будите заказать😉*"
    await message.answer_photo(photo=open('images/zakaz.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=buyurtma)
    await call.message.delete()
    






####################  UZ Menu va song yonalshi  #####################
'''Buyurtma bosilgandan song Menu ga otadi'''
'''Pastki menu'''
@dp.callback_query_handler(text="buyurtma")
async def echo(call: CallbackQuery):
    info = f"*😋Menu*"
    i = 'Bosh Menu'
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz,)
    await call.message.answer(i,parse_mode='markdown',reply_markup=pastki_menu_uz)
    await call.message.delete()




###### UZ menu
@dp.message_handler(text="Menu")
async def echo(message: types.Message):
    info = f"*Bosh menu*"
    await message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

###### UZ Sozlamalar
@dp.message_handler(text="⚙Boshidan sozlash")
async def echo(message: types.Message):
    info = f"*Boshidan sozlaymiz*"
    await message.answer_photo(photo=open('images/setting.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=til_uz)
    await call.message.delete()

###### UZ Buyurtmalar
@dp.message_handler(text="Buyurtmalar")
async def echo(message: types.Message):
    info = f"*Siznig Buyurtmalaringiz*"
    await message.answer_photo(photo=open('images/buyurtmalar.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=till)
    await call.message.delete()

###### UZ Ariza va shikoyatlar
@dp.message_handler(text="Ariza va shikoyatlar")
async def echo(message: types.Message):
    info = f"*Ariza va shikoyatlaringizni yozib qoldiring*"
    await message.answer_photo(photo=open('images/ariza.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=None)
    await call.message.delete()

###### UZ Ariza va shikoyatlar
@dp.message_handler(text="FasFood haqida malumot")
async def echo(message: types.Message):
    info = f"*Fast-fud - bu ommaviy ishlab chiqarilgan oziq-ovqat turi bo'lib , xizmat ko'rsatish tezligiga ustuvor ahamiyat beriladi. Bu tijorat atamasi bo'lib, restoran yoki do'konda muzlatilgan, oldindan qizdirilgan yoki oldindan pishirilgan ingredientlar bilan sotiladigan va olib ketish / olib ketish uchun qadoqlangan holda sotiladigan oziq-ovqat uchun cheklangan. Fast food ko'p sonli band yo'lovchilar, sayohatchilar va maoshli ishchilarni joylashtirish uchun tijorat strategiyasi sifatida yaratilgan . 2018 yilda tez oziq-ovqat sanoati global miqyosda taxminan 570 milliard dollarni tashkil etdi*"
    await message.answer_photo(photo=open('images/fass.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=None)
    await call.message.delete()





#ASOSIY MENU
#.............. UZ Taomlar royxati va song yonalshi  ..................
'''Menu dan nima olinish bosilgandan song otadigan yonalishlar'''

# 1
#################  BARCHA KNOPKA MENU FUNKSIYALARI  #####################
'''Barcha menu knopkasi'''
@dp.callback_query_handler(text="bar")
async def echo(call: CallbackQuery):
    info = f"*Quidagilardan birini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=barcha_menu_uz)
    await call.message.delete()

# ......................  Barcha mini menunisi ..................................
@dp.callback_query_handler(text="kartoshkafri")
async def echo(call: CallbackQuery):
    info = f"*🍟Kartoshka-Fri \n Narxi: 15 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/kartoshkafri.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_son)
    await call.message.delete()

@dp.callback_query_handler(text="derevenskoe")
async def echo(call: CallbackQuery):
    info = f"*🍟Derevenskoe-Fri \n Narxi: 13 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/derevenskoe.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_son)
    await call.message.delete()


'''Pitzza menusi'''
@dp.callback_query_handler(text="pizza")
async def echo(call: CallbackQuery):
    info = f"*🍕Pizza qaysi xilidan olasiz👇*"
    await call.message.answer_photo(photo=open('images/pizza.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_menu_pizza_uz)
    await call.message.delete()

@dp.callback_query_handler(text="p_sir")
async def echo(call: CallbackQuery):
    info = f"*🍕Pizza Sirli \n Narxi: 45 000 so'm \n Miqdorini tanlang yoki kiriting👇*"
    await call.message.answer_photo(photo=open('images/p_sir.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_pizza_son)
    await call.message.delete()

@dp.callback_query_handler(text="p_korona")
async def echo(call: CallbackQuery):
    info = f"*🍕Pizza Korona \n Narxi: 48 000 so'm \n Miqdorini tanlang yoki kiriting👇*"
    await call.message.answer_photo(photo=open('images/p_korona.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_pizza_son)
    await call.message.delete()

@dp.callback_query_handler(text="p_oddiy")
async def echo(call: CallbackQuery):
    info = f"*🍕Pizza Oddiy \n Narxi: 50 000 so'm \n Miqdorini tanlang yoki kiriting👇*"
    await call.message.answer_photo(photo=open('images/p_oddiy.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_pizza_son)
    await call.message.delete()


######  НАЗАД BARCHA MENU
'''Barcha menu dan Glavni menu ga'''
@dp.callback_query_handler(text="barchadan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

'''Sondan Barcha menuga'''
@dp.callback_query_handler(text="barcha_son_ort")
async def echo(call: CallbackQuery):
    info = f"*Quidagilardan birini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=barcha_menu_uz)
    await call.message.delete()

'''Barcha menu ichdagi Pizza Sonidan pizza menuga'''
@dp.callback_query_handler(text="barcha_pizza_son_ort")
async def echo(call: CallbackQuery):
    info = f"*🍕Pizza qaysi xilidan olasiz👇*"
    await call.message.answer_photo(photo=open('images/pizza.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_menu_pizza_uz)
    await call.message.delete()





#2
#################  SOZLAMALAR KNOPKA MENU FUNKSIYALARI  #####################
''' Sozlamalar Glavnidagi knopkasi'''
@dp.callback_query_handler(text="sozlama")
async def echo(call: CallbackQuery):
    info = f"*❌❌❌❌*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=sozlama_menu_uz)
    await call.message.delete()

# ......................  Sozlama ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="mavjud")
async def echo(call: CallbackQuery):
    info = f"*❌❌❌❌*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=sozlama_menu_uz)
    await call.message.delete()


######  НАЗАД Sozlamalar MENU
'''Barcha menu dan Glavni menu ga'''
@dp.callback_query_handler(text="sozlamadan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()





#3
#################  BOSHQALAR KNOPKA MENU FUNKSIYALARI  #####################
''' Boshqalar Glavnidagi knopkasi'''
@dp.callback_query_handler(text="bosh")
async def echo(call: CallbackQuery):
    info = f"*Quidagilardan birini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=boshqa_menu_uz)
    await call.message.delete()

# ......................  Boshqa mini menunisi ..................................
@dp.callback_query_handler(text="sen")
async def echo(call: CallbackQuery):
    info = f"*🥪Sendvich \n Narxi: 32 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/sen.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_son)
    await call.message.delete()

@dp.callback_query_handler(text="chic")
async def echo(call: CallbackQuery):
    info = f"*🥪Chickens \n Narxi: 27 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/chic.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_son)
    await call.message.delete()


'''Shaurma menusi'''
@dp.callback_query_handler(text="shaurma")
async def echo(call: CallbackQuery):
    info = f"*🫔Shaurma qaysi xilidan olasiz👇*"
    await call.message.answer_photo(photo=open('images/shaurma.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_menu_shaurma_uz)
    await call.message.delete()

@dp.callback_query_handler(text="kla")
async def echo(call: CallbackQuery):
    info = f"*🫔Shaurma klassika \n Narxi: 20 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/kla.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_shaurma_son)
    await call.message.delete()

@dp.callback_query_handler(text="achi")
async def echo(call: CallbackQuery):
    info = f"*🫔Shaurma achiq \n Narxi: 25 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/achi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_shaurma_son)
    await call.message.delete()

@dp.callback_query_handler(text="qoz")
async def echo(call: CallbackQuery):
    info = f"*🫔Shaurma qoziqorinlik \n Narxi: 30 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/qoz.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_shaurma_son)
    await call.message.delete()


######  НАЗАД BARCHA MENU
'''Boshqa menu dan Glavni menu ga'''
@dp.callback_query_handler(text="boshqadan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

'''Sondan Boshqa menuga'''
@dp.callback_query_handler(text="boshqa_son_ort")
async def echo(call: CallbackQuery):
    info = f"*Quidagilardan birini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=boshqa_menu_uz)
    await call.message.delete()

'''Boshqa menu ichdagi shaurma Sonidan shourma menuga'''
@dp.callback_query_handler(text="barcha_shaurma_son_ort")
async def echo(call: CallbackQuery):
    info = f"*🫔Shaurma qaysi xilidan olasiz👇*"
    await call.message.answer_photo(photo=open('images/shaurma.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_menu_shaurma_uz)
    await call.message.delete()




#4
#################  LAVASH KNOPKA MENU FUNKSIYALARI  #####################
''' Lavash Glavnidagi knopkasi'''
@dp.callback_query_handler(text="lavash")
async def echo(call: CallbackQuery):
    info = f"*🌯Lavash turini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_uz)
    await call.message.delete()

# ......................  Lavash mini menunisi ..................................
@dp.callback_query_handler(text="l_tovuqlik")
async def echo(call: CallbackQuery):
    info = f"*🌯Lavash xilini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_tovuq_uz)
    await call.message.delete()

@dp.callback_query_handler(text="l_goshtlik")
async def echo(call: CallbackQuery):
    info = f"*🌯Lavash xilini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_gosht_uz)
    await call.message.delete()


'''Lavash tovuq menusi'''
@dp.callback_query_handler(text="l_min")
async def echo(call: CallbackQuery):
    info = f"*🌯Tovuqli mini \n Narxi: 17 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/l_min.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_tovuq_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="l_sir")
async def echo(call: CallbackQuery):
    info = f"*🌯Tovuqli sir \n Narxi: 25 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/l_sir.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_tovuq_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="l_qal")
async def echo(call: CallbackQuery):
    info = f"*🌯Tovuqli qalampir \n Narxi: 23 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/l_qal.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_tovuq_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="l_odi")
async def echo(call: CallbackQuery):
    info = f"*🌯Tovuqli oddiy \n Narxi: 15 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/l_odi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_tovuq_son_uz)
    await call.message.delete()


'''Lavash gosht menusi'''
@dp.callback_query_handler(text="la_min")
async def echo(call: CallbackQuery):
    info = f"*🌯Goshtlik mini \n Narxi: 18 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/la_min.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_gosht_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="la_sir")
async def echo(call: CallbackQuery):
    info = f"*🌯Goshtlik sir \n Narxi: 22 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/la_sir.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_gosht_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="la_qal")
async def echo(call: CallbackQuery):
    info = f"*🌯Goshtlik qalampir \n Narxi: 20 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/la_qal.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_gosht_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="la_odi")
async def echo(call: CallbackQuery):
    info = f"*🌯Goshtlik oddiy \n Narxi: 17 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/la_odi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_gosht_son_uz)
    await call.message.delete()




######  НАЗАД LAVASH MENU
'''Lavash menu dan Glavni menu ga'''
@dp.callback_query_handler(text="lavashdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

'''Lavash Tovuq ichi goshtlik ichidan --> Lavash t va g ga menuga'''
@dp.callback_query_handler(text="lavash_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🌯Lavash turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_uz)
    await call.message.delete()

'''Lavash tovuqli sonidan ortga'''
@dp.callback_query_handler(text="lavash_menu_tovuq_uz")
async def echo(call: CallbackQuery):
    info = f"*🌯Lavash xilini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_tovuq_uz)
    await call.message.delete()

'''Lavash goshli sonidan ortga'''
@dp.callback_query_handler(text="lavash_menu_gosht_uz")
async def echo(call: CallbackQuery):
    info = f"*🌯Lavash xilini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_gosht_uz)
    await call.message.delete()





#5
#################  HOT-DOG KNOPKA MENU FUNKSIYALARI  #####################
''' Hot-dog Glavnidagi knopkasi'''
@dp.callback_query_handler(text="hotdog")
async def echo(call: CallbackQuery):
    info = f"*🌭Hot-Dog turini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=hotdog_menu_uz)
    await call.message.delete()

# ......................  Hot-Dog ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="h_kor")
async def echo(call: CallbackQuery):
    info = f"*🌭Korolevski hot-dog \n Narxi: 20 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/h_kor.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=hotdog_kor_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="h_odi")
async def echo(call: CallbackQuery):
    info = f"*🌭Oddiy hot-dog \n Narxi: 15 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/h_odi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=hotdog_odi_son_uz)
    await call.message.delete()


######  НАЗАД HOT-DOG MENU
'''Hot-dog menu dan Glavni menu ga'''
@dp.callback_query_handler(text="hotdogdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

@dp.callback_query_handler(text="hotdog_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🌭Hot-Dog turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=hotdog_menu_uz)
    await call.message.delete()





#6
#################  HAGGI KNOPKA MENU FUNKSIYALARI  #####################
''' Haggi Glavnidagi knopkasi'''
@dp.callback_query_handler(text="haggi")
async def echo(call: CallbackQuery):
    info = f"*🌮Haggi turini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=haggi_menu_uz)
    await call.message.delete()

# ......................  Haggi ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="ha_tov")
async def echo(call: CallbackQuery):
    info = f"*🌮Haggi tovuqli \n Narxi: 29 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/ha_tov.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=haggi_tov_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="ha_gosh")
async def echo(call: CallbackQuery):
    info = f"*🌮Haggi goshtli \n Narxi: 24 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/ha_gosh.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=haggi_gosh_son_uz)
    await call.message.delete()


######  НАЗАД HAGGI MENU
'''Haggi menu dan Glavni menu ga'''
@dp.callback_query_handler(text="haggidan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

@dp.callback_query_handler(text="haggi_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🌮Haggi turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=haggi_menu_uz)
    await call.message.delete()






#7
#################  TACOS KNOPKA MENU FUNKSIYALARI  #####################
''' Tacos Glavnidagi knopkasi'''
@dp.callback_query_handler(text="tacos")
async def echo(call: CallbackQuery):
    info = f"*🥙Taco turini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=tacos_menu_uz)
    await call.message.delete()

# ......................  Haggi ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="le")
async def echo(call: CallbackQuery):
    info = f"*🥙Taco le crispy \n Narxi: 35 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/le.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=tacos_le_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="so")
async def echo(call: CallbackQuery):
    info = f"*🥙Taco so gourmand \n Narxi: 32 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/so.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=tacos_so_son_uz)
    await call.message.delete()


######  НАЗАД TACOS MENU
'''Tacos menu dan Glavni menu ga'''
@dp.callback_query_handler(text="tacosdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

@dp.callback_query_handler(text="tacos_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🥙Taco turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=tacos_menu_uz)
    await call.message.delete()






#8
#################  GAMBURGER KNOPKA MENU FUNKSIYALARI  #####################
''' Gamburger Glavnidagi knopkasi'''
@dp.callback_query_handler(text="gamburger")
async def echo(call: CallbackQuery):
    info = f"*🍔Gamburger turini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=gamburger_menu_uz)
    await call.message.delete()

# ......................  Gamburger ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="g_big")
async def echo(call: CallbackQuery):
    info = f"*🍔Bigburger \n Narxi: 25 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/g_big.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=gamburger_big_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="g_ches")
async def echo(call: CallbackQuery):
    info = f"*🍔Bigcheese \n Narxi: 29 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/g_ches.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=gamburger_ches_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="g_chick")
async def echo(call: CallbackQuery):
    info = f"*🍔ChickenBurger \n Narxi: 32 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/g_chick.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=gamburger_chick_son_uz)
    await call.message.delete()


######  НАЗАД GAMBURGER MENU
'''Gamburger menu dan Glavni menu ga'''
@dp.callback_query_handler(text="gamburgerdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

@dp.callback_query_handler(text="gamburger_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🍔Gamburger turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=gamburger_menu_uz)
    await call.message.delete()






#9
#################  CLAP-sendvich KNOPKA MENU FUNKSIYALARI  #####################
''' CLAP-sendvich Glavnidagi knopkasi'''
@dp.callback_query_handler(text="clap")
async def echo(call: CallbackQuery):
    info = f"*🥪CLAP-sendvich turini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=clap_menu_uz)
    await call.message.delete()

# ......................  CLAP-sendvich ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="c_chick")
async def echo(call: CallbackQuery):
    info = f"*🥪Clap-Chicken \n Narxi: 27 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/chick.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=clap_chick_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="c_meat")
async def echo(call: CallbackQuery):
    info = f"*🥪Clap-Meat \n Narxi: 30 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/meat.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=clap_meat_son_uz)
    await call.message.delete()


######  НАЗАД CLAP-sendvich MENU
'''CLAP-sendvich menu dan Glavni menu ga'''
@dp.callback_query_handler(text="clapdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

@dp.callback_query_handler(text="clap_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🥪CLAP-sendvich turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=clap_menu_uz)
    await call.message.delete()






#10
#################  SHIRINLIKLAR KNOPKA MENU FUNKSIYALARI  #####################
''' Shirinliklar Glavnidagi knopkasi'''
@dp.callback_query_handler(text="shirinliklar")
async def echo(call: CallbackQuery):
    info = f"*😋🍩Shirinlik turini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=shirinliklar_menu_uz)
    await call.message.delete()

# ......................  Shirinliklar ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="pirog")
async def echo(call: CallbackQuery):
    info = f"*🥮Pirog \n Narxi: 35 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/pirog.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=shirinliklar_pirog_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="p_moloko")
async def echo(call: CallbackQuery):
    info = f"*🧁Ptichi-moloko \n Narxi: 15 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz neshta olasiz👇*"
    await call.message.answer_photo(photo=open('images/moloko.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=shirinliklar_ptichimoloko_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="ch_cake")
async def echo(call: CallbackQuery):
    info = f"*🍰Chees-cake \n Narxi: 20 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz neshta olasiz👇*"
    await call.message.answer_photo(photo=open('images/cake.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=shirinliklar_cake_son_uz)
    await call.message.delete()


######  НАЗАД shirinliklar MENU
'''Shirinliklar menu dan Glavni menu ga'''
@dp.callback_query_handler(text="shirinliklardan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

@dp.callback_query_handler(text="shirinliklar_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*😋🍩Shirinlik turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=shirinliklar_menu_uz)
    await call.message.delete()






#11
#################  ICHIMLIKLAR KNOPKA MENU FUNKSIYALARI  #####################
''' Ichimliklar Glavnidagi knopkasi'''
@dp.callback_query_handler(text="ichimliklar")
async def echo(call: CallbackQuery):
    info = f"*Ichimliklik turini tanlang*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_menu_uz)
    await call.message.delete()

# ......................  Ichimliklar ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="sharbat")
async def echo(call: CallbackQuery):
    info = f"*🧃Sharbat turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_uz)
    await call.message.delete()

@dp.callback_query_handler(text="gazli")
async def echo(call: CallbackQuery):
    info = f"*🍷Gazli-ichimlik turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_gazli_uz)
    await call.message.delete()

@dp.callback_query_handler(text="kofe")
async def echo(call: CallbackQuery):
    info = f"*☕️Kove turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_kofe_uz)
    await call.message.delete()

# ......................  Ichimliklar ichidagi sharbat knopka yonalishi ............................
@dp.callback_query_handler(text="olma")
async def echo(call: CallbackQuery):
    info = f"*🍏Olma \n Narxi: 12 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/olma.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="orik")
async def echo(call: CallbackQuery):
    info = f"*🍈O'rik \n Narxi: 12 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/orik.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="anor")
async def echo(call: CallbackQuery):
    info = f"*🫒Anor \n Narxi: 12 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/anor.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="olcha")
async def echo(call: CallbackQuery):
    info = f"*🍒Olcha \n Narxi: 12 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/olcha.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="qulupnay")
async def echo(call: CallbackQuery):
    info = f"*🍓Qulupnay \n Narxi: 12 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/qulupnay.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="banan")
async def echo(call: CallbackQuery):
    info = f"*🍌Banan \n Narxi: 12 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/banan.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_uz)
    await call.message.delete()


# ......................  Ichimliklar ichidagi Gazli knopka yonalishi ............................

@dp.callback_query_handler(text="cola")
async def echo(call: CallbackQuery):
    info = f"*⚫️Coca-Cola \n Narxi: 10 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/cola.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_gazli_son_uz)
    await call.message.delete()


@dp.callback_query_handler(text="pepsi")
async def echo(call: CallbackQuery):
    info = f"*⚫️Pepsi \n Narxi: 10 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/pepsi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_gazli_son_uz)
    await call.message.delete()


@dp.callback_query_handler(text="fanta")
async def echo(call: CallbackQuery):
    info = f"*🟠Fanta \n Narxi: 10 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/fanta.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_gazli_son_uz)
    await call.message.delete()

@dp.callback_query_handler(text="sprite")
async def echo(call: CallbackQuery):
    info = f"*⚪️Sprite \n Narxi: 10 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/sprite.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_gazli_son_uz)
    await call.message.delete()


# ......................  Ichimliklar ichidagi Kofe knopka yonalishi ............................

@dp.callback_query_handler(text="k_qora")
async def echo(call: CallbackQuery):
    info = f"*☕️Qora Kof \n Narxi: 15 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/kofeqora.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_kofe_son_uz)
    await call.message.delete()


@dp.callback_query_handler(text="k_kapuchino")
async def echo(call: CallbackQuery):
    info = f"*☕️Kofe kapuchino \n Narxi: 15 000 so'm \n Miqdorini tanlang yoki kiritingta olasiz👇*"
    await call.message.answer_photo(photo=open('images/kofekapuchina.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_kofe_son_uz)
    await call.message.delete()





######  НАЗАД Ichimliklar MENU
'''Ichimliklar menu dan Glavni menu ga'''
@dp.callback_query_handler(text="ichimliklardan_menu")
async def echo(call: CallbackQuery):
    info = f"*Menu*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_uz)
    await call.message.delete()

@dp.callback_query_handler(text="ichimliklar_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*Ichimlik turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_menu_uz)
    await call.message.delete()


@dp.callback_query_handler(text="ichimliklar_sharbat_son_uz")
async def echo(call: CallbackQuery):
    info = f"*🧃Sharbat turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_uz)
    await call.message.delete()

@dp.callback_query_handler(text="ichimliklar_gazli_son_uz")
async def echo(call: CallbackQuery):
    info = f"*🍷Gazli-ichimlik turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_gazli_uz)
    await call.message.delete()

@dp.callback_query_handler(text="ichimliklar_kofe_son_uz")
async def echo(call: CallbackQuery):
    info = f"*☕️Kofe turini tanlang👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_kofe_uz)
    await call.message.delete()






# SONI
############# UZ raqam ##########
'''Neshtaligini tanlab bolgach Zakaz qabul qilindi yonalishi'''


@dp.callback_query_handler(text="1")
async def echo(call: CallbackQuery):
    await call.answer('Buyurtma qabul qilindi🥳',show_alert=True)

@dp.callback_query_handler(text="2")
async def echo(call: CallbackQuery):
    await call.answer('Buyurtma qabul qilindi🥳',show_alert=True)

@dp.callback_query_handler(text="3")
async def echo(call: CallbackQuery):
    await call.answer('Buyurtma qabul qilindi🥳',show_alert=True)

@dp.callback_query_handler(text="4")
async def echo(call: CallbackQuery):
    await call.answer('Buyurtma qabul qilindi🥳',show_alert=True)

@dp.callback_query_handler(text="5")
async def echo(call: CallbackQuery):
    await call.answer('Buyurtma qabul qilindi🥳',show_alert=True)

@dp.callback_query_handler(text="6")
async def echo(call: CallbackQuery):
    await call.answer('Buyurtma qabul qilindi🥳',show_alert=True)

@dp.callback_query_handler(text="7")
async def echo(call: CallbackQuery):
    await call.answer('Buyurtma qabul qilindi🥳',show_alert=True)

@dp.callback_query_handler(text="8")
async def echo(call: CallbackQuery):
    await call.answer('Buyurtma qabul qilindi🥳',show_alert=True)

@dp.callback_query_handler(text="9")
async def echo(call: CallbackQuery):
    await call.answer('Buyurtma qabul qilindi🥳',show_alert=True)



































####################  UZ Menu va song yonalshi  #####################
'''Buyurtma bosilgandan song Menu ga otadi'''
'''Pastki menu'''
@dp.callback_query_handler(text="заказ")
async def echo(call: CallbackQuery):
    info = f"*😋Menu*"
    i = '*Главный Меню*'
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.answer(i,parse_mode='markdown',reply_markup=pastki_menu_ru)
    await call.message.delete()










####################  RU Menu va song yonalshi  #####################
'''Buyurtma bosilgandan song Menu ga otadi'''
'''Pastki menu'''
@dp.callback_query_handler(text="buyurtma")
async def echo(call: CallbackQuery):
    info = f"*😋Меню*"
    i = 'Главный Меню'
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru,)
    await call.message.answer(i,parse_mode='markdown',reply_markup=pastki_menu_ru)
    await call.message.delete()



###### ru меню
@dp.message_handler(text="Меню")
async def echo(message: types.Message):
    info = f"*Главнй Меню*"
    await message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

###### ru Настройка
@dp.message_handler(text="⚙Настроить заново")
async def echo(message: types.Message):
    info = f"*Начнём заново*"
    await message.answer_photo(photo=open('images/setting.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=til_uz)
    await call.message.delete()

###### ru Заказы
@dp.message_handler(text="Заказы")
async def echo(message: types.Message):
    info = f"*Вашы заказы*"
    await message.answer_photo(photo=open('images/buyurtmalar.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=tilll)
    await call.message.delete()

###### ru Отзывы
@dp.message_handler(text="Отзывы")
async def echo(message: types.Message):
    info = f"*Оставьте ваш отзыв*"
    await message.answer_photo(photo=open('images/ariza.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=None)
    await call.message.delete()

###### ru Информатция о Фасфоод
@dp.message_handler(text="Информатция о FasFood")
async def echo(message: types.Message):
    info = f"*Fast-fud - Фаст-фуд - это тип продуктов массового производства , предназначенных для коммерческой перепродажи, при этом приоритет отдается скорости обслуживания. Это коммерческий термин, ограниченный едой, продаваемой в ресторане или магазине с замороженными, подогретыми или предварительно приготовленными ингредиентами и подаваемой в упаковке на вынос /на вынос. Фаст-фуд был создан как коммерческая стратегия для обслуживания большого количества занятых пассажиров, путешественников и наемных работников . В 2018 году мировая стоимость индустрии быстрого питания оценивалась в 570 миллиардов долларов. *"
    await message.answer_photo(photo=open('images/fass.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=None)
    await call.message.delete()





#ASOSIY MENU
#.............. RU Taomlar royxati va song yonalshi  ..................
'''Menu dan nima olinish bosilgandan song otadigan yonalishlar'''

# 1
#################  ВСЁ KNOPKA MENU FUNKSIYALARI  #####################
'''всё menu knopkasi'''
@dp.callback_query_handler(text="всё")
async def echo(call: CallbackQuery):
    info = f"*Выберите один из них*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=barcha_menu_ru)
    await call.message.delete()

# ......................  Всё мини  меню ..................................
@dp.callback_query_handler(text="картошкафри")
async def echo(call: CallbackQuery):
    info = f"*🍟Картошка-фри \n Цена: 15 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/kartoshkafri.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="деревенский")
async def echo(call: CallbackQuery):
    info = f"*🍟Деревенский-фри \n Цена: 13 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/derevenskoe.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_son_ru)
    await call.message.delete()


'''пица меню'''
@dp.callback_query_handler(text="пицца")
async def echo(call: CallbackQuery):
    info = f"*🍕Какой пиццу выберете👇*"
    await call.message.answer_photo(photo=open('images/pizza.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_menu_pizza_ru)
    await call.message.delete()

@dp.callback_query_handler(text="п_сир")
async def echo(call: CallbackQuery):
    info = f"*🍕Пица сирный \n Цена: 45 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/p_sir.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_pizza_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="п_корона")
async def echo(call: CallbackQuery):
    info = f"*🍕Пица корона \n Цена: 48 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/p_korona.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_pizza_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="п_прастой")
async def echo(call: CallbackQuery):
    info = f"*🍕Пица прастой \n Цена: 50 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/p_oddiy.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_pizza_son_ru)
    await call.message.delete()


######  НАЗАД ВСЁ MENU
'''Всё menu dan Glavni menu ga'''
@dp.callback_query_handler(text="всёdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

'''Sondan Barcha menuga'''
@dp.callback_query_handler(text="всё_son_ort")
async def echo(call: CallbackQuery):
    info = f"*Выберите один из них*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=barcha_menu_ru)
    await call.message.delete()

'''Barcha menu ichdagi Pizza Sonidan pizza menuga'''
@dp.callback_query_handler(text="всё_pizza_son_ort")
async def echo(call: CallbackQuery):
    info = f"*🍕Какой пиццу выберете👇*"
    await call.message.answer_photo(photo=open('images/pizza.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=barcha_menu_pizza_ru)
    await call.message.delete()





#2
#################  НАСТРОЙКА KNOPKA MENU FUNKSIYALARI  #####################
''' Настройка Glavnidagi knopkasi'''
@dp.callback_query_handler(text="настройка")
async def echo(call: CallbackQuery):
    info = f"*❌❌❌❌*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=sozlama_menu_ru)
    await call.message.delete()

# ......................  Sozlama ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="не_сущесствует")
async def echo(call: CallbackQuery):
    info = f"*❌❌❌❌*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=sozlama_menu_ru)
    await call.message.delete()


######  НАЗАД Насторка MENU
'''настройка menu dan Glavni menu ga'''
@dp.callback_query_handler(text="настройкаdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()





#3
#################  Другие KNOPKA MENU FUNKSIYALARI  #####################
''' друние Glavnidagi knopkasi'''
@dp.callback_query_handler(text="другие")
async def echo(call: CallbackQuery):
    info = f"*Выберите один из них*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=boshqa_menu_ru)
    await call.message.delete()

# ......................  Другие mini menunisi ..................................
@dp.callback_query_handler(text="сен")
async def echo(call: CallbackQuery):
    info = f"*🥪Сендвич \n Цена: 32 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/sen.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="чик")
async def echo(call: CallbackQuery):
    info = f"*🥪Чикенс \n Цена: 27 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/chic.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_son_ru)
    await call.message.delete()


'''Шаурма menusi'''
@dp.callback_query_handler(text="шаурма")
async def echo(call: CallbackQuery):
    info = f"*🫔Какой шаурму выберите👇*"
    await call.message.answer_photo(photo=open('images/shaurma.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_menu_shaurma_ru)
    await call.message.delete()

@dp.callback_query_handler(text="кл")
async def echo(call: CallbackQuery):
    info = f"*🫔Классика шаурма \n Цена: 20 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/kla.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_shaurma_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="ос")
async def echo(call: CallbackQuery):
    info = f"*🫔Острый шаурма \n Цена: 25 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/achi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_shaurma_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="гр")
async def echo(call: CallbackQuery):
    info = f"*🫔Грибная шаурма \n Цена: 30 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/qoz.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_shaurma_son_ru)
    await call.message.delete()


######  НАЗАД Другие MENU
'''Boshqa menu dan Glavni menu ga'''
@dp.callback_query_handler(text="другиеdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

'''Sondan Boshqa menuga'''
@dp.callback_query_handler(text="другие_son_ort")
async def echo(call: CallbackQuery):
    info = f"*Выберите один из них👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=boshqa_menu_ru)
    await call.message.delete()

'''Boshqa menu ichdagi shaurma Sonidan shourma menuga'''
@dp.callback_query_handler(text="другие_shaurma_son_ort")
async def echo(call: CallbackQuery):
    info = f"*🫔Какой шаурму выберите👇*"
    await call.message.answer_photo(photo=open('images/shaurma.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=boshqa_menu_shaurma_ru)
    await call.message.delete()




#4
#################  ЛАВАШ KNOPKA MENU FUNKSIYALARI  #####################
''' ЛАВАШ Glavnidagi knopkasi'''
@dp.callback_query_handler(text="лаваш")
async def echo(call: CallbackQuery):
    info = f"*🌯Какой лаваш выберите*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_ru)
    await call.message.delete()

# ......................  Лаваш mini menunisi ..................................
@dp.callback_query_handler(text="л_куриный")
async def echo(call: CallbackQuery):
    info = f"*🌯Выберите тип куриный лаваша👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_tovuq_ru)
    await call.message.delete()

@dp.callback_query_handler(text="л_говядина")
async def echo(call: CallbackQuery):
    info = f"*🌯Выберите тип говядина лаваша👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_gosht_ru)
    await call.message.delete()


'''Lavash tovuq menusi'''
@dp.callback_query_handler(text="л_мин")
async def echo(call: CallbackQuery):
    info = f"*🌯Мини куриные \n Цена: 17 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/l_min.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_tovuq_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="л_сир")
async def echo(call: CallbackQuery):
    info = f"*🌯Сирный куриные \n Цена: 25 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/l_sir.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_tovuq_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="л_ост")
async def echo(call: CallbackQuery):
    info = f"*🌯Острый куриные \n Цена: 23 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/l_qal.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_tovuq_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="л_пр")
async def echo(call: CallbackQuery):
    info = f"*🌯Прастой куриные \n Цена: 15 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/l_odi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_tovuq_son_ru)
    await call.message.delete()


'''Lavash gosht menusi'''
@dp.callback_query_handler(text="ла_мин")
async def echo(call: CallbackQuery):
    info = f"*🌯Мини говядина \n Цена: 18 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/la_min.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_gosht_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="ла_сир")
async def echo(call: CallbackQuery):
    info = f"*🌯Сирный говядина \n Цена: 22 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/la_sir.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_gosht_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="ла_ост")
async def echo(call: CallbackQuery):
    info = f"*🌯Острый говядина \n Цена: 20 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/la_qal.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_gosht_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="ла_пр")
async def echo(call: CallbackQuery):
    info = f"*🌯Прастой говядина \n Цена: 17 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/la_odi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=lavash_gosht_son_ru)
    await call.message.delete()




######  НАЗАД Лаваш MENU
'''Лаваш menu dan Glavni menu ga'''
@dp.callback_query_handler(text="лавашdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

'''Lavash Tovuq ichi goshtlik ichidan --> Lavash t va g ga menuga'''
@dp.callback_query_handler(text="лаваш_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🌯Какой лаваш выберите👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_ru)
    await call.message.delete()

'''Lavash tovuqli sonidan ortga'''
@dp.callback_query_handler(text="лаваш_menu_tovuq_uz")
async def echo(call: CallbackQuery):
    info = f"*🌯Выберите тип куриные лаваша👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_tovuq_ru)
    await call.message.delete()

'''Lavash goshli sonidan ortga'''
@dp.callback_query_handler(text="лаваш_menu_gosht_uz")
async def echo(call: CallbackQuery):
    info = f"*🌯Выберите тип говядина лаваша👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=lavash_menu_gosht_ru)
    await call.message.delete()





#5
#################  HOT-DOG KNOPKA MENU FUNKSIYALARI  #####################
''' Hot-dog Glavnidagi knopkasi'''
@dp.callback_query_handler(text="хотдог")
async def echo(call: CallbackQuery):
    info = f"*🌭Выберите тип Хот-Дог*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=hotdog_menu_ru)
    await call.message.delete()

# ......................  Hot-Dog ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="х_кор")
async def echo(call: CallbackQuery):
    info = f"*🌭Королевскый Хот-Дог \n Цена: 20 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/h_kor.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=hotdog_kor_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="х_пр")
async def echo(call: CallbackQuery):
    info = f"*🌭Прастой Хот-Дог \n Цена: 15 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/h_odi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=hotdog_odi_son_ru)
    await call.message.delete()


######  НАЗАД HOT-DOG MENU
'''Hot-dog menu dan Glavni menu ga'''
@dp.callback_query_handler(text="хотдогdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

@dp.callback_query_handler(text="хотдог_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🌭Выберите тип Хот-Дог👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=hotdog_menu_ru)
    await call.message.delete()





#6
#################  Хагг KNOPKA MENU FUNKSIYALARI  #####################
''' Хагги Glavnidagi knopkasi'''
@dp.callback_query_handler(text="хагги")
async def echo(call: CallbackQuery):
    info = f"*🌮Выберите тип Хагги*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=haggi_menu_ru)
    await call.message.delete()

# ......................  Хагги ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="ха_кур")
async def echo(call: CallbackQuery):
    info = f"*🌮Хагги куриные \n Цена: 29 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/ha_tov.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=haggi_tov_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="ха_гов")
async def echo(call: CallbackQuery):
    info = f"*🌮Хагги говядина \n Цена: 24 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/ha_gosh.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=haggi_gosh_son_ru)
    await call.message.delete()


######  НАЗАД HAGGI MENU
'''Haggi menu dan Glavni menu ga'''
@dp.callback_query_handler(text="хаггиdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

@dp.callback_query_handler(text="хагги_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🌮Выберите тип Хагги👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=haggi_menu_ru)
    await call.message.delete()






#7
#################  TACOS KNOPKA MENU FUNKSIYALARI  #####################
''' Tacos Glavnidagi knopkasi'''
@dp.callback_query_handler(text="тако")
async def echo(call: CallbackQuery):
    info = f"*🥙Выберите тип Тако*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=tacos_menu_ru)
    await call.message.delete()

# ......................  Haggi ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="ле")
async def echo(call: CallbackQuery):
    info = f"*🥙Тако le crispy \n Цена: 35 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/le.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=tacos_le_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="со")
async def echo(call: CallbackQuery):
    info = f"*🥙Тако so gourmand \n Цена: 32 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/so.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=tacos_so_son_ru)
    await call.message.delete()


######  НАЗАД TACOS MENU
'''Tacos menu dan Glavni menu ga'''
@dp.callback_query_handler(text="такоdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

@dp.callback_query_handler(text="тако_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🥙Выберите тип Тако👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=tacos_menu_ru)
    await call.message.delete()






#8
#################  GAMBURGER KNOPKA MENU FUNKSIYALARI  #####################
''' Gamburger Glavnidagi knopkasi'''
@dp.callback_query_handler(text="гамбургер")
async def echo(call: CallbackQuery):
    info = f"*🍔Выберите тип гамбургер*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=gamburger_menu_ru)
    await call.message.delete()

# ......................  Gamburger ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="г_биг")
async def echo(call: CallbackQuery):
    info = f"*🍔Бигбургер \n Цена: 25 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/g_big.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=gamburger_big_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="г_чес")
async def echo(call: CallbackQuery):
    info = f"*🍔Бигчес \n Цена: 29 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/g_ches.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=gamburger_ches_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="г_чик")
async def echo(call: CallbackQuery):
    info = f"*🍔Чикенбургер \n Цена: 32 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/g_chick.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=gamburger_chick_son_ru)
    await call.message.delete()


######  НАЗАД GAMBURGER MENU
'''Gamburger menu dan Glavni menu ga'''
@dp.callback_query_handler(text="гамбургерdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

@dp.callback_query_handler(text="гамбургер_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🍔Выберите тип гамбургер👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=gamburger_menu_ru)
    await call.message.delete()






#9
#################  Клап-sendvich KNOPKA MENU FUNKSIYALARI  #####################
''' Клап-sendvich Glavnidagi knopkasi'''
@dp.callback_query_handler(text="клап")
async def echo(call: CallbackQuery):
    info = f"*🥪Выберите тип Клап-Сендвич*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=clap_menu_ru)
    await call.message.delete()

# ......................  CLAP-sendvich ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="к_кур")
async def echo(call: CallbackQuery):
    info = f"*🥪Клап-Куриный \n Цена: 27 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/chick.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=clap_chick_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="к_гов")
async def echo(call: CallbackQuery):
    info = f"*🥪Клап-говядина \n Цена: 30 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/meat.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=clap_meat_son_ru)
    await call.message.delete()


######  НАЗАД Клап-sendvich MENU
'''клап-sendvich menu dan Glavni menu ga'''
@dp.callback_query_handler(text="клапdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

@dp.callback_query_handler(text="клап_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*🥪Выберите тип Клап-Сендвич👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=clap_menu_ru)
    await call.message.delete()






#10
#################  Сладости KNOPKA MENU FUNKSIYALARI  #####################
''' Сладости Glavnidagi knopkasi'''
@dp.callback_query_handler(text="сладости")
async def echo(call: CallbackQuery):
    info = f"*😋🍩Выберите тип сладости*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=shirinliklar_menu_ru)
    await call.message.delete()

# ......................  Shirinliklar ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="пирог")
async def echo(call: CallbackQuery):
    info = f"*🥮Пирог \n Цена: 35 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/pirog.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=shirinliklar_pirog_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="п_молоко")
async def echo(call: CallbackQuery):
    info = f"*🧁Птичи-молоко \n Цена: 15 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/moloko.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=shirinliklar_ptichimoloko_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="ч_чаке")
async def echo(call: CallbackQuery):
    info = f"*🍰Чес-саке \n Цена: 20 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/cake.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=shirinliklar_cake_son_ru)
    await call.message.delete()


######  НАЗАД shirinliklar MENU
'''Shirinliklar menu dan Glavni menu ga'''
@dp.callback_query_handler(text="сладостиdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

@dp.callback_query_handler(text="сладости_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*😋🍩Выберите тип сладости👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=shirinliklar_menu_ru)
    await call.message.delete()






#11
#################  ICHIMLIKLAR KNOPKA MENU FUNKSIYALARI  #####################
''' Ichimliklar Glavnidagi knopkasi'''
@dp.callback_query_handler(text="напитки")
async def echo(call: CallbackQuery):
    info = f"*Выберите тип напиток*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_menu_ru)
    await call.message.delete()

# ......................  Ichimliklar ichidagi knopka yonalishi ............................
@dp.callback_query_handler(text="натуралные")
async def echo(call: CallbackQuery):
    info = f"*🧃Выберите тип натуралный напиток👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_ru)
    await call.message.delete()

@dp.callback_query_handler(text="газ")
async def echo(call: CallbackQuery):
    info = f"*🍷Выберите тип газировиные напиток👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_gazli_ru)
    await call.message.delete()

@dp.callback_query_handler(text="кофе")
async def echo(call: CallbackQuery):
    info = f"*☕️Выберите тип кофе напиток👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_kofe_ru)
    await call.message.delete()

# ......................  Ichimliklar ichidagi натуралный knopka yonalishi ............................
@dp.callback_query_handler(text="яблока")
async def echo(call: CallbackQuery):
    info = f"*🍏Яблочный \n Цена: 12 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/olma.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="урюк")
async def echo(call: CallbackQuery):
    info = f"*🍈Урюк \n Цена: 12 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/orik.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="граната")
async def echo(call: CallbackQuery):
    info = f"*🫒Гранатовый \n Цена: 12 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/anor.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="вишня")
async def echo(call: CallbackQuery):
    info = f"*🍒Вишнёвый \n Цена: 12 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/olcha.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="клубника")
async def echo(call: CallbackQuery):
    info = f"*🍓Клубничный \n Цена: 12 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/qulupnay.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="банан")
async def echo(call: CallbackQuery):
    info = f"*🍌Банановый \n Цена: 12 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/banan.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_son_ru)
    await call.message.delete()


# ......................  Ichimliklar ichidagi Газировыние knopka yonalishi ............................

@dp.callback_query_handler(text="кола")
async def echo(call: CallbackQuery):
    info = f"*⚫️Кока-Кола \n Цена: 10 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/cola.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_gazli_son_ru)
    await call.message.delete()


@dp.callback_query_handler(text="пепси")
async def echo(call: CallbackQuery):
    info = f"*⚫️Пепси \n Цена: 10 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/pepsi.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_gazli_son_ru)
    await call.message.delete()


@dp.callback_query_handler(text="фанта")
async def echo(call: CallbackQuery):
    info = f"*🟠Фанта \n Цена: 10 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/fanta.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_gazli_son_ru)
    await call.message.delete()

@dp.callback_query_handler(text="спрайт")
async def echo(call: CallbackQuery):
    info = f"*⚪️Спрайт \n Цена: 10 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/sprite.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_gazli_son_ru)
    await call.message.delete()


# ......................  Ichimliklar ichidagi Kofe knopka yonalishi ............................

@dp.callback_query_handler(text="к_чор")
async def echo(call: CallbackQuery):
    info = f"*☕️Чёрный кофе \n Цена: 15 000 so'm \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/kofeqora.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_kofe_son_ru)
    await call.message.delete()


@dp.callback_query_handler(text="к_капучина")
async def echo(call: CallbackQuery):
    info = f"*☕️Капучина кофе \n Цена: 15 000 сум \n Вы можете выбрать или ввести цифр👇*"
    await call.message.answer_photo(photo=open('images/kofekapuchina.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=ichimliklar_kofe_son_ru)
    await call.message.delete()





######  НАЗАД Ichimliklar MENU
'''Ichimliklar menu dan Glavni menu ga'''
@dp.callback_query_handler(text="напиткиdan_menu")
async def echo(call: CallbackQuery):
    info = f"*Меню*"
    await call.message.answer_photo(photo=open('images/menu.jpg','rb'),caption=info,parse_mode='markdown',reply_markup=menu_ru)
    await call.message.delete()

@dp.callback_query_handler(text="напитки_menu_uz")
async def echo(call: CallbackQuery):
    info = f"*Выберите тип напиток👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_menu_ru)
    await call.message.delete()


@dp.callback_query_handler(text="напитки_sharbat_son_uz")
async def echo(call: CallbackQuery):
    info = f"*🧃Выберите тип натуралный напиток👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_sharbat_ru)
    await call.message.delete()

@dp.callback_query_handler(text="напитки_gazli_son_uz")
async def echo(call: CallbackQuery):
    info = f"*🍷Выберите тип газировиные напиток👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_gazli_ru)
    await call.message.delete()

@dp.callback_query_handler(text="напитки_kofe_son_uz")
async def echo(call: CallbackQuery):
    info = f"*☕️Выберите тип кофе напиток👇*"
    await call.message.answer(info,parse_mode='markdown',reply_markup=ichimliklar_kofe_ru)
    await call.message.delete()






# SONI
############# UZ raqam ##########
'''Neshtaligini tanlab bolgach Zakaz qabul qilindi yonalishi'''

@dp.callback_query_handler(text="один")
async def echo(call: CallbackQuery):
    await call.answer('Ваш заказ был принят🥳',show_alert=True)

@dp.callback_query_handler(text="два")
async def echo(call: CallbackQuery):
    await call.answer('Ваш заказ был принят🥳',show_alert=True)

@dp.callback_query_handler(text="три")
async def echo(call: CallbackQuery):
    await call.answer('Ваш заказ был принят🥳',show_alert=True)

@dp.callback_query_handler(text="читири")
async def echo(call: CallbackQuery):
    await call.answer('Ваш заказ был принят🥳',show_alert=True)

@dp.callback_query_handler(text="пят")
async def echo(call: CallbackQuery):
    await call.answer('Ваш заказ был принят🥳',show_alert=True)

@dp.callback_query_handler(text="шест")
async def echo(call: CallbackQuery):
    await call.answer('Ваш заказ был принят🥳',show_alert=True)

@dp.callback_query_handler(text="сем")
async def echo(call: CallbackQuery):
    await call.answer('Ваш заказ был принят🥳',show_alert=True)

@dp.callback_query_handler(text="восем")
async def echo(call: CallbackQuery):
    await call.answer('Ваш заказ был принят🥳',show_alert=True)

@dp.callback_query_handler(text="деветь")
async def echo(call: CallbackQuery):
    await call.answer('Ваш заказ был принят🥳',show_alert=True)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)