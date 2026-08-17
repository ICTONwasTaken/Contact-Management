def display_menu(contacts_list):
    print("\n=== Contact List ===")
    display_contacts(contacts_list)

    print("\n=== Add/Delete Menu ===")
    print("1. Add a Contact")
    print("2. Delete a Contact")
    print("3. Exit")
    return input("Choose(1-3): ")

def display_contacts(contacts_list):
    if not contacts_list:
        print("No contacts found.")
        return
    for contact in contacts_list:
        print(f"  {contact['Name']}: {contact['Contact Number']}")

def add_contact(contacts_list):
    name = input("Name: ")
    number = input("Contact Number: ")
    contacts_list.append({"Name": name, "Contact Number": number})
    searched = name.capitalize()
    print(f"\n--- {searched} added to contacts! ---")

def del_contact(contacts_list):
    name = input("Name to delete: ")
    if not contacts_list:
        print("No contacts found.")
        return

    found = any(c["Name"].lower() == name.lower() for c in contacts_list) # Looks through list, if one matches name it outputs true, woooow
    if not found:
        print(f"\n--- No contact named '{name.capitalize()}' found. ---")
        return

    contacts_list[:] = [c for c in contacts_list if c["Name"].lower() != name.lower()]
    print(f"\n--- {name.capitalize()} deleted from contacts! ---")

def display_main(contacts_list):
    while True:
        choice = display_menu(contacts_list)
        if choice == "1":
            add_contact(contacts_list)
        elif choice == "2":
            del_contact(contacts_list)
        elif choice == "3":
            print("\n=== Exiting Contact List... ===")
            break
        else:
            print("Invalid option. Please choose 1-3.")
    return contacts_list

if __name__ == "__main__":
    display_main()