'''fasfood buttons'''

from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton



#........................ Til yasash ................................

til_uz = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="🇸🇱 Uzbek"),
		],
		[
			KeyboardButton(text="🇷🇺 Русский"),
		]
	],
	resize_keyboard=True	
	)



#........................ Region tanlash .............................

rayon_uz = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="📍Yunusobot"),
			KeyboardButton(text="📍Mirobod"),
			KeyboardButton(text="📍Uchtepa"),
		],

		[
			KeyboardButton(text="📍Olmazor"),
			KeyboardButton(text="📍Bektimir"),
		],

		[
			KeyboardButton(text="📍Mirzo-Ulugbek")	
		],

		[
			KeyboardButton(text="📍Chilonzor"),
			KeyboardButton(text="📍Yakkasaroy"),
		],

		[
			KeyboardButton(text="📍Sergili"),
			KeyboardButton(text="📍Shayxontoxur"),
			KeyboardButton(text="📍Yashnobot"),
		],
	],
	resize_keyboard=True
	)

rayon_ru = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="📍Юнусабать"),
			KeyboardButton(text="📍Мирабать"),
			KeyboardButton(text="📍Учтепа"),
		],

		[
			KeyboardButton(text="📍Алмазар"),
			KeyboardButton(text="📍Бектемир"),
		],

		[
			KeyboardButton(text="📍Мирзо-Улугбек")	
		],

		[
			KeyboardButton(text="📍Чиланзар"),
			KeyboardButton(text="📍Яккасарай"),
		],

		[
			KeyboardButton(text="📍Сергили"),
			KeyboardButton(text="📍Шайхантахур"),
			KeyboardButton(text="📍Яшнабать"),
		],
	],
	resize_keyboard=True
	)












#....................... Telefon nomer knopkasi ....................................

uz_tel = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Raqamni yuborish📞",request_contact=True), #foydalanuvchi Kontakti jonatiladi
			KeyboardButton(text="Locatsiya yuborish📍",request_location=True), #foydalanuvchi Loctasiyasi jonatiladi
		],
	],
	resize_keyboard=True  #<-- Klavyatura tegidan knopka jjirni bomasligi un chiroylikro chiqishi un
	)

ru_tel = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Отправить номер📞",request_contact=True), #foydalanuvchi Kontakti jonatiladi
			KeyboardButton(text="Отправить местоположение📍",request_location=True), #foydalanuvchi Loctasiyasi jonatiladi
		],
	],
	resize_keyboard=True  #<-- Klavyatura tegidan knopka jjirni bomasligi un chiroylikro chiqishi un
	)





pastki_menu_uz = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Menu"),
			KeyboardButton(text="⚙Boshidan sozlash"),
		],
		[
			KeyboardButton(text="Buyurtmalar"),
			KeyboardButton(text="Mening manzilim",request_location=True),
		],
		[
			KeyboardButton(text="Ariza va shikoyatlar"),
			KeyboardButton(text="FasFood haqida malumot"),
		],
	],
	resize_keyboard=True  #<-- Klavyatura tegidan knopka jjirni bomasligi un chiroylikro chiqishi un	
	)









# 1.......................... Buyurtma berish knopkasi .............................

buyurtma = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="🇸🇱Buyurtma qilish",callback_data='buyurtma'),
			InlineKeyboardButton(text="🇷🇺Заказать",callback_data='заказ'),
		],
	]
)








############ UZ Menu  Taom xilini tanlash va yonalishi va ortga  ###############'''
menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="🍱Barcha Menu",callback_data='bar'), # 1
			InlineKeyboardButton(text="⚙Sozlamalar",callback_data='sozlama'), # 2
		],
		[
			InlineKeyboardButton(text="🍟🍕Boshqa",callback_data='bosh'), # 3
			InlineKeyboardButton(text="🌯Lavash",callback_data='lavash'), # 4
		],

		[
			InlineKeyboardButton(text="🌭Hot-Dog",callback_data='hotdog'), # 5
			InlineKeyboardButton(text="🌮Haggi",callback_data='haggi'), # 6
		],

		[
			InlineKeyboardButton(text="🥙Taco",callback_data='tacos'), # 7
			InlineKeyboardButton(text="🍔Gamburger",callback_data='gamburger'), # 8
		],

		[
			InlineKeyboardButton(text="🥪Clap-Sendvich",callback_data='clap'), # 7
			InlineKeyboardButton(text="🍰🧁🥮Shirinliklar",callback_data='shirinliklar'), # 8
		],

		[
			InlineKeyboardButton(text="🧃🍷☕️Ichimlikllar",callback_data='ichimliklar'), # 7
		],
					]
)



