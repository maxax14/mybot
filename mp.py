bot_version = "2.0"

import telebot
import pickle
import re
import random
import datetime
import os
import math

import const
bot = telebot.TeleBot('818916051:AAE5fi1XFmwuB_cQ8H6RHGvnJ28_zDNKVV4')
print(bot.get_me())





@bot.message_handler(commands=['aaa'])
def text(message):
	bot.send_message(message.from_user.id, "падай")
	const.aut = True


#ответ на команду help
@bot.message_handler(commands=['help'])
def text(message):
	    if(message.from_user.id in const.admins):
	    	bot.send_message(message.from_user.id, const.help)
	    else:
	    	bot.send_message(message.from_user.id, 'Я бот Меги Anime Company @acorporation, извини, но  ты не администратор и у тебя нет доступа к моим функциям')
	    	






#ответ на команду dop_menu

@bot.message_handler(commands = ['dop_menu'])
def start(message):
	if(message.from_user.id in const.admins):
		
		dop_key = telebot.types.InlineKeyboardMarkup() #создаем "вместилище" кнопок
		
		editbirza =  telebot.types.InlineKeyboardButton(text= 'Измен. тек. /birza', callback_data= 'birzatext')
		edit_list = telebot.types.InlineKeyboardButton(text= 'Измен. текст. /list', callback_data= 'listtext')
		editosnova =  telebot.types.InlineKeyboardButton(text= 'Измен. тек. /osnova', callback_data= 'osnovatext') #создаем кнопки
		
		dop_key.add(editbirza)
		dop_key.add(edit_list)
		dop_key.add(editosnova)
		bot.send_message(message.from_user.id, ''' Доп. меню, чтобы вернутся в основное пиши /start''', reply_markup= dop_key) #подключаем кгопки и отправляем с сообщением



#ответ на команду start                                            	    		    	
@bot.message_handler(commands=['start'])
def start(message):
	if(message.from_user.id in const.admins):
		
		
		
# все также как и в dop_menu

		
		stop_key = telebot.types.InlineKeyboardMarkup()
		printop =  telebot.types.InlineKeyboardButton(text= 'Настройки', callback_data= 'settings')
		editverh = telebot.types.InlineKeyboardButton(text= 'Изменить верхушку', callback_data= 'editedverh')
		editniz = telebot.types.InlineKeyboardButton(text= 'Изменить низ', callback_data= 'editniz')
		addgif = telebot.types.InlineKeyboardButton(text= 'Изменить GIF', callback_data= 'editgif')
		addop = telebot.types.InlineKeyboardButton(text= 'Редакт. соб. открытия', callback_data= 'adsop')
		addcl = telebot.types.InlineKeyboardButton(text= 'Редакт. соб. закрытия', callback_data= 'adscl')
		addgo = telebot.types.InlineKeyboardButton(text= 'Редакт. соб. готовности', callback_data= 'adsgo')
		skin = telebot.types.InlineKeyboardButton(text= 'Сброс', callback_data= 'sbros')
		chan = telebot.types.InlineKeyboardButton(text= 'Задать канал в 0-1к', callback_data= 'zadat')
		adm = telebot.types.InlineKeyboardButton(text= 'Добавить администратора', callback_data= 'addad')
		
		
		
		
		stop_key.add(skin)
		
		stop_key.add(printop, editniz)
		stop_key.add(editverh)
		stop_key.add(addgif)
		stop_key.add(addop, addcl)
		stop_key.add(addgo)
		stop_key.add(chan)
		stop_key.add(adm)
		
		
		
		
		
		
		bot.send_message(message.from_user.id, ''' Привет! Ты в главном меню! 
    /dop_menu - доп меню
	/start - вызвать клавиатуру
	/clear - очистить список автоподачи''', reply_markup= stop_key)
	
	else:
		
		usermenu = telebot.types.InlineKeyboardMarkup()
		addauto =  telebot.types.InlineKeyboardButton(text= 'Добавить канал', callback_data= 'add')
		delete =  telebot.types.InlineKeyboardButton(text= 'Удалить канал', callback_data= 'delete')
		
		usermenu.add(addauto)
		usermenu.add(delete)

		bot.send_message(message.from_user.id, ''' Привет! Ты в главном меню!''', reply_markup= usermenu)
		
	
