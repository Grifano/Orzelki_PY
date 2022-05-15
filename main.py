import random
import datetime

# *** Dane do losowania ***

sniadania = ['Owsianka', 'Pancakes', 'Serniki', 'Twarog', 'Zapiekanka z gruszką', 'Zapiekanka z cukinią', 'leniwa owsianka', 'granola', 'Kasza przenna z pomarańczą', 'Omlet', 'Jaja gotowane']

drugie_sniadania = ['Kanapki z bananowym twarogiem', 'lawasz', 'Jogurt', 'herbata z ciasteczkami/rogalikami']

obiady = ['Barszcz', 'Makaron z ketchupem/serem', 'Jakaś kasza']

kolacje = ['Ryba z owocami', 'Kasza gryczna z buraczkiem', 'Herbata']

# *** End ***

# *** Controller ***

# Funcja losowania dan
#   - Uzyc biblioteki random
#   - Nie losowac Te danie jakie juz bylo wczoraj
#   - Losowac odpowidni posilek do godziny dnai (Sniadania miedzy 07:00 - 08:00)
#   - Zwrucic wylosowane danie

def losowanie_dania(lista_dan):
  print(random.choice(lista_dan))
  
# *** End ***

# *** Interface Urzytkownika (User Interface)
# 
# *** End ***

godzina = datetime.datetime.now().time()

# if godzina in range(7,8):
#   losowanie_dania(sniadania)
# elif godzina in range(13,14):
#   losowanie_dania(obiady)
# elif godzina in range(11,12):
#   losowanie_dania(drugie_sniadania)
# elif godzina in range(16,17):
#   losowanie_dania(kolacje)
# else:
#   print('Nie casz na jedzenie, swinko!')