#.1....................... Barcha menu Funksiyalari .............................
barcha_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🍟Kartoshka-fri",callback_data='kartoshkafri'),
 			InlineKeyboardButton(text="🍟Derevenskoe-Fri",callback_data='derevenskoe'),
 		],

 		[
 			InlineKeyboardButton(text="🍕Pizza",callback_data='pizza'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='barchadan_menu'), 
 		]
 	],
 )

barcha_son = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='barcha_son_ort'),
 		],
 	],
 )

barcha_menu_pizza_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🍕Pizza Sirli",callback_data='p_sir'),
 			InlineKeyboardButton(text="🍕Pizza korona",callback_data='p_korona'),
 			InlineKeyboardButton(text="🍕Pizza Oddiy",callback_data='p_oddiy'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='barcha_son_ort'),
 		]
 	],
 )

barcha_pizza_son = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='barcha_pizza_son_ort'),
 		],
 	],
 )






# 2.......................... Sozlamalar knopkasi .............................
sozlama_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[
 		[
 			InlineKeyboardButton(text="Mavjud emas❌🚫 ",callback_data='mavjud'),
 			InlineKeyboardButton(text="🔙Ortka",callback_data='sozlamadan_menu'),
 		],
 	],
 )









#.3....................... Boshqa menu Funksiyalari .............................
boshqa_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🥪Senvich",callback_data='sen'),
 			InlineKeyboardButton(text="🥪Chickens",callback_data='chic'),
 			InlineKeyboardButton(text="🫔Shaurma",callback_data='shaurma'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='boshqadan_menu'), 
 		]
 	],
 )

boshqa_son = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='boshqa_son_ort'),
 		],
 	],
 )

boshqa_menu_shaurma_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🫔Shaurma klassika",callback_data='kla'),
 		],
 		[

 			InlineKeyboardButton(text="🫔Shaurma achiq",callback_data='achi'),
 		],

 		[

 			InlineKeyboardButton(text="🫔Shaurma qoziqorinlik",callback_data='qoz'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='boshqa_son_ort'),
 		]
 	],
 )

boshqa_shaurma_son = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='barcha_shaurma_son_ort'),
 		],
 	],
 )









#.4....................... Lavash menu Funksiyalari .............................
lavash_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌯Tovuqlik lavash",callback_data='l_tovuqlik'),
 			InlineKeyboardButton(text="🌯Goshtlik lavash",callback_data='l_goshtlik'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='lavashdan_menu'), 
 		]
 	],
 )

lavash_menu_tovuq_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌯Mini lavash",callback_data='l_min'),
 			InlineKeyboardButton(text="🌯Sirli lavash",callback_data='l_sir'),
 		],

 		[

 			InlineKeyboardButton(text="🌯Qalampirli lavash",callback_data='l_qal'),
 			InlineKeyboardButton(text="🌯Oddiy lavash",callback_data='l_odi'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='lavash_menu_uz'),
 		]
 	],
 )

lavash_tovuq_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='lavash_menu_tovuq_uz'),
 		],
 	],
 )

lavash_menu_gosht_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌯Mini lavash",callback_data='la_min'),
 			InlineKeyboardButton(text="🌯Sirli lavash",callback_data='la_sir'),
 		],

 		[

 			InlineKeyboardButton(text="🌯Qalampirli lavash",callback_data='la_qal'),
 			InlineKeyboardButton(text="🌯Oddiy lavash",callback_data='la_odi'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='lavash_menu_uz'),
 		]
 	],
 )

lavash_gosht_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='lavash_menu_gosht_uz'),
 		],
 	],
 )









#.5....................... Hot-Dog menu Funksiyalari .............................
hotdog_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌭Korolevski",callback_data='h_kor'),
 			InlineKeyboardButton(text="🌭Oddiy",callback_data='h_odi'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='hotdogdan_menu'), 
 		]
 	],
 )
