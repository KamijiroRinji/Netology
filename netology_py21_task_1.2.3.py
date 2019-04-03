# Источник дат знаков: https://ru.wikipedia.org/wiki/%D0%97%D0%BD%D0%B0%D0%BA%D0%B8_%D0%B7%D0%BE%D0%B4%D0%B8%D0%B0%D0%BA%D0%B0, "Даты пребывания Солнца в зодиакальных созвездиях"

def astrological_sign_qualifier():
  month = int(input('Введите номер месяца: '))
  day = int(input('Введите число: '))

  if (month == 4 and day in range(18, 31)) or (month == 5 and day in range(1, 15)):
    print('Вывод:\nОвен')
  elif (month == 5 and day in range(14, 32)) or (month == 6 and day in range(1, 22)):
    print('Вывод:\nТелец')
  elif (month == 6 and day in range(21, 31)) or (month == 7 and day in range(1, 21)):
    print('Вывод:\nБлизнецы')
  elif (month == 7 and day in range(20, 32)) or (month == 8 and day in range(1, 12)):
    print('Вывод:\nРак')
  elif (month == 8 and day in range(11, 32)) or (month == 9 and day in range(1, 18)):
    print('Вывод:\nЛев')
  elif (month == 9 and day in range(17, 31)) or (month == 10 and day in range(1, 32)):
    print('Вывод:\nДева')
  elif (month == 10 and day == 31) or (month == 11 and day in range(1, 23)):
    print('Вывод:\nВесы')
  elif month == 11 and day in range(22, 31):
    print('Вывод:\nСкорпион')
  elif (month == 11 and day == 30) or (month == 12 and day in range(1, 19)):
    print('Вывод:\nЗмееносец')
  elif (month == 12 and day in range(18, 32)) or (month == 1 and day in range(1, 20)):
    print('Вывод:\nСтрелец')
  elif (month == 1 and day in range(19, 32)) or (month == 2 and day in range(1, 17)):
    print('Вывод:\nКозерог')
  elif (month == 2 and day in range(16, 30)) or (month == 3 and day in range(1, 13)):
    print('Вывод:\nВодолей')
  elif (month == 3 and day in range(12, 32)) or (month == 4 and day in range(1, 19)):
    print('Вывод:\nРыбы')
  else:
    print('Вывод:\nПривет радужным единорожкам :3')

astrological_sign_qualifier()
