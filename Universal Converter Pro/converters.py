from locale import normalize
from os import name
import textwrap
from unicodedata import decimal
from urllib import response
import requests
from decimal import Decimal, Overflow, InvalidOperation, DivisionByZero

from main import Decimal

    # The 'r' before the string helps Python handle backslashes
    # We use 34 dashes/lines for a clean 40-character wide look
def main_menu():    
    print("\033[92m╔══════════════════════════════════════════╗")
    print("║     ⚙️  UNIVERSAL CONVERTER v1.0 ⚙️      ║")
    print("╠══════════════════════════════════════════╣")
    print("║  💰 1. Currency  (USD CONVERTER)         ║")
    print("║  🌡️ 2. Temperature                       ║")
    print("║  📏 3. Length                            ║")
    print("║  ⚖️ 4. Weight                            ║")
    print("║                                          ║")
    print("║  ❌ 0. Exit                              ║")
    print("╠══════════════════════════════════════════╣")
    print("║   ⌨️  QUICK EXIT: [CTRL+C] or [CTRL+Z]   ║")
    print("║             AT ANY MOMENT                ║")
    print("╚══════════════════════════════════════════╝\033[0m")
 
def currency_menu():
    print("\033[92m╔═════════════════════════════════════════════════════════════╗")
    print("║                   💰 CURRENCY CONVERTER 💰                  ║")
    print("╠═════════════════════════════════════════════════════════════╣")
    print("║  1. Afghan Afghani (AFN)      11. Swedish Krona (SEK)       ║")
    print("║  2. Euro (EUR)                12. South Korean Won (KRW)    ║")
    print("║  3. Japanese Yen (JPY)        13. Singapore Dollar (SGD)    ║")
    print("║  4. British Pound (GBP)       14. Norwegian Krone (NOK)     ║")
    print("║  5. Australian Dollar (AUD)   15. Mexican Peso (MXN)        ║")
    print("║  6. Canadian Dollar (CAD)     16. Indian Rupee (INR)        ║")
    print("║  7. Swiss Franc (CHF)         17. Russian Ruble (RUB)       ║")
    print("║  8. Chinese Yuan (CNY)        18. South African Rand (ZAR)  ║")
    print("║  9. Hong Kong Dollar (HKD)    19. Turkish Lira (TRY)        ║")
    print("║  10. New Zealand Dollar (NZD) 20. Brazilian Real (BRL)      ║")
    print('╠═════════════════════════════════════════════════════════════╣')
    print("║  0. Back to Main Menu                                       ║")
    print("╚═════════════════════════════════════════════════════════════╝\033[0m")

def temp_menu():
    # We use \033[92m to keep it that consistent green theme
    print("\033[92m╔══════════════════════════════════════════════════╗")
    print("║           🌡️ TEMPERATURE CONVERTER 🌡️            ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  1. °C to °F (Celsius to Fahrenheit)             ║")
    print("║  2. °F to °C (Fahrenheit to Celsius)             ║")
    print("║  3. °C to K  (Celsius to Kelvin)                 ║")
    print("║  4. K to °C  (Kelvin to Celsius)                 ║")
    print("║  5. °F to K  (Fahrenheit to Kelvin)              ║")
    print("║  6. K to °F  (Kelvin to Fahrenheit)              ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  0. Back to Main Menu                            ║")
    print("╚══════════════════════════════════════════════════╝\033[0m")

def length_initial_menu():
    print("\033[92m╔══════════════════════════════════════════════════╗")
    print("║        📏 SELECT YOUR (INITIAL) UNIT 📏          ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  1. mm  (Millimeters)                            ║")
    print("║  2. cm  (Centimeters)                            ║")
    print("║  3. m   (Meters)                                 ║")
    print("║  4. km  (Kilometers)                             ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  0. Back to Main Menu                            ║")
    print("╚══════════════════════════════════════════════════╝\033[0m")

def length_final_menu():
    print("\033[92m╔══════════════════════════════════════════════════╗")
    print("║         🏁 SELECT YOUR (FINAL) UNIT 🏁           ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  1. mm  (Millimeters)                            ║")
    print("║  2. cm  (Centimeters)                            ║")
    print("║  3. m   (Meters)                                 ║")
    print("║  4. km  (Kilometers)                             ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  0. Back to (Initial) Unit Selection             ║")
    print("╚══════════════════════════════════════════════════╝\033[0m")

