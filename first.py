#simple calculator
while True:
    print('Hello! This is a calculator.\nThese are the choices (add, subtract, multiply, divide)')
    
    try:
        number1 = float(input('First number: '))
        number2 = float(input('Second number: '))
        oper = input('Input operation: ') 
        
        match oper:
            case "add":
                        output = number1 + number2
                        print(output)
            case "subtract":
                        output = number1-number2
                        print(output)
                            
            case "multiply":
                        output = number1*number2
                        print(output)
                            
            case "divide":
                        output = number1/number2 
                        print(output)
            case _:
                        print('Invalid operation')
    
    except:
        print('Invalid Input. Please try again')
    
    confirmation = input('Continue? (y/n): ').lower()
    if confirmation == 'y':
        continue
    elif confirmation == 'n':
        print('Shutting down...')
        break
    else:
        print('Unknown Command...')        