from datetime import date
import random

PRICE_ENTRY = 10.00
PRICE_DRINK = 4.00
PRICE_GAMBLING_TAX = 2.10
MIN_AGE = 18

name = input("Wat is je voor- en achternaam: ").title()

birthdate = input("Wat is je geboortedatum? Vul dit in als dd-mm-yyyy: ")
birth_day, birth_month, birth_year = birthdate.split("-")
if date.today().year - int(birth_year) < 18:
    print("Sorry je bent helaas nog niet oud genoeg, kom terug als je dat wel bent.")
    exit(1)

gender = input("Wat is je gender? (m/v/x): ").lower()
initial_budget = float(input("Hoeveel geld neem je mee naar Casino de Gouden Driehoek: € "))

last_name = name.split()
total_cost = PRICE_ENTRY + PRICE_DRINK + PRICE_GAMBLING_TAX
balance = initial_budget - total_cost

if gender == "m":
    greeting = ", meneer " + last_name[1]
elif gender == "v":
    greeting = ", mevrouw " + last_name[1]
else:
    greeting = " " + name

if balance > 0:
    entry_balance = "nog genoeg"
else:
    entry_balance = "niet voldoende"

print(f"""
Casino de Gouden Driehoek
-------------------------
Welkom{greeting}

Startbudget:    €{initial_budget:.2f}
Vaste kosten:   €{total_cost:.2f}
Saldo:          €{balance:.2f}

Je hebt {entry_balance} budget voor toegang tot het casino.
Kies één van de volgende opties:
1. Rood
2. Zwart
3. Even
4. Oneven
0. Stop
""")

spin = random.randint(1,36)
color = "onbekend"
odd_even = "onbekend"

while True:
    choice = int(input("Kies je gok (0 om te stoppen): "))
    if choice == 0:
        break
    elif choice in range(1,5):
        stake = float(input("Hoeveel geld wil je inzetten in euro's? € "))
        if stake <= 0 or stake > balance:
            print("Het is niet mogelijk om deze hoeveelheid in te zetten.")
            continue
        else:
            balance -= stake
            if spin == 0:
                color = "groen"
                odd_even = "geen"
            else:
                if spin <= 18:
                    if spin % 2 == 0:
                        color = "zwart"
                        odd_even = "even"
                    else:
                        color = "rood"
                        odd_even = "oneven"
                else:
                    if spin % 2 == 0:
                        color = "rood"
                        odd_even = "even"
                    else:
                        color = "zwart"
                        odd_even = "oneven"
    else:
        continue

    if choice == 1 and color == "rood":
        win = True
    elif choice == 2 and color == "zwart":
        win = True
    elif choice == 3 and odd_even == "even":
        win = True
    elif choice == 4 and odd_even == "oneven":
        win = True
    else:
        win = False

    if not win:
        print(f"""
De bal eindigde op nummer {spin} ({color}) 
Helaas je hebt verloren, je nieuwe saldo is: €{balance:.2f}.
""")
    elif win:
        balance += 2 * stake
        print(f"""
De bal eindigde op nummer {spin} ({color})
Je wint €{stake:.2f} en je nieuwe saldo is: €{balance:.2f}
""")

    else:
        print(f"Deze keuze is helaas niet geldig.")
        continue

print(f"Je verlaat het casino met €{balance:.2f}, tot de volgende keer!")
