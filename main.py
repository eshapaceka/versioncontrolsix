def encoder(password):
    new_integer = ''  # acts as a "list" but a string to develop a new set of integers
    for integer in password:  # for loop to add three to each digit
        single_int = ((int(integer)) + 3) % 10  # wraps the integer in int to add three with modulo to isolate the integer
        single_int = str(single_int). # changes to str to be able to be added
        new_integer += single_int  # added to the empty string
    return new_integer  # returns the new integer after the for loop concludes



def main():
    while True:  # continues to run the code
        print()
        print('Welcome to Password Coding!')
        print('------------------')
        print()
        print('1. Encode Password')
        print('2. Decode Password')
        print('3. Exit')
        print()
        selection = int(input('Select an option: '))

        if selection in range(1, 3):  # ensures numbers other than 1 or 2 are not entered
            password = input('Enter the password: ')
            if selection == 1:
                print(f'The encoded password is: {encoder(password)}!')

            elif selection == 2:
                print(f'The decoded password is: {decoder(password)}!')

        else:  # exits for option 3 and any other number besides 1 and 2
            exit()


main()
