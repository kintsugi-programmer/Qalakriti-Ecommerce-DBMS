DROP DATABASE IF EXISTS Qalakriti;
CREATE DATABASE Qalakriti;
USE Qalakriti;



CREATE TABLE IF NOT EXISTS `User` (
  `usrID` int NOT NULL AUTO_INCREMENT,
  `usrName` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usrEmail` varchar(255) COLLATE utf8mb4_unicode_ci UNIQUE NOT NULL,
  `usrPassword` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usrRegDate` date NOT NULL,
  `usrMobNumber` bigint NOT NULL,
  PRIMARY KEY (`usrID`),
  INDEX (`usrName`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `User` (`usrName`, `usrEmail`, `usrPassword`, `usrRegDate`, `usrMobNumber`) VALUES
('Siddhant Bali', 'siddhant22496@iiitd.ac.in', 'balinux', '2020-01-01', 8076218888),
('Nishchay Yadav', 'nischay22332@iiitd.ac.in', 'nischay', '2024-01-01', 1234123412),
('Pankhuri Singh', 'pankhuri22348@iiitd.ac.in', 'singh', '2024-01-01', 1010101010),
('Mudit Bansal', 'mudit22300@iiitd.ac.in', 'bansal', '2024-01-01', 9999999999),
('Somay Jalan', 'somay22301@iiitd.ac.in', 'jalan', '2024-01-01', 8888888888),
('Chahat Ahuja', 'chahat22302@iiitd.ac.in', 'ahuja', '2024-01-01', 7777777777),
('Kushagra Gupta', 'kushagra22303@iiitd.ac.in', 'gupta', '2024-01-01', 6666666666),
('Rayyan Hussain', 'rayyan22304@iiitd.ac.in', 'hussain', '2024-01-01', 5555555555),
('Vibhuti Malhotra', 'vibhuti22305@iiitd.ac.in', 'malhotra', '2024-01-01', 4444444444),
('Shreya Kalra', 'shreya22306@iiitd.ac.in', 'kalra', '2024-01-01', 3333333333);

CREATE TABLE IF NOT EXISTS login (
    usrName VARCHAR(255) COLLATE utf8mb4_unicode_ci PRIMARY KEY,
    usrPassword VARCHAR(255) NOT NULL,
    login_attempt INT NOT NULL DEFAULT 0,
    status VARCHAR(255) NOT NULL DEFAULT 'allowed' CHECK (status IN ('allowed', 'blocked')),
    FOREIGN KEY (usrName) REFERENCES User(usrName)
);
INSERT INTO login (usrName, usrPassword, login_attempt, status) VALUES 
('Siddhant Bali', 'balinux', 0, 'allowed'),
('Nishchay Yadav', 'nischay', 0, 'allowed'),
('Pankhuri Singh', 'singh', 0, 'allowed'),
('Mudit Bansal', 'bansal', 0, 'allowed'),
('Somay Jalan', 'jalan', 0, 'allowed'),
('Chahat Ahuja', 'ahuja', 0, 'allowed'),
('Kushagra Gupta', 'gupta', 0, 'allowed'),
('Rayyan Hussain', 'hussain', 0, 'allowed'),
('Vibhuti Malhotra', 'malhotra', 0, 'allowed'),
('Shreya Kalra', 'kalra', 0, 'allowed');


CREATE TABLE IF NOT EXISTS Product (
    prodType VARCHAR(100) PRIMARY KEY,
    craftID CHAR(8) NOT NULL,
    stock DOUBLE NOT NULL,
    price INT NOT NULL DEFAULT 0);
INSERT INTO Product (prodType, craftID, stock, price) VALUES
    ('kintsugi_vase', 'm5N6oP7Q', 700, 599.99),
    ('lavender_candles', 'R8sT9uVW', 707, 799.99),
    ('diamond_necklace', 'XyZ1A2B3', 760, 9999.99),
    ('craftland_chair', 'c4DE5fG6', 700, 2499.99),
    ('vintage_compass', 'H7iJ8kL9', 703, 1999.99),
    ('aranmula_kannadi_mirror', 'm0nOPqR1', 700, 3999.99),
    ('madhubani_painting_decor', 'S2tU3vWx', 400, 1499.99),
    ('rajasthani_jewellery_box', 'P2Q3r4S5', 700, 2999.99);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE TABLE OrderItems (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
