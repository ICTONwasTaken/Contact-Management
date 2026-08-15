def choice():
    print("Choose\nAdd a Contact(1)\nRemove a Contact(2)\nSort Contacts\(3)\n")
    x = input()
    return x


decision = choice()
print("You chose " + decision)