# import class_file 
import class_file

#=============Shoe list===========
shoe_list = []

#==========Functions==============

# define function to read the csv file and add each shoe as an object, using class_file, to shoe list
# use try except to make sure file exists
def read_shoes_data():
    loop = 0
    try:
        with open('inventory.csv', 'r') as f:
            for line in f:
                if loop == 0:
                    loop += 1
                    continue
                line = line.strip()
                line = line.split(',')
                shoe_class = class_file.Shoe(line[0],line[1],line[2],line[3],line[4])
                shoe_list.append(shoe_class)
                loop += 1
    except FileExistsError:
        print('File doesn\'t exist')
    loop = 0

# define function to write new shoe to csv file
def write_new_shoe(new_shoe):
    with open('inventory.csv', 'a') as f:
        f.write(f'\n{new_shoe}')
    
# define function to take in new shoe. append new object to list, using class_file, call write new shoe
def capture_shoes():
    print('========================================================')
    new_country = input('Enter Country:        ')
    new_code = input('Enter Code:           ')
    new_product = input('Enter Product:        ')
    new_cost = input('Enter cost:           ')
    new_quantity = input('Enter Quantity:       ')
    print('========================================================')
    shoe_list.append(class_file.Shoe(new_country,new_code,new_product,new_cost,new_quantity))
    write_new_shoe(f'{new_country},{new_code},{new_product},{new_cost},{new_quantity}')

# define function to view all objects
def view_all():
    for shoe in shoe_list:
        print(f'''
========================================================
            Country:        {shoe.country}
            Code:           {shoe.code}
            Product:        {shoe.product}
            Cost:           {shoe.cost}
            Quantity:       {shoe.quantity}
========================================================
''')

# define function to find the lowest stock amount and display each item
# ask user how many they want to re-stock and check if correct
# update stock quantity and rewrite csv file
def re_stock():
    stock_amounts = []
    for shoe in shoe_list:
        stock_amounts.append(int(shoe.get_quantity()))

    sorted_stock = sorted(stock_amounts)
    lowest_stock = sorted_stock[0]

    for shoe in shoe_list:
        if shoe.quantity == str(lowest_stock):
            print(f'''
========================================================
            Country:        {shoe.country}
            Code:           {shoe.code}
            Product:        {shoe.product}
            Cost:           {shoe.cost}
            Quantity:       {shoe.quantity}
========================================================''')
    
    while True:
        try:
            amount = int(input('How many pairs to re-stock?:                        '))
            break
        except ValueError:
            print('Please enter a number')
            continue

    refill = input(f'Refill stock by {amount} pairs of each shoe in list? y/n:      ').lower()
    print('========================================================')
    if refill == 'y':
        for line in shoe_list:
            if line.quantity == str(lowest_stock):
                line.quantity = str(int(line.quantity) + {amount})
        with open('inventory.csv', 'w') as f:
            f.write('Country,Code,Product,Cost,Quantity')
            for line in shoe_list:
                f.write(f'\n{line}')
        print('''                   Stock Refilled
========================================================''')
        return         
    else: 
        return

# define function to search shoe by code or product display searched shoe
def search_shoe():
    search_param = input('''
========================================================
   Search by Code or Product? c/p:          ''').lower()
    if search_param == 'c':
        search = input('''
========================================================
            Enter the Code:         ''')
        for shoe in shoe_list:
            if shoe.code == search:
                print(f'''
========================================================
            Country:        {shoe.country}
            Code:           {shoe.code}
            Product:        {shoe.product}
            Cost:           {shoe.cost}
            Quantity:       {shoe.quantity}
========================================================
            ''')
        return     
    elif search_param == 'p':
        search = input('Enter the Product:         ')
        for shoe in shoe_list:
            if shoe.product == search:
                print(f'''
========================================================
            Country:        {shoe.country}
            Code:           {shoe.code}
            Product:        {shoe.product}
            Cost:           {shoe.cost}
            Quantity:       {shoe.quantity}
========================================================
''')
        return
    else:
        print('Incorrect input')

# define function to show stock value for each stock item
def value_per_item():
    for shoe in shoe_list:
        try:
            shoe_cost = int(shoe.get_cost())
            shoe_quantity = int(shoe.get_quantity())
        except ValueError:
            print('Not a number')
        total_cost = shoe_cost * shoe_quantity
        print(f'''
========================================================
    {shoe.product} total stock cost is {total_cost}
========================================================
''')

# define function to find highest quantity and show it for sale  
def highest_qty():
    stock_amounts = []
    for line in shoe_list:
        stock_amounts.append(int(line.quantity))

    sorted_stock = sorted(stock_amounts)
    highest_stock = sorted_stock[-1]

    for line in shoe_list:
        if line.quantity == str(highest_stock):
            print(f'''
========================================================
                    For Sale:
            Country:        {line.country}
            Code:           {line.code}
            Product:        {line.product}
            Cost:           {line.cost}
            Quantity:       {line.quantity}
========================================================
''')    