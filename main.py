import pyperclip as pc

def cipher_text():
    text_input = input('Gimme a sentence to cipher: \n\n>>> ')
    shift_amount = input('Number please: \n\n>>> ')

    cipher = []
    for i in text_input:
        ordinal_code = ord(i) + int(shift_amount)
        letter_code = chr(ordinal_code)
        cipher.append(letter_code)
        
    cipher = ''.join(cipher)

    print(f'Plain text is: {text_input}')
    print(f'Ciphered text is: {cipher}')
    print(f'Ciphered using ROT{shift_amount}')


    confirmation = input("Would you like to copy to clipboard?\n Please enter yes or y")
    if confirmation == 'yes' or 'y':
        pc.copy(cipher)
        print('Text copied to clipboard.')

def decipher_text():
    text_input = input('Gimme a sentence to decipher: \n\n>>> ')
    shift_amount = input('Number please: \n\n>>> ')

    plain = []
    for i in text_input:
        ordinal_code = ord(i) - int(shift_amount)
        letter_code = chr(ordinal_code)
        plain.append(letter_code)
    
    plain = ''.join(plain)
    print(f'Plain text is: {plain}')


def menu():
    print('\n1: Cipher text')
    print('2: Decipher text')
    print('3: Exit program')
    choice = input('\nPlease choose a number based off of the options provided above:\n\n>>> ')

    if choice == '1':
        cipher_text()
    elif choice == '2':
        decipher_text()
    elif choice == '3':
        print('\nExiting program.')
        return
    else:
        print('\nNot an option. Let us try this again.')
        menu()

menu()