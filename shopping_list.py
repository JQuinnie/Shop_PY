import os


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
    print("="*30)
    print("What do you need to pick up at the store?")
    print("""
Enter 'SHOW' to show current list of items.
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
""")
    print("="*30)


# create a function named add_to_list that declares a parameter named item
def add_to_list(item):
    show_list()
    # add the item to the list
    shopping_list.append(item)
    # notify user that the item was added, and state the number of items in the list currently
    print("Item added succesfully. There are currently {} items on the list.".format(
        len(shopping_list)))


# define a function named show_list that prints all the items in the list
def show_list():
    clear_screen()
    print("Here's your list:")
    # start index at 1 to add number to list items
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

    print("-"*16)


show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == "HELP":
        show_help()
        # continue continues on the iteration
        continue
    # enable the SHOW command to show the list
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    # call add_to_list with new_item as an argument
    else:
        add_to_list(new_item)
# show list on completion
show_list()
