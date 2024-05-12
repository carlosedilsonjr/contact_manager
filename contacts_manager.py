def add_contact(contacts: list, name: str, phone: str, email: str, favorite=False):
  contacts.append({
    'name': name,
    'phone': phone,
    'email': email,
    'favorite': favorite
  })
  print(f'--> The contact "{name}" was added successfully!')

def list_contacts(contacts: list):
  for index, contact in enumerate(contacts):
    print(f'{index + 1:2d}. {contact['name']:10s} | {contact['phone']:10} | {contact['email']:15s} | {contact['favorite']}')

def edit_contact(contacts: list, contact_index: str, name: str, phone: str, email: str):
  adjusted_contact_index = int(contact_index) - 1
  if name:
    contacts[adjusted_contact_index]['name'] = name
  if phone:
    contacts[adjusted_contact_index]['phone'] = phone
  if email:
    contacts[adjusted_contact_index]['email'] = email
  print(f'\n--> Contact "{contacts[adjusted_contact_index]['name']}" was updated successfully!')

def favorite_contact(contacts: list, contact_index: str):
  adjusted_contact_index = int(contact_index) - 1
  contacts[adjusted_contact_index]['favorite'] = not contacts[adjusted_contact_index]['favorite']
  if contacts[adjusted_contact_index]['favorite']:
    print(f'\n--> Contact "{contacts[adjusted_contact_index]['name']}" marked as favorite!')
  else:
    print(f'\n--> Contact "{contacts[adjusted_contact_index]['name']}" unmarked as favorite!')
