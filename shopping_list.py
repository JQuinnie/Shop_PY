def show_help():
    print('')
    print('========================================')
    print("What do you need to pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
""")
    print('========================================')


show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        # continue continues on the iteration
        continue
