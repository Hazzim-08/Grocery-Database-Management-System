import mysql.connector as mys
from tabulate import tabulate
#------------------------------------------------------------------ESTABLISHING CONNECTION------------------------------------------------------------------#

mydb = mys.connect(
    host='localhost',
    user='root',
    passwd='123password',
    database='Grocery_Database_Management_System')

mycursor = mydb.cursor()
if mydb.is_connected():
    print('SUCCESSFULLY CONNECTED')

#----------------------------------------------------------------------CREATING TABLES----------------------------------------------------------------------#

def create_table_items():
    query = 'CREATE TABLE ITEMS (Item_ID VARCHAR(255),Description VARCHAR(100), Brand_Name VARCHAR(100), Category VARCHAR(100), Barcode VARCHAR(255))'
    mycursor.execute(query)
    print('ITEMS TABLE CREATED')
    
create_table_items()

def create_table_item_category():
    query = 'CREATE TABLE ITEM_CATEGORY (Category_Code VARCHAR(100), Description VARCHAR(100), Category VARCHAR(200))'
    mycursor.execute(query)
    print('ITEM_CATEGORY TABLE CREATED')
    
create_table_item_category()

def create_table_item_brand():
    query = 'CREATE TABLE ITEM_BRAND (Brand_Code VARCHAR(100), Brand_Name VARCHAR(200))'
    mycursor.execute(query)
    print('ITEM_BRAND TABLE CREATED')
    
create_table_item_brand()

def create_table_item_prices():
    query = 'CREATE TABLE ITEM_PRICES (Item_ID VARCHAR(255), Barcode VARCHAR(255), Price_AED INT(255))'
    mycursor.execute(query)
    print('ITEM_PRICES TABLE CREATED')
    
create_table_item_prices()

def create_table_item_stock():
    query = 'CREATE TABLE ITEM_STOCK (Item_ID VARCHAR(255), Barcode VARCHAR(255), Stock_Quantity INT(255))'
    mycursor.execute(query)
    print('ITEM_STOCK TABLE CREATED')
    
create_table_item_stock()

#----------------------------------------------------------------------INSERTING VALUES----------------------------------------------------------------------#

def insert_values_items():
    values = [("01", "Eggs", "DairyDays", "Dairy", "000000000001"),
              ("02", "Milk", "DairyDays", "Dairy", "000000000002"),
              ("03", "Cheese", "DairyDays", "Dairy", "000000000003"),
              ("04", "Butter", "DairyDays", "Dairy", "000000000004"),
              ("05", "Crackers", "CrunchyDelights", "Biscuits", "000000000005"),
              ("06", "Cream Biscuits", "CrunchyDelights", "Biscuits", "000000000006"),
              ("07", "Rusks", "CrunchyDelights", "Biscuits", "000000000007"),
              ("08", "Cookies", "CrunchyDelights", "Biscuits", "000000000008"),
              ("09", "Tea Powder", "FreshMornings", "Drinks", "000000000009"),
              ("10", "Coffee Powder", "FreshMornings", "Drinks", "000000000010"),
              ("11", "Chicken", "RoyalButchers", "Meat", "000000000011"),
              ("12", "Mutton", "RoyalButchers", "Meat", "000000000012"),
              ("13", "Beef", "RoyalButchers", "Meat", "000000000013"),
              ("14", "Fish", "RoyalButchers", "Meat", "000000000014"),
              ("15", "Turkey", "RoyalButchers", "Meat", "000000000015"),
              ("16", "Apple", "FarmToPlate", "Fruits/Vegetables", "000000000016"),
              ("17", "Mango", "FarmToPlate", "Fruits/Vegetables", "000000000017"),
              ("18", "Orange", "FarmToPlate", "Fruits/Vegetables", "000000000018"),
              ("19", "Pineapple", "FarmToPlate", "Fruits/Vegetables", "000000000019"),
              ("20", "Watermelon", "FarmToPlate", "Fruits/Vegetables", "000000000020"),
              ("21", "Carrot", "FarmToPlate", "Fruits/Vegetables", "000000000021"),
              ("22", "Cucumber", "FarmToPlate", "Fruits/Vegetables", "000000000022"),
              ("23", "Tomatoes", "FarmToPlate", "Fruits/Vegetables", "000000000023"),
              ("24", "Onion", "FarmToPlate", "Fruits/Vegetables", "000000000024"),
              ("25", "Ginger", "FarmToPlate", "Fruits/Vegetables", "000000000025")]
              
    query = 'INSERT INTO ITEMS (Item_ID, Description, Brand_Name, Category, Barcode) VALUES (%s, %s, %s, %s, %s)'
    mycursor.executemany(query, values)
    mydb.commit()
    print('ITEMS TABLE SUCCESSFULLY POPULATED')
    
