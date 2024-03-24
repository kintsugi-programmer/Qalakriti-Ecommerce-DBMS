import pymysql

# Function to establish connection to MySQL database
def connect_to_database():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='username',
            password='password',
            database='Qalakriti'
        )
        print("Connected to database successfully!")
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")
        return None


# Customer Menu Functions
def browse_products():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM Product"
        cursor.execute(query)
        products = cursor.fetchall()
        print("Available Products:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[3]}")
        conn.close()

def view_product_details():
    product_id = input("Enter the product ID: ")
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM Product WHERE prodID = %s"
        cursor.execute(query, (product_id,))
        product = cursor.fetchone()
        if product:
            print(f"Product ID: {product[0]}")
            print(f"Name: {product[1]}")
            print(f"Description: {product[2]}")
            print(f"Price: {product[3]}")
            print(f"Stock: {product[4]}")
        else:
            print(f"Product with ID {product_id} not found.")
        conn.close()

def search_products():
    search_term = input("Enter a search term: ")
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM Product WHERE prodName LIKE %s"
        cursor.execute(query, ('%' + search_term + '%',))
        products = cursor.fetchall()
        print("Search Results:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[3]}")
        conn.close()
def view_cart():
    user_id = input("Enter your user ID: ")
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = """
            SELECT p.prodName, oi.itemQty, oi.itemSubtotal
            FROM OrderItem oi
            JOIN `Order` o ON oi.ordID = o.ordID
            JOIN Product p ON oi.prodID = p.prodID
            WHERE o.usrID = %s AND o.ordStatus = 'pending'
        """
        cursor.execute(query, (user_id,))
        cart_items = cursor.fetchall()
        print("Cart Items:")
        total_amount = 0
        for item in cart_items:
            product_name, quantity, subtotal = item
            print(f"Product: {product_name}, Quantity: {quantity}, Subtotal: {subtotal}")
            total_amount += subtotal
        print(f"Total Amount: {total_amount}")
        conn.close()

def checkout():
    user_id = input("Enter your user ID: ")
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = """
            SELECT SUM(oi.itemSubtotal) AS total_amount
            FROM OrderItem oi
            JOIN `Order` o ON oi.ordID = o.ordID
            WHERE o.usrID = %s AND o.ordStatus = 'pending'
        """
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        total_amount = result[0] if result[0] else 0

        if total_amount > 0:
            print(f"Total Amount: {total_amount}")
            confirm = input("Confirm checkout (y/n): ")
            if confirm.lower() == 'y':
                update_query = """
                    UPDATE `Order`
                    SET ordStatus = 'completed'
                    WHERE usrID = %s AND ordStatus = 'pending'
                """
                cursor.execute(update_query, (user_id,))
                conn.commit()
                print("Checkout successful!")
            else:
                print("Checkout canceled.")
        else:
            print("Your cart is empty.")

        conn.close()

def view_order_history():
    user_id = input("Enter your user ID: ")
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = """
            SELECT o.ordID, o.ordDate, o.ordTotalAmt, o.ordStatus
            FROM `Order` o
            WHERE o.usrID = %s
            ORDER BY o.ordDate DESC
        """
        cursor.execute(query, (user_id,))
        orders = cursor.fetchall()
        print("Order History:")
        for order in orders:
            order_id, order_date, total_amount, status = order
            print(f"Order ID: {order_id}, Date: {order_date}, Total Amount: {total_amount}, Status: {status}")
        conn.close()