#ответ на команду add... назначение админа по команде
   		    		    	
	    				    			
@bot.message_handler(commands=['addrrgsgrafgwadf'])
def start(message):
    const.admins.append(message.from_user.id)
    print(const.admins)
    bot.send_message(message.from_user.id, 'Приветствую вы админ')
    
    
	    	

#ответ на команду osnova
@bot.message_handler(commands=['osnova'])
def start(message):
    bot.send_message (message.chat.id, const.osnova)
 
          
#ответ на команду list  
  
@bot.message_handler(commands=['list'])
def start(message):
    bot.send_message (message.chat.id, const.list_chan)
    
    
@bot.message_handler(commands=['add_auto'])
def start(message):
	bot.send_message (message.from_user.id, '''' Привет, я бот меги @acorporation!
	если ты ховешь подать заявку в автоподачу нажми ниже!''')
	const.aut = True

  
 #ответ на команду birza 
 
@bot.message_handler(commands=['birza'])
def start(message):
    bot.send_message (message.chat.id, const.birza , parse_mode = 'Markdown')


#ответ на команду open

@bot.message_handler(commands=['open'])
def start(message):
    if(message.from_user.id in const.admins):
        const.setings['open_id'] = message.message_id 
        
# выше запоминаем айди открытия        
       
        bot.send_message(message.chat.id, const.setings['Открытие'])
       
        bot.pin_chat_message(message.chat.id, message.message_id +1)
        try:
        	for ty in const.autt:
        		bot.send_message(message.chat.id, '{a}'.format(a = ty))
        except:
        	pass
        
  			
        		
        
        		
        	
    
    	
    		

#ответ на команду close

@bot.message_handler(commands=['close'])
def start(message):
	
    if(message.from_user.id in const.admins):
        const.megaac = []
        const.setings['close_id'] = message.message_id
        
        
        
        
        #выше запоминаем айди закрытия
        
        
        bot.send_message(message.chat.id, const.setings['Закрытие'])
        


        
        for d in range(const.setings['open_id'], const.setings['close_id']): #чекаем айди и начинаем форвард сообщений
        
        
            try:
                mes = bot.forward_message(-1001469250576, message.chat.id, d)
            except telebot.apihelper.ApiException:
                pass
            if (mes.text != ''):
                if (mes.content_type == 'text'):
                	acmeg = re.findall(r'\[.+\]\(.+?\.me/.+?\)', mes.text)
                	for ms in acmeg:
                		if ms not in const.megaac:
                			const.megaac.append(ms)
                			
          
            	
            			
        else:
        	
        	
            f = const.setings['Гиф_меги'] + const.setings['Заголовок'] + "\n" + "\n"+ const.ch + "\n" + "\n"
            for innt in const.megaac:
            
                f = f  + str(innt)  + "\n"
            else:
                bot.send_message(message.chat.id, f + "\n" + "\n" + const.ch + "\n" + '\n' + const.setings['Окончание'] + "\n", parse_mode='Markdown')

                		
                
                                                
#сообщение готовности
                
                bot.send_message(message.chat.id, const.setings['Готовность'], parse_mode='Markdown')
                bot.send_message(message.chat.id, '''Каналов в меге: {ch}'''.format(ch = len(const.megaac)))
                
                	
            
                                    
#вытягиваем юзер и отправляем                
                
                for huinya in const.megaac:
                	chuser = re.findall(r'\(.+?\.me/(.+?)\)', huinya)
                	         	
                	aaa = "@{ch}".format(ch = chuser[0])
                	
                	
                	try:
                		bot.send_message(aaa, f + "\n" + "\n" + const.ch + "\n" + '\n' + const.setings['Окончание'] + "\n", parse_mode='Markdown')
                		bot.send_message(message.from_user.id,  '''Каналов в меге: {kolvo}
Мега разослана на: {razos}
Попыток сделано: {kolvo}'''.format(kolvo = len(const.megaac), razos = len(chuser)))
                		
                		
    		            		              		            		              		
                	except telebot.apihelper.ApiException as exc:
                		print('SYSTEM ERROR')
                	
	 

	 
	 

                
                                                
# закрепляем и выводим колво каналов   

                          
                bot.pin_chat_message(message.chat.id, message.message_id +3)

                
          


    else:
    	bot.send_message(message.chat.id, 'шота нитак')

  
  
  
   
  
    	   	
# тут подключены основные кнопки    	
@bot.callback_query_handler(func=lambda call: True)
def call_buton(call):
	