hotdog_kor_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='hotdog_menu_uz'),
 		],
 	],
 )
hotdog_odi_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='hotdog_menu_uz'),
 		],
 	],
 )









#.6....................... Haggi menu Funksiyalari .............................
haggi_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌮Haggi tovuqli",callback_data='ha_tov'),
 			InlineKeyboardButton(text="🌮Haggi goshtli",callback_data='ha_gosh'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='haggidan_menu'), 
 		]
 	],
 )
haggi_tov_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='haggi_menu_uz'),
 		],
 	],
 )
haggi_gosh_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='haggi_menu_uz'),
 		],
 	],
 )









#.7....................... Tacos menu Funksiyalari .............................
tacos_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🥙Taco le crispy",callback_data='le'),
 			InlineKeyboardButton(text="🥙Taco so gourmand",callback_data='so'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='tacosdan_menu'), 
 		]
 	],
 )
tacos_le_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='tacos_menu_uz'),
 		],
 	],
 )
tacos_so_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='tacos_menu_uz'),
 		],
 	],
 )










#.8....................... Gamburger menu Funksiyalari .............................
gamburger_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🍔Bigburger",callback_data='g_big'),
 			InlineKeyboardButton(text="🍔Bigcheese",callback_data='g_ches'),
 		],

 		[
 			InlineKeyboardButton(text="🍔Chickenburger",callback_data='g_chick'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='gamburgerdan_menu'), 
 		]
 	],
 )
gamburger_big_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='gamburger_menu_uz'),
 		],
 	],
 )
gamburger_ches_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='gamburger_menu_uz'),
 		],
 	],
 )
gamburger_chick_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='gamburger_menu_uz'),
 		],
 	],
 )









#.9....................... Clap-sendvich menu Funksiyalari .............................
clap_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🥪🍗Clap-Chicken",callback_data='c_chick'),
 			InlineKeyboardButton(text="🥪🥩Clap-Meat",callback_data='c_meat'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='clapdan_menu'), 
 		]
 	],
 )
clap_chick_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='clap_menu_uz'),
 		],
 	],
 )
clap_meat_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='clap_menu_uz'),
 		],
 	],
 )










#.10....................... Shirinliklar menu Funksiyalari .............................
shirinliklar_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🥮Pirog",callback_data='pirog'),
 			InlineKeyboardButton(text="🍰Cheese-cake",callback_data='ch_cake'),
 		],

 		[
 			InlineKeyboardButton(text="🧁Ptichi-Moloko",callback_data='p_moloko'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='shirinliklardan_menu'), 
 		]
 	],
 )
shirinliklar_pirog_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='shirinliklar_menu_uz'),
 		],
 	],
 )
shirinliklar_ptichimoloko_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='shirinliklar_menu_uz'),
 		],
 	],
 )
shirinliklar_cake_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='shirinliklar_menu_uz'),
 		],
 	],
 )










#.11....................... Ichimliklarliklar menu Funksiyalari .............................
ichimliklar_menu_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🧃Sharbat",callback_data='sharbat'),
 			InlineKeyboardButton(text="☕️Kofe",callback_data='kofe'),
 		],

 		[
 			InlineKeyboardButton(text="🍷Gazli-ichimliklar",callback_data='gazli'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='ichimliklardan_menu'), 
 		]
 	],
 )
ichimliklar_sharbat_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🍏Olma",callback_data='olma'),
 			InlineKeyboardButton(text="🍈O'rik",callback_data='orik'),
 		],

 		[
 			InlineKeyboardButton(text="🫒Anor",callback_data='anor'),
  			InlineKeyboardButton(text="🍒Olcha",callback_data='olcha'), 		
 		],

 		[
 			InlineKeyboardButton(text="🍓Qulpunoy",callback_data='qulupnay'),
  			InlineKeyboardButton(text="🍌Banan",callback_data='banan'), 		
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='ichimliklar_menu_uz'), 
 		]
 	],
 )

ichimliklar_gazli_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="⚫️Coca-Cola",callback_data='cola'),
 			InlineKeyboardButton(text="⚫️Pepsi",callback_data='pepsi'),
 		],

 		[
 			InlineKeyboardButton(text="🟠Fanta",callback_data='fanta'),
  			InlineKeyboardButton(text="⚪️Sprite",callback_data='sprite'), 		
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='ichimliklar_menu_uz'), 
 		]
 	],
 )

