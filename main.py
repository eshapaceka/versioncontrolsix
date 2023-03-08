def encoder(password):
    new_integer = ''
    for integer in password:
        single_int = ((int(integer)) + 3) % 10
        single_int = str(single_int)
        new_integer += single_int
    return new_integer



def main():
    while True:
        print()
        print('Welcome to Password Coding!')
        print('------------------')
        print()
        print('1. Encode Password')
        print('2. Decode Password')
        print('3. Exit')
        print()
        selection = int(input('Select an option: '))

        if selection in range(1, 3):
            password = input('Enter the password: ')
            if selection == 1:
                print(f'The encoded password is: {encoder(password)}!')

            elif selection == 2:
                print(f'The decoded password is: {decoder(password)}!')

        else:
            exit()


main()
