import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="Qalakriti"
)

cursor = mydb.cursor()

def startpage():

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
        startpage()

# def register():

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
        startpage()
      
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
        
    quantity = int(input("Enter the quantity to buy (if none enter -1) : "))
    if quantity != -1:
        cursor.execute("INSERT INTO OrderItem (ordID, prodID, itemQty) VALUES (%s, %s, %s)", (user_id, product_id, quantity))
        mydb.commit()
        print("Product added to order successfully!")

    review = input("Do you want to add a review? (y/n): ")
    if review == 'y':
        rating = int(input("Enter the rating (1-5): "))
        comment = input("Enter the comment: ")
        cursor.execute("INSERT INTO Review (usrID, prodID, revRating, revComment, revDate) VALUES (%s, %s, %s, %s, CURDATE())", (user_id, product_id, rating, comment))
        mydb.commit()
        print("Review added successfully!")

    homepage(user_id)

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

def profile_page(usr_id):
    # Fetch user details
    cursor.execute("SELECT * FROM User WHERE usrID = %s", (usr_id,))
    user = cursor.fetchone()
    print("\n\033[1m\033[34mProfile Page\033[0m\n")
    print("User ID:", user[0])
    print("Username:", user[1])
    print("Email:", user[2])
    print("Password:", user[3])
    print("User Type:", user[4])
    print("Registration Date:", user[5])
    print("Mobile Number:", user[6])
    print()
  
    cursor.execute("SELECT * FROM `Order` WHERE usrID = %s", (usr_id,))
    orders = cursor.fetchall()
    print("Orders:")
    for order in orders:
        print("Order ID:", order[0])
        print("Order Date:", order[1])
        print("Total Amount:", order[2])
        print("Order Status:", order[3])
        print()
      
    cursor.execute("SELECT * FROM Review WHERE usrID = %s", (usr_id,))
    reviews = cursor.fetchall()
    print("Reviews:")
    for review in reviews:
        print("Product ID:", review[1])
        print("Rating:", review[2])
        print("Comment:", review[3])
        print("Review Date:", review[4])
        print()
    homepage(usr_id)


startpage() # starting the cli app