ichimliklar_kofe_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="☕️Qora kofe",callback_data='k_qora'),
 			InlineKeyboardButton(text="☕️Kapuchino",callback_data='k_kapuchino'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='ichimliklar_menu_uz'), 
 		]
 	],
 )


ichimliklar_sharbat_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='ichimliklar_sharbat_son_uz'),
 		],
 	],
 )

ichimliklar_gazli_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='ichimliklar_gazli_son_uz'),
 		],
 	],
 )

ichimliklar_kofe_son_uz = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='1'),
 			InlineKeyboardButton(text="2⃣",callback_data='2'),
 			InlineKeyboardButton(text="3⃣",callback_data='3'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='4'),
 			InlineKeyboardButton(text="5⃣",callback_data='5'),
 			InlineKeyboardButton(text="6⃣",callback_data='6'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='7'),
 			InlineKeyboardButton(text="8⃣",callback_data='8'),
 			InlineKeyboardButton(text="9⃣",callback_data='9'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='ichimliklar_kofe_son_uz'),
 		],
 	],
 )






















pastki_menu_ru = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Меню"),
			KeyboardButton(text="⚙Настроить заново"),
		],
		[
			KeyboardButton(text="Заказы"),
			KeyboardButton(text="Мой(я) адрес",request_location=True),
		],
		[
			KeyboardButton(text="Отзывы"),
			KeyboardButton(text="Информатция о FasFood"),
		],
	],
	resize_keyboard=True  #<-- Klavyatura tegidan knopka jjirni bomasligi un chiroylikro chiqishi un	
	)








############ РУ Menu  Taom xilini tanlash va yonalishi va ortga  ###############'''
menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="🍱Вес меню",callback_data='всё'), # 1
			InlineKeyboardButton(text="⚙Настроить",callback_data='настройка'), # 2
		],
		[
			InlineKeyboardButton(text="🍟🍕Другие",callback_data='другие'), # 3
			InlineKeyboardButton(text="🌯Лаваш",callback_data='лаваш'), # 4
		],

		[
			InlineKeyboardButton(text="🌭Хот-Дог",callback_data='хотдог'), # 5
			InlineKeyboardButton(text="🌮Хагги",callback_data='хагги'), # 6
		],

		[
			InlineKeyboardButton(text="🥙Тако",callback_data='тако'), # 7
			InlineKeyboardButton(text="🍔Гамбургер",callback_data='гамбургер'), # 8
		],

		[
			InlineKeyboardButton(text="🥪Клап-Сендвич",callback_data='клап'), # 7
			InlineKeyboardButton(text="🍰🧁🥮Сладости",callback_data='сладости'), # 8
		],

		[
			InlineKeyboardButton(text="🧃🍷☕️Напитки",callback_data='напитки'), # 7
		],
					]
)



#.1....................... Barcha menu Funksiyalari .............................
barcha_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🍟Картошка-фри",callback_data='картошкафри'),
 			InlineKeyboardButton(text="🍟Деревенское-фри",callback_data='деревенский'),
 		],

 		[
 			InlineKeyboardButton(text="🍕Пицца",callback_data='пицца'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='всёdan_menu'), 
 		]
 	],
 )

barcha_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='всё_son_ort'),
 		],
 	],
 )

barcha_menu_pizza_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🍕Пицца сирный",callback_data='п_сир'),
 			InlineKeyboardButton(text="🍕Пицца корона",callback_data='п_корона'),
 		],

 		[

 			InlineKeyboardButton(text="🍕Пицца пастой",callback_data='п_прастой'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='всё_son_ort'),
 		]
 	],
 )

barcha_pizza_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='всё_pizza_son_ort'),
 		],
 	],
 )






# 2.......................... Sozlamalar knopkasi .............................
sozlama_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[
 		[
 			InlineKeyboardButton(text="Не существуеть❌🚫 ",callback_data='не_сущесствует'),
 			InlineKeyboardButton(text="🔙Назад",callback_data='настройкаdan_menu'),
 		],
 	],
 )









