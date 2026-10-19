from datetime import date

PRICE_ENTRY = 10.00
PRICE_DRINK = 4.00
PRICE_GAMBLING_TAX = 2.10
MIN_AGE = 18

name = input("Wat is je voor- en achternaam: ").title()

birthdate = input("Wat is je geboortedatum? Vul dit in als dd-mm-yyyy: ")
birth_day, birth_month, birth_year = birthdate.split("-")
birth_year = int(birth_year)
datum = date.today()
if datum.year - birth_year < 18:
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

Je hebt {entry_balance} budget voor toegang tot het casino""")
