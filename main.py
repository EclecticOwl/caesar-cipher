def cipher_text():

    text_input = input('Gimme a sentence to cipher: \n\n>>> ')
    shift_amount = input('Number please: \n\n>>> ')

    cipher = []
    for i in text_input:
        number_code = ord(i) + int(shift_amount)
        letter_code = chr(number_code)
        cipher.append(letter_code)
    
    cipher = ' '.join(cipher)
    cipher = cipher.replace(' ', '')

    print(f'Plain text is: {text_input}')
    print(f'Ciphered text is: {cipher}')
    print(f'Ciphered using ROT{shift_amount}')

def decipher_text():

    text_input = input('Gimme a sentence to decipher: \n\n>>> ')
    shift_amount = input('Number please: \n\n>>> ')

    plain = []
    for i in text_input:
        number_code = ord(i) - int(shift_amount)
        letter_code = chr(number_code)
        plain.append(letter_code)
    
    plain = ' '.join(plain)
    plain = plain.replace(' ', '')

    print(f'Plain text is: {plain}')


def menu():
    print('1: Cipher text')
    print('2: Decipher text')
    choice = input('Please choose a number based off of the options provided above: \n\n')

    if choice == '1':
        cipher_text()
    elif choice == '2':
        decipher_text()
    else:
        print('That is not a valid choice. \n\nNow exiting function....')






menu()