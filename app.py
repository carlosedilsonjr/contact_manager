import contacts_manager

def app():
  contacts = []
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

    if option_selected == '1':
      name = input('Enter a name of the contact: ')
      phone = input('Enter a phone of the contact: ')
      email = input('Enter an email of the contact: ')
      contacts_manager.add_contact(contacts, name, phone, email)
      print(f'--> The contact "{name}" was added successfully!')
    elif option_selected == '2':
      contacts_manager.list_contacts(contacts)
    elif option_selected == '0':
      break

app()
