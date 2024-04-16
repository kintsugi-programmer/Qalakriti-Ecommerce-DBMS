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
  `craftPassword` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL, -- Added password field

  
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
INSERT INTO `Craftsman` (`craftName`, `craftMobNumber`, `craftEmail`, `craftBusType`, `craftPassword`) VALUES
('Siddhant Bali', 8076218888, 'siddhant22496@iiitd.ac.in', 'admin', 'balinux'),
('Dheeraj', 1234567890, 'crafty@example.com', 'Flower Decor', 'password1'),
('Fabindia', 1111111111, 'fabindia@example.com', 'Textile', 'password2'),
('KhadiGran', 2222222222, 'khadigramindia@example.com', 'Textile', 'password3'),
('Jaypore', 3333333333, 'jaypore@example.com', 'Candles', 'password4'),
('JodhpurSpecial', 4444444444, 'jodhpurspl@example.com', 'Pottery', 'password5'),
('Anokhi', 5555555555, 'anokhi@example.com', 'Textile', 'password6'),
('Kala Drishti', 6666666666, 'kdrishti@example.com', 'Woodwork', 'password7'),
('Neerja', 7777777777, 'neerjaorg@example.com', 'Leather', 'password8');


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
