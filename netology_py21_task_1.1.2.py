def financial_planner():
  salary = int(input("Введите заработную плату: "))
  loan_percent = int(input("Введите, сколько процентов уходит на ипотеку: "))
  life_percent = int(input("Введите, сколько процентов уходит на жизнь: "))
  bonuses_amount = int(input("Введите количество премий за год: "))
  annual_income = int(12*salary)
  bonuses = bonuses_amount*salary
  print("На ипотеку было потрачено: ", int((loan_percent/100)*annual_income))
  print("Было накоплено: ", int(annual_income-(loan_percent/100)*annual_income-(life_percent/100)*annual_income)+int(bonuses/2))

financial_planner()
