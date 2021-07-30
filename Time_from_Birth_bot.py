import telebot
bot = telebot.TeleBot('')
from time import *
def is_valid_data(data, nd, nm, ny):
    if len(data) == 3:
        if data[0].isdigit() == True and data[1].isdigit() == True and data[2].isdigit() == True:
            data[0], data[1], data[2] = int(data[0]), int(data[1]), int(data[2])
            if is_valid_thdays(nd, nm, ny, data[0], data[1], data[2]) == True:
                if leap_year(data[2]) == True:
                    if data[1] == 2:
                        if data[0] <= 29 and data[0] > 0:
                            return True
                        else:
                            return False
                    elif data[1] > 0 and data[1] <= 5 and data[1] % 2 == 1 or data[1] >= 6 and data[1] <= 12 and data[1] % 2 == 0:
                        if data[0] <= 31 and data[0] > 0:
                            return True
                        else:
                            return False
                    elif data[1] > 0 and data[1] <= 5 and data[1] % 2 == 0 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 1:
                        if data[0] <= 30 and data[0] > 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    if data[1] == 2:
                        if data[0] <= 28 and data[0] > 0:
                            return True
                        else:
                            return False
                    elif data[1] > 0 and data[1] <= 5 and data[1] % 2 == 1 or data[1] >= 6 and data[1] <= 12 and data[1] % 2 == 0:
                        if data[0] <= 31 and data[0] > 0:
                            return True
                        else:
                            return False
                    elif data[1] > 0 and data[1] <= 5 and data[1] % 2 == 0 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 1:
                        if data[0] <= 30 and data[0] > 0:
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False
def is_valid_thdays(d, m, y, nd, nm, ny):
    if y == ny:
        if m == nm:
            if d >= nd:
                return True
            else:
                return False
        if m > nm:
            return True
    if y > ny:
        return True
    else:
        return False
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет! чтобы узнать список команд, напиши /cmd.')
    elif message.text == '/cmd':
        bot.send_message(message.from_user.id, '1. Чтобы активировать бота, надо написать /start. \n2. Чтобы посмотреть список команд, надо написать /cmd. \n3. Чтобы узнать ближайшую тысячу дней со дня рождения, надо написать /1000days. \n4. Чтобы узнать сколько дней тебе со дня рождения, надо написать /days. \n4. Чтобы узнать сколько месяцев тебе со дня рождения, надо написать /months. \n6. Чтобы узнать сколько недель тебе со дня рождения, надо написать /weeks.')
    elif message.text == '/1000days':
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать ближайшую тысячу дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days1000)
    elif message.text == '/days':
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days)
    elif message.text == '/months':
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе месяцев, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, months)
    elif message.text == '/weeks':
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе недель, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, weeks)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, напиши правильную комманду, например /cmd.')
def days1000(message):
    now_data = gmtime(time())
    now_year, now_mon, now_day, daycnt, th, thousands = now_data[0], now_data[1], now_data[2], 0, 0, 0
    data = message.text.split('.')
    if data == ['/cmd']:
        bot.send_message(message.from_user.id, '1. Чтобы активировать бота, надо написать /start. \n2. Чтобы посмотреть список команд, надо написать /cmd. \n3. Чтобы узнать ближайший юбилей тысяч дней со дня рождения, надо написать /1000days. \n4. Чтобы узнать сколько дней тебе со дня рождения, надо написать /days. \n4. Чтобы узнать сколько месяцев тебе со дня рождения, надо написать /months. \n6. Чтобы узнать сколько недель тебе со дня рождения, надо написать /weeks.')
        bot.register_next_step_handler(message, get_text_messages)
    elif data == ['/1000days']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать ближайшую тысячу дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days1000)
    elif data == ['/days']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days)
    elif data == ['/weeks']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе недель, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, weeks)
    elif data == ['/months']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе месяцев, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, months)
    elif is_valid_data(data, now_day, now_mon, now_year) != True:
        bot.send_message(message.from_user.id, 'Не корректный ввод, введи правильную дату, например: 01.01.2000.')
        bot.register_next_step_handler(message, days1000)
    else:
        data = [int(s) for s in data]
        if now_year == data[2] and now_mon == data[1] and now_day == data[0]:
            now_day += 1
        while is_valid_thdays(data[0], data[1], data[2], now_day, now_mon, now_year) != True:
            while daycnt < 1000:
                daycnt += 1
                data[0] += 1
                if data[1] == 12 and data[0] == 32:
                    data[0], data[1] = 1, 1
                    data[2] += 1
                if data[1] <= 5 and data[1] % 2 == 1 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 0:
                    if data[0] == 32:
                        data[0] = 1
                        data[1] += 1
                if data[1] <= 5 and data[1] % 2 == 0 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 1:
                    if data[0] == 31:
                        data[0] = 1
                        data[1] += 1
                if data[1] == 2 and leap_year(data[2]) == True:
                    if data[0] == 30:
                        data[0] = 1
                        data[1] += 1
                if data[1] == 2 and leap_year(data[2]) == False:
                    if data[0] == 29:
                        data[0] = 1
                        data[1] += 1
            daycnt = 0
            th += 1
        if len(str(data[0])) == 1 and len(str(data[1])) != 1:
            data[0] = '0' + str(data[0])
        if len(str(data[0])) == 1 and len(str(data[1])) == 1:
            data[0], data[1] = '0' + str(data[0]), '0' + str(data[1])
        if len(str(data[0])) != 1 and len(str(data[1])) == 1:
            data[1] = '0' + str(data[1])
        part1 = str(th * 1000) + ' дней тебе будет '
        part2 = str(data[0]) + '.' + str(data[1]) + '.' + str(data[2]) + '.'
        bot.send_message(message.from_user.id, part1 + part2)
        bot.register_next_step_handler(message, get_text_messages)
