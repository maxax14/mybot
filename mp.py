import telebot
import re
import const
bot = telebot.TeleBot('845158446:AAHqFOnog759zdBsvnjhALg1Edzq6tv2Ym4')
print(bot.get_me())
@bot.message_handler(commands = ["start"])
def start(message):
	
	stop_key = telebot.types.InlineKeyboardMarkup()
	editlink =  telebot.types.InlineKeyboardButton(text= "Изменить ссылку", callback_data= "edit_link")
	subnav = telebot.types.InlineKeyboardButton(text= 'Найти аниме с сабами', callback_data= "sub_search")
	stop_key.add(editlink)
	stop_key.add(subnav)
	
	
	bot.send_message(message.from_user.id, ''' Привет! Ты в главном меню! ''', reply_markup= stop_key)
		
		
@bot.callback_query_handler(func=lambda call: True)
def call_buton(call):
	if(call.data == 'edit_link'):
		editlink =  telebot.types.InlineKeyboardButton(text= "Изменить ссылку", callback_data= "edit_link")
		bot.send_message(call.from_user.id, "Пришли ссылку")
		const.ms = True	
		
	if(call.data == 'sub_search'):
		subnav = telebot.types.InlineKeyboardButton(text= 'Найти аниме с сабами', callback_data= "sub_search")
		bot.send_message(-1001237057642, "запрос")
		bot.send_message(call.from_user.id, "идет разработка..")
		const.zapros = True
			
@bot.message_handler(content_types = ["text"])
def start(message):
	if(const.ms == True):
		try:
			string = message.text
			aa = re.sub('/AnimeSAV/', '/c/1132588512/', string,count = 0)
			bot.send_message(message.from_user.id, aa)
			const.ms = False
			
		except:
			bot.send_message(message.from_user.id, "Смоук лох)")
			const.ms = False
			pass
		
			
			
			
		
			
		
						
bot.polling(none_stop = True)
