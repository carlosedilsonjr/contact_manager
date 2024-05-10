def add_contact(contacts: list, name: str, phone: str, email: str, favorite=False):
  contacts.append({
    "name": name,
    "phone": phone,
    "email": email,
    "favorite": favorite
  })

def list_contacts(contacts: list):
  for index, contact in enumerate(contacts):
    print(f'{index + 1}. {contact["name"].capitalize()} ({contact["phone"]})')
