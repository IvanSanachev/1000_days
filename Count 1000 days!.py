from time import *
now_data = gmtime(time())
now_year, now_mon, now_day, daycnt, th = now_data[0], now_data[1], now_data[2], 0, 0
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
def is_valid_data(data, nd, nm, ny):
    if len(data) == 3:
        if data[0].isdigit() == True and data[1].isdigit() == True and data[2].isdigit() == True:
            data[0], data[1], data[2] = int(data[0]), int(data[1]), int(data[2])
            if is_valid_thdays(nd, nm, ny, data[0], data[1], data[2]) == True:
                if leap_year(data[2]) == True:
                    if data[1] == 2:
                        if data[0] <= 29:
                            return True
                        else:
                            return False
                    elif data[1] <= 5 and data[1] % 2 == 1 or data[1] >= 6 and data[1] <= 12 and data[1] % 2 == 0:
                        if data[0] <= 31:
                            return True
                        else:
                            return False
                    elif data[1] <= 5 and data[1] % 2 == 0 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 1:
                        if data[0] <= 30:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    if data[1] == 2:
                        if data[0] <= 28:
                            return True
                        else:
                            return False
                    elif data[1] <= 5 and data[1] % 2 == 1 or data[1] >= 6 and data[1] <= 12 and data[1] % 2 == 0:
                        if data[0] <= 31:
                            return True
                        else:
                            return False
                    elif data[1] <= 5 and data[1] % 2 == 0 or data[1] >= 6 and data[1] < 12 and data[1] % 2 == 1:
                        if data[0] <= 30:
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
valid = False
while valid != True:
    print('Пожалуйста, введите Вашу корректную дату рождения, например: (01.01.2000).')
    data = [int(s) for s in input().split('.')]
    valid = is_valid_data(data)
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
print(th * 1000, 'дней, Вам будет', end= ' ')
print(data[0], data[1], data[2], sep = '.', end= '.')