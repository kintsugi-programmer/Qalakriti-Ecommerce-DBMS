-- Create a database named 'ecommerce_db'
CREATE DATABASE IF NOT EXISTS ecommerce_db;

-- Use the 'ecommerce_db' database
USE ecommerce_db;

-- Create the 'products' table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the 'orders' table
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create the 'order_items' table
CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert dummy data into the 'products' table
INSERT INTO products (name, price, description)
VALUES 
    ('Product 1', 19.99, 'Description of Product 1'),
    ('Product 2', 29.99, 'Description of Product 2'),
    ('Product 3', 39.99, 'Description of Product 3');

-- Insert dummy data into the 'users' table
INSERT INTO users (username, email, password)
VALUES 
    ('user1', 'user1@example.com', 'password1'),
    ('user2', 'user2@example.com', 'password2'),
    ('user3', 'user3@example.com', 'password3');

-- Insert dummy data into the 'orders' table
INSERT INTO orders (user_id, total_amount)
VALUES 
    (1, 59.98),
    (2, 89.97),
    (3, 129.96);

-- Insert dummy data into the 'order_items' table
INSERT INTO order_items (order_id, product_id, quantity, subtotal)
VALUES 
    (1, 1, 2, 39.98),
    (1, 2, 1, 19.99),
    (2, 2, 3, 89.97),
    (3, 3, 2, 79.98);
