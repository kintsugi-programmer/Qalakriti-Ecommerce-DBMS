import mysql.connector
from mysql.connector import Error  
from decimal import Decimal

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Db_Password",
    database="Qalakriti"
)
cursor = mydb.cursor()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def startpage_user():

    print("\n\033[1m\033[32mWelcome to Qalakriti\033[0m")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter : "))

    if(choice==1):
        login()
    elif(choice==2):
        register()
    else:
        print("Exiting")
        begin()

def register():
    print("\n\033[1m\033[32mRegister Page\033[0m")
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user_type = "customer"
    mobile = int(input("Enter your mobile number: "))
    cursor.execute("INSERT INTO User (usrName, usrEmail, usrPassword, usrType, usrRegDate, usrMobNumber) VALUES (%s, %s, %s, %s, CURDATE(), %s)", (username, email, password, user_type, mobile))
    mydb.commit()

    street = input("Enter your street: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zipcode = input("Enter your zipcode: ")

    cursor.execute("SELECT usrID FROM User WHERE usrEmail = %s", (email,))
    user_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO Address (usrID, addrStreet, addrCity, addrState, addrZipCode) VALUES (%s, %s, %s, %s, %s)", (user_id, street, city, state, zipcode))
    mydb.commit()

    print("User registered successfully!")
    startpage_user()

def login():
    print("\n\033[1m\033[32mLogin Page\033[0m")
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT * FROM User WHERE usrName = %s AND usrEmail = %s AND usrPassword = %s", (username, email, password))
    row = cursor.fetchone()
    if row:
        print("Login successful for",row[1])
        user_id = row[0]
        homepage(user_id)
    else:
        print("Login failed. User doesn't exist or email/password is incorrect. Please try again.")
        startpage_user()

def homepage(user_id):
    print("\n\033[1m\033[32mHome Page\033[0m")
    print("Welcome to Qalakriti")
    print("1. View Categories")
    print("2. View Craftsmen")
    print("3. View Profile")
    print("4. Logout")
    choice = int(input("Enter: "))

    if choice == 1:
        categories_page(user_id)
    elif choice == 2:
        craftsmen_page(user_id)
    elif choice == 3:
        profile_page(user_id)
    else:
        startpage_user()

# a fucntion that will only show the product selected and will allow you to manipulate it like addd to orders , add review see stock or not etf 
def deepview(user_id, product_id):
    cursor.execute("SELECT * FROM Product WHERE prodID = %s", (product_id,))
    product = cursor.fetchone()
    print("\n\033[1m\033[32mProduct Details\033[0m\n")
    print("Product ID:", product[0])
    print("Product Name:", product[1])
    print("Description:", product[2])
    print("Price: Rs.", product[3])
    if(product[4]>0):
        print("In Stock: Yes")
    else:
        print("In Stock: No")
    cursor.execute("SELECT AVG(revRating) FROM Review WHERE prodID = %s", (product_id,))
    avg_rating = cursor.fetchone()[0]
    print("Average Rating:", avg_rating)
    
    cursor.execute("SELECT Review.revRating, Review.revComment, User.usrName FROM Review NATURAL JOIN User WHERE Review.prodID = %s", (product_id,))
    reviews = cursor.fetchall()
    print("Reviews:")
    for review in reviews:
        print()
        print("Rating:",  review[0])
        print("User:", review[2])
        print("Comment:", review[1])

    review = input("Do you want to add a review? (y/n): ")
    if review == 'y':
        rating = int(input("Enter the rating (1-5): "))
        comment = input("Enter the comment: ")
        cursor.execute("INSERT INTO Review (usrID, prodID, revRating, revComment, revDate) VALUES (%s, %s, %s, %s, CURDATE())", (user_id, product_id, rating, comment))
        mydb.commit()
        print("Review added successfully!")
    
    # functionality to remove a review 
    remove_review = input("Do you want to remove a review? (y/n): ")
    if remove_review == 'y':
        cursor.execute("SELECT * FROM Review WHERE usrID = %s AND prodID = %s", (user_id, product_id))
        reviews = cursor.fetchall()
        print("Reviews:")
        for review in reviews:
            print("Review ID:", review[0])
            print("Rating:", review[2])
            print("Comment:", review[3])
            print("Review Date:", review[4])
            print()
        review_id = int(input("Enter the review ID to remove: "))
        cursor.execute("DELETE FROM Review WHERE revID = %s", (review_id,))
        mydb.commit()
        print("Review removed successfully!")
        
    quantity = int(input("Enter the quantity to buy (if none enter -1) : "))
    if quantity != -1:
        order_cart(user_id,product_id,quantity)

    homepage(user_id)

def order_cart(user_id,prod_id,quantity):
    # what this fucntion does is , that it checks if a current order is processing and not confirmed and paid for yet, if it exists the order item gets ordered in that order else a new order is created and then the order item is added to that order
    try :
        cursor.execute("SELECT * FROM `Order` WHERE usrID = %s AND ordPlaced = 'no'", (user_id,))
        order = cursor.fetchone()
        if order:
            order_id = order[0]
            cursor.execute("SELECT prodPrice FROM Product WHERE prodID = %s", (prod_id,))
            price = cursor.fetchone()[0]
            subtotal = price * quantity
            cursor.execute("INSERT INTO OrderItem (ordID, prodID, itemQty, itemSubtotal) VALUES (%s, %s, %s, %s)", (order_id, prod_id, quantity, subtotal))
            mydb.commit()
            print("Product added to order successfully!")

        else:
            cursor.execute("INSERT INTO `Order` (usrID, ordDate, ordTotalAmt, ordStatus, ordPlaced) VALUES (%s, CURDATE(), 0, 'pending', 'no')", (user_id,))
            mydb.commit()
            cursor.execute("SELECT LAST_INSERT_ID()")
            order_id = cursor.fetchone()[0]
            cursor.execute("SELECT prodPrice FROM Product WHERE prodID = %s", (prod_id,))
            price = cursor.fetchone()[0]
            subtotal = price * quantity
            cursor.execute("INSERT INTO OrderItem (ordID, prodID, itemQty, itemSubtotal) VALUES (%s, %s, %s, %s)", (order_id, prod_id, quantity, subtotal))
            mydb.commit()
            print("Product added to order successfully!")

    except Error as e:
        print("Error while adding product to order:", e)
    

# a function for displaying the products that will take the craftsmen id and category id as parameters . one of them will be zero to showcase that i do not need to give products under that. then display all products and give an option to add them to an order
def display_products(craft_id, cat_id, user_id):
    print("\n\033[1m\033[32mProducts\033[0m\n")
    if craft_id == 0  :
        cursor.execute("SELECT * FROM Product WHERE catID = %s", (cat_id,))
        products = cursor.fetchall()
        for product in products:
            print("\n\033[1m\033[35m%s\033[0m" % product[1])
            print("Product ID:", product[0])
            print("Description:", product[2])
            print("Price: Rs.", product[3])

        product_id = int(input("Select product (if none enter -1): "))
        if(product_id != -1):
            deepview(user_id, product_id)


    elif cat_id == 0 :
        cursor.execute("SELECT * FROM Product WHERE craftID = %s", (craft_id,))
        products = cursor.fetchall()
        print("Products:")
        for product in products:
            print("Product ID:", product[0])
            print("Product Name:", product[1])
            print("Description:", product[2])
            print("Price: Rs.", product[3])
            print()

        product_id = int(input("Select product (if none enter -1): "))
        if(product_id != -1):
            deepview(user_id, product_id)

        
def categories_page(user_id):
    print("\n\033[1m\033[32mCategories\033[0m\n")
    choice = 1
    while True:
        if choice == 1:
            cursor.execute("SELECT * FROM Category")
            categories = cursor.fetchall()
            print("Categories:")
            for category in categories:
                print(category[0], category[1])

            cat_id = int(input("Enter the category ID to view products: "))
            display_products(0, cat_id, user_id)
            
        elif choice == 2:
            break

        print("1. View Categories")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

    homepage(user_id)

def craftsmen_page(user_id):
    print("\n\033[1m\033[32mCraftsmen\033[0m\n")
    choice = 1
    while True:
        if choice == 1:
            cursor.execute("SELECT * FROM Craftsman")
            craftsmen = cursor.fetchall()
            print("Craftsmen:")
            for craftsman in craftsmen:
                print(craftsman[0], craftsman[1])

            craft_id = int(input("Enter the craftsman ID to view products: "))
            display_products(craft_id, 0, user_id)
            
        elif choice == 2:
            break

        print("1. View Craftsmen")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

    homepage(user_id)

def view_cart(user_id):
    print("1.View Current Order Cart")
    print("2. Place Order")
    print("3. Go Back")
    choice = int(input("Enter: "))
    if choice == 1: #VIEWING ORDER
        cursor.execute("SELECT * FROM `Order` WHERE usrID = %s AND ordPlaced = 'no'", (user_id,))
        order = cursor.fetchone()
        if order:
            cursor.execute("SELECT OrderItem.prodID, prodName, itemQty, itemSubtotal FROM OrderItem NATURAL JOIN Product WHERE ordID = %s", (order[0],))
            order_items = cursor.fetchall()
            print("Order Cart:")
            total=0
            for order_item in order_items:
                total+=order_item[3]
                print("Product ID:", order_item[0])
                print("Product Name:", order_item[1])
                print("Quantity:", order_item[2])
                print("Price:", order_item[3])
                print()

            print("Total Amount:",total)
        else:
            print("No items in the order cart.")

    elif choice == 2: # PLACING AND PAYMENT FOR ORDER THIS IS HERE BALANCE TRIGGER WILL WORK
        cursor.execute("SELECT * FROM `Order` WHERE usrID = %s AND ordPlaced = 'no'", (user_id,))
        order = cursor.fetchone()
        if order:
                try: # trigger 1 working
                    # Deduct total amount from user's balance
                    cursor.execute("SELECT usrBalance FROM User WHERE usrID = %s", (user_id,))
                    usr_balance = cursor.fetchone()[0]

                    cursor.execute("SELECT SUM(itemSubtotal) FROM OrderItem WHERE ordID = %s", (order[0],))
                    total_amt = cursor.fetchone()[0]
                    new_balance = usr_balance - total_amt

                    cursor.execute("UPDATE User SET usrBalance = %s WHERE usrID = %s", (new_balance, user_id))
                    mydb.commit()
                    print("Total amount deducted from your balance.")
                
                    # Update the stock for each item in the order
                    cursor.execute("SELECT prodID, itemQty FROM OrderItem WHERE ordID = %s", (order[0],))
                    order_items = cursor.fetchall()

                    for item in order_items:
                        prod_id = item[0]
                        item_qty = item[1]
                        cursor.execute("UPDATE Product SET prodStock = (prodStock - %s) WHERE prodID = %s", (item_qty, prod_id))
                    mydb.commit()

                    #place order
                    cursor.execute("UPDATE `Order` SET ordTotalAmt = %s, ordPlaced = 'yes' WHERE ordID = %s", (total_amt, order[0]))
                    mydb.commit()
                    print("Order placed successfully!")

                except Error as e:
                    print("An error occurred:", e)


        else:
            print("No items in the order cart.")

    elif choice == 3:
        profile_page(user_id)
    else:
        print("Invalid choice. Please try again.")
    
    profile_page(user_id)


def mod_profile(user_id):
    print("1. Change Username")
    print("2. Change Email")
    print("3. Change Password")
    print("4. Change Mobile Number")
    print("5. Change Address")
    print("6. Go Back")
    c3 = int(input("Enter your choice: "))
    if c3 == 1:
        new_username = input("Enter new username: ")
        cursor.execute("UPDATE User SET usrName = %s WHERE usrID = %s", (new_username, user_id))
        mydb.commit()
        print("Username changed successfully!")
    elif c3 == 2:
        new_email = input("Enter new email: ")
        cursor.execute("UPDATE User SET usrEmail = %s WHERE usrID = %s", (new_email, user_id))
        mydb.commit()
        print("Email changed successfully!")
    elif c3 == 3:
        new_password = input("Enter new password: ")
        cursor.execute("UPDATE User SET usrPassword = %s WHERE usrID = %s", (new_password, user_id))
        mydb.commit()
        print("Password changed successfully!")
    elif c3 == 4:
        new_mobile = int(input("Enter new mobile number: "))
        cursor.execute("UPDATE User SET usrMobNumber = %s WHERE usrID = %s", (new_mobile, user_id))
        mydb.commit()
        print("Mobile number changed successfully!")
    elif c3 == 5:
        new_street = input("Enter new street: ")
        new_city = input("Enter new city: ")
        new_state = input("Enter new state: ")
        new_zipcode = input("Enter new zipcode: ")
        cursor.execute("UPDATE Address SET addrStreet = %s, addrCity = %s, addrState = %s, addrZipCode = %s WHERE usrID = %s", (new_street, new_city, new_state, new_zipcode, user_id))
        mydb.commit()
        print("Address changed successfully!")
    elif c3 == 6:
        profile_page(user_id)


def profile_page(user_id):
    while True:
        print("\n\033[1m\033[34mUser Menu\033[0m\n")
        print("1. View and Modify Profile")
        print("2. View Current Order Cart")
        print("3. See Previous Orders")
        print("4. See All Your Reviews")
        print("5. Balance Details")
        print("6. Go Back to Homepage")
        choice = int(input("Enter your choice: "))

        if choice==1:
            # Fetch user details
            # features to modify this data
            cursor.execute("SELECT * FROM User WHERE usrID = %s", (user_id,))
            user = cursor.fetchone()
            print("\n\033[1m\033[32mProfile Page\033[0m\n")
            print("User ID:", user[0])
            print("Username:", user[1])
            print("Email:", user[2])
            print("Password:", user[3])
            print("User Type:", user[4])
            print("Registration Date:", user[5])
            print("Mobile Number:", user[6])
            # add adress associated with the user also
            cursor.execute("SELECT * FROM Address WHERE usrID = %s", (user_id,))
            address = cursor.fetchone()
            print("Address:")
            print("Street:", address[1])
            print("City:", address[2])
            print("State:", address[3])
            print("Zipcode:", address[4])
            print()

            c2=input("Do you want to modify your profile? (y/n)")
            if c2=='y':
                mod_profile(user_id)
                
        elif choice == 2:
            view_cart(user_id)

        elif choice == 3:
            # Fetch orders for the user
            cursor.execute("SELECT * FROM `Order` WHERE usrID = %s", (user_id,))
            orders = cursor.fetchall()
            print("\n\033[1m\033[32mOrders\033[0m")
            for order in orders:
                print("Order ID:", order[0])
                print("Order Date:", order[2])
                print("Total Amount:", order[3])
                print("Order Status:", order[5])
                print("Order Placed:", order[4])
                print()
          
        elif choice == 4:
            # Fetch reviews given by the user
            cursor.execute("SELECT Review.prodID, prodName, revRating, revComment, revDate FROM Review NATURAL JOIN Product WHERE usrID = %s", (user_id,))
            reviews = cursor.fetchall()
            print("\n\033[1m\033[32mReviews\033[0m")
            for review in reviews:
                print("Review Date:", review[4])
                print("Product ID:", review[0])
                print("Product Name:", review[1])
                print("Rating:", review[2])
                print("Comment:", review[3])
                print()
        
        elif choice == 5: # balance details
            print("\n\033[1m\033[32mBalance\033[0m")
            print("1. View Balance")
            print("2. Add Balance")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                cursor.execute("SELECT usrBalance FROM User WHERE usrID = %s", (user_id,))
                balance = cursor.fetchone()[0]
                print("Balance:", balance)
            elif choice == 2:
                cursor.execute("SELECT usrBalance FROM User WHERE usrID = %s", (user_id,))
                balance = cursor.fetchone()[0]
                print("Current Balance:", balance)

                amount = Decimal(input("Enter the amount to add: "))
                new_balance = balance + amount
                cursor.execute("UPDATE User SET usrBalance = %s WHERE usrID = %s", (new_balance, user_id))
                mydb.commit()
                print("Balance added successfully!")
                print("New Balance:", new_balance)


        elif choice == 6:
            homepage(user_id)
        else:
            print("Invalid choice. Please try again.")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def startpage_seller():
    print("\n\033[1m\033[32mWelcome to Qalakriti\033[0m")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter : "))

    if(choice==1):
        login_seller()
    elif(choice==2):
        register_seller()
    else:
        print("Exiting")
        begin()

def register_seller(): 
    # register seller by inserting inro the craftsman table
    print("\n\033[1m\033[32mRegister Page\033[0m")
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    business_type = input("Enter your business type/cateogy: ")
    cursor.execute("INSERT INTO Craftsman (craftName, craftMobNumber, craftEmail, craftPass, craftBusType) VALUES (%s, %s, %s, %s, %s)", (username, 0, email, password, business_type))
    mydb.commit()

    print("Craftsman registered successfully!")
        
def login_seller(): 
    print("\n\033[1m\033[32mLogin Page\033[0m")
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
     
    cursor.execute("SELECT * FROM Craftsman WHERE craftName = %s AND craftEmail = %s AND craftPass = %s", (username, email, password))
    row = cursor.fetchone()
    if row:
        print("Login successful for",row[1])
        seller_id = row[0]
        homepage_seller(seller_id)
    else:
        print("Login failed. Craftsman doesn't exist or email/password is incorrect. Please try again.")
        startpage_seller()

def homepage_seller(craft_id):
    # craftsmen should have the ability to add products , see their listed products , the details of the product orders they received and the reviews for their [rodcts]. they should also be able to see the earnings they have made
    cursor.execute("SELECT craftName FROM Craftsman WHERE craftID = %s", (craft_id,))
    craftsman_name = cursor.fetchone()[0]
    print("\n\033[1m\033[32mHome Page\033[0m")
    print("Welcome to Qalakriti, " + craftsman_name)
    print("1. Add or Remove Product")
    print("2. View Products")
    print("3. View Orders")
    print("4. View Reviews")
    print("5. View Earnings")
    print("6. Logout")
    choice = int(input("Enter: "))
    if choice == 1:
        mod_product(craft_id)
    elif choice == 2:
        view_products(craft_id)
    elif choice == 3:
        view_orders(craft_id)
    elif choice == 4:
        view_reviews(craft_id)
    elif choice == 5:
        view_earnings(craft_id)
    else:
        startpage_seller()

def mod_product(craft_id):
    print("\n\033[1m\033[32mAdd or Remove Product\033[0m")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Go Back")
    choice = int(input("Enter: "))

    if choice == 1:
        product_name = input("Enter product name: ")
        product_desc = input("Enter product description: ")
        product_price = Decimal(input("Enter product price: "))
        product_stock = int(input("Enter product stock: "))

        # showcase all categories before asking for the id for UI reasons. think of a dropdown
        cursor.execute("SELECT * FROM Category")
        categories = cursor.fetchall()
        print("Categories:")
        for category in categories:
            print(category[0], category[1])
        cat_id = int(input("Enter category ID: "))
        cursor.execute("INSERT INTO Product (prodName, prodDesc, prodPrice, prodStock, catID, craftID, prodCreateDate) VALUES (%s, %s, %s, %s, %s, %s, CURDATE())", (product_name, product_desc, product_price, product_stock, cat_id, craft_id))
        mydb.commit()
        print("Product added successfully!")

    elif choice == 2:
        product_id = int(input("Enter the product ID to remove: "))
        cursor.execute("DELETE FROM Product WHERE prodID = %s", (product_id,))
        mydb.commit()
        print("Product removed successfully!")

    homepage_seller(craft_id)

def view_products(craft_id):
    cursor.execute("SELECT * FROM Product WHERE craftID = %s", (craft_id,))
    products = cursor.fetchall()
    print("\n\033[1m\033[32mProducts\033[0m\n")
    for product in products:
        print("Product ID:", product[0])
        print("Product Name:", product[1])
        print("Description:", product[2])
        print("Price: Rs.", product[3])
        print("Stock:", product[4])
        print()

    product_id = int(input("Enter the product ID to view details ( enter -1 if none ): "))
    if(product_id!= -1):
        deepview_seller(craft_id, product_id)
    homepage_seller(craft_id)

def deepview_seller(craft_id,prod_id):
    cursor.execute("SELECT * FROM Product WHERE prodID = %s", (prod_id,))
    product = cursor.fetchone()
    print("\n\033[1m\033[32mProduct Details\033[0m\n")
    print("Product ID:", product[0])
    print("Product Name:", product[1])
    print("Description:", product[2])
    print("Price: Rs.", product[3])
    print("Stock:", product[4])

    cursor.execute("SELECT AVG(revRating) FROM Review WHERE prodID = %s", (prod_id,))
    avg_rating = cursor.fetchone()[0]
    print("Average Rating:", avg_rating)
    
    cursor.execute("SELECT Review.revRating, Review.revComment, User.usrName FROM Review NATURAL JOIN User WHERE Review.prodID = %s", (prod_id,))
    reviews = cursor.fetchall()
    print("Reviews:")
    for review in reviews:
        print()
        print("Rating:",  review[0])
        print("User:", review[2])
        print("Comment:", review[1])

    homepage_seller(craft_id)

def view_orders(craft_id):
    #This functions gives all the orderitems that are from the craftsmen only for the orders that have been succesfully placed , i.e where ordPlaced is yes
    cursor.execute("SELECT OrderItem.prodID, prodName, itemQty, itemSubtotal, ordID, usrID FROM OrderItem NATURAL JOIN Product NATURAL JOIN `Order` WHERE craftID = %s AND ordPlaced = 'yes'", (craft_id,))
    order_items = cursor.fetchall()
    print("\n\033[1m\033[32mOrders\033[0m\n")
    for order_item in order_items:
        print("Product ID:", order_item[0])
        print("Product Name:", order_item[1])
        print("Quantity:", order_item[2])
        print("Subtotal:", order_item[3])
        print("Order ID:", order_item[4])
        print("User ID:", order_item[5])
        print()
    
    print("1. Update Order Status (y/n) : ")
    choice = input("Enter: ")
    if choice == 'y':
        order_id = int(input("Enter the order ID to update status: "))
        status = input("Enter the new status ( pending / shipped ): ")
        cursor.execute("UPDATE `Order` SET ordStatus = %s WHERE ordID = %s", (status, order_id))
        mydb.commit()
        print("Order status updated successfully!")
    
def view_reviews(craft_id):
    cursor.execute("SELECT Product.prodID, prodName, revRating, revComment, revDate FROM Review NATURAL JOIN Product WHERE craftID = %s", (craft_id,))
    reviews = cursor.fetchall()
    print("\n\033[1m\033[32mReviews\033[0m\n")
    for review in reviews:
        print("Product ID:", review[0])
        print("Product Name:", review[1])
        print("Rating:", review[2])
        print("Comment:", review[3])
        print("Review Date:", review[4])
        print()

    homepage_seller(craft_id)

def view_earnings(craft_id):
    cursor.execute("SELECT SUM(itemSubtotal) FROM OrderItem NATURAL JOIN Product NATURAL JOIN `Order` WHERE craftID = %s AND ordPlaced = 'yes'", (craft_id,))
    earnings = cursor.fetchone()[0]
    print("\n\033[1m\033[32mEarnings\033[0m\n")
    print("Total Earnings:", earnings)
    homepage_seller(craft_id)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def startpage_admin():
    print("\n\033[1m\033[32mWelcome to Qalakriti\033[0m")
    print("1. Login")
    print("2. Exit")
    choice = int(input("Enter : "))

    if(choice==1):
        login_admin()
    else:
        print("Exiting")
        begin()
        
def login_admin():
    # there is only one system admin. they have a fixed password
    print("\n\033[1m\033[32mLogin Page\033[0m")
    password = input("Enter the password: ")
    if password == "admin123":
        print("Login successful")
        homepage_admin()
    else:
        print("Login failed. Incorrect password. Please try again.")
        startpage_admin()

def homepage_admin():
    print("\n\033[1m\033[32mHome Page\033[0m")
    print("Welcome to Qalakriti Admin")
    print("1. View Orders")
    print("2. View Users")
    print("3. View Craftsman")
    print("4. View Categories")
    print("5. View Products")
    print("6. Logout")

    choice = int(input("Enter: "))
    if choice == 1:
        view_orders_admin()
    elif choice == 2:
        view_users_admin()
    elif choice == 3:
        view_craftsmen_admin()
    elif choice == 4:
        view_categories_admin()
    elif choice == 5:
        view_products_admin()
    else:
        startpage_admin()
    
def view_orders_admin():
    cursor.execute("SELECT * FROM `Order` WHERE ordPlaced = 'yes'")
    orders = cursor.fetchall()
    print("\n\033[1m\033[32mOrders\033[0m\n")
    
    for order in orders:
        print("Order ID:", order[0])
        print("User ID:", order[1])
        print("Order Date:", order[2])
        print("Total Amount:", order[3])
        print("Order Status:", order[4])
        print()
    homepage_admin()

def view_users_admin():
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    print("\n\033[1m\033[32mUsers\033[0m\n")
    for user in users:
        print("User ID:", user[0])
        print("Username:", user[1])
        print("Email:", user[2])
        print("User Type:", user[4])
        print("Registration Date:", user[5])
        print("Mobile Number:", user[6])
        print()
    homepage_admin()

def view_craftsmen_admin():
    cursor.execute("SELECT Craftsman.craftID, craftName, AVG(result.avgRating) AS avgRating FROM Craftsman JOIN Product ON Craftsman.craftID = Product.craftID LEFT JOIN (SELECT Product.craftID, AVG(revRating) AS avgRating FROM Product LEFT JOIN Review ON Product.prodID = Review.prodID GROUP BY Product.craftID) AS result ON Craftsman.craftID = result.craftID GROUP BY Craftsman.craftID, craftName")
    craftsmen = cursor.fetchall()
    print("\n\033[1m\033[32mCraftsmen\033[0m\n")


    for craftsman in craftsmen:
        print("Craftsman ID:", craftsman[0])
        print("Craftsman Name:", craftsman[1])
        print("Average Rating:", craftsman[2])

        cursor.execute("SELECT SUM(itemSubtotal) FROM OrderItem NATURAL JOIN Product NATURAL JOIN `Order` WHERE craftID = %s AND ordPlaced = 'yes'", (craftsman[0],))
        earnings = cursor.fetchone()[0]
        print("Total Earnings:", earnings)

        print()
    homepage_admin()
        

def view_categories_admin():
    cursor.execute("SELECT Category.catName, COUNT(Product.prodID) AS NumProducts FROM Category LEFT JOIN Product ON Category.catID = Product.catID GROUP BY Category.catID")
    categories = cursor.fetchall()
    print("\n\033[1m\033[32mCategories\033[0m\n")
    for category in categories:
        print("Category Name:", category[0])
        print("Number of Products:", category[1])
        print()
    homepage_admin()

def view_products_admin():
    cursor.execute("SELECT Product.prodID, Product.prodName, Product.prodDesc, Product.prodPrice, Product.prodStock, Category.catID, Category.catName, Craftsman.craftID, Craftsman.craftName, Product.prodCreateDate FROM Product JOIN Category ON Product.catID = Category.catID JOIN Craftsman ON Product.craftID = Craftsman.craftID")
    products = cursor.fetchall()
    print("\n\033[1m\033[32mProducts\033[0m\n")
    for product in products:
        print("Product ID:", product[0])
        print("Product Name:", product[1])
        print("Description:", product[2])
        print("Price: Rs.", product[3])
        print("Stock:", product[4])
        print("Category ID:", product[5])
        print("Category Name:", product[6])
        print("Craftsman ID:", product[7])
        print("Craftsman Name:", product[8])
        print("Creation Date:", product[9])
        print()
    homepage_admin()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def begin():
    while(True):
        print("1.Enter as User"+"\n2.Enter as Seller"+"\n3.Enter as Admin"+"\n4.Exit")
        c1=int(input("Enter: "))  # starting the cli app
        if c1==1:
            startpage_user()
        elif c1==2:
            startpage_seller()
        elif c1==3:
            startpage_admin()
        else:
            print("Exiting")
            exit()

begin() # absolute start
