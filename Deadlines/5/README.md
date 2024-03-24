# Qalakriti - Handcrafted E-commerce Platform Using MySQL,Html,CSS,JS,Flask

## Table of Contents
- [Qalakriti - Handcrafted E-commerce Platform Using MySQL,Html,CSS,JS,Flask](#qalakriti---handcrafted-e-commerce-platform-using-mysqlhtmlcssjsflask)
  - [Table of Contents](#table-of-contents)
- [Qalakriti](#qalakriti)
  - [Webpages](#webpages)
- [File Stucture](#file-stucture)
    - [Detailed Description:](#detailed-description)
- [db](#db)
  - [Tech Stack](#tech-stack)
    - [MySQL:](#mysql)
    - [Flask:](#flask)
    - [HTML:](#html)
    - [CSS:](#css)
    - [JavaScript:](#javascript)
    - [General:](#general)
- [Flask](#flask-1)
    - [Installation:](#installation)
    - [Creating a Flask Application:](#creating-a-flask-application)
    - [Running the Application:](#running-the-application)
    - [Routes:](#routes)
    - [View Functions:](#view-functions)
    - [Templates:](#templates)
    - [Request and Response Objects:](#request-and-response-objects)
    - [Static Files:](#static-files)
    - [Flask Extensions:](#flask-extensions)
    - [Deployment:](#deployment)
- [PyMySQL](#pymysql)
    - [Installation:](#installation-1)
    - [Connecting to a MySQL Database:](#connecting-to-a-mysql-database)
    - [Executing SQL Queries:](#executing-sql-queries)
    - [Inserting Data:](#inserting-data)
    - [Updating Data:](#updating-data)
    - [Closing the Connection:](#closing-the-connection)
    - [1. Parameterized Queries:](#1-parameterized-queries)
    - [2. Fetching Data:](#2-fetching-data)
    - [3. Transactions:](#3-transactions)
    - [4. Error Handling:](#4-error-handling)
    - [5. Connection Pooling:](#5-connection-pooling)
- [integrating PyMySQL, Flask, HTML, and JavaScript](#integrating-pymysql-flask-html-and-javascript)
    - [1. Setting Up Flask and PyMySQL:](#1-setting-up-flask-and-pymysql)
    - [2. Create a Flask Application:](#2-create-a-flask-application)
    - [3. Create HTML Templates:](#3-create-html-templates)
    - [4. Modify Flask App to Fetch Data from Database:](#4-modify-flask-app-to-fetch-data-from-database)
    - [5. Run Your Flask Application:](#5-run-your-flask-application)
- [Flask CRUD MySQL](#flask-crud-mysql)
    - [1. Install PyMySQL:](#1-install-pymysql)
    - [2. Connect to the MySQL Database:](#2-connect-to-the-mysql-database)
    - [3. Create Data:](#3-create-data)
    - [4. Read Data:](#4-read-data)
    - [5. Update Data:](#5-update-data)
    - [6. Delete Data:](#6-delete-data)
    - [7. Close Connection:](#7-close-connection)
  - [Html supporting this](#html-supporting-this)
    - [1. Setting Up Flask:](#1-setting-up-flask)
    - [2. Create Flask Application:](#2-create-flask-application)
    - [3. HTML Template:](#3-html-template)
    - [4. Python Routes for CRUD Operations:](#4-python-routes-for-crud-operations)
    - [5. Run Your Flask Application:](#5-run-your-flask-application-1)
    - [6. Test CRUD Operations:](#6-test-crud-operations)
- [Flask Architecture](#flask-architecture)
    - [1. Application Object:](#1-application-object)
    - [2. Routes:](#2-routes)
    - [3. View Functions:](#3-view-functions)
    - [4. Templates:](#4-templates)
    - [5. Static Files:](#5-static-files)
    - [6. Request and Response Cycle:](#6-request-and-response-cycle)
    - [7. Configuration:](#7-configuration)
    - [8. Extensions:](#8-extensions)
    - [9. Middleware:](#9-middleware)
    - [10. Deployment:](#10-deployment)

# Qalakriti
Qalakriti: Bringing handcrafted excellence to your doorstep
Meaning of Qalakriti: Qala means art, and Kriti means work.
Overview: Qalakriti will be an e-commerce initiative spotlighting handcrafted treasures from
various regions of India. We aspire to create a digital haven that preserves traditional
craftsmanship while providing a platform for these talented individuals to share their unique
stories and creations with the world. Qalakriti celebrates the cultural richness of India, offering a
curated collection of handicrafts like textiles, pottery, and more.
Objectives:
● Building an efficient and reliable e-commerce website
● Empowering craftsmen, especially those from underprivileged backgrounds
● Providing a wholistic customer experience
● Creating a user-friendly interface
● Creating a functioning and efficient database
Features and Functionality:
The primary features will be focused on the following target groups :
1. Administrator
○ System Configuration and Maintenance: The administrator will oversee the
overall system setup and ensure seamless functioning
○ Access Controls and User Management: Admin will handle adding new
registrations and manage what each user can access.
○ Categorizing products: Admin will be responsible for organising products into
different categories for enhanced navigation for customers.
○ Discounts and offers: Admin can add/remove special limited period offers or
discounts ( with the help of coupons or price reductions during a sale) on the
purchase of specific items.
○ Safe Payments and Order Processing: Ensuring secure payment transactions
and managing order processing, including shipping and tracking.
2. Craftsmen and businesses
○ Registration and deletion of account: Sellers like craftsmen and businesses
can register or remove their brand from the website. They can then use this
information to access their account by signing in.
○ Product Management: Sellers can add, update, or delete their listed products as
and when convenient.
○ Revenue Collection: Craftsmen receive payment when customers purchase
their products, with transactions facilitated by the administrator.
○ Shipping: Craftsmen need to pack and ship products with the help of Admin.
3. Customers
○ Registration and deletion of account: Buyers need to register themselves with
valid information to browse products and buy them. This account can be
accessed by signing in. They may also choose to delete their accounts.
○ Product Browsing: Users can browse through the diverse range of products
available on the platform and search for them using categories and a search bar.
○ Payments and Purchasing: Users can use their bank accounts to make
payments for their purchases.
○ Item Reviews: Users have the ability to review purchased items.
○ Tracking order history: After placing an order, users may choose to track the
delivery process or have a look at their previous order history

## Webpages
Certainly! Here's the refined list with additional sub-points to highlight specific features or functionalities within each page:

1. **Home Page**
   - Introduction to Qalakriti
   - Featured products or promotions
   - Navigation menu
   - Search bar
   - Quick links to important sections

2. **About Us**
   - Mission and vision of Qalakriti
   - History and background
   - Team members or artisans spotlight
   - Contact information

3. **Product Listing Page**
   - Grid or list view of available products
   - Filter options (by category, price, etc.)
   - Sorting options
   - Pagination for browsing multiple pages

4. **Category-wise Listing**
   - Segregation of products into different categories
   - Navigation through various product categories

5. **Search Functionality**
   - Ability to search for products using keywords
   - Search suggestions or autocomplete
   - Advanced search filters

6. **Product Details Page**
   - Detailed description of the selected product
   - High-resolution images
   - Pricing information
   - Add to cart button
   - Product reviews and ratings

7. **Shopping Cart**
   - Display of selected items with images and details
   - Quantity adjustment
   - Option to remove items
   - Subtotal calculation

8. **Checkout Page**
   - Input fields for billing and shipping information
   - Selection of payment method
   - Order summary
   - Proceed to payment button

9. **Order Confirmation Page**
   - Confirmation message of successful order placement
   - Order number and summary
   - Estimated delivery time
   - Additional information or recommendations

10. **Order Tracking Page**
    - Tracking order delivery status
    - Shipment tracking number
    - Estimated delivery date

11. **My Account**
    - Order history with details
    - Saved addresses for easier checkout
    - Wish list management
    - Account settings and preferences

12. **Registration Page (for Customers)**
    - Input fields for user registration
    - Captcha or security measures
    - Terms and conditions acceptance

13. **Login Page (for Customers)**
    - Username and password fields
    - Forgot password option
    - Secure login mechanism

14. **Seller Registration Page**
    - Registration form for sellers or artisans
    - Verification process details

15. **Seller Login Page**
    - Login interface for registered sellers
    - Secure authentication methods

16. **Seller Dashboard**
    - Interface to add/edit products
    - View and manage orders received
    - Shipping management tools

17. **Contact Us**
    - Contact form for inquiries or feedback
    - Contact information (phone, email, address)

18. **FAQ**
    - Frequently asked questions and answers
    - Searchable FAQ section

19. **Terms and Conditions**
    - Detailed terms of service
    - Legal agreements for website usage

20. **Privacy Policy**
    - Information on data handling and privacy
    - GDPR compliance details

21. **Admin Panel**
    - User management tools
    - Product category management interface
    - Order management system
    - Discount/Coupon management tools
    - Configuration options for payment and shipping

22. **Blog or News Section (optional)**
    - Articles or updates related to crafts and artisans
    - Insights into Indian culture and craftsmanship

23. **Testimonials/Reviews Page (optional)**
    - Customer testimonials
    - Product reviews and ratings showcase

This detailed list covers various aspects and functionalities of the Qalakriti e-commerce platform.

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

# db
'''
-- Database Management Systems
-- Deadline III: Database schema and Indexes creation
-- Dev. Team 
-- 1. Siddhant Bali: 2022496 - Schema and Data
-- 2. Nishchay Yadav: 2022332 - Ideation
-- 3. Pankhuri Singh: 2022348 - Ideation and Data

-- Schema
DROP DATABASE IF EXISTS Qalakriti;
CREATE DATABASE Qalakriti;
USE Qalakriti;

DROP TABLE IF EXISTS `User`;

CREATE TABLE `User` (
  `usrID` int NOT NULL AUTO_INCREMENT,
  `usrName` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usrEmail` varchar(255) COLLATE utf8mb4_unicode_ci UNIQUE NOT NULL,
  `usrPassword` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usrType` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usrRegDate` date NOT NULL,
  `usrMobNumber` bigint NOT NULL,
  PRIMARY KEY (`usrID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `Address`;

CREATE TABLE `Address` (
    `addrID` INT NOT NULL AUTO_INCREMENT,
    `usrID` INT NOT NULL,
    `addrStreet` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `addrCity` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `addrState` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `addrZipCode` VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL,
    PRIMARY KEY (`addrID`),
    FOREIGN KEY (usrID) REFERENCES `User`(usrID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `Product`;

CREATE TABLE `Product` (
  `prodID` int NOT NULL AUTO_INCREMENT,
  `prodName` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `prodDesc` text,
  `prodPrice` decimal(10, 2) NOT NULL, 
  `prodStock` int NOT NULL,
  `catID` int,
  `craftID` int,
   `prodCreateDate` date NOT NULL,
  
  PRIMARY KEY (`prodID`)

) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
DROP TABLE IF EXISTS `Category`;

CREATE TABLE `Category` (
  `catID` int NOT NULL AUTO_INCREMENT,
  `catName` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  
  PRIMARY KEY (`catID`)

) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
DROP TABLE IF EXISTS `Craftsman`;

CREATE TABLE `Craftsman` (
  `craftID` int NOT NULL AUTO_INCREMENT,
  `craftName` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `craftMobNumber` bigint,
  `craftEmail` varchar(255) COLLATE utf8mb4_unicode_ci,
  `craftBusType` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  
  PRIMARY KEY (`craftID`)
  
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
DROP TABLE IF EXISTS `Order`;

CREATE TABLE `Order` (
    `ordID` INT NOT NULL AUTO_INCREMENT,
    `usrID` INT NOT NULL,
    `ordDate` DATE NOT NULL,
    `ordTotalAmt` DECIMAL(10, 2) NOT NULL,
    `ordStatus` VARCHAR(50) COLLATE utf8mb4_unicode_ci NOT NULL,
    PRIMARY KEY (`ordID`),
    FOREIGN KEY (usrID) REFERENCES `User`(usrID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `OrderItem`;

CREATE TABLE `OrderItem` (
    `itemID` INT NOT NULL AUTO_INCREMENT,
    `ordID` INT NOT NULL, 
    `prodID` INT NOT NULL,
    `itemQty` INT NOT NULL,
    `itemSubtotal` DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (`itemID`),
    FOREIGN KEY (ordID) REFERENCES `Order`(ordID),
    FOREIGN KEY (prodID) REFERENCES `Product`(prodID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `Review`;

CREATE TABLE `Review` (
    `revID` INT NOT NULL AUTO_INCREMENT,
    `usrID` INT NOT NULL,
    `prodID` INT NOT NULL,
    `revRating` INT NOT NULL,
    `revComment` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `revDate` DATE NOT NULL,
    PRIMARY KEY (`revID`),
    FOREIGN KEY (usrID) REFERENCES `User`(usrID),
    FOREIGN KEY (prodID) REFERENCES `Product`(prodID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Rest of CREATE TABLE statements 

-- Add foreign keys after creating all tables
ALTER TABLE `Address` 
  ADD FOREIGN KEY (`usrID`) REFERENCES `User`(`usrID`);

ALTER TABLE `Product`
  ADD FOREIGN KEY (`catID`) REFERENCES `Category`(`catID`),
  ADD FOREIGN KEY (`craftID`) REFERENCES `Craftsman`(`craftID`);
 
-- Data

-- User Table
INSERT INTO `User` (`usrName`, `usrEmail`, `usrPassword`, `usrType`, `usrRegDate`, `usrMobNumber`) VALUES
('Siddhant Bali', 'siddhant22496@iiitd.ac.in', 'balinux', 'admin', '2020-01-01', 8076218888),
('Nishchay Yadav', 'nischay22332@iiitd.ac.in', 'nischay', 'customer', '2024-01-01', 1234123412),
('Pankhuri Singh', 'pankhuri22348@iiitd.ac.in', 'singh', 'customer', '2024-01-01', 1010101010),
('Mudit Bansal', 'mudit22300@iiitd.ac.in', 'bansal', 'customer', '2024-01-01',9999999999),
('Somay Jalan', 'somay22301@iiitd.ac.in', 'jalan', 'customer', '2024-01-01', 8888888888),
('Chahat Ahuja', 'chahat22302@iiitd.ac.in', 'ahuja', 'customer', '2024-01-01',7777777777),
('Kushagra Gupta', 'kushagra22303@iiitd.ac.in', 'gupta', 'customer', '2024-01-01', 6666666666),
('Rayyan Hussain', 'rayyan22304@iiitd.ac.in', 'hussain', 'customer', '2024-01-01', 5555555555),
('Vibhuti Malhotra', 'vibhuti22305@iiitd.ac.in', 'malhotra', 'customer', '2024-01-01', 4444444444),
('Shreya Kalra', 'shreya22306@iiitd.ac.in', 'kalra', 'customer', '2024-01-01',3333333333 );

-- Address Table
INSERT INTO `Address` (`usrID`, `addrStreet`, `addrCity`, `addrState`, `addrZipCode`) VALUES
(1, 'BH1', 'Govindpuri', 'Delhi', '110092'),
(2, 'BH2', 'Govindpuri', 'Delhi', '110092'),
(3, 'GH1', 'Govindpuri', 'Delhi', '110092'),
(4, 'BH1', 'Govindpuri', 'Delhi', '110092'),
(5, 'BH2', 'Govindpuri', 'Delhi', '110092'),
(6, 'GH1', 'Govindpuri', 'Delhi', '110092'),
(7, 'BH2', 'Govindpuri', 'Delhi', '110092'),
(8, 'BH2', 'Govindpuri', 'Delhi', '110092'),
(9, 'GH1', 'Govindpuri', 'Delhi', '110092'),
(10, 'GH1', 'Govindpuri', 'Delhi', '110092');


-- Craftsman Table
INSERT INTO `Craftsman` (`craftName`, `craftMobNumber`, `craftEmail`, `craftBusType`) VALUES
('Dheeraj', 1234567890, 'crafty@example.com', 'Flower Decor'),
('Fabindia', 1111111111, 'fabindia@example.com', 'Textile'),
('KhadiGran', 2222222222, 'khadigramindia@example.com', 'Textile'),
('Jaypore', 3333333333, 'jaypore@example.com', 'Candles'),
('JodhpurSpecial', 4444444444, 'jodhpurspl@example.com', 'Pottery'),
('Anokhi', 5555555555, 'anokhi@example.com', 'Textile'),
('Kala Drishti', 6666666666, 'kdrishti@example.com', 'Woodwork'),
('Neerja', 7777777777, 'neerjaorg@example.com', 'Leather');


-- Category Table
INSERT INTO `Category` (`catName`) VALUES
('Woodwork'),
('Flower Decor'),
('Textile'),
('Resin Art'),
('Candles'),
('Leather'),
('Jewelery'),
('Glasswork'),
('Skin Care'),
('Pottery');

-- Product Table
INSERT INTO `Product` (`prodName`, `prodDesc`, `prodPrice`, `prodStock`, `catID`, `craftID`, `prodCreateDate`) VALUES
('Wood Chair', 'Antique Oak Wood Chair From Chennai.', 100, 100, 1, 1, '2022-01-01'),
('Kintsugi Clay Vase', 'Handcrafted vase made of clay from Rajasthan.', 49.99, 50, 2, 2, '2023-01-02'),
('Lavender scented Candles', 'Set of 2 lavender scented candles from Kashmir', 250, 20, 3, 3, '2022-01-03'),
('Mango scented Candles', 'Set of 2 mango scented candles from Maharashtra', 250, 20, 3, 3, '2022-01-03'),
('Silver Necklace', 'Handcrafted silver necklace with intricate filigree work.', 499, 30, 5, 5, '2023-02-05'),
('Khadi tote bag', 'Tote bag woven with love by KhadiGramIndia', 149, 50, 4, 4, '2022-01-04');

-- Order Table
INSERT INTO `Order` (`usrID`, `ordDate`, `ordTotalAmt`, `ordStatus`) VALUES
(2, '2024-02-01', 200.00, 'completed'),
(5, '2024-02-02', 150.00, 'completed'),
(3, '2024-02-03', 200.00, 'completed'),
(4, '2024-02-04', 50.00, 'pending');

-- OrderItem Table
INSERT INTO `OrderItem` (`ordID`, `prodID`, `itemQty`, `itemSubtotal`) VALUES
(1, 1, 2, 200.00),
(2, 2, 1, 150.00),
(3, 3, 1, 200.00),
(4, 4, 1, 50.00);

-- Review Table
INSERT INTO `Review` (`usrID`, `prodID`, `revRating`, `revComment`, `revDate`) VALUES
(1, 1, 5, 'Great chair, very comfortable and feeling royal !', '2024-02-03'),
(2, 2, 4, 'Lovely vase,with great philosophy perfect for my living room.', '2024-02-04'),
(3, 3, 4, 'Amazing Fragrance but not that long-lasting', '2024-02-04'),
(4, 5, 5, 'Absolutely stunning necklace! Exceeded my expectations.', '2024-02-06');

'''
## Tech Stack
To develop the Qalakriti project using MySQL, Flask, HTML, CSS, and JavaScript, you'll need to learn several key concepts in each technology. Here's a list of concepts to cover for each:

### MySQL:
1. **Database Design**: Understanding how to design efficient database schemas.
2. **DDL and DML**: Learning SQL Data Definition Language (DDL) for creating tables, and Data Manipulation Language (DML) for inserting, updating, and deleting data.
3. **Constraints**: Familiarize yourself with primary keys, foreign keys, unique constraints, and check constraints.
4. **Queries**: Writing SQL queries for data retrieval, filtering, aggregation, and joining tables.
5. **Indexing**: Understanding how to create indexes to improve query performance.
6. **Transactions**: Learning about ACID properties and implementing transactions for maintaining data consistency.
7. **Normalization**: Understanding database normalization techniques to avoid data redundancy and improve data integrity.
8. **Stored Procedures and Triggers**: Knowledge of creating stored procedures and triggers for automating tasks and enforcing business rules.

### Flask:
1. **Routing**: Understanding how to define routes for different URLs in Flask.
2. **Templates**: Learning how to use Jinja templates for rendering HTML pages with dynamic content.
3. **Forms**: Working with Flask-WTF to create and validate forms for user input.
4. **Sessions**: Managing user sessions for authentication and authorization.
5. **Middleware**: Understanding how to use middleware for request and response processing.
6. **Database Integration**: Integrating Flask with MySQL database using SQLAlchemy or other libraries.
7. **Error Handling**: Handling errors and exceptions gracefully in Flask applications.
8. **RESTful APIs**: Optionally, learning to create RESTful APIs for interacting with the database.

### HTML:
1. **Semantics**: Understanding HTML5 semantics and structuring web pages appropriately.
2. **Forms**: Learning form elements and attributes for user input.
3. **Tables and Lists**: Using tables and lists to organize and present data.
4. **Media**: Embedding images, videos, and audio files in HTML pages.
5. **Hyperlinks and Anchors**: Creating hyperlinks and anchors for navigation.
6. **Semantic Elements**: Using header, footer, nav, article, section, etc., for better structuring.
7. **Accessibility**: Ensuring accessibility standards are met for users with disabilities.
8. **Metadata**: Understanding meta tags for SEO and social sharing.

### CSS:
1. **Selectors and Properties**: Learning CSS selectors and properties for styling HTML elements.
2. **Layouts**: Understanding different layout techniques like Flexbox and Grid for responsive design.
3. **Box Model**: Understanding the box model and its properties (margin, border, padding, content).
4. **Responsive Design**: Implementing media queries for designing responsive layouts.
5. **Transitions and Animations**: Adding transitions and animations to enhance user experience.
6. **Typography**: Styling text elements with different fonts, sizes, and weights.
7. **Colors and Backgrounds**: Using colors, gradients, and background images effectively.
8. **CSS Preprocessors**: Optionally, learning preprocessors like Sass or Less for efficient CSS development.

### JavaScript:
1. **DOM Manipulation**: Understanding how to manipulate HTML elements using the Document Object Model (DOM).
2. **Event Handling**: Learning to handle user interactions like clicks, mouse movements, etc.
3. **AJAX**: Understanding Asynchronous JavaScript and XML (AJAX) for making asynchronous requests to the server.
4. **ES6+ Features**: Familiarize yourself with modern JavaScript features like arrow functions, template literals, destructuring, etc.
5. **Client-Side Validation**: Implementing client-side validation for form inputs.
6. **DOM Traversal and Manipulation**: Working with DOM elements, traversing the DOM tree, and modifying elements dynamically.
7. **Promises and Fetch API**: Understanding Promises and using Fetch API for making HTTP requests.
8. **Local Storage**: Learning to use local storage for storing data on the client-side.

### General:
1. **Version Control**: Using Git for version control to manage project changes effectively.
2. **Deployment**: Understanding how to deploy Flask applications to production servers.
3. **Security Best Practices**: Learning about security vulnerabilities and implementing best practices to secure the application.
4. **Testing**: Writing unit tests and integration tests to ensure application reliability.
5. **Performance Optimization**: Optimizing code and database queries for better performance.
6. **User Experience (UX) Design**: Understanding UX principles for creating intuitive and user-friendly interfaces.

Start by mastering the basics of each technology and gradually build your skills as you work on the project. Practice regularly and refer to documentation and tutorials to deepen your understanding. Good luck with your project!

# Flask

Flask is a lightweight and flexible web application framework written in Python. It is designed to make getting started with web development in Python easy, and it's commonly used for building web applications, APIs, and more. Here's a rundown of the basics of Flask:

### Installation:
Before using Flask, you need to install it. You can install Flask using pip, Python's package manager. Open your terminal or command prompt and run:

```
pip install Flask
```

### Creating a Flask Application:
To create a Flask application, you need to create a Python script. Typically, this script will be named `app.py`, but you can name it anything you like. Here's a simple example:

```python
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and a function to handle the request
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Running the Application:
After creating your Flask application, you can run it using the following command:

```
python app.py
```

### Routes:
In Flask, routes are used to map URLs to Python functions. When a user visits a specific URL in the browser, Flask calls the corresponding Python function, also known as a view function. In the example above, `@app.route('/')` is a decorator that tells Flask to call the `hello()` function when the root URL (`/`) is accessed.

### View Functions:
View functions are Python functions that return a response to the client. In the example above, the `hello()` function returns the string `'Hello, World!'`.

### Templates:
In larger applications, you'll often want to separate your HTML markup from your Python code. Flask supports Jinja2 templates for this purpose. Templates allow you to render dynamic content by passing variables from your Python code to your HTML templates.

### Request and Response Objects:
Flask provides request and response objects that allow you to access data submitted by the client and construct responses to send back to the client.

### Static Files:
Flask can serve static files such as CSS, JavaScript, and images. By default, Flask looks for static files in a directory named `static` in your application's root directory.

### Flask Extensions:
Flask has a rich ecosystem of extensions that provide additional functionality, such as form handling, authentication, database integration, and more. You can easily integrate these extensions into your Flask application to extend its capabilities.

### Deployment:
Flask applications can be deployed to various platforms, including traditional web servers like Apache or Nginx, as well as Platform as a Service (PaaS) providers like Heroku, AWS Elastic Beanstalk, or PythonAnywhere.

This is just a brief overview of Flask. There's a lot more to explore, including Flask's configuration options, error handling, authentication, database integration, and more. The Flask documentation is an excellent resource for diving deeper into these topics: [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/).

# PyMySQL

Sure, I'd be happy to introduce you to PyMySQL, which is a Python library used to interact with MySQL databases. Here's a basic tutorial to get you started:

### Installation:

First, you need to install PyMySQL. You can do this via pip, Python's package manager:

```bash
pip install pymysql
```

### Connecting to a MySQL Database:

To connect to a MySQL database using PyMySQL, you need to provide the necessary connection details such as hostname, username, password, and database name. Here's how you can establish a connection:

```python
import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database_name',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor  # Return rows as dictionaries
)

# Create a cursor object
cursor = connection.cursor()
```

### Executing SQL Queries:

Once you've established a connection, you can execute SQL queries using the cursor object. Here's how you can execute a simple SELECT query:

```python
# Execute a SELECT query
sql_query = "SELECT * FROM your_table_name"
cursor.execute(sql_query)

# Fetch all rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)
```

### Inserting Data:

You can insert data into a table using an INSERT query. Here's an example:

```python
# Insert data into a table
sql_query = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"
data = ('value1', 'value2')  # Data to be inserted
cursor.execute(sql_query, data)

# Commit changes
connection.commit()
```

### Updating Data:

To update existing data in a table, you can use an UPDATE query:

```python
# Update data in a table
sql_query = "UPDATE your_table_name SET column1 = %s WHERE condition"
data = ('new_value',)  # New value
cursor.execute(sql_query, data)

# Commit changes
connection.commit()
```

### Closing the Connection:

It's important to close the connection once you're done with it:

```python
# Close the cursor and connection
cursor.close()
connection.close()
```

This is a basic introduction to PyMySQL. You can explore more advanced features such as transactions, error handling, and more as you become familiar with the library. Remember to handle exceptions properly, especially when dealing with database connections and queries.


Certainly! Building upon the basics, let's delve into some intermediate concepts and best practices when using PyMySQL.

### 1. Parameterized Queries:

Using parameterized queries is a best practice to prevent SQL injection attacks and improve performance. Instead of directly formatting values into your SQL queries, you can use placeholders and provide the values separately. PyMySQL takes care of escaping the values properly.

```python
# Parameterized query
sql_query = "SELECT * FROM your_table_name WHERE column1 = %s AND column2 = %s"
data = ('value1', 'value2')
cursor.execute(sql_query, data)
```

### 2. Fetching Data:

PyMySQL provides various methods to fetch data. You can fetch a single row, multiple rows, or even iterate over the result set using a cursor. For large result sets, consider fetching data in chunks to avoid excessive memory consumption.

```python
# Fetch single row
row = cursor.fetchone()

# Fetch multiple rows
rows = cursor.fetchmany(size=5)  # Fetch 5 rows

# Iterate over result set
for row in cursor:
    print(row)
```

### 3. Transactions:

Transactions ensure data integrity by allowing you to execute a group of SQL queries as a single unit. If any query within the transaction fails, the entire transaction can be rolled back to maintain consistency.

```python
try:
    # Begin transaction
    connection.begin()

    # Execute SQL queries
    cursor.execute(sql_query1)
    cursor.execute(sql_query2)

    # Commit transaction
    connection.commit()
except Exception as e:
    # Rollback if any error occurs
    connection.rollback()
    print("Transaction failed:", e)
```

### 4. Error Handling:

It's crucial to handle errors gracefully when interacting with databases. PyMySQL provides exceptions that you can catch and handle appropriately.

```python
try:
    # Execute SQL query
    cursor.execute(sql_query)

    # Fetch data
    rows = cursor.fetchall()
except pymysql.Error as e:
    print("Error:", e)
finally:
    # Close cursor and connection
    cursor.close()
    connection.close()
```

### 5. Connection Pooling:

Managing a pool of database connections can improve performance and scalability, especially in multi-threaded or multi-process applications. Libraries like `pymysqlpool` can be used for connection pooling with PyMySQL.

```python
from pymysqlpool import ConnectionPool

# Create a connection pool
pool = ConnectionPool(host='localhost', user='your_username', password='your_password', database='your_database')

# Acquire connection from pool
connection = pool.get_connection()

# Use the connection
cursor = connection.cursor()
cursor.execute(sql_query)

# Release connection back to pool
connection.close()
```

These are some intermediate concepts and best practices that can enhance your usage of PyMySQL. As you become more proficient, you can explore further optimizations and advanced features offered by PyMySQL and MySQL databases.

Sure, integrating PyMySQL with Flask for building web applications involves creating routes in Flask to handle HTTP requests, querying the database using PyMySQL, and rendering HTML templates to display the data. Additionally, you can use JavaScript to enhance the interactivity of your web pages.

# integrating PyMySQL, Flask, HTML, and JavaScript
Here's a step-by-step guide to integrating PyMySQL, Flask, HTML, and JavaScript:

### 1. Setting Up Flask and PyMySQL:

First, make sure you have Flask and PyMySQL installed. You can install them via pip:

```bash
pip install flask pymysql
```

### 2. Create a Flask Application:

Create a new Python file for your Flask application, e.g., `app.py`, and set up a basic Flask application:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. Create HTML Templates:

Create an `templates` directory in your project folder and add an HTML file, e.g., `index.html`, to display data retrieved from the database:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
</head>
<body>
    <h1>Data from Database</h1>
    <ul id="data-list">
        <!-- Data will be displayed here -->
    </ul>
    
    <script>
        // JavaScript code for fetching data from Flask route
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                const dataList = document.getElementById('data-list');
                data.forEach(item => {
                    const li = document.createElement('li');
                    li.textContent = item.name; // Assuming 'name' is a field from your database
                    dataList.appendChild(li);
                });
            });
    </script>
</body>
</html>
```

### 4. Modify Flask App to Fetch Data from Database:

Modify your Flask app to fetch data from the database using PyMySQL and pass it to the HTML template:

```python
import pymysql

# Function to connect to the database and fetch data
def get_data():
    connection = pymysql.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database_name',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM your_table_name")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Update route to return data
@app.route('/data')
def get_data_route():
    data = get_data()
    return jsonify(data)
```

### 5. Run Your Flask Application:

Run your Flask application and navigate to `http://localhost:5000` in your web browser to see the data fetched from the database and displayed on the webpage.

```bash
python app.py
```

# Flask CRUD MySQL

This is a basic example of integrating PyMySQL, Flask, HTML, and JavaScript. You can further enhance it by adding more routes, handling form submissions, and incorporating more complex JavaScript functionalities. Additionally, consider security measures such as input validation and sanitization to protect against SQL injection attacks.


To perform CRUD operations (Create, Read, Update, Delete) in a MySQL database using Python and PyMySQL, you can follow these steps:

### 1. Install PyMySQL:

Make sure you have PyMySQL installed. If not, you can install it via pip:

```bash
pip install pymysql
```

### 2. Connect to the MySQL Database:

```python
import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database_name',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor  # Return rows as dictionaries
)
```

### 3. Create Data:

To create data, you can execute an SQL INSERT query:

```python
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql_query = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"
        data = ('value1', 'value2')  # Data to be inserted
        cursor.execute(sql_query, data)

    # Commit changes
    connection.commit()
    print("Data inserted successfully!")
except Exception as e:
    # Rollback in case of any error
    connection.rollback()
    print("Error inserting data:", e)
```

### 4. Read Data:

To read data, you can execute an SQL SELECT query:

```python
try:
    with connection.cursor() as cursor:
        # Read data
        sql_query = "SELECT * FROM your_table_name"
        cursor.execute(sql_query)

        # Fetch all rows
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print("Error reading data:", e)
```

### 5. Update Data:

To update existing data, you can execute an SQL UPDATE query:

```python
try:
    with connection.cursor() as cursor:
        # Update data
        sql_query = "UPDATE your_table_name SET column1 = %s WHERE condition"
        data = ('new_value',)  # New value
        cursor.execute(sql_query, data)

    # Commit changes
    connection.commit()
    print("Data updated successfully!")
except Exception as e:
    # Rollback in case of any error
    connection.rollback()
    print("Error updating data:", e)
```

### 6. Delete Data:

To delete data, you can execute an SQL DELETE query:

```python
try:
    with connection.cursor() as cursor:
        # Delete data
        sql_query = "DELETE FROM your_table_name WHERE condition"
        cursor.execute(sql_query)

    # Commit changes
    connection.commit()
    print("Data deleted successfully!")
except Exception as e:
    # Rollback in case of any error
    connection.rollback()
    print("Error deleting data:", e)
```

### 7. Close Connection:

Finally, don't forget to close the database connection when you're done:

```python
connection.close()
```

These are the basic CRUD operations you can perform on a MySQL database using PyMySQL in Python. Adjust the SQL queries and data as per your specific use case and database schema.

## Html supporting this

To integrate HTML and JavaScript with your Python and PyMySQL CRUD operations, you'll need to create a web interface to interact with your database. We'll use Flask for the backend (Python), and HTML along with JavaScript for the frontend.

### 1. Setting Up Flask:

First, make sure you have Flask and PyMySQL installed:

```bash
pip install Flask PyMySQL
```

### 2. Create Flask Application:

Create a file named `app.py` and set up a basic Flask application:

```python
from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

# MySQL Configuration
db = pymysql.connect(host='localhost',
                     user='your_username',
                     password='your_password',
                     database='your_database',
                     cursorclass=pymysql.cursors.DictCursor)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. HTML Template:

Create an HTML file named `index.html` inside a folder named `templates` in your project directory:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD App</title>
</head>
<body>
    <h1>CRUD App</h1>
    
    <!-- Form for creating data -->
    <form id="create-form">
        <input type="text" id="name" placeholder="Enter Name">
        <button type="submit">Create</button>
    </form>

    <!-- Display area for fetched data -->
    <ul id="data-list"></ul>

    <script>
        // JavaScript code for fetching and displaying data
        const form = document.getElementById('create-form');
        const dataList = document.getElementById('data-list');

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;

            // Send POST request to create data
            fetch('/create', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: name })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Clear input field
                    document.getElementById('name').value = '';
                    // Fetch and display updated data
                    fetchAndDisplayData();
                } else {
                    console.error(data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });

        // Function to fetch and display data
        function fetchAndDisplayData() {
            fetch('/read')
            .then(response => response.json())
            .then(data => {
                dataList.innerHTML = '';
                data.items.forEach(item => {
                    const li = document.createElement('li');
                    li.textContent = item.name;
                    dataList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
        }

        // Initial fetch and display data
        fetchAndDisplayData();
    </script>
</body>
</html>
```

### 4. Python Routes for CRUD Operations:

Add routes in your Flask app to handle CRUD operations:

```python
# Route for creating data
@app.route('/create', methods=['POST'])
def create():
    try:
        name = request.json['name']
        with db.cursor() as cursor:
            cursor.execute("INSERT INTO your_table_name (name) VALUES (%s)", (name,))
            db.commit()
        return jsonify({'success': True, 'message': 'Data created successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

# Route for reading data
@app.route('/read')
def read():
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM your_table_name")
            data = cursor.fetchall()
        return jsonify({'success': True, 'items': data})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
```

### 5. Run Your Flask Application:

Run your Flask application:

```bash
python app.py
```

### 6. Test CRUD Operations:

Now, you can visit `http://localhost:5000` in your browser to interact with your CRUD application. You can create, read, update, and delete data using the provided form and JavaScript logic.

This setup demonstrates a basic CRUD application using Flask, PyMySQL, HTML, and JavaScript. You can expand and customize it further based on your requirements, such as adding update and delete functionality, implementing error handling, and enhancing the user interface.

# Flask Architecture
Flask follows a simple yet powerful architecture that makes it easy to develop web applications. At its core, Flask is based on the WSGI (Web Server Gateway Interface) specification, which defines a standard interface between web servers and Python web applications or frameworks. Here's an overview of the architecture of a Flask application:

### 1. Application Object:

At the heart of every Flask application is the Flask object. This object represents the Flask application and is used to configure it and define its routes.

```python
from flask import Flask

app = Flask(__name__)
```

### 2. Routes:

Routes are URLs that the application listens for. They are associated with functions that handle the requests made to those URLs. In Flask, routes are defined using the `@app.route()` decorator.

```python
@app.route('/')
def index():
    return 'Hello, World!'
```

### 3. View Functions:

View functions are Python functions that handle requests from clients and return responses. They are associated with routes and are responsible for generating the content that is sent back to the client.

```python
@app.route('/user/<username>')
def user_profile(username):
    return f'Hello, {username}!'
```

### 4. Templates:

Templates are HTML files that define the structure of web pages. They allow you to dynamically generate HTML content by inserting data into placeholders. Flask uses Jinja2 templating engine for rendering templates.

```html
<!-- template.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('template.html', title='Welcome', name='John')
```

### 5. Static Files:

Static files, such as CSS, JavaScript, and images, are served directly by the web server without modification. Flask provides a built-in mechanism to serve static files from a directory named `static`.

```
project/
    app.py
    static/
        css/
            style.css
        js/
            script.js
```

### 6. Request and Response Cycle:

When a client sends a request to a Flask application, the request is processed by the routing system, which determines which view function should handle the request based on the URL. The view function generates a response, which is then returned to the client.

### 7. Configuration:

Flask applications can be configured using configuration variables, which are typically defined as uppercase variables in the main application module.

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your_secret_key'
```

### 8. Extensions:

Flask is designed to be lightweight and modular. Additional functionality can be added to Flask applications using extensions, which are third-party packages that integrate with Flask. Extensions exist for a wide range of purposes, including database integration, authentication, and form validation.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
```

### 9. Middleware:

Middleware are components that intercept and process requests and responses. While Flask itself doesn't have built-in middleware support, you can use WSGI middleware or extensions to add middleware functionality to your application.

### 10. Deployment:

Flask applications can be deployed using a variety of web servers, including built-in development server, Gunicorn, uWSGI, or as part of larger web server setups like Apache or Nginx. Deployment often involves configuring the web server to forward requests to the Flask application using WSGI.

This is a high-level overview of the architecture of a Flask application. Flask's simplicity and flexibility make it an excellent choice for developing web applications of varying complexity.