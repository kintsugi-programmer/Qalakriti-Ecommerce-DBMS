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
    print("Product Management Menu:")
    print("1. Add New Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. View All Products")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_new_product()
    elif choice == '2':
        update_product()
    elif choice == '3':
        delete_product()
    elif choice == '4':
        view_all_products()
    else:
        print("Invalid choice. Please try again.")

def add_new_product():
    # Gather information for the new product
    prod_name = input("Enter product name: ")
    prod_desc = input("Enter product description: ")
    prod_price = float(input("Enter product price: "))
    prod_stock = int(input("Enter product stock: "))
    cat_id = int(input("Enter category ID: "))
    craft_id = int(input("Enter craftsman ID: "))
    prod_create_date = input("Enter product creation date (YYYY-MM-DD): ")

    # Perform insertion into the Product table
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = """
            INSERT INTO Product (prodName, prodDesc, prodPrice, prodStock, catID, craftID, prodCreateDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (prod_name, prod_desc, prod_price, prod_stock, cat_id, craft_id, prod_create_date))
        conn.commit()
        print("New product added successfully.")
        conn.close()

def update_product():
    # Prompt for the product ID to update
    product_id = input("Enter the product ID to update: ")

    # Fetch existing product details from the database
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM Product WHERE prodID = %s"
        cursor.execute(query, (product_id,))
        product = cursor.fetchone()
        conn.close()

        if product:
            print("Existing Product Details:")
            print("1. Name:", product[1])
            print("2. Description:", product[2])
            print("3. Price:", product[3])
            print("4. Stock:", product[4])
            print("5. Category ID:", product[5])
            print("6. Craftsman ID:", product[6])
            print("7. Creation Date:", product[7])

            # Prompt for updated information
            new_name = input("Enter new product name (or press Enter to keep the same): ")
            new_desc = input("Enter new product description (or press Enter to keep the same): ")
            new_price = input("Enter new product price (or press Enter to keep the same): ")
            new_stock = input("Enter new product stock (or press Enter to keep the same): ")
            new_cat_id = input("Enter new category ID (or press Enter to keep the same): ")
            new_craft_id = input("Enter new craftsman ID (or press Enter to keep the same): ")
            new_create_date = input("Enter new creation date (YYYY-MM-DD) (or press Enter to keep the same): ")

            # Perform the update if any field is modified
            if any([new_name, new_desc, new_price, new_stock, new_cat_id, new_craft_id, new_create_date]):
                conn = connect_to_database()
                if conn:
                    cursor = conn.cursor()
                    update_query = """
                        UPDATE Product
                        SET prodName = %s, prodDesc = %s, prodPrice = %s, prodStock = %s,
                            catID = %s, craftID = %s, prodCreateDate = %s
                        WHERE prodID = %s
                    """
                    update_values = (new_name, new_desc, new_price, new_stock, new_cat_id, new_craft_id,
                                     new_create_date, product_id)
                    cursor.execute(update_query, update_values)
                    conn.commit()
                    print("Product updated successfully.")
                    conn.close()
            else:
                print("No changes made.")
        else:
            print(f"Product with ID {product_id} not found.")
    else:
        print("Error connecting to the database.")

def delete_product():
    # Prompt for the product ID to delete
    product_id = input("Enter the product ID to delete: ")

    # Perform deletion from the Product table
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        delete_query = "DELETE FROM Product WHERE prodID = %s"
        cursor.execute(delete_query, (product_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Product deleted successfully.")
        else:
            print(f"No product found with ID {product_id}.")
        conn.close()
    else:
        print("Error connecting to the database.")


def view_all_products():
    # Fetch and display all products from the Product table
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM Product"
        cursor.execute(query)
        products = cursor.fetchall()
        print("All Products:")
        for product in products:
            print(product)
        conn.close()


def manage_orders():
    print("Order Management Menu:")
    print("1. View All Orders")
    print("2. Update Order Status")
    print("3. Delete Order")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        view_all_orders()
    elif choice == '2':
        update_order_status()
    elif choice == '3':
        delete_order()
    else:
        print("Invalid choice. Please try again.")

def view_all_orders():
    # Fetch and display all orders from the Order table
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM `Order`"
        cursor.execute(query)
        orders = cursor.fetchall()
        print("All Orders:")
        for order in orders:
            print(order)
        conn.close()

def update_order_status():
    # Prompt for the order ID and new status
    order_id = input("Enter the order ID to update: ")
    new_status = input("Enter the new status: ")

    # Perform update in the Order table
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        update_query = "UPDATE `Order` SET ordStatus = %s WHERE ordID = %s"
        cursor.execute(update_query, (new_status, order_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Order status updated successfully.")
        else:
            print(f"No order found with ID {order_id}.")
        conn.close()
    else:
        print("Error connecting to the database.")

def delete_order():
    # Prompt for the order ID to delete
    order_id = input("Enter the order ID to delete: ")

    # Perform deletion from the Order table
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        delete_query = "DELETE FROM `Order` WHERE ordID = %s"
        cursor.execute(delete_query, (order_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Order deleted successfully.")
        else:
            print(f"No order found with ID {order_id}.")
        conn.close()
    else:
        print("Error connecting to the database.")

def manage_customers():
    print("Customer Management:")
    print("1. View Customers")
    print("2. Update Customer Information")
    print("3. Delete Customer")
    print("4. Back to Admin Menu")

    choice = input("Enter your choice: ")

    if choice == '1':
        view_customers()
    elif choice == '2':
        update_customer()
    elif choice == '3':
        delete_customer()
    elif choice == '4':
        admin_menu()  # Assuming admin_menu() is defined elsewhere
    else:
        print("Invalid choice. Please try again.")
        manage_customers()

def view_customers():
    # Retrieve and display customer information from the database
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM User WHERE usrType = 'customer'"
        cursor.execute(query)
        customers = cursor.fetchall()
        if customers:
            print("Customer Information:")
            for customer in customers:
                print(f"ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}, Mobile Number: {customer[6]}")
        else:
            print("No customers found.")
        conn.close()

def update_customer():
    # Prompt for the customer ID to update
    customer_id = input("Enter the customer ID to update: ")

    # Fetch existing customer details from the database
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM User WHERE usrType = 'customer' AND usrID = %s"
        cursor.execute(query, (customer_id,))
        customer = cursor.fetchone()
        conn.close()

        if customer:
            print("Existing Customer Details:")
            print("1. Name:", customer[1])
            print("2. Email:", customer[2])
            print("3. Mobile Number:", customer[6])

            # Prompt for updated information
            new_name = input("Enter new name (or press Enter to keep the same): ")
            new_email = input("Enter new email (or press Enter to keep the same): ")
            new_mobile_number = input("Enter new mobile number (or press Enter to keep the same): ")

            # Perform the update if any field is modified
            if any([new_name, new_email, new_mobile_number]):
                conn = connect_to_database()
                if conn:
                    cursor = conn.cursor()
                    update_query = """
                        UPDATE User
                        SET usrName = %s, usrEmail = %s, usrMobNumber = %s
                        WHERE usrID = %s
                    """
                    update_values = (new_name, new_email, new_mobile_number, customer_id)
                    cursor.execute(update_query, update_values)
                    conn.commit()
                    print("Customer information updated successfully.")
                    conn.close()
            else:
                print("No changes made.")
        else:
            print(f"Customer with ID {customer_id} not found.")
    else:
        print("Error connecting to the database.")

def delete_customer():
    # Prompt for the customer ID to delete
    customer_id = input("Enter the customer ID to delete: ")

    # Perform deletion from the User table
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        delete_query = "DELETE FROM User WHERE usrID = %s AND usrType = 'customer'"
        cursor.execute(delete_query, (customer_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Customer deleted successfully.")
        else:
            print(f"No customer found with ID {customer_id}.")
        conn.close()
    else:
        print("Error connecting to the database.")

def manage_categories():
    print("Category Management:")
    print("1. View Categories")
    print("2. Add New Category")
    print("3. Update Category")
    print("4. Delete Category")
    print("5. Back to Admin Menu")

    choice = input("Enter your choice: ")

    if choice == '1':
        view_categories()
    elif choice == '2':
        add_category()
    elif choice == '3':
        update_category()
    elif choice == '4':
        delete_category()
    elif choice == '5':
        admin_menu()  # Assuming admin_menu() is defined elsewhere
    else:
        print("Invalid choice. Please try again.")
        manage_categories()

def view_categories():
    # Retrieve and display category information from the database
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM Category"
        cursor.execute(query)
        categories = cursor.fetchall()
        if categories:
            print("Categories:")
            for category in categories:
                print(f"ID: {category[0]}, Name: {category[1]}")
        else:
            print("No categories found.")
        conn.close()

def add_category():
    # Prompt for new category name
    new_name = input("Enter the name of the new category: ")

    # Insert new category into the Category table
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        insert_query = "INSERT INTO Category (catName) VALUES (%s)"
        cursor.execute(insert_query, (new_name,))
        conn.commit()
        print("Category added successfully.")
        conn.close()
    else:
        print("Error connecting to the database.")

def update_category():
    # Prompt for the category ID to update
    category_id = input("Enter the category ID to update: ")

    # Fetch existing category name from the database
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT catName FROM Category WHERE catID = %s"
        cursor.execute(query, (category_id,))
        category_name = cursor.fetchone()
        conn.close()

        if category_name:
            print(f"Existing Category Name: {category_name[0]}")

            # Prompt for updated category name
            new_name = input("Enter new category name: ")

            # Perform the update
            conn = connect_to_database()
            if conn:
                cursor = conn.cursor()
                update_query = "UPDATE Category SET catName = %s WHERE catID = %s"
                cursor.execute(update_query, (new_name, category_id))
                conn.commit()
                print("Category updated successfully.")
                conn.close()
        else:
            print(f"No category found with ID {category_id}.")
    else:
        print("Error connecting to the database.")

def delete_category():
    # Prompt for the category ID to delete
    category_id = input("Enter the category ID to delete: ")

    # Check if the category exists before deletion
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        check_query = "SELECT catID FROM Category WHERE catID = %s"
        cursor.execute(check_query, (category_id,))
        existing_category = cursor.fetchone()
        conn.close()

        if existing_category:
            # Perform deletion from the Category table
            conn = connect_to_database()
            if conn:
                cursor = conn.cursor()
                delete_query = "DELETE FROM Category WHERE catID = %s"
                cursor.execute(delete_query, (category_id,))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Category deleted successfully.")
                else:
                    print(f"No category found with ID {category_id}.")
                conn.close()
        else:
            print(f"No category found with ID {category_id}.")
    else:
        print("Error connecting to the database.")


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
    print("Financial Management Menu:")
    print("1. View Financial Reports")
    print("2. Manage Expenses")
    print("3. Handle Transactions")
    print("4. Generate Invoices")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        view_financial_reports()
    elif choice == '2':
        manage_expenses()
    elif choice == '3':
        handle_transactions()
    elif choice == '4':
        generate_invoices()
    else:
        print("Invalid choice. Please try again.")

def view_financial_reports():
    # Placeholder for viewing financial reports
    print("Viewing Financial Reports...")
    
def manage_expenses():
    # Placeholder for managing expenses
    print("Managing Expenses...")
    
def handle_transactions():
    # Placeholder for handling transactions
    print("Handling Transactions...")
    
def generate_invoices():
    # Placeholder for generating invoices
    print("Generating Invoices...")

def businessman_logout():
    print("Logout successful.")

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
    