#кнопка сведения
	
	if(call.data == 'settings'):
		printop =  telebot.types.InlineKeyboardButton(text= 'Сведения', callback_data= 'settings')
		bot.edit_message_text('Заголовок меги:\n' + str(const.setings['Заголовок']) + '\n\nОкончание меги:\n' + str(const.setings['Окончание']) + '\n\nТекст открытия сбора:\n' + const.setings['Открытие'] +'\n\nТекст закрытия сбора:\n' + const.setings['Закрытие'] + '\n\nТекст готовности меги:\n' + const.setings['Готовность'],call.from_user.id, call.message.message_id , reply_markup=printop)

		
						
# кнопка редакт. верх
		
	if(call.data == 'editedverh'):
		editverh =  telebot.types.InlineKeyboardButton(text= 'верх', callback_data= 'editedverh')
		bot.send_message(call.from_user.id, 'Пришли текст верхушки')
		const.verh = True

		
						
#кнопка редакт. низ		
				
	if(call.data == 'editniz'):
		editniz = telebot.types.InlineKeyboardButton(text= 'Изменить низ', callback_data= 'editniz')
		bot.send_message(call.from_user.id, 'Пришли текст Низа меги')
		const.niz = True	

		
						
#кнопка редакт. гиф		
		
	if(call.data == 'editgif'):
		addgif = telebot.types.InlineKeyboardButton(text= 'Изменить GIF', callback_data= 'editgif')
		bot.send_message(call.from_user.id, 'Пришли ссылку на gif в формате [ ](ссылка)')
		const.gif = True

		
						
# кнопка редакт. соб. открытия			            	            
	if(call.data == 'adsop'):
		addop = telebot.types.InlineKeyboardButton(text= 'Редакт. соб. открытия', callback_data= 'adsop')		     
		bot.send_message(call.from_user.id, 'Пришли текст открытия меги')
		const.op = True
	
		
				
		
#кнопка редакт. соб. закрытия		
		
	if(call.data == 'adscl'):
		addcl = telebot.types.InlineKeyboardButton(text= 'Редакт. соб. закрытия', callback_data= 'adscl')		     
		bot.send_message(call.from_user.id, 'Пришли текст открытия меги')
		const.cl = True		



#кнопка редакт. соб. готовности
				
	if(call.data == 'adsgo'):
		addgo = telebot.types.InlineKeyboardButton(text= 'Редакт. соб. готовности', callback_data= 'adsgo')		  
		bot.send_message(call.from_user.id, 'Пришли текст готовности меги')
		const.go = True		




#КНОПКА СБРОС

	if(call.data == 'sbros'):
		skin = telebot.types.InlineKeyboardButton(text= 'Сброс', callback_data= 'sbros')
		const.setings =  {'Заголовок': 'пусто', 'Открытие': 'пусто', 'Закрытие': 'пусто', 'Окончание': 'пусто', 'Готовность': 'пусто', 'open_id': '0', 'close_id': '0', 'Гиф_меги': '[⁠]( )'}
		bot.send_message(call.from_user.id, 'Сброшено! нажмите /start')
	if(call.data == 'birzatext'):
		editbirza =  telebot.types.InlineKeyboardButton(text= 'Измен. тек. /birza', callback_data= 'birzatext')
		bot.send_message(call.from_user.id, 'Пришли текст для команды /birza')
		const.birz = True





#кнопка редакт. тек. list

	if(call.data == 'listtext'):
		edit_list = telebot.types.InlineKeyboardButton(text= 'Измен. текст. /list', callback_data= 'listtext')
		bot.send_message(call.from_user.id, 'Пришли текст для команды /list')
		const.lister = True
		
		
		
		
#кнопка редакт. тек. osnova		
						
	if(call.data == 'osnovatext'):
		editosnova =  telebot.types.InlineKeyboardButton(text= 'Измен. тек. /osnova', callback_data= 'osnovatext')
		
		
		bot.send_message(call.from_user.id, 'Пришли текст для команды /osnova')
		const.osn = True



#кнопка зад. канал в меге		
						
	if(call.data == 'zadat'):
		chan = telebot.types.InlineKeyboardButton(text= 'Задать канал в 0-1к', callback_data= 'zadat')
		bot.send_message(call.from_user.id, 'Пришли канал в формате [СмайлНазвание](ссылка)')
		const.cha = True
		
				
						
										
