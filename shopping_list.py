# create a new empty list named shopping_list
shopping_list = []


# create function for display HELP
def show_help():
    print('')
    print('========================================')
    print("What do you need to pick up at the store?")
    print("""
Enter 'SHOW' to show current list of items.
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
""")
    print('========================================')


# create a function named add_to_list that declares a parameter named item
def add_to_list(item):
    # add the item to the list
    shopping_list.append(item)
    # notify user that the item was added, and state the number of items in the list currently
    print("Item added succesfully. There are currently {} items on the list.".format(
        len(shopping_list)))


# define a function named show_list that prints all the items in the list
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print("- " + item)


show_help()

while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        # continue continues on the iteration
        continue
    # enable the SHOW command to show the list
    elif new_item == 'SHOW':
        show_list()
        continue
    # call add_to_list with new_item as an argument
    add_to_list(new_item)
# show list on completion
show_list()
