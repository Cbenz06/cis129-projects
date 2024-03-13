def main():
    while True:
        userNumber = getInteger('Enter a numbah blud: ')
        if (userNumber % 2 == 0):
            print('The number is even')
        else:
            print('The number is odd')
        print('Do you wanna run it back?')
        again = input('enter \'y\' to loop again: ')
        if again != 'y':
            break

def getInteger(message):
    while True:
        try:
            userInput = int(input(message))
            return userInput
        except ValueError:
            print('Incorrect data entered. please try again')

main()