insert_values_items()

def insert_values_item_category():
    values = [("101", "Eggs", "Dairy"),
              ("102", "Milk", "Dairy"),
              ("103", "Cheese", "Dairy"),
              ("104", "Butter", "Dairy"),
              ("201", "Crackers", "Biscuits"),
              ("202", "Cream Biscuits", "Biscuits"),
              ("203", "Rusks", "Biscuits"),
              ("204", "Cookies", "Biscuits"),
              ("301", "Tea Powder", "Drinks"),
              ("302", "Coffee Powder", "Drinks"),
              ("401", "Chicken", "Meat"),
              ("402", "Mutton", "Meat"),
              ("403", "Beef", "Meat"),
              ("404", "Fish", "Meat"),
              ("405", "Turkey", "Meat"),
              ("501", "Apple", "Fruits/Vegetables"),
              ("502", "Mango","Fruits/Vegetables"),
              ("503", "Orange", "Fruits/Vegetables"),
              ("504", "Pineapple", "Fruits/Vegetables"),
              ("505", "Watermelon","Fruits/Vegetables"),
              ("506", "Carrot", "Fruits/Vegetables"),
              ("507", "Cucumber", "Fruits/Vegetables"),
              ("508", "Tomatoes", "Fruits/Vegetables"),
              ("509", "Onion", "Fruits/Vegetables"),
              ("510", "Ginger", "Fruits/Vegetables")]
              
    query = 'INSERT INTO ITEM_CATEGORY (Category_Code, Description, Category) VALUES (%s, %s, %s)'
    mycursor.executemany(query, values)
    mydb.commit()
    print('ITEM_CATEGORY TABLE SUCCESSFULLY POPULATED')
    
insert_values_item_category()

def insert_values_item_brand():
    values = [("DD", "DairyDays"),
              ("DD", "DairyDays"),
              ("DD", "DairyDays"),
              ("DD", "DairyDays"),
              ("CD", "CrunchyDelights"),
              ("CD", "CrunchyDelights"),
              ("CD", "CrunchyDelights"),
              ("CD", "CrunchyDelights"),
              ("FM", "FreshMornings"),
              ("FM", "FreshMornings"),
              ("RB", "RoyalButchers"),
              ("RB", "RoyalButchers"),
              ("RB", "RoyalButchers"),
              ("RB", "RoyalButchers"),
              ("RB", "RoyalButchers"),
              ("FTP", "FarmToPlate"),
              ("FTP", "FarmToPlate"),
              ("FTP", "FarmToPlate"),
              ("FTP", "FarmToPlate"),
              ("FTP", "FarmToPlate"),
              ("FTP", "FarmToPlate"),
              ("FTP", "FarmToPlate"),
              ("FTP", "FarmToPlate"),
              ("FTP", "FarmToPlate"),
              ("FTP", "FarmToPlate")]
              
    query = 'INSERT INTO ITEM_BRAND (Brand_Code, Brand_Name) VALUES (%s, %s)'
    mycursor.executemany(query, values)
    mydb.commit()
    print('ITEM_BRAND TABLE SUCCESSFULLY POPULATED')
    
insert_values_item_brand()

def insert_values_item_prices():
    values = [("01", "000000000001",15),
              ("02", "000000000002", 5),
              ("03", "000000000003", 10),
              ("04", "000000000004", 15),
              ("05", "000000000005", 10),
              ("06", "000000000006", 15),
              ("07", "000000000007", 10),
              ("08", "000000000008", 10),
              ("09", "000000000009", 20),
              ("10", "000000000010", 20),
              ("11", "000000000011", 15),
              ("12", "000000000012", 40),
              ("13", "000000000013", 30),
              ("14", "000000000014", 50),
              ("15", "000000000015", 200),
              ("16", "000000000016", 10),
              ("17", "000000000017", 25),
              ("18", "000000000018", 5),
              ("19", "000000000019", 15),
              ("20", "000000000020", 10),
              ("21", "000000000021", 5),
              ("22", "000000000022", 5),
              ("23", "000000000023", 5),
              ("24", "000000000024", 10),
              ("25", "000000000025", 5)]
              
    query = 'INSERT INTO ITEM_PRICES (Item_ID, Barcode, Price_AED) VALUES (%s, %s, %s)'
    mycursor.executemany(query, values)
    mydb.commit()
    print('ITEM_PRICES TABLE SUCCESSFULLY POPULATED')
    
