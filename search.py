class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"{self.name}: {self.phone}"

contacts = [
    {
        "Name" : "Jerms",
        "Contact Number" : "0928906123"
    },

    {
        "Name" : "Andrei",
        "Contact Number" : "12345"
    },

    {
        "Name" : "Marius",
        "Contact Number" : "999"
    }
]

def display_menu():
    print("\n=== Contact Management ===")
    print("1. Sort by Name (A-Z)")
    print("2. Sort by Name (Z-A)")
    print("3. Sort by Phone Number")
    print("4. Search by Name")
    print("5. View All Contacts")
    print("6. Exit")
    return input("Choose an option (1-6): ")

def sort_by_name(contacts, reverse=False):
    return sorted(contacts, key=lambda x: x["Name"].lower(), reverse=reverse)

def sort_by_phone(contacts):
    return sorted(contacts, key=lambda x: x["Contact Number"])

def search_by_name(contacts, query):
    results = [c for c in contacts if query.lower() in c["Name"].lower()]
    return results if results else None

def display_contacts(contacts_list):
    if not contacts_list:
        print("No contacts found.")
        return
    for contact in contacts_list:
        print(f"  {contact['Name']}: {contact['Contact Number']}")

# Main loop
while True:
    choice = display_menu()
    
    if choice == "1":
        sorted_contacts = sort_by_name(contacts)
        print("\n--- Sorted by Name (A-Z) ---")
        display_contacts(sorted_contacts)
    elif choice == "2":
        sorted_contacts = sort_by_name(contacts, reverse=True)
        print("\n--- Sorted by Name (Z-A) ---")
        display_contacts(sorted_contacts)
    elif choice == "3":
        sorted_contacts = sort_by_phone(contacts)
        print("\n--- Sorted by Phone Number ---")
        display_contacts(sorted_contacts)
    elif choice == "4":
        search_query = input("Enter name to search: ")
        results = search_by_name(contacts, search_query)
        if results:
            print(f"\n--- Search Results for '{search_query}' ---")
            display_contacts(results)
        else:
            print(f"No contacts found matching '{search_query}'")
    elif choice == "5":
        print("\n--- All Contacts ---")
        display_contacts(contacts)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-6.")


