
# File Stucture
'''
Qalakriti_Project/
│
├── static/
│   ├── css/
│   │   ├── styles.css              # Custom CSS styles
│   │   └── ...                     # Other CSS files if needed
│   │
│   ├── js/
│   │   ├── script.js               # Custom JavaScript functions
│   │   └── ...                     # Other JS files if needed
│   │
│   └── img/                        # Images used in the project
│       ├── product1.jpg
│       ├── product2.jpg
│       └── ...
│
├── templates/
│   ├── admin/
│   │   ├── admin_dashboard.html   # Admin dashboard page
│   │   ├── admin_login.html       # Admin login page
│   │   ├── order_management.html  # Order management page
│   │   └── product_management.html# Product management page
│   │
│   ├── user/
│   │   ├── cart.html              # Shopping cart page
│   │   ├── checkout.html          # Checkout page
│   │   ├── confirmation.html      # Order confirmation page
│   │   ├── home.html              # Home page
│   │   ├── login.html             # User login page
│   │   ├── orders.html            # Order history page
│   │   ├── product.html           # Product details page
│   │   └── register.html          # User registration page
│   │
│   └── includes/
│       ├── header.html            # Common header template
│       ├── footer.html            # Common footer template
|       ├── about.html
│       └── ...                    # Other common templates if needed
│
├── app.py                          # Flask application script
│
├── requirements.txt                # Python dependencies
│
└── database.sql                    # SQL script for database schema and data
'''

# Bash script to make directories
#!/bin/bash

# Create project directory
mkdir Qalakriti_Project
cd Qalakriti_Project

# Create static directory and its subdirectories
mkdir -p static/css static/js static/img

# Create templates directory and its subdirectories
mkdir -p templates/admin templates/user templates/includes

# Create individual HTML files
touch templates/admin/admin_dashboard.html
touch templates/admin/admin_login.html
touch templates/admin/order_management.html
touch templates/admin/product_management.html

touch templates/user/cart.html
touch templates/user/checkout.html
touch templates/user/confirmation.html
touch templates/user/home.html
touch templates/user/login.html
touch templates/user/orders.html
touch templates/user/product.html
touch templates/user/register.html

# Create common template files
touch templates/includes/header.html
touch templates/includes/footer.html

# Create app.py file
touch app.py

# Create requirements.txt file
touch requirements.txt

# Create database.sql file
touch database.sql

# Display completion message
echo "Directory structure and files created successfully."

### Detailed Description:

- **static/**: Contains static files like CSS, JavaScript, and images.
  - **css/**: Holds CSS files for styling the webpage.
  - **js/**: Contains JavaScript files for client-side scripting.
  - **images/**: Stores images used in the webpage.
  
- **templates/**: Contains HTML templates for different pages.
  - **base.html**: Base template with common elements like header, footer, and navigation bar.
  - **home.html**: Template for the home page.
  - **product.html**: Template for displaying product details.
  - **cart.html**: Template for the shopping cart page.
  - Add more templates as needed for additional pages.
  
- **app.py**: Main Flask application file containing route definitions and configurations.
- **database.py**: Contains functions to interact with the MySQL database (e.g., connecting, querying).
- **models.py**: Defines SQLAlchemy models to represent database tables as Python classes.
- **routes.py**: Contains Flask route definitions separated from the main app file for better organization.
- **requirements.txt**: Lists all Python dependencies required for the project. You can generate it using `pip freeze > requirements.txt`.

This structure should help organize your project effectively and keep related files together. Adjust and expand it as needed based on your specific requirements and preferences.
