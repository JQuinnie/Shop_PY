# Shop_PY

A simple shopping list application in Python using the Python interactive shell.

## Before You Begin

1.  Install Python for your OS (it might be pre-installed): https://wiki.python.org/moin/BeginnersGuide/Download
2.  Make sure the installed Python version is Python 3
3.  `Git Clone` or `Git Fork` this repo to get the `shopping_list.py` file

## Application Usage

1.  Start up file by using Python interactive shell and type:

```
> python shopping_list.py
```

2.  You will be given the **HELP** prompt as displayed below:

```
==================================================
What do you need to pick up at the store?

Enter 'SHOW' to show current list of items.
Enter 'REMOVE' to delete an item from list.
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.

==================================================
```

3.  Start typing an item to add to the shopping list, press **ENTER** to add each item
4.  On subsequent items to be added to the list, you will be prompted to specify the number where the item should go, such as below:

```
Your Shopping list:
--------------------
1. apples
--------------------
What number should bananas be on the list?
Press ENTER to add to the end of the list
```

5.  To remove an item, simply enter command **REMOVE** and type the item you would like to remove

```
Your Shopping list:
--------------------
1. apples
2. bananas
3. oranges
4. carrots
--------------------
What would you like to remove?
> carrots
```

6.  Finally, finish the list and exit program by entering **DONE**, this command will also print your shopping list to a file called `my_shopping_list.txt` located in the same directory as your `shopping_list.py` file

_HAPPY SHOPPING!_

## Additional Resources

- Python for Beginners: https://www.python.org/about/gettingstarted/
- Python Setup and Usage: https://docs.python.org/3/using/index.html
