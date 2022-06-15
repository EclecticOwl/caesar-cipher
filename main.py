import pyperclip as pc
import random

class CaesarCipher():

    def __init__(self):

        self.menu()

    def wipe(self):
        print("\033c", end='')

    def rand_reply(self):
        rando = random.randint(1, 5)

        if rando == 1:
            print('You think it is that easy to break it? Try again!\n')
        elif rando == 2:
            print('Sorry, champ! Try again.\n')
        elif rando == 3:
            print('Please listen to the instructions for some cake.\n')
        elif rando == 4:
            print('There are only three options available. No cash prizes.\n')
        else:
            print('You win a prize! The exact same menu!\n')
    
    def cipher_text(self):
        text_input = input('Gimme a sentence to cipher: \n\n>>> ')
        shift_amount = input('Choose a shift amount for the cipher: \n\n>>> ')

        if not shift_amount.isnumeric():
            print('No cake for you! Only numbers')
            self.menu()

        cipher = []
        for i in text_input:
            ordinal_code = ord(i) + int(shift_amount)
            letter_code = chr(ordinal_code)
            cipher.append(letter_code)
            
        cipher = ''.join(cipher)

        print(f'Plain text is: {text_input}\n')
        print(f'Ciphered text is: {cipher}')
        print(f'Ciphered using ROT{shift_amount}')

        confirmation = input("\nWould you like to copy to clipboard?\nPlease enter yes or y:\n\n>>> ")
        if confirmation == 'yes' or 'y':
            pc.copy(cipher)
            print('Text copied to clipboard.')
        
        self.menu()
    
    def decipher_text(self):
        text_input = input('Gimme a sentence to decipher: \n\n>>> ')
        shift_amount = input('Please enter the required cipher shift amount: \n\n>>> ')

        if not shift_amount.isnumeric():
            print('No cake for you! Only numbers')
            self.decipher_text()

        plain = []
        for i in text_input:
            ordinal_code = ord(i) - int(shift_amount)
            letter_code = chr(ordinal_code)
            plain.append(letter_code)
        
        plain = ''.join(plain)
        print(f'Plain text is: {plain}')

        self.menu()
    
    def menu(self):
        print('Menu options:')
        print('\n1: Cipher text\n')
        print('2: Decipher text\n')
        print('3: Exit program\n\n')

        choice = input('\nPlease choose a menu option based off of the numbers above:\n\n>>> ')

        if choice == '1':
            self.wipe()
            self.cipher_text()
        elif choice == '2':
            self.wipe()
            self.decipher_text()
        elif choice == '3':
            self.wipe()
            print('\nExiting program.')
            return
        else:
            self.wipe()
            self.rand_reply()
            self.menu()

caesar = CaesarCipher()