insert_values_item_prices()

def insert_values_item_stock():
    values = [("01", "000000000001", 110),
              ("02", "000000000002", 245),
              ("03", "000000000003", 255),
              ("04", "000000000004", 150),
              ("05", "000000000005", 200),
              ("06", "000000000006", 455),
              ("07", "000000000007", 700),
              ("08", "000000000008", 170),
              ("09", "000000000009", 500),
              ("10", "000000000010", 200),
              ("11", "000000000011", 125),
              ("12", "000000000012", 405),
              ("13", "000000000013", 125),
              ("14", "000000000014", 565),
              ("15", "000000000015", 100),
              ("16", "000000000016", 365),
              ("17", "000000000017", 735),
              ("18", "000000000018", 815),
              ("19", "000000000019", 685),
              ("20", "000000000020", 165),
              ("21", "000000000021", 515),
              ("22", "000000000022", 215),
              ("23", "000000000023", 455),
              ("24", "000000000024", 110),
              ("25", "000000000025", 435)]
              
    query = 'INSERT INTO ITEM_STOCK (Item_ID, Barcode, Stock_Quantity) VALUES (%s, %s, %s)'
    mycursor.executemany(query, values)
    mydb.commit()
    print('ITEM_STOCK TABLE SUCCESSFULLY POPULATED')
    
insert_values_item_stock()

#----------------------------------------------------------------------MAIN FUNCTIONS----------------------------------------------------------------------#

def search_record():
    while True:
        table = input('What table would you like a record from? (ITEMS, ITEM_CATEGORY, ITEM_BRAND, ITEM_PRICES, ITEM_STOCK): ')
        if table.upper() in ('ITEMS', 'ITEM_CATEGORY', 'ITEM_BRAND', 'ITEM_PRICES', 'ITEM_STOCK'):
            break
        else:
            print('Table not found. Please try again.')

    query_dict = {
        'ITEMS': 'SELECT * FROM ITEMS',
        'ITEM_CATEGORY': 'SELECT * FROM ITEM_CATEGORY',
        'ITEM_BRAND': 'SELECT * FROM ITEM_BRAND',
        'ITEM_PRICES': 'SELECT * FROM ITEM_PRICES',
        'ITEM_STOCK': 'SELECT * FROM ITEM_STOCK'
    }

    mycursor.execute(query_dict[table.upper()])
    records = mycursor.fetchall()

    while True:
        try:
            if table.upper() == 'ITEMS':
                item_id = int(input('Enter the Item_ID of the record (1 - 25): '))
                for record in records:
                    if int(record[0]) == item_id:
                        print(record)
                        return

            elif table.upper() == 'ITEM_CATEGORY':
                category_code = int(input('Enter the Category_Code (101-104/201-204/301-302/401-405/501-510): '))
                for record in records:
                    if int(record[0]) == category_code:
                        print(record)
                        return

            elif table.upper() == 'ITEM_BRAND':
                brand_code = input('Enter the Brand_Code (DD, CD, FM, RB, FTP): ').upper()
                for record in records:
                    if record[0] == brand_code:
                        print(record)
                        return

            elif table.upper() == 'ITEM_PRICES':
                item_id = int(input('Enter the Item_ID of the record (1 - 25): '))
                for record in records:
                    if int(record[0]) == item_id:
                        print(record)
                        return

            elif table.upper() == 'ITEM_STOCK':
                item_id = int(input('Enter the Item_ID of the record (1 - 25): '))
                for record in records:
                    if int(record[0]) == item_id:
                        print(record)
                        return

            print('Record not found. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a valid ID.')


