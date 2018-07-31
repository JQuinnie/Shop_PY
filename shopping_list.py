import os
import sys

# create a new empty list named shopping_list
shopping_list = []


# create function to clear screen between operations
# os library can run system level script, if user on windows? either run nt or clear depending on OS
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# create function for display HELP
def show_help():
    clear_screen()
    print("")
    print("="*50)
    print("What do you need to pick up at the store?")
    print("""
Enter 'SHOW' to show current list of items.
Enter 'REMOVE' to delete an item from list.
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
""")
    print("="*50)


# create a function named add_to_list that declares a parameter named item
def add_to_list(item):
    show_list()
    # if there is something on the list then ask where to add it
    if len(shopping_list):
        position = input("What number should {} be on the list?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0
    # try to turn position into integer, absolute value
    try:
        position = abs(int(position))
    # ValueError thrown if position is not an integer, then make it position None and append to list
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(item)

    show_list()


# define a function named show_list that prints all the items in the list
def show_list():
    clear_screen()
    print("Your Shopping list:")
    print("-"*20)
    # start index at 1 to add number to list items
    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))

    print("-"*20)


# define a function named remove_from_list that will remove an item from the list
def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
        print("{} where not on the list".format(what_to_remove))
    show_list()


show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        # redirect stdout into a file and prints output
        sys.stdout = open('my_shopping_list.txt', 'wt')
        print()
        break
    elif new_item.upper() == "HELP":
        show_help()
        # continue continues on the iteration
        continue
    # enable the SHOW command to show the list
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    # enable the REMOVE command to remove an item from list
    elif new_item.upper() == "REMOVE":
        remove_from_list()
    # call add_to_list with new_item as an argument
    else:
        add_to_list(new_item)
# show list on completion
show_list()
