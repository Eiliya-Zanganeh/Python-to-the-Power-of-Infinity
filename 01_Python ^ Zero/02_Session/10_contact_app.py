contacts = {}


while True:
    name = input('Enter your name ( q for quit ): ')
    if name == 'q':
        break
    number = input('Enter your phone number: ')

    contacts[name] = number

print(contacts)