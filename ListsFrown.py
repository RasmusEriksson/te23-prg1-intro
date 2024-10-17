#I'm bored


Items = ["Potion","Sword","Deathspell"]

while True:
    choice = input("Whatcha wanna doo, write the corresponding number for your option \n[1] see items\n[2] add new item to inventory \n[3] Remove item from inventory")

    if choice == "1":

        print("\n")
        for item in Items:
            print(item)
        print("\n")

    elif choice == "2":

        print("\n")
        newItem = input("What's your new item?: ")
        Items.append(newItem)
        print("\n")

    elif choice == "3":
        removed = False

        while removed == False:


            print("\n")
            print(" ".join(Items))
            print("input [none] if you don't wanna remove anything")
            itemRemove = input("What item would you like to remove from this list? ")

            if itemRemove in Items:
                Items.pop(Items.index(itemRemove))
                removed = True
            elif itemRemove.lower() == "none":
                removed = True

        
        


