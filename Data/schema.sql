-- run?
-- mysql -u root -p < Data/schema.sql
-- mysql -u root -p Qalakriti < Data/schema.sql

-- relationship check

DROP DATABASE IF EXISTS Qalakriti;

CREATE DATABASE Qalakriti;

USE Qalakriti;

DROP TABLE IF EXISTS `User`;

CREATE TABLE `User` (
    `usrID` INT NOT NULL AUTO_INCREMENT,
    `usrName` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `usrEmail` VARCHAR(255) COLLATE utf8mb4_unicode_ci UNIQUE NOT NULL,
    `usrPassword` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `usrType` VARCHAR(50) COLLATE utf8mb4_unicode_ci NOT NULL,
    `usrRegDate` DATE NOT NULL,
    `usrMobNumber` BIGINT NOT NULL,
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
    `prodID` INT NOT NULL AUTO_INCREMENT,
    `prodName` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `prodDesc` TEXT,
    `prodPrice` DECIMAL(10, 2) NOT NULL,
    `prodStock` INT NOT NULL,
    `catID` INT,
    `craftID` INT,
    `prodCreateDate` DATE NOT NULL,
    FOREIGN KEY (catID) REFERENCES `Category`(catID),
    FOREIGN KEY (craftID) REFERENCES `Craftsman`(craftID)
    PRIMARY KEY (`prodID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `Category`;

CREATE TABLE `Category` (
    `catID` INT NOT NULL AUTO_INCREMENT,
    `catName` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL
    PRIMARY KEY (`catID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `Craftsman`;

CREATE TABLE `Craftsman` (
    `craftID` INT NOT NULL AUTO_INCREMENT,
    `craftName` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `craftMobNumber` BIGINT,
    `craftEmail` VARCHAR(255) COLLATE utf8mb4_unicode_ci,
    `craftBusType` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL
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
