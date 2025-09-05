def calcu(oper, num1, num2):
    match oper:
        case "add":
            output = num1 + num2
            print(output)
        case "subtract":
            output = num1-num2
            print(output)
        case "multiply":
            output = num1*num2
            print(output)
        case "divide":
            output = num1/num2 
            print(output)
        case _:
            print('Invalid operation')

print('Hello! This is a calculator.\nThese are the choices (add, subtract, multiply, divide)')

while True:
    
    operation = input('Input operation: ')
    number1 = input('First number: ')
    number2 = input('Second number: ')
    
    print(calcu(operation, float(number1), float(number2)))
    confirmation = input('Continue? (y/n): ').lower()
    
    if confirmation == 'y':
        print('These are the choices (add, subtract, multiply, divide)')
    elif confirmation == 'n':
        print('Shutting down...')
        break
    else:
        print('Unknown. Continuing...')
    