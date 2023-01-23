'''
I have split the code into 3 files, 
class_file for class,
functions for functions,
and inventory for the main logic.

I have also changed the .txt file into a .csv file as it has more real world use case.
As well as adding a new shoe into the csv file, rather than just to the list. 
'''
# import all functions from functions 
import functions

# call read shoe data to add csv into shoe list 
functions.read_shoes_data()

#==========Main Menu=============
# while True show menu for user input 
while True:
    menu = input('''
========================================================
                Please select action
========================================================
                  Enter new Shoe (n)
                  View all Shoes (v)
                  Restock lowest (r)
                    Search Shoe (s)
                View value of stock (vs)
            View highest quantity shoe (vq)
                        Exit (e)
========================================================
:                         ''').lower()

    # if n call capture shoes from functions
    if menu == 'n':
        functions.capture_shoes()

    # else if v call view all from functions
    elif menu == 'v':
        functions.view_all()

    # else if r call re_stock from functions
    elif menu == 'r':
        functions.re_stock()

    # else if s call search shoe from functions
    elif menu == 's':
        functions.search_shoe()

    # else if vs call value per item from functions
    elif menu == 'vs':
        functions.value_per_item()

    # else if vq call highest qty from functions
    elif menu == 'vq':
        functions.highest_qty()

    # else if e exit break
    elif menu == 'e':
        print('''
========================================================
                     Goodbye
========================================================
''')
        break
    
    # else incorrect input
    else:
        print('''
========================================================
                 Incorrect input
========================================================''')
        continue