#.3....................... Boshqa menu Funksiyalari .............................
boshqa_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🥪Сендвич",callback_data='сен'),
 			InlineKeyboardButton(text="🥪Чикенс",callback_data='чик'),
 			InlineKeyboardButton(text="🫔Шаурма",callback_data='шаурма'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='другиеdan_menu'), 
 		]
 	],
 )

boshqa_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='другие_son_ort'),
 		],
 	],
 )

boshqa_menu_shaurma_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🫔Шаурма классика",callback_data='кл'),
 		],
 		[

 			InlineKeyboardButton(text="🫔Шаурма острый",callback_data='ос'),
 		],

 		[

 			InlineKeyboardButton(text="🫔Шаурма грибнй",callback_data='гр'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='другие_son_ort'),
 		]
 	],
 )

boshqa_shaurma_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='другие_shaurma_son_ort'),
 		],
 	],
 )









#.4....................... Lavash menu Funksiyalari .............................
lavash_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌯Куриный лаваш",callback_data='л_куриный'),
 			InlineKeyboardButton(text="🌯Говядиный лаваш",callback_data='л_говядина'),
 		],

 		[
 			InlineKeyboardButton(text="🔙назад",callback_data='лавашdan_menu'), 
 		]
 	],
 )

lavash_menu_tovuq_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌯Мини лаваш",callback_data='л_мин'),
 			InlineKeyboardButton(text="🌯Сирный лаваш",callback_data='л_сир'),
 		],

 		[

 			InlineKeyboardButton(text="🌯Острый лаваш",callback_data='л_ост'),
 			InlineKeyboardButton(text="🌯Прастой лаваш",callback_data='л_пр'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='лаваш_menu_uz'),
 		]
 	],
 )

lavash_tovuq_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='лаваш_menu_tovuq_uz'),
 		],
 	],
 )

lavash_menu_gosht_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌯Мини лаваш",callback_data='ла_мин'),
 			InlineKeyboardButton(text="🌯Сирный лаваш",callback_data='ла_сир'),
 		],

 		[

 			InlineKeyboardButton(text="🌯Острый лаваш",callback_data='ла_ост'),
 			InlineKeyboardButton(text="🌯Прастой лаваш",callback_data='ла_пр'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='лаваш_menu_uz'),
 		]
 	],
 )

lavash_gosht_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='лаваш_menu_gosht_uz'),
 		],
 	],
 )









#.5....................... Hot-Dog menu Funksiyalari .............................
hotdog_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌭Королефский",callback_data='х_кор'),
 			InlineKeyboardButton(text="🌭Прастой",callback_data='х_пр'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='хотдогdan_menu'), 
 		]
 	],
 )
hotdog_kor_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='хотдог_menu_uz'),
 		],
 	],
 )
hotdog_odi_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='хотдог_menu_uz'),
 		],
 	],
 )









#.6....................... Haggi menu Funksiyalari .............................
haggi_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🌮Куриный хагги",callback_data='ха_кур'),
 			InlineKeyboardButton(text="🌮Говядиный хагги",callback_data='ха_гов'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='хаггиdan_menu'), 
 		]
 	],
 )
haggi_tov_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='хагги_menu_uz'),
 		],
 	],
 )
haggi_gosh_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Ortka",callback_data='хагги_menu_uz'),
 		],
 	],
 )









#.7....................... Tacos menu Funksiyalari .............................
tacos_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🥙Тако le crispy",callback_data='ле'),
 			InlineKeyboardButton(text="🥙Тако so gourmand",callback_data='со'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='такоdan_menu'), 
 		]
 	],
 )
tacos_le_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='тако_menu_uz'),
 		],
 	],
 )
tacos_so_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='тако_menu_uz'),
 		],
 	],
 )










#.8....................... Gamburger menu Funksiyalari .............................
gamburger_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🍔Бигбургер",callback_data='г_биг'),
 			InlineKeyboardButton(text="🍔Бигчес",callback_data='г_чес'),
 			InlineKeyboardButton(text="🍔Чикенбургер",callback_data='г_чик'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='гамбургерdan_menu'), 
 		]
 	],
 )
gamburger_big_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='гамбургер_menu_uz'),
 		],
 	],
 )
