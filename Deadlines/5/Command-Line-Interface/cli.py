import mysql.connector
from decimal import Decimal

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ", # not adding here for privacy purposes
    database="Qalakriti"
)
cursor = mydb.cursor()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def startpage_user():

    print("\n\033[1m\033[32mWelcome to Qalakriti\033[0m")
    # print("\n\033[1m\033[34mWelcome to Qalakriti\033[0m")
    # print("\n\033[1m\033[35mWelcome to Qalakriti\033[0m")
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
        exit()

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
        

    # Insert the order item into the OrderItem table
    quantity = int(input("Enter the quantity to buy (if none enter -1) : "))
    if quantity != -1:
        # cursor.execute("INSERT INTO OrderItem (ordID, prodID, itemQty) VALUES (%s, %s, %s)", (user_id, product_id, quantity))
        # mydb.commit()
        # print("Product added to order successfully!")
        order_cart(user_id,product_id,quantity)

    homepage(user_id)

def order_cart(user_id,prod_id,quantity):

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

def profile_page(user_id):
    # Fetch user details
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
    print()

    while True:
        print("\n\033[1m\033[34mUser Menu\033[0m\n")
        print("1. View Current Order Cart")
        print("2. See Previous Orders")
        print("3. See All Your Reviews")
        print("4. Balance Deatils")
        print("5. Go Back to Homepage")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
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

            elif choice == 2: # PLACING AND PAYMENT FOR ORDER
                cursor.execute("SELECT * FROM `Order` WHERE usrID = %s AND ordPlaced = 'no'", (user_id,))
                order = cursor.fetchone()
                if order:
                    cursor.execute("SELECT SUM(itemSubtotal) FROM OrderItem WHERE ordID = %s", (order[0],))
                    total_amt = cursor.fetchone()[0]
                    cursor.execute("UPDATE `Order` SET ordTotalAmt = %s, ordPlaced = 'yes' WHERE ordID = %s", (total_amt, order[0]))
                    mydb.commit()
                    print("Order placed successfully!")
                    
                    # Deduct total amount from user's balance
                    cursor.execute("SELECT usrBalance FROM User WHERE usrID = %s", (user_id,))
                    usr_balance = cursor.fetchone()[0]
                    new_balance = usr_balance - total_amt
                    cursor.execute("UPDATE User SET usrBalance = %s WHERE usrID = %s", (new_balance, user_id))
                    mydb.commit()
                    print("Total amount deducted from your balance.")
                else:
                    print("No items in the order cart.")

            elif choice == 3:
                profile_page(user_id)
            else:
                print("Invalid choice. Please try again.")

        elif choice == 2:
            # Fetch orders for the user
            cursor.execute("SELECT * FROM `Order` WHERE usrID = %s", (user_id,))
            orders = cursor.fetchall()
            print("Orders:")
            for order in orders:
                print("Order ID:", order[0])
                print("Order Date:", order[1])
                print("Total Amount:", order[2])
                print("Order Status:", order[3])
                print()
        elif choice == 3:
            # Fetch reviews given by the user
            cursor.execute("SELECT Review.prodID, prodName, revRating, revComment, revDate FROM Review NATURAL JOIN Product WHERE usrID = %s", (user_id,))
            reviews = cursor.fetchall()
            print("Reviews:")
            for review in reviews:
                print("Review Date:", review[4])
                print("Product ID:", review[0])
                print("Product Name:", review[1])
                print("Rating:", review[2])
                print("Comment:", review[3])
                print()
        
        elif choice == 4: # balance details
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


        elif choice == 5:
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
        exit()


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
