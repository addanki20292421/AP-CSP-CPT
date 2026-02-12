items = {} # stores items
running = True # keeps the program running until the user dosent want it to anymore


def select_itemtype(text, items):
    item_types = items.keys()
    number = 1
    itemtype_number_thingy = {}
    for item_type in item_types:
        print(f"{number}) {item_type}")
        itemtype_number_thingy[str(number)] = item_type
        number += 1
    
    item_to_change = input(text)
    # validate that the user wants to select something that exists
    if not item_to_change in itemtype_number_thingy.keys():
        print("item_to_change", " is not a item type that exists.\n\n")
        return
    item_to_change = itemtype_number_thingy[item_to_change]
    return item_to_change

while running:
    # show the user a menu for what they can fo
    print("\n\n\tInventory Management System")
    print(" 1) Get inventory\n 2) Update item\n 3) Change item types\n 0) Stop")
    user_input = input(">")
    print("\n\n\n")
    
    # stop if the user says stop
    if user_input == "0":
        running = False
    # show the inventory
    elif user_input == "1":
        for item_type in items:
            print(f"{item_type}: {items[item_type]}")
    # the user selected to update an item
    elif user_input == "2":
        item_to_change = select_itemtype("what item to change? ", items)
        
        amount_to_change = input("How much has the amount changed(represent loss with negative)? ")

        # because you can never have negative of something
        if items[item_to_change] + int(amount_to_change) < 0:
            print("Item cannot lose more than than its current volume\n\n")
            continue

        #actually make the change and show it to the user
        items[item_to_change] += int(amount_to_change)
        print("Item successfully changed")
        print("Old volume: ", items[item_to_change] - int(amount_to_change))
        print("New volume: ", items[item_to_change])
        print("\n\n")
    elif user_input == "3":
        print("\tItem Type Management")
        print(" 1) Delete Item Type\n 2) Add Item Type\n 0) Exit Item Type Management")
        itm_user_input = input(">")
        # Exit
        if itm_user_input == "0":
            print("Exiting Item Type Management\n")
            continue
        elif itm_user_input == "1":
            itemtype_to_delete = select_itemtype("what item to delete? ", items)
            # make sure the user isnt deleting something that is nonexistent
            del items[itemtype_to_delete]
            print(f"Successfully deleted \"{itemtype_to_delete}\" and all data relating to it\n\n")
        elif itm_user_input == "2":
            itemtype_to_add = input("What is the name of the new item type? ")
            # make sure the user didnt already make this type
            if itemtype_to_add in items.keys():
                print(f"\"{itemtype_to_add}\" already exists")
                continue
            items[itemtype_to_add] = 0
            print(f"added \"{itemtype_to_add}\"")
    else:
        # in case the user didnt select a option that exists
        print("invalid option")

        
        