def days(message):
    now_data = gmtime(time())
    now_year, now_mon, now_day, daycnt, th, thousands = now_data[0], now_data[1], now_data[2], 0, 0, 0
    data = message.text.split('.')
    if data == ['/cmd']:
        bot.send_message(message.from_user.id, '1. Чтобы активировать бота, надо написать /start. \n2. Чтобы посмотреть список команд, надо написать /cmd. \n3. Чтобы узнать ближайший юбилей тысяч дней со дня рождения, надо написать /1000days. \n4. Чтобы узнать сколько дней тебе со дня рождения, надо написать /days. \n4. Чтобы узнать сколько месяцев тебе со дня рождения, надо написать /months. \n6. Чтобы узнать сколько недель тебе со дня рождения, надо написать /weeks.')
        bot.register_next_step_handler(message, get_text_messages)
    elif data == ['/1000days']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать ближайшую тысячу дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days1000)
    elif data == ['/days']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days)
    elif data == ['/weeks']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе недель, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, weeks)
    elif data == ['/months']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе месяцев, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, months)
    elif is_valid_data(data, now_day, now_mon, now_year) != True:
        bot.send_message(message.from_user.id, 'Не корректный ввод, введи правильную дату, например: 01.01.2000.')
        bot.register_next_step_handler(message, days)
    else:
        data = [int(s) for s in data]
        while is_valid_thdays(data[0], data[1], data[2], now_day, now_mon, now_year) != True:
            daycnt += 1
            data[0] += 1
            if data[1] == 12 and data[0] == 32:
                data[0], data[1] = 1, 1
                data[2] += 1
            if data[1] <= 5 and data[1] % 2 == 1 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 0:
                if data[0] == 32:
                    data[0] = 1
                    data[1] += 1
            if data[1] <= 5 and data[1] % 2 == 0 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 1:
                if data[0] == 31:
                    data[0] = 1
                    data[1] += 1
            if data[1] == 2 and leap_year(data[2]) == True:
                if data[0] == 30:
                    data[0] = 1
                    data[1] += 1
            if data[1] == 2 and leap_year(data[2]) == False:
                if data[0] == 29:
                    data[0] = 1
                    data[1] += 1
        if daycnt % 10 == 1 and daycnt // 10 % 10 != 1:
            part = 'Тебе сегодня ' + str(daycnt) + ' день.'
        elif daycnt % 10 <= 4 and daycnt % 10 >= 2 and daycnt // 10 % 10 != 1:
            part = 'Тебе сегодня ' + str(daycnt) + ' дня.'
        else:
            part = 'Тебе сегодня ' + str(daycnt) + ' дней.'
        bot.send_message(message.from_user.id, part)
        bot.register_next_step_handler(message, get_text_messages)