def update_account_information():
    user_id = input("Enter your user ID: ")
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT usrName, usrEmail, usrMobNumber FROM `User` WHERE usrID = %s"
        cursor.execute(query, (user_id,))
        user_info = cursor.fetchone()
        if user_info:
            name, email, mobile_number = user_info
            print(f"Current Name: {name}")
            new_name = input("Enter new name (or leave blank to keep the same): ")
            print(f"Current Email: {email}")
            new_email = input("Enter new email (or leave blank to keep the same): ")
            print(f"Current Mobile Number: {mobile_number}")
            new_mobile_number = input("Enter new mobile number (or leave blank to keep the same): ")

            update_query = "UPDATE `User` SET "
            update_values = []
            if new_name:
                update_query += "usrName = %s, "
                update_values.append(new_name)
            if new_email:
                update_query += "usrEmail = %s, "
                update_values.append(new_email)
            if new_mobile_number:
                update_query += "usrMobNumber = %s, "
                update_values.append(new_mobile_number)
            update_query = update_query.rstrip(", ") + " WHERE usrID = %s"
            update_values.append(user_id)

            if update_values:
                cursor.execute(update_query, update_values)
                conn.commit()
                print("Account information updated successfully!")
            else:
                print("No changes were made.")
        else:
            print(f"User with ID {user_id} not found.")
        conn.close()

def logout():
    print("Logged out successfully.")

# Admin Menu Functions
def manage_products():
    pass

def manage_orders():
    pass

def manage_customers():
    pass

def manage_categories():
    pass

def view_sales_analytics():
    pass

def manage_discounts_promotions():
    pass

def manage_inventory():
    pass

# Businessman Menu Functions
def businessman_manage_products():
    pass

def view_orders():
    pass

def businessman_manage_inventory():
    pass

def sales_analytics():
    pass

def customer_management():
    pass

def marketing_campaigns():
    pass

def financial_management():
    pass

def businessman_logout():
    pass

# Main function to display menu and handle user choices
def main():
    print("Welcome to the menu!")
    print("1. Customer Menu")
    print("2. Admin Menu")
    print("3. Businessman Menu")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        customer_menu()
    elif choice == '2':
        admin_menu()
    elif choice == '3':
        businessman_menu()
    elif choice == '4':
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main()

# Customer Menu
def customer_menu():
    print("Customer Menu:")
    print("1. Browse Products")
    print("2. View Product Details")
    print("3. Search Products")
    print("4. View Cart")
    print("5. Checkout")
    print("6. View Order History")
    print("7. Update Account Information")
    print("8. Logout")

    choice = input("Enter your choice: ")

    if choice == '1':
        browse_products()
    elif choice == '2':
        view_product_details()
    elif choice == '3':
        search_products()
    elif choice == '4':
        view_cart()
    elif choice == '5':
        checkout()
    elif choice == '6':
        view_order_history()
    elif choice == '7':
        update_account_information()
    elif choice == '8':
        logout()
    else:
        print("Invalid choice. Please try again.")
        customer_menu()

# Admin Menu
def admin_menu():
    print("Admin Menu:")
    print("1. Manage Products")
    print("2. Manage Orders")
    print("3. Manage Customers")
    print("4. Manage Categories")
    print("5. View Sales Analytics")
    print("6. Manage Discounts/Promotions")
    print("7. Manage Inventory")
    print("8. Logout")

    choice = input("Enter your choice: ")

    if choice == '1':
        manage_products()
    elif choice == '2':
        manage_orders()
    elif choice == '3':
        manage_customers()
    elif choice == '4':
        manage_categories()
    elif choice == '5':
        view_sales_analytics()
    elif choice == '6':
        manage_discounts_promotions()
    elif choice == '7':
        manage_inventory()
    elif choice == '8':
        logout()
    else:
        print("Invalid choice. Please try again.")
        admin_menu()

# Businessman Menu
def businessman_menu():
    print("Businessman Menu:")
    print("1. Manage Products")
    print("2. View Orders")
    print("3. Manage Inventory")
    print("4. Sales Analytics")
    print("5. Customer Management")
    print("6. Marketing Campaigns")
    print("7. Financial Management")
    print("8. Logout")

    choice = input("Enter your choice: ")

    if choice == '1':
        businessman_manage_products()
    elif choice == '2':
        view_orders()
    elif choice == '3':
        businessman_manage_inventory()
    elif choice == '4':
        sales_analytics()
    elif choice == '5':
        customer_management()
    elif choice == '6':
        marketing_campaigns()
    elif choice == '7':
        financial_management()
    elif choice == '8':
        businessman_logout()
    else:
        print("Invalid choice. Please try again.")
        businessman_menu()

if __name__ == "__main__":
    main()
    