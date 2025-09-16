#number guessing game
import random

print("Number guessing game")
while True:

        min = input("Minimum number: ")
        max = input("Maximum number: ")
        difficulty = input("ENABLE HARD MODE? (Decimal values) (y|n) ")
        print("Loading random number...")
        
        match difficulty:
            case "n":
                numbers = int(random.randint(min, max))
            case "y":
                numbers = float(random.random(min, max))
            case _:
                print('Invalid. Restarting')

        confirmation = input('Continue? (y/n): ').lower()
        if confirmation == 'y':
            continue
        elif confirmation == 'n':
            print('Shutting down...')
            break
        else:
            print('Unknown Command...')   