import search, addel

def choice():
    print("\n=== Contact List ===")
    search.display_contacts(contacts)

    print("\n=== Main Menu ===")
    print("1. Add/Remove Contact\n2. Contact List\n3. Exit")
    decision = int(input("Choose(1-3): "))
    return decision


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
    },
    {
        "Name" : "Martin",
        "Contact Number" : "998"
    }
]

doing = True

while doing == True:
    decision = choice()
    if decision == 1:
        contacts = addel.display_main(contacts)
    elif decision == 2:
        search.display_main(contacts)
    elif decision == 3:
        doing = False