def weight_initial_menu():
    print("\033[92m╔══════════════════════════════════════════════════╗")
    print("║           ⚖️ SELECT YOUR (INITIAL) UNIT ⚖️       ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  1. Kilograms (kg)                               ║")
    print("║  2. Pounds (lb)                                  ║")
    print("║  3. Grams (g)                                    ║")
    print("║  4. Ounces (oz)                                  ║")
    print("║  5. Tons (t)                                     ║")
    print("║  6. Milligrams (mg)                              ║")
    print("║  7. Stone (st)                                   ║")
    print("║  8. Centigrams (cg)                              ║")
    print("║  9. Decigrams (dg)                               ║")
    print("║  10. Dekagrams (dag)                             ║")
    print("║  11. Hectograms (hg)                             ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  0. Back to Main Menu                            ║")
    print("╚══════════════════════════════════════════════════╝\033[0m")
def weight_final_menu():
    print("\033[92m╔══════════════════════════════════════════════════╗")
    print("║           🏁 SELECT YOUR (FINAL) UNIT 🏁         ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  1. Kilograms (kg)                               ║")
    print("║  2. Pounds (lb)                                  ║")
    print("║  3. Grams (g)                                    ║")
    print("║  4. Ounces (oz)                                  ║")
    print("║  5. Tons (t)                                     ║")
    print("║  6. Milligrams (mg)                              ║")
    print("║  7. Stone (st)                                   ║")
    print("║  8. Centigrams (cg)                              ║")
    print("║  9. Decigrams (dg)                               ║")
    print("║  10. Dekagrams (dag)                             ║")
    print("║  11. Hectograms (hg)                             ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  0. Back to Main Menu                            ║")
    print("╚══════════════════════════════════════════════════╝\033[0m")


currencyNames = {
    1: "afn", 2: "eur", 3: "jpy", 4: "gbp", 5: "aud", 6: "cad", 7: "chf",
    8: "cny", 9: "hkd", 10: "nzd", 11: "sek", 12: "krw", 13: "sgd", 14: "nok",
    15: "mxn", 16: "inr", 17: "rub", 18: "zar", 19: "try", 20: "brl"
}
try:
    url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json"
    response = requests.get(url, timeout=5)
    currency_rates = response.json()['usd']  
except Exception:
    print("\033[91m╔══════════════════════════════════════════════════╗")
    print("║      ⚠️  ERROR FETCHING CURRENCY RATES  ⚠️      ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║                                                  ║")
    print("║  Unable to retrieve live currency rates.         ║")
    print("║  Please check your internet connection and try    ║")
    print("║  again.                                         ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝\033[0m")


def currency(pick_currency, usdAmt):
    try:
        findCurrency = currencyNames[pick_currency]
        if findCurrency:
            money = usdAmt * Decimal(currency_rates[findCurrency])
            name = findCurrency.upper()  
    except Overflow:
        print("\033[91m╔══════════════════════════════════════════════════╗")
        print("║      ⚠️        VALUE ERROR DETECTED        ⚠️    ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║                                                  ║")
        print("║  Error: The result is too large to display       ║")
        print("║  Please try a smaller input value.               ║")
        print("║                                                  ║")
        print("╚══════════════════════════════════════════════════╝\033[0m")
        return
  
    cText = f"💰 RESULT: {usdAmt:,.2f} USD  = {money.normalize():,.2f} {name}"
    cLine = textwrap.wrap(cText, width=67)

    print("\033[92m╔══════════════════════════════════════════════════════════════════════╗")
    for line in cLine:
        if "💰" in line:
            print(f"║ {line.ljust(68)}║")
        else:
            print(f"║ {line.ljust(69)}║")

    print("╠══════════════════════════════════════════════════════════════════════╣")
    print("║ ↩️  To Change Currency: Press '0'                                    ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\033[0m")

