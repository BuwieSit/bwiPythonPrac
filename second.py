#number guessing game
import random

print("Number guessing game")
while True:

        min = int(input("Minimum number: "))
        max = int(input("Maximum number: "))
        difficulty = input("ENABLE HARD MODE? (Decimal values) (y|n) ")
        print("Loading random number...")
        
        match difficulty:
            case "n":
                number = random.randint(min, max)
            case "y":
                
                number = float(random.uniform(min, max))
                number = round(number, 2)
            case _:
                print('Invalid. Restarting')

        print("debug", number)
        while True:
            if type(number) == float:
                answer = float(input("Guess it: "))
            elif type(number) == int:
                answer = int(input("Guess it: "))
            else:
                print("Type error.")
                
            if answer == number:
                print("You guessed it right! The number was ",number)
                break
            elif answer < number:
                print("Maybe higher?")
            elif answer > number:
                print("Maybe lower")
            else:
                print("Uhhh what?")
            
        confirmation = input('Want another session? (y/n): ').lower()
        if confirmation == 'y':
            continue
        elif confirmation == 'n':
            print('Shutting down...')
            break
        else:
            print('Unknown Command...')   