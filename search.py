# This is menu brooo
def display_menu(contacts_list):
    print("\n=== Contact List ===")
    display_contacts(contacts_list)

    print("\n=== List Menu ===")
    print("1. Sort by Name (A-Z)")
    print("2. Sort by Name (Z-A)")
    print("3. Sort by Phone Number")
    print("4. Search by Name")
    print("5. Exit")
    return input("Choose(1-5): ")

# Core functions stuff
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
def display_main(contacts_list:dict):
    while True:
        choice = display_menu(contacts_list)
        
        if choice == "1":
            sorted_contacts = sort_by_name(contacts_list)
            print("\n--- Sorted by Name (A-Z) ---")
            display_contacts(sorted_contacts)
            print("--- Sorted by Name (A-Z) ---")
        elif choice == "2":
            sorted_contacts = sort_by_name(contacts_list, reverse=True)
            print("\n--- Sorted by Name (Z-A) ---")
            display_contacts(sorted_contacts)
            print("--- Sorted by Name (Z-A) ---")
        elif choice == "3":
            sorted_contacts = sort_by_phone(contacts_list)
            print("\n--- Sorted by Phone Number ---")
            display_contacts(sorted_contacts)
            print("--- Sorted by Phone Number ---")
        elif choice == "4":
            search_query = input("Enter name to search: ")
            results = search_by_name(contacts_list, search_query)
            if results:
                print(f"\n--- Search Results for '{search_query}' ---")
                display_contacts(results)
                print(f"--- Search Results for '{search_query}' ---")
            else:
                print(f"\n--- No contacts found matching '{search_query}' ---")
        elif choice == "5":
            print("\n=== Exiting Contact List... ===")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    display_main()