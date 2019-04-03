def travel_assistant():
  eu_ru_exchange_rate = 80
  print('Euro to rouble exchange rate: ', eu_ru_exchange_rate)
  
  cost_per_day = 15 # euro
  
  count_trips = 3
  
  day_by_trip1 = 10 # Turkey
  day_by_trip2 = 5 # France
  day_by_trip3 = 14 # Germany
  
  cost_ticket = 50
  count_fly = 2
  
  cost_trip = cost_per_day * (day_by_trip1 + day_by_trip2 + day_by_trip3)
  cost_trip += cost_ticket * count_fly * count_trips
  cost_trip_ru = cost_trip * eu_ru_exchange_rate
  
  print('Total vacation cost:', cost_trip, 'euros (approximately', cost_trip_ru, 'roubles)')

  vacation_budget = int(input('What`s your vacation budget in euro? '))

  if vacation_budget < cost_trip:
    print('Unfortunately, you don`t have enough money, friend :(')
  else:
    print('Have a nice adventure!')

travel_assistant()
