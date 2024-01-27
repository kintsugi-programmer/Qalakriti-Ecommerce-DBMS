INSERT INTO `User` (usrID, usrName, usrEmail, usrPassword, usrType, usrRegDate)
VALUES
(1, 'Rajesh Kumar', 'rajesh.kumar@example.com', 'password123', 'Customer', '2024-01-01'),
(2, 'Priya Patel', 'priya.patel@example.com', 'securepass', 'Craftsman', '2024-01-02'),
(3, 'Admin User', 'admin@example.com', 'adminpass', 'Administrator', '2024-01-03'),
(4, 'Aishwarya Singh', 'aishwarya.singh@example.com', 'pass1234', 'Customer', '2024-01-04'),
(5, 'Vikram Sharma', 'vikram.sharma@example.com', 'secretword', 'Craftsman', '2024-01-05');

INSERT INTO Address (addrID, usrID, addrStreet, addrCity, addrState, addrZipCode)
VALUES
(1, 1, '123 Main St', 'Mumbai', 'Maharashtra', '400001'),
(2, 2, '456 Craftsman Lane', 'Jaipur', 'Rajasthan', '302001'),
(3, 3, '789 Admin Blvd', 'Delhi', 'Delhi', '110001'),
(4, 4, '321 Customer Ave', 'Bangalore', 'Karnataka', '560001'),
(5, 5, '555 Craftsman Street', 'Kolkata', 'West Bengal', '700001');

INSERT INTO Category (catID, catName)
VALUES
(1, 'Textiles'),
(2, 'Pottery'),
(3, 'Woodwork'),
(4, 'Metal Crafts'),
(5, 'Leather Goods');

INSERT INTO Craftsman (craftID, craftName, craftContact, craftBusType)
VALUES
(1, 'ArtisanCrafts', 'artisan@example.com', 'Individual'),
(2, 'WoodenWonders', 'woodworker@example.com', 'Small Business'),
(3, 'MetalMasters', 'metalworker@example.com', 'Small Business'),
(4, 'LeatherCraftsCo', 'leatherworker@example.com', 'Medium Business'),
(5, 'TextileArtistry', 'textileworker@example.com', 'Individual');

INSERT INTO Product (prodID, prodName, prodDesc, prodPrice, prodStock, catID, craftID, prodCreateDate)
VALUES
(1, 'Silk Sari', 'Handwoven silk sari with traditional patterns.', 4999.99, 100, 1, 5, '2024-01-01'),
(2, 'Terracotta Diya', 'Handcrafted terracotta diya for festivals.', 299.99, 50, 2, 2, '2024-01-02'),
(3, 'Teak Wood Furniture', 'Artisan-crafted teak wood furniture for the home.', 3999.99, 75, 3, 2, '2024-01-03'),
(4, 'Brass Pooja Thali', 'Intricately designed brass pooja thali for religious ceremonies.', 899.99, 25, 4, 3, '2024-01-04'),
(5, 'Hand-stitched Leather Bag', 'Premium leather bag with traditional embroidery.', 599.99, 50, 5, 4, '2024-01-05');

INSERT INTO `Order` (ordID, usrID, ordDate, ordTotalAmt, ordStatus)
VALUES
(1, 4, '2024-02-01', 14997.00, 'Shipped'),
(2, 1, '2024-02-02', 899.99, 'Processing'),
(3, 5, '2024-02-03', 299.99, 'Delivered'),
(4, 2, '2024-02-04', 1199.98, 'Shipped'),
(5, 3, '2024-02-05', 499.99, 'Processing');

INSERT INTO OrderItem (itemID, ordID, prodID, itemQty, itemSubtotal)
VALUES
(1, 1, 1, 3, 14997.00),
(2, 2, 4, 1, 899.99),
(3, 3, 2, 1, 299.99),
(4, 4, 3, 2, 1199.98),
(5, 5, 5, 1, 499.99);

INSERT INTO Review (revID, usrID, prodID, revRating, revComment, revDate)
VALUES
(1, 4, 1, 5, 'Beautiful silk sari, love the traditional patterns!', '2024-02-01'),
(2, 1, 4, 4, 'Impressive brass pooja thali, great craftsmanship.', '2024-02-02'),
(3, 5, 2, 5, 'The terracotta diya is stunning, exceeded my expectations.', '2024-02-03'),
(4, 2, 3, 4, 'Love the teak wood furniture, perfect for my home.', '2024-02-04'),
(5, 3, 5, 5, 'High-quality leather bag, very pleased with the purchase.', '2024-02-05');