#кнопка доб. админа
		
	if(call.data == 'addad'):
		adm = telebot.types.InlineKeyboardButton(text= 'Добавить администратора', callback_data= 'addad')
		bot.send_message(call.from_user.id, 'Перешли сообщение от того кого хочешь сделать администратором')
		const.addadmin = True
		

		
# кнопка автоподачи
		
	if(call.data == 'add'):
		addauto =  telebot.types.InlineKeyboardButton(text= 'Добавить канал', callback_data= 'add')
		bot.send_message(call.from_user.id, 
		'''Пришли заявку в формате: [*Смайл*Название](ссылка
		
		Пожалуйста прочти все!
		следите за тем чтобыв заявке не было ошибок!
		обязательно выдайте боту админку в канале, для автопостинга меги! это ну очень важно!
		спасибо за понимание''')
		const.aut = True
		
	if(call.data == 'delete'):
		delete =  telebot.types.InlineKeyboardButton(text= 'Удалить канал', callback_data= 'delete')
		bot.send_message(call.from_user.id, 'для удаления пришли заявку в формате: [*Смайл*Название](ссылка)')
		const.dell = True
		
#ответ на текст

@bot.message_handler(content_types=['text'])
def text(message):

        
        
#сведения о настройках	
	
    if(message.text == 'Сведения') and (message.from_user.id in const.admins):
        bot.send_message(message.from_user.id, 'Заголовок меги:\n' + str(const.setings['Заголовок']) + '\n\nОкончание меги:\n' + str(const.setings['Окончание']) + '\n\nТекст открытия сбора:\n' + const.setings['Открытие'] +'\n\nТекст закрытия сбора:\n' + const.setings['Закрытие'] + '\n\nТекст готовности меги:\n' + const.setings['Готовность'])

        
                        

#редактируем окончание
    
    if(const.niz == True) and (message.from_user.id in const.admins):
        const.setings['Окончание'] = str(message.text)
        bot.send_message(message.from_user.id,'Изменения приняты.')
        bot.send_message(message.from_user.id, 'Заголовок меги:\n' + str(const.setings['Заголовок']) + '\n\nОкончание меги:\n' + str(const.setings['Окончание']) + '\n\nТекст открытия сбора:\n' + const.setings['Открытие'] +'\n\nТекст закрытия сбора:\n' + const.setings['Закрытие'] + '\n\nТекст готовности меги:\n' + const.setings['Готовность'])
        
        
        const.niz = False




#редактируем соб. открытия   
     
    if(const.op == True) and (message.from_user.id in const.admins):
        const.setings['Открытие'] = str(message.text)
        bot.send_message(message.from_user.id,'Изменения приняты.')
        bot.send_message(message.from_user.id, 'Заголовок меги:\n' + str(const.setings['Заголовок']) + '\n\nОкончание меги:\n' + str(const.setings['Окончание']) + '\n\nТекст открытия сбора:\n' + const.setings['Открытие'] +'\n\nТекст закрытия сбора:\n' + const.setings['Закрытие'] + '\n\nТекст готовности меги:\n' + const.setings['Готовность'])
        
        const.op = False     



#редактируем соб. закрытия   
     
    if(const.cl == True) and (message.from_user.id in const.admins):
        const.setings['Закрытие'] = str(message.text)
        bot.send_message(message.from_user.id,'Изменения приняты.')
        bot.send_message(message.from_user.id, 'Заголовок меги:\n' + str(const.setings['Заголовок']) + '\n\nОкончание меги:\n' + str(const.setings['Окончание']) + '\n\nТекст открытия сбора:\n' + const.setings['Открытие'] +'\n\nТекст закрытия сбора:\n' + const.setings['Закрытие'] + '\n\nТекст готовности меги:\n' + const.setings['Готовность'])
        

        

        const.cl = False          

 
     
             
#добавляем gif

    if(const.gif == True) and (message.from_user.id in const.admins):
        const.setings['Гиф_меги'] = str(message.text)
        bot.send_message(message.from_user.id,'Изменения приняты.')
        bot.send_message(message.from_user.id, const.setings['Гиф_меги'])
        
        const.gif = False 




               
#редактируем соб. готовности

    if(const.go == True) and (message.from_user.id in const.admins):
        const.setings['Готовность'] = str(message.text)
        bot.send_message(message.from_user.id,'Изменения приняты.')
        bot.send_message(message.from_user.id, 'Заголовок меги:\n' + str(const.setings['Заголовок']) + '\n\nОкончание меги:\n' + str(const.setings['Окончание']) + '\n\nТекст открытия сбора:\n' + const.setings['Открытие'] +'\n\nТекст закрытия сбора:\n' + const.setings['Закрытие'] + '\n\nТекст готовности меги:\n' + const.setings['Готовность'])
        
        
               
               
        

        const.go = False 

         





