# Contact Book Application

contacts = []

def add_contact():
    """Adds a new contact to the list."""
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"Contact for {name} added successfully!")

def view_contacts():
    """Displays all contacts."""
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Your Contacts ---")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")
    print("--------------------")

def search_contact():
    """Searches for a contact by name."""
    search_term = input("Enter the name of the contact to search for: ")
    found_contacts = [c for c in contacts if search_term.lower() in c['name'].lower()]
    
    if not found_contacts:
        print("No contact found with that name.")
        return
    
    print("\n--- Found Contacts ---")
    for contact in found_contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print("--------------------")

def update_contact():
    """Updates an existing contact."""
    view_contacts()
    try:
        contact_index = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= contact_index < len(contacts):
            contact = contacts[contact_index]
            print("Leave field empty to keep current value.")
            
            new_name = input(f"New Name ({contact['name']}): ")
            new_phone = input(f"New Phone ({contact['phone']}): ")
            new_email = input(f"New Email ({contact['email']}): ")
            new_address = input(f"New Address ({contact['address']}): ")

            if new_name: contact['name'] = new_name
            if new_phone: contact['phone'] = new_phone
            if new_email: contact['email'] = new_email
            if new_address: contact['address'] = new_address
            
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid contact number.")

def delete_contact():
    """Deletes a contact."""
    view_contacts()
    try:
        contact_index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            removed_contact = contacts.pop(contact_index)
            print(f"Contact for {removed_contact['name']} deleted successfully!")
        else:
            print("Invalid contact number.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid contact number.")

def main():
    while True:
        print("\n--- CONTACT BOOK MENU ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()