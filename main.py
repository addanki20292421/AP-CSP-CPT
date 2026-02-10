"""
we needa big infinity loop
dictionary to store everything
conditionals to validate
inputs to take usert input
procedures
other stuff later
"""

items = {}
running = True
while running:
    print(" 1) Get inventory\n 2) Update item\n 3) Change item types\n 0) Stop")
    user_input = input(">")
    if user_input == "0":
        running = False
    elif user_input=="1":
        print(items)
    elif user_input=="2":
        print(items)
        item_to_change = input("what item do you want to update? ")