def temperature(pick_temp, temp):
    try:
       
        if (pick_temp == 1):
            res = (temp * Decimal('9')/Decimal('5')) + Decimal('32')
            u1, u2 = "\u00b0C", "\u00b0F"           
        elif (pick_temp == 2):
            res = (temp - Decimal('32')) * Decimal('5')/Decimal('9')
            u1, u2 = "\u00b0F", "\u00b0C"
        elif (pick_temp == 3):
            res = temp + Decimal('273.15')
            u1, u2 = "\u00b0C", "K"
        elif (pick_temp == 4):
            res = temp - Decimal('273.15')
            u1, u2 = "K", "\u00b0C"
        elif (pick_temp == 5):
            res = (temp - Decimal('32')) * Decimal('5')/Decimal('9') + Decimal('273.15')
            u1, u2 = "\u00b0F", "K"
        elif (pick_temp == 6):
            res = (temp - Decimal('273.15')) * Decimal('9')/Decimal('5') + Decimal('32')
            u1, u2 = "K", "\u00b0F"
    except (Overflow):
        print("\033[91m╔══════════════════════════════════════════════════╗")
        print("║      ⚠️        VALUE ERROR DETECTED        ⚠️    ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║                                                  ║")
        print("║  Error: The result is too large to display       ║")
        print("║  Please try a smaller input value.               ║")
        print("║                                                  ║")
        print("╚══════════════════════════════════════════════════╝\033[0m")
        return

        # make it so user keep inputing the same temp untill they want to go back
    tText = f" 🌡️  RESULT: {temp}{u1} = {res.normalize():f}{u2}"
    tLine = textwrap.wrap(tText, width=68)

    print("\033[92m╔══════════════════════════════════════════════════════════════════════╗")
    for line in tLine:
        print(f"║ {line.ljust(69)}║")
    print("╠══════════════════════════════════════════════════════════════════════╣")
    print("║ ↩️  To Change Units: Press 'q'                                       ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\033[0m")
    
def length(len1, len2, dist):
    
    units = {1:("mm",1), 2:("cm",10), 3:("m",1000),4:("km",1000000)}
    u1 = units.get(len1)
    u2 = units.get(len2)

    unit1 , factor1 = u1
    unit2 , factor2 = u2

    try:
        res = dist * factor1 / factor2
    except (Overflow, ZeroDivisionError, InvalidOperation):
        print("\033[91m╔══════════════════════════════════════════════════╗")
        print("║      ⚠️        VALUE ERROR DETECTED        ⚠️      ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║                                                  ║")
        print("║  Error: The result is too large to display       ║")
        print("║  Please try a smaller input value.               ║")
        print("║                                                  ║")
        print("╚══════════════════════════════════════════════════╝\033[0m")
        return
    if(res == Decimal('-Infinity')):
        print("\033[91m╔══════════════════════════════════════════════════╗")
        print("║      ⚠️        VALUE ERROR DETECTED        ⚠️      ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║                                                  ║")
        print("║  Error: The result is too small to be displayed  ║")
        print("║  Please try a larger input value.                ║")
        print("║                                                  ║")
        print("╚══════════════════════════════════════════════════╝\033[0m")
        return
    else:
        lText = f"📏 RESULT: {dist}{unit1} = {res.normalize():f}{unit2}"
        lLine = textwrap.wrap(lText, width=68)
        print("\033[92m╔══════════════════════════════════════════════════════════════════════╗")
        for line in lLine:
            if("📏" in line):
                print(f"║ {line.ljust(68)}║")
            else:
                print(f"║ {line.ljust(69)}║")
        print("╠══════════════════════════════════════════════════════════════════════╣")
        print("║ ↩️  To Change (Initial) Unit: Press '0'                              ║")
        print("╚══════════════════════════════════════════════════════════════════════╝\033[0m")    

# Units in gram
units_wt = { 
    1: ("kg", Decimal("1000")), 
    2: ("lb", Decimal("453.592")), 
    3: ("g", Decimal("1")), 
    4: ("oz", Decimal("28.3495")), 
    5: ("t", Decimal("1000000")), 
    6: ("mg", Decimal("0.001")), 
    7: ("st", Decimal("6350.29")), 
    8: ("cg", Decimal("0.01")), 
    9: ("dg", Decimal("0.1")), 
    10: ("dag", Decimal("10")), 
    11: ("hg", Decimal("100")) 
}
def weight(wgt1, wgt2 , weight):
    unit_name1 = units_wt[wgt1][0]
    unit_name2 = units_wt[wgt2][0]

    unit_factor1 = Decimal(str(units_wt[wgt1][1]))
    unit_factor2 = Decimal(str(units_wt[wgt2][1]))

    grams = weight * unit_factor1
    result_wt = grams / unit_factor2

    wText = f" ⚖️  RESULT: {weight}{unit_name1} = {result_wt.normalize():f}{unit_name2}"
    wLine = textwrap.wrap(wText, width=68)
    print("\033[92m╔══════════════════════════════════════════════════════════════════════╗")
    for line in wLine:
        print(f"║ {line.ljust(69)}║")
    print("╠══════════════════════════════════════════════════════════════════════╣")
    print("║ ↩️  To Change Units: Press '0'                                       ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\033[0m")
