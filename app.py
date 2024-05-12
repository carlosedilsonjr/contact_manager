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
    elif option_selected == '2':
      contacts_manager.list_contacts(contacts)
    elif option_selected == '3':
      contacts_manager.list_contacts(contacts)
      contact_index = input('Enter the number of the contact you want to edit: ')
      name = input('Enter the new name of the contact or leave it blank: ')
      phone = input('Enter the new phone of the contact or leave it blank: ')
      email = input('Enter the new email of the contact or leave it blank: ')
      contacts_manager.edit_contact(contacts, contact_index, name, phone, email)
    elif option_selected == '4':
      contacts_manager.list_contacts(contacts)
      contact_index = input('Enter the number of the contact you want to favorite: ')
      contacts_manager.favorite_contact(contacts, contact_index)
    elif option_selected == '5':
      contacts_manager.list_favorite_contacts(contacts)
    elif option_selected == '0':
      break

app()
