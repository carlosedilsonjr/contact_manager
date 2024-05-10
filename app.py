# import contacts

def app():
  while True:
    print('\nContact Manager Menu')
    print('1. Add contact')
    print('2. List all contacts')
    print('3. Edit a contact')
    print('4. Set contact as favorite')
    print('5. List the favorite contacts')
    print('6. Delete contact')
    print('0. Exit the program\n')

    option_selected = input('Choose one option: ')

    if option_selected == '0':
      break

app()