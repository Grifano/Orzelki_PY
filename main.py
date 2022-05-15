import random  
# Podlaczcy biblioteke random

powitania = ['Hej', 'Hejka', 'Siema', 'Dzien dobry', 'Siemanko', 'Dzien doberek']
# Lista z powitaniem

losowe_powitanie = random.choice(powitania)
# Losowanie powitania

imiona = ['Anna', 'Dawid', 'Frania', 'Irek', 'Kasia', 'Oliwka', 'Piotr', 'Szymon', 'Ola L.', 'Milena', 'Ola S.']
# Lista z imonami

losowe_imie = random.choice(imiona)
# Losowanie imiona

imie_osoby = input(f'{losowe_powitanie}, jak masz na imie? ') 
# Pyta jak masz na imie

print(f'Witaj {imie_osoby} a ja jestem {losowe_imie}') 
# Zwrucic sie do urzytkownika z wylosowanym imiem

print('Ile masz lat?')
# Zapytaj uzytkownika o imie

mam_lat = input('Mam, ')
# Napisac ile masz lat

wiek = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# Lista z Wiekiem 

losowy_wiek = random.choice(wiek)
# Wylosuj uzytkownikowi wiek

print(f'Ja mam {losowy_wiek}')
# Zwrucic sie do urzytkownika z wylosowanym wiekiem

