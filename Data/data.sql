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
INSERT INTO `Craftsman` (`craftName`, `craftMobNumber`, `craftEmail`, `craftBusType`) VALUES
('Dheeraj', 1234567890, 'craftydheeraj@example.com', 'Flower Decor');


-- Category Table
INSERT INTO `Category` (`catName`) VALUES
('Woodwork'),
('Flower Decor'),
('Pottery');

-- Product Table
INSERT INTO `Product` (`prodName`, `prodDesc`, `prodPrice`, `prodStock`, `catID`, `craftID`, `prodCreateDate`) VALUES
('Wood Chair', 'Antique Oak Wood Chair From Chennai.', 100, 100, 1, 1, '2022-01-01'),
('Kintsugi Clay Vase', 'Handcrafted vase made of clay from Rajasthan.', 49.99, 50, 2, 2, '2023-01-02');

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