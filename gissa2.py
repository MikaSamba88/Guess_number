import random
import os

#the scoreboard
scoreboard = []

# function to generate number between 1 - 100
def generate_number():
    return random.randint(1, 100)

#function to clear code
def clear_consol():
    if os.name == 'nt':
        os.system('cls') #this will clear my code so it looks nice (for windows)

# function that takes our guesses
def check_guess(guess_num, rand):
    if guess_num > rand:
        if abs(guess_num - rand) <= 5:  # write this if the guess is closer than 5
            print('Tyvärr var din gissning för hög, men du var nära! prova igen!\n')
        else:
            print('Tyvärr var din gissning för hög, vänligen prova igen\n')
    elif guess_num < rand:
        if abs(guess_num - rand) <= 5: # write this if the guess is closer than 5
            print('tyvärr var din gissning för låg, men du var nära! prova igen!\n')
        else:
            print('Tyvärr var din gissning för låg, vänligen prova igen\n')
    else:
        return True
    
def start_game():
    random_number = generate_number()# this generate a random number
    print("*********************************************************************")
    print('* Välkommen till mitt gissnings spel, gissa ett nummer mellan 1-100 *')
    print("*********************************************************************\n")# made som stars to seperate the text for a nice look

    # loop to we guess the right number
    guess = 0
    count = 0 # count the guesses
    max_gissningar = 10 #max amount of guesses

    while guess != random_number:
        try: 
            guess = int(input('Skriv din gissning här: ')) # show where you can write your guess

            # control if your guess is between 1 - 100
            if guess < 1 or guess > 100:
                print("Ogiltig gissning! Vänligen ange ett nummer mellan 1 och 100.")
                continue  # continue the loop

            count = count + 1

            #if you guess the right number
            if check_guess(guess, random_number):
                print(f'\n*****Bra jobbat! du gissade rätt på {count} gissning(ar).*****\n')
                break

            #if you reach 10 guesses
            if count == max_gissningar:
                print(f"---Spelet är över! Du nådde {max_gissningar} gissningar. Talet vi sökte va {random_number}.---\n")
                break     

        except ValueError:
                print("Ogiltig inmatning, Vänligen prova igen")    

    #asks if the player want to play again       
    spela_igen = input("Skulle du vilja spela igen? (ja/nej): ")
    if spela_igen == "ja":
        print("Okej, tack för du spelade!\n")
        clear_consol()
        start_game()
    else:
        avsluta_spelet()

#Function to quit the game            
def avsluta_spelet():
    clear_consol() #clear the console
    print("Okej, tack för du spelade mitt spel!\n")
    input("Tryck Enter för att avsluta")

#this starts the game
start_game()