def delete_record():
    mycursor.execute('SELECT * from ITEMS')
    items = mycursor.fetchall()

    items_dict = {}
    for x in items:
        item_id = int(x[0])
        item_desc = x[1]
        brand_name = x[2]
        category = x[3]
        barcode = x[4]
        items_dict[item_id] = (item_desc, brand_name, category, barcode)

    while True:
        try:
            item_id = int(input('Enter the Item_ID of the record to delete (1-25) or 0 to exit: '))
            if item_id == 0:
                break
            elif item_id in items_dict:
                item_desc = items_dict[item_id][0]

                mycursor.execute('DELETE FROM ITEMS WHERE Item_ID = %s', (item_id,))
                mydb.commit()

                print(f'Record for {item_desc} has been deleted.')

                while True:
                    more = input('Delete more? (y/n): ').lower()
                    if more == 'y':
                        break
                    elif more == 'n':
                        return
                    else:
                        print('Invalid input. Please try again.')
            else:
                print('Item_ID not found. Please try again.')
        except ValueError:
            print("Invalid input. Please enter a numeric Item_ID.")


def check_stock():
    mycursor.execute('SELECT ITEMS.Item_ID, ITEMS.Description, ITEM_STOCK.Stock_Quantity FROM ITEMS INNER JOIN ITEM_STOCK ON ITEMS.Item_ID = ITEM_STOCK.Item_ID')
    stock = mycursor.fetchall()

    stock_dict = {}
    for x in stock:
        item_id = int(x[0])
        item_desc = x[1]
        stock_qty = x[2]
        stock_dict[item_id] = (item_desc, stock_qty)

    while True:
        try:
            check = int(input('Enter the Item_ID for which you would like to check stock (1-25) or 0 to exit: '))
            if check == 0:
                break
            elif check in stock_dict:
                item_desc, stock_qty = stock_dict[check]
                print(f'The stock quantity for {item_desc} is {stock_qty}')

                while True:
                    more = input('Check more? (y/n): ').lower()
                    if more == 'y':
                        break
                    elif more == 'n':
                        return
                    else:
                        print('Invalid input. Please try again.')
            else:
                print('Item_ID not found. Please try again.')
        except ValueError:
            print("Invalid input. Please enter a numeric Item_ID.")


cart = {}
def purchase():
    print('---------------------------------------- WELCOME TO PYGROCERS! ----------------------------------------')
    mycursor.execute('SELECT ITEMS.Description, ITEMS.Brand_Name, ITEMS.Category, ITEM_PRICES.Price_AED FROM ITEMS INNER JOIN ITEM_PRICES ON ITEMS.Item_ID = ITEM_PRICES.ITEM_ID')
    menu = mycursor.fetchall()
    print("Here's the menu:")
    print(tabulate(menu, headers=['Item', 'Brand', 'Category', 'Price (AED)'], tablefmt="double_outline"))

    global cart


    while True:
        item = input('Enter an item to purchase: ').lower()

        found = False
        for i in menu:
            if item == i[0].lower():
                print(f"Added to cart: {i[0]}")
                cart[i[0]] = i[3]
                found = True
                break

        if not found:
            print('Item not found. Please enter a valid item.')

        else:
            add = input('Add more? (y/n): ').lower()
            if add not in ('y', 'n'):
                print("Invalid entry. Please try again.")
                add = input('Add more? (y/n): ').lower()

            if add == 'n':
                cart_val = cart.items()
                print('Your cart:')
                print(tabulate(cart_val, headers = ['Item', 'Price (AED)'], tablefmt = 'heavy_outline'))
                total = 0

                for price in cart_val:
                    total += price[1]

                print(f'YOUR TOTAL = {total}')
                print('---------------------------------------- THANK YOU FOR SHOPPING WITH US! ----------------------------------------')
                break

def main():
    while True:
        print('\nWelcome to the Grocery Database Management System!')
        print('Choose an option to perform the corresponding function:')
        print('1. Search record')
        print('2. Delete record')
        print('3. Check stock')
        print('4. Purchase items')
        print('5. Exit')

        try:
            choice = int(input('Enter your choice (1-5): '))

            if choice == 1:
                search_record()
            elif choice == 2:
                delete_record()
            elif choice == 3:
                check_stock()
            elif choice == 4:
                purchase()
            elif choice == 5:
                print('Exiting the system...')
                break
            else:
                print('Invalid input. Please select a number between 1 and 5.')
        except ValueError:
            print('Invalid input. Please enter a numeric value.')

main()

