DROP DATABASE IF EXISTS Qalakriti;
CREATE DATABASE Qalakriti;
USE Qalakriti;
DROP TABLE IF EXISTS `User`;
CREATE TABLE `User` (
    usrID INT PRIMARY KEY,
    usrName VARCHAR(255) NOT NULL,
    usrEmail VARCHAR(255) UNIQUE NOT NULL,
    usrPassword VARCHAR(255) NOT NULL,
    usrType VARCHAR(50) NOT NULL,
    usrRegDate DATE NOT NULL
);
DROP TABLE IF EXISTS Address;
CREATE TABLE Address (
    addrID INT PRIMARY KEY,
    usrID INT,
    addrStreet VARCHAR(255) NOT NULL,
    addrCity VARCHAR(255) NOT NULL,
    addrState VARCHAR(255) NOT NULL,
    addrZipCode VARCHAR(20) NOT NULL,
    FOREIGN KEY (usrID) REFERENCES `User`(usrID)
);
DROP TABLE IF EXISTS Product;
CREATE TABLE Product (
    prodID INT PRIMARY KEY,
    prodName VARCHAR(255) NOT NULL,
    prodDesc TEXT,
    prodPrice DECIMAL(10, 2) NOT NULL,
    prodStock INT NOT NULL,
    catID INT,
    craftID INT,
    prodCreateDate DATE NOT NULL,
    FOREIGN KEY (catID) REFERENCES Category(catID),
    FOREIGN KEY (craftID) REFERENCES Craftsman(craftID)
);
DROP TABLE IF EXISTS Category;
CREATE TABLE Category (
    catID INT PRIMARY KEY,
    catName VARCHAR(255) NOT NULL
);
DROP TABLE IF EXISTS Craftsman;
CREATE TABLE Craftsman (
    craftID INT PRIMARY KEY,
    craftName VARCHAR(255) NOT NULL,
    craftContact VARCHAR(20) NOT NULL,
    craftBusType VARCHAR(255) NOT NULL
);
DROP TABLE IF EXISTS `Order`;
CREATE TABLE `Order` (
    ordID INT PRIMARY KEY,
    usrID INT,
    ordDate DATE NOT NULL,
    ordTotalAmt DECIMAL(10, 2) NOT NULL,
    ordStatus VARCHAR(50) NOT NULL,
    FOREIGN KEY (usrID) REFERENCES `User`(usrID)
);
DROP TABLE IF EXISTS OrderItem;
CREATE TABLE OrderItem (
    itemID INT PRIMARY KEY,
    ordID INT,
    prodID INT,
    itemQty INT NOT NULL,
    itemSubtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ordID) REFERENCES `Order`(ordID),
    FOREIGN KEY (prodID) REFERENCES Product(prodID)
);
DROP TABLE IF EXISTS Review;
CREATE TABLE Review (
    revID INT PRIMARY KEY,
    usrID INT,
    prodID INT,
    revRating INT NOT NULL,
    revComment TEXT,
    revDate DATE NOT NULL,
    FOREIGN KEY (usrID) REFERENCES `User`(usrID),
    FOREIGN KEY (prodID) REFERENCES Product(prodID)
);