def months(message):
    now_data = gmtime(time())
    now_year, now_mon, now_day, moncnt = now_data[0], now_data[1], now_data[2], 0
    data = message.text.split('.')
    if data == ['/cmd']:
        bot.send_message(message.from_user.id, '1. Чтобы активировать бота, надо написать /start. \n2. Чтобы посмотреть список команд, надо написать /cmd. \n3. Чтобы узнать ближайший юбилей тысяч дней со дня рождения, надо написать /1000days. \n4. Чтобы узнать сколько дней тебе со дня рождения, надо написать /days. \n4. Чтобы узнать сколько месяцев тебе со дня рождения, надо написать /months. \n6. Чтобы узнать сколько недель тебе со дня рождения, надо написать /weeks.')
        bot.register_next_step_handler(message, get_text_messages)
    elif data == ['/1000days']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать ближайшую тысячу дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days1000)
    elif data == ['/days']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days)
    elif data == ['/weeks']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе недель, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, weeks)
    elif data == ['/months']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе месяцев, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, months)
    elif is_valid_data(data, now_day, now_mon, now_year) != True:
        bot.send_message(message.from_user.id, 'Не корректный ввод, введи правильную дату, например: 01.01.2000.')
        bot.register_next_step_handler(message, months)
    else:
        data = [int(s) for s in data]
        if now_day >= data[0]:
            moncnt += (now_year - data[2]) * 12 + now_mon - data[1]
        else:
            moncnt += (now_year - data[2]) * 12 + now_mon - data[1] - 1
        if moncnt % 10 == 1 and moncnt // 10 % 10 != 1:
            part = 'Тебе сегодня ' + str(moncnt) + ' месяц.'
        elif moncnt % 10 <= 4 and moncnt % 10 >= 2 and moncnt // 10 % 10 != 1:
            part = 'Тебе сегодня ' + str(moncnt) + ' месяца.'
        else:
            part = 'Тебе сегодня ' + str(moncnt) + ' месяцев.'
        bot.send_message(message.from_user.id, part)
        bot.register_next_step_handler(message, get_text_messages)
def weeks(message):
    now_data = gmtime(time())
    now_year, now_mon, now_day, daycnt = now_data[0], now_data[1], now_data[2], 0
    data = message.text.split('.')
    if data == ['/cmd']:
        bot.send_message(message.from_user.id, '1. Чтобы активировать бота, надо написать /start. \n2. Чтобы посмотреть список команд, надо написать /cmd. \n3. Чтобы узнать ближайший юбилей тысяч дней со дня рождения, надо написать /1000days. \n4. Чтобы узнать сколько дней тебе со дня рождения, надо написать /days. \n4. Чтобы узнать сколько месяцев тебе со дня рождения, надо написать /months. \n6. Чтобы узнать сколько недель тебе со дня рождения, надо написать /weeks.')
        bot.register_next_step_handler(message, get_text_messages)
    elif data == ['/1000days']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать ближайшую тысячу дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days1000)
    elif data == ['/days']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе дней, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, days)
    elif data == ['/weeks']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе недель, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, weeks)
    elif data == ['/months']:
        bot.send_message(message.from_user.id, 'Напиши дату рождения, чтобы узнать сколько тебе месяцев, пример ввода: 01.01.2000.')
        bot.register_next_step_handler(message, months)
    elif is_valid_data(data, now_day, now_mon, now_year) != True:
        bot.send_message(message.from_user.id, 'Не корректный ввод, введи правильную дату, например: 01.01.2000.')
        bot.register_next_step_handler(message, weeks)
    else:
        data = [int(s) for s in data]
        while is_valid_thdays(data[0], data[1], data[2], now_day, now_mon, now_year) != True:
            daycnt += 1
            data[0] += 1
            if data[1] == 12 and data[0] == 32:
                data[0], data[1] = 1, 1
                data[2] += 1
            if data[1] <= 5 and data[1] % 2 == 1 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 0:
                if data[0] == 32:
                    data[0] = 1
                    data[1] += 1
            if data[1] <= 5 and data[1] % 2 == 0 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 1:
                if data[0] == 31:
                    data[0] = 1
                    data[1] += 1
            if data[1] == 2 and leap_year(data[2]) == True:
                if data[0] == 30:
                    data[0] = 1
                    data[1] += 1
            if data[1] == 2 and leap_year(data[2]) == False:
                if data[0] == 29:
                    data[0] = 1
                    data[1] += 1
        weekcnt = daycnt // 7
        if weekcnt % 10 == 1 and weekcnt // 10 % 10 != 1:
            part = 'Тебе сегодня ' + str(weekcnt) + ' неделя.'
        elif weekcnt % 10 <= 4 and weekcnt % 10 >= 2 and weekcnt // 10 % 10 != 1:
            part = 'Тебе сегодня ' + str(weekcnt) + ' недели.'
        else:
            part = 'Тебе сегодня ' + str(weekcnt) + ' недель.'
        bot.send_message(message.from_user.id, part)
        bot.register_next_step_handler(message, get_text_messages)
bot.polling(none_stop=True, interval=0)