#редактируем заг. меги
			
    if(const.verh == True) and (message.from_user.id in const.admins):
        const.setings['Заголовок'] = str(message.text)
        
        
        bot.send_message(message.from_user.id,'Изменения приняты.')
        bot.send_message(message.from_user.id, 'Заголовок меги:\n' + str(const.setings['Заголовок']) + '\n\nОкончание меги:\n' + str(const.setings['Окончание']) + '\n\nТекст открытия сбора:\n' + const.setings['Открытие'] +'\n\nТекст закрытия сбора:\n' + const.setings['Закрытие'] + '\n\nТекст готовности меги:\n' + const.setings['Готовность'])
        

        const.verh = False




#редактируем соб. на комм. birza

    if(const.birz == True) and (message.from_user.id in const.admins):
        const.birza = str(message.text)
        bot.send_message(message.from_user.id,'Изменения приняты.')
        
        const.birz = False
                    
  
                                                              
#редактируем срб. на комм. list
		
    if(const.lister == True) and (message.from_user.id in const.admins):
        const.list_chan = str(message.text)
        bot.send_message(message.from_user.id,'Изменения приняты.')
        
        const.lister = False
                             
                                        
                                                        
#редактируем срб. на комм. osnova     		
    if(const.osn == True) and (message.from_user.id in const.admins):
        const.osnova = str(message.text)
        bot.send_message(message.from_user.id,'Изменения приняты.')
        
        const.osn = False
#автоподача
        
    if(const.aut == True):
    	mes = message.text
    	acmeg = re.findall(r'\[.+\]\(.+?\.me/.+?\)', mes)
    	try:
    		for ms in acmeg:
    			if  ms not in const.autt:
    				
    				const.autt.append(ms)
    				
    				
    				bot.send_message(message.from_user.id,  '''Канал 
    				
    				{ch} 
    				
    				добавлен'''.format(ch = ms))
    				
    		
    				const.aut = False
    				
    					
    				
    				


    	
    			elif  ms  in const.autt:
    				bot.send_message(message.from_user.id, "Этот канал уже добавлен в автоподачу")
    				const.aut = False
    				pass
    			
    	except:
    		const.aut = False
    		pass
    		
    if(const.dell == True):
    	mee = message.text
    	acm = re.findall(r'\[.+\]\(.+?\.me/.+?\)', mee)
    	try:
    		for mis in acm:
    			if mis in const.autt:
    				const.autt.remove(mis)
    				bot.send_message(message.from_user.id, '''заявка 
    				
    				{m} 
    				
    				удалена'''.format(m = mis))
    			
    				const.dell = False
    				
    				
    		
    			elif  mis  not in const.autt:
    				bot.send_message(message.from_user.id, "Я не нашел такой заявки")
    				const.dell = False
    				pass
    				
    			elif const.autt == []:
    				bot.send_message(message.from_user.id, "Нечего удалять")
    				const.dell = False			
    		
    	except:
    		const.dell = False
    		pass   			
	    			
 		
                          
# редактируем канал в меге

    if(const.cha == True) and (message.from_user.id in const.admins):
        const.ch = str(message.text)
        bot.send_message(message.from_user.id,'Изменения приняты.')
        bot.send_message(message.from_user.id, const.ch)
        
        const.cha = False		
 
            	          		
            	          		           	          		
            	          		           	          		           	          		
            	          		           	          		           	          		           	          		           	          		
#вытаскиваем ID для добавления админа 
 
    if(const.addadmin == True) and (message.from_user.id in const.admins):
        const.admins.append(message.forward_from.id)
        bot.send_message(message.forward_from.id, 'Поздравляю!' +  "\n" + '@' + str(message.from_user.username) + "\n" + "сделал тебя администратором бота")
        
        
        bot.send_message(message.from_user.id , 'Нового администратора добавлено\nID:' + str(message.forward_from.id) + '\nUsername: @' + str(message.forward_from.username) + '\nName: ' + str(message.forward_from.first_name))
        
        
        const.addadmin = False


        	
            	          	          	          	
bot.polling(none_stop=True)
            	
  
         
