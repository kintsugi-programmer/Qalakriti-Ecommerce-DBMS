-- Project Deadline-3 DBMS 
-- drop eleminate 

-- Dev. Team 
-- 1. Siddhant Bali: 2022496 - Schema and Data
-- 2. Nishchay Yadav: 2022332 - Ideation
-- 3. Pankhuri Singh: 2022348 - Ideation

-- Schema
-- 

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
  
-- INSERT statements


-- Data
-- User Table
INSERT INTO `User` (`usrName`, `usrEmail`, `usrPassword`, `usrType`, `usrRegDate`, `usrMobNumber`) VALUES
('Siddhant Bali', 'siddhant22496@iiitd.ac.in', 'balinux', 'admin', '2024-01-01', 8076218888),
('Nishchay Yadav', 'nischay22332@iiitd.ac.in', 'nischay', 'customer', '2024-01-01', 1234123412),
('Pankhuri Singh', 'pankhuri22348@iiitd.ac.in', 'singh', 'customer', '2020-01-01', 1010101010);

-- Address Table
INSERT INTO `Address` (`usrID`, `addrStreet`, `addrCity`, `addrState`, `addrZipCode`) VALUES
(1, 'H1', 'Govindpuri', 'Delhi', '110092'),
(2, 'H2', 'Govindpuri', 'Delhi', '110092'),
(3, 'H3', 'Govindpuri', 'Delhi', '110092');

-- Craftsman Table
INSERT INTO Craftsman (craftName, craftMobNumber, craftEmail, craftBusType) 
VALUES
  ('Dheeraj', 1234567890, 'craftydheeraj@example.com', 'Flower Decor'),
  ('Mahesh', 9876543210, 'craftymahesh@email.com', 'Pottery');

-- Category Table
INSERT INTO `Category` (`catName`) VALUES
('Woodwork'),
('Flower Decor'),
('Pottery');

-- Product Table
INSERT INTO Product 
  (prodName, prodDesc, prodPrice, prodStock, catID, craftID, prodCreateDate)
VALUES
  ('Wood Chair', 'Antique Chair', 100, 100, 1, 1, '2022-01-01'),
  ('Clay Vase', 'Clay Vase', 50, 50, 3, 2, '2023-01-02');

-- Order Table
INSERT INTO `Order` (`usrID`, `ordDate`, `ordTotalAmt`, `ordStatus`) VALUES
(1, '2024-02-01', 99.98, 'completed'),
(2, '2024-02-02', 29.99, 'pending');

-- OrderItem Table
INSERT INTO `OrderItem` (`ordID`, `prodID`, `itemQty`, `itemSubtotal`) VALUES
(1, 1, 2, 99.98),
(2, 2, 1, 29.99);

-- Review Table
INSERT INTO `Review` (`usrID`, `prodID`, `revRating`, `revComment`, `revDate`) VALUES
(1, 1, 5, 'Great chair, very comfortable and feeling royal !', '2024-02-03'),
(2, 2, 4, 'Lovely vase,with great philosophy perfect for my living room.', '2024-02-04');