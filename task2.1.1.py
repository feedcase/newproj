import datetime

dt = input('Input date in format DD.MM.YYYY: ')
my_date = datetime.datetime.strptime(dt, '%d.%m.%Y')
print('Day of week: ', my_date.strftime("%A"))
