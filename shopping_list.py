def show_help():
    print("What do you need to pick up at the stor?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
""")


while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
