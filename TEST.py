def choice():
    print("Choose\nAdd a Contact(1)\nRemove a Contact(2)\nSort Contacts(3)\nExit(4)\n \n")
    x = input("Choice: ")
    return x

Doing = True

while Doing == True:
    decision = int(choice())
    if decision >= 4:
        Doing = False
    print("YAY!\n")
