n1 = int(input("Input a number: "))
n2 = int(input("Input a number: "))

if n2 != 0:
    print(f"Our result is {n1 / n2}")
else:
    print("Don't divide over zero!!!")

"""
NAPISZCIE PROGRAM KTÓRY SPRAWDZI CZY MOZESZ SKORZYSTAC Z ATRKACJI TURYSTYCZNEJ
- MINIMALNY WIEK TO 12 LAT.
- MINIMALNY WZROST TO 130 CM.
- MAKSYMALNY WZROST TO 195 CM.

PROGRAM MA ZAPYTAC UZYTKOWNIKA O WIEK I WZROST, A NASTEPNIE WYSWIETLIC KOMUNIKAT.
"""

age = int(input("Input your age: "))
height = int(input("Input your height (in centimetre): "))

if age >= 12 and 130 < height < 195:
    print("Yes, you can!")
else:
    print("No, you can't!")

"""
BIERZESZ UDZIAL W PIERWSZEJ FAZIE TURNIEJU E-SPORTOWEGO. O PRZEJŚCIU DALEJ DECYDUJE LICZBA WYGRANYCH MECZÓW ORAZ 
ZDOBYTYCH ODZNACZEŃ MVP. ABY PRZEJŚĆ DALEJ NALEŻY ZDOBYĆ MINIMUM 10 WYGRANYCH ORAZ MIEĆ ICH WIĘCEJ NIŻ PRZEGRANYCH
LUB ZDOBYĆ 7 ODZNACZEŃ MVP.
LICZBĘ MECZY WYGRANYCH, PRZEGRANYCH ORAZ LICZBĘ MVP NALEZY ODCZYTAC OD UZYTKOWNIKA NA POCZATKU.

WINS = int
LOSES = int
MVP = int

IF ... :
    PRINT("GRATULUJE UDALO CI SIE!")
"""

wins = int(input("Input wins: "))
loses = int(input("Input loses: "))
mvp = int(input("Input mvp: "))

if wins >= 10 and wins > loses or mvp >= 7:
    print("Gratuluje przejścia do kolejnego etapu.")
else:
    print("Nie udało się.")

"""
UŻYTKOWNIK WPROWADZA LICZBĘ I DOSTAJE ODPOWIEDZ CZY LICZBA JEST: POZYTYWNA, NEGATYWNA CZY RÓWNA ZERO?

number = int

if ... :
    print()
elif ... :
    print()
else:
    print()
"""

number = int(input("Input a number: "))

if number < 0:
    print("Negative")
elif number > 0:
    print("Positive")
else:
    print("It's a zero.")

"""
NAPISZ PROGRAM, KTÓRY INFORMUJE UŻYTKOWNIKA O KOSZCIE ATRAKCJI TURYSTYCZNEJ W ZALEŻNOŚĆI OD MIESIĄCA. PROGRAM POWINIEN
ZAPYTAC O NUMER MIESIACA, A NASTEPNIE WYSWIETLIC INFORMACJE CO DO PONIŻSZEJ ZASADY:
- W STYCZNIU ORAZ LUTYM $150
- W MARCU I KWIETNIU $199
- W MAJU ORAZ CZERWCU $249
- W LIPCU, SIERPNIU ORAZ WRZEŚNIU $299
- W PAŻDZIERNIKU $249
- W LISTOPADZIE ORAZ GRUDNIU $199


month = int

if ... :
    print()
elif ... :
    print()
elif ... :
    print()
elif ... :
    print()
else:
    print()
"""

month = int(input("Input a month: "))

if 1 <= month <= 2:
    print("$150")
elif 3 <= month <= 4 or 11 <= month <= 12:
    print("$199")
elif 5 <= month <= 6 or month == 10:
    print("$249")
elif 7 <= month <= 8:
    print("$299")
else:
    print("Month number is valid!")
