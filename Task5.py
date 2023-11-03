# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    contacts[name] = contact
    print(f"Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for name, contact in contacts.items():
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found = False
    
    for name, contact in contacts.items():
        if search_term.lower() in name.lower() or search_term in contact['phone']:
            print("Search Result:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            
    if not found:
        print("Contact not found.")

# Function to update an existing contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        contact = contacts[name]
        print("Current Contact Information:")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        
        new_phone = input("Enter the new phone number (press Enter to keep current): ")
        new_email = input("Enter the new email address (press Enter to keep current): ")
        new_address = input("Enter the new address (press Enter to keep current): ")
        
        if new_phone:
            contact['phone'] = new_phone
        if new_email:
            contact['email'] = new_email
        if new_address:
            contact['address'] = new_address
        
        print("Contact updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

# Main function to display the menu and handle user input
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the Contact Book application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
