import random
import os

# Poänglistan (tom från början)
poanglista = []

# funktion som genererar ett nummer mellan 1 - 100
def generate_number():
    return random.randint(1, 100)

# funktion som rensar konsolen
def clear_consol():
    if os.name == 'nt':
        os.system('cls')  # För Windows
    else:
        os.system('clear')  # För Mac/Linux

# funktion för att hantera gissningarna
def check_guess(guess_num, rand):
    if guess_num > rand:
        if abs(guess_num - rand) <= 5:
            print('Tyvärr var din gissning för hög, men du var nära! Prova igen!')
        else:
            print('Tyvärr var din gissning för hög, vänligen prova igen.')
    elif guess_num < rand:
        if abs(guess_num - rand) <= 5:
            print('Tyvärr var din gissning för låg, men du var nära! Prova igen!')
        else:
            print('Tyvärr var din gissning för låg, vänligen prova igen.')
    else:
        return True

# funktion för att visa poänglistan
def visa_poanglista():
    clear_consol()
    if not poanglista:
        print("Det finns inga poäng än! Spela spelet för att skapa några.")
    else:
        print("🏆 Poänglista 🏆")
        for index, entry in enumerate(sorted(poanglista, key=lambda x: x['poang'])):
            print(f"{index + 1}. {entry['namn']} - {entry['poang']} gissningar")
    print("\n")

# starta spelet
def start_game():
    global poanglista

    clear_consol()
    print("*********************************************************************")
    print('* Välkommen till mitt gissnings spel, gissa ett nummer mellan 1-100 *')
    print("*********************************************************************\n")

    namn = input("Vad heter du? ").strip()
    if not namn:
        namn = "Anonym spelare"  # Standardnamn om inget skrivs in

    random_number = generate_number()
    guess = 0
    count = 0
    max_gissningar = 10

    while guess != random_number:
        try:
            guess = int(input('Skriv din gissning här: '))

            # Kontrollera om gissningen är inom intervallet
            if guess < 1 or guess > 100:
                print("Ogiltig gissning! Vänligen ange ett nummer mellan 1 och 100.")
                continue

            count += 1  # Öka räknaren

            # Kontrollera gissningen
            if check_guess(guess, random_number):
                print(f'Bra jobbat, {namn}! Du gissade rätt på {count} försök.')
                poanglista.append({'namn': namn, 'poang': count})  # Lägg till resultat i poänglistan
                break

            # Avsluta spelet efter 10 gissningar
            if count == max_gissningar:
                print(f"Du har nått max antal gissningar. Det hemliga talet var {random_number}.")
                break

        except ValueError:
            print("Ogiltig inmatning! Vänligen ange ett giltigt heltal.")

    # Fråga om spelaren vill spela igen eller visa poänglistan
    while True:
        val = input("Vill du (1) spela igen, (2) visa poänglistan, eller (3) avsluta? ")
        if val == "1":
            start_game()
            break
        elif val == "2":
            visa_poanglista()
        elif val == "3":
            avsluta_spelet()
            break
        else:
            print("Ogiltigt val, försök igen.")

# funktion för att avsluta spelet snyggt
def avsluta_spelet():
    clear_consol()
    print("Tack för att du spelade mitt spel! Välkommen åter.")
    visa_poanglista()  # Visa poänglistan en sista gång
    input("Tryck Enter för att avsluta...")

# Starta spelet första gången
start_game()





# Symboler för spelet:
# ⭐ = "⭐" eller "\u2B50"
# 🎉 = "🎉" eller "\U0001F389"
# 🏆 = "🏆" eller "\U0001F3C6"
# 🥇 = "🥇" eller "\U0001F947"
# 🥈 = "🥈" eller "\U0001F948"
# 🥉 = "🥉" eller "\U0001F949"