gamburger_ches_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='гамбургер_menu_uz'),
 		],
 	],
 )
gamburger_chick_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='гамбургер_menu_uz'),
 		],
 	],
 )









#.9....................... Clap-sendvich menu Funksiyalari .............................
clap_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🥪🍗Клап-куриный",callback_data='к_кур'),
 			InlineKeyboardButton(text="🥪🥩Клап-говядиный",callback_data='к_гов'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='клапdan_menu'), 
 		]
 	],
 )
clap_chick_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='клап_menu_uz'),
 		],
 	],
 )
clap_meat_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='клап_menu_uz'),
 		],
 	],
 )










#.10....................... Shirinliklar menu Funksiyalari .............................
shirinliklar_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🥮Пирог",callback_data='пирог'),
 			InlineKeyboardButton(text="🧁Птичи-молоко",callback_data='п_молоко'),
 			InlineKeyboardButton(text="🍰Чесе-чаке",callback_data='ч_чаке'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='сладостиdan_menu'), 
 		]
 	],
 )
shirinliklar_pirog_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='сладости_menu_uz'),
 		],
 	],
 )
shirinliklar_ptichimoloko_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='сладости_menu_uz'),
 		],
 	],
 )
shirinliklar_cake_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='сладости_menu_uz'),
 		],
 	],
 )










#.11....................... Ichimliklarliklar menu Funksiyalari .............................
ichimliklar_menu_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🧃Натуралные",callback_data='натуралные'),
 			InlineKeyboardButton(text="☕️Кофе",callback_data='кофе'),
 		],

 		[
 			InlineKeyboardButton(text="🍷Газировыние",callback_data='газ'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='напиткиdan_menu'), 
 		]
 	],
 )
ichimliklar_sharbat_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="🍏Яблочный",callback_data='яблока'),
 			InlineKeyboardButton(text="🍈Урюковый",callback_data='урюк'),
 		],

 		[
 			InlineKeyboardButton(text="🫒Гранатовый",callback_data='граната'),
  			InlineKeyboardButton(text="🍒Вишнёвый",callback_data='вишня'), 		
 		],

 		[
 			InlineKeyboardButton(text="🍓Гулубничный",callback_data='клубника'),
  			InlineKeyboardButton(text="🍌Банановый",callback_data='банан'), 		
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='напитки_menu_uz'), 
 		]
 	],
 )

ichimliklar_gazli_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="⚫️Кока-Кола",callback_data='кола'),
 			InlineKeyboardButton(text="⚫️Пепси",callback_data='пепси'),
 		],

 		[
 			InlineKeyboardButton(text="🟠Фанта",callback_data='фанта'),
  			InlineKeyboardButton(text="⚪️Спрайт",callback_data='спрайт'), 		
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='напитки_menu_uz'), 
 		]
 	],
 )

ichimliklar_kofe_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="☕️Чёрный кофе",callback_data='к_чор'),
 			InlineKeyboardButton(text="☕️Кофе капучина",callback_data='к_капучина'),
 		],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='напитки_menu_uz'), 
 		]
 	],
 )


ichimliklar_sharbat_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='напитки_sharbat_son_uz'),
 		],
 	],
 )

ichimliklar_gazli_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='напитки_gazli_son_uz'),
 		],
 	],
 )

ichimliklar_kofe_son_ru = InlineKeyboardMarkup(
	inline_keyboard=[

 		[
 			InlineKeyboardButton(text="1️⃣",callback_data='один'),
 			InlineKeyboardButton(text="2⃣",callback_data='два'),
 			InlineKeyboardButton(text="3⃣",callback_data='три'),
 		],

 		[
 			InlineKeyboardButton(text="4⃣",callback_data='читири'),
 			InlineKeyboardButton(text="5⃣",callback_data='пят'),
 			InlineKeyboardButton(text="6⃣",callback_data='шест'),
 		],

 		[
 			InlineKeyboardButton(text="7⃣",callback_data='сем'),
 			InlineKeyboardButton(text="8⃣",callback_data='восем'),
 			InlineKeyboardButton(text="9⃣",callback_data='деветь'),
 			],

 		[
 			InlineKeyboardButton(text="🔙Назад",callback_data='напитки_kofe_son_uz'),
 		],
 	],
 )
