-- =====================================
-- Database: sales_db
-- =====================================

CREATE DATABASE IF NOT EXISTS sales_db;
USE sales_db;

-- =====================================
-- Table: order_leads
-- =====================================
CREATE TABLE order_leads (
    lead_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    product_interested VARCHAR(100),
    lead_status ENUM('New', 'Contacted', 'Converted', 'Lost') DEFAULT 'New',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- Table: sales
-- =====================================
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    lead_id INT,
    sale_date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    payment_mode ENUM('Cash', 'Card', 'UPI', 'Bank Transfer'),
    sale_status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (lead_id) REFERENCES order_leads(lead_id)
);

-- =====================================
-- Table: invoices
-- =====================================
CREATE TABLE invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_id INT NOT NULL,
    invoice_number VARCHAR(50) UNIQUE NOT NULL,
    invoice_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    tax DECIMAL(10,2) DEFAULT 0.00,
    total_payable DECIMAL(10,2) GENERATED ALWAYS AS (amount + tax) STORED,
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id)
);

-- =====================================
-- Sample Data (Optional)
-- =====================================

INSERT INTO order_leads (customer_name, email, phone, product_interested, lead_status) VALUES
('Rahul Sharma','rahul@gmail.com','9000000001','Laptop','Converted'),
('Ayesha Khan','ayesha@gmail.com','9000000002','Mobile','Converted'),
('Amit Verma','amit@gmail.com','9000000003','Tablet','Contacted'),
('Sneha Patel','sneha@gmail.com','9000000004','Smart Watch','Converted'),
('Rohit Mehta','rohit@gmail.com','9000000005','Laptop','Lost'),
('Neha Gupta','neha@gmail.com','9000000006','Printer','Converted'),
('Arjun Singh','arjun@gmail.com','9000000007','Router','Contacted'),
('Kavita Joshi','kavita@gmail.com','9000000008','Mobile','Converted'),
('Imran Shaikh','imran@gmail.com','9000000009','Laptop','Converted'),
('Pooja Nair','pooja@gmail.com','9000000010','Tablet','New'),

('Sahil Malhotra','sahil@gmail.com','9000000011','Camera','Converted'),
('Riya Sen','riya@gmail.com','9000000012','Mobile','Contacted'),
('Ankit Jain','ankit@gmail.com','9000000013','Laptop','Converted'),
('Mehul Shah','mehul@gmail.com','9000000014','Smart TV','Converted'),
('Fatima Noor','fatima@gmail.com','9000000015','Headphones','New'),
('Varun Kapoor','varun@gmail.com','9000000016','Printer','Lost'),
('Alok Mishra','alok@gmail.com','9000000017','Router','Converted'),
('Simran Kaur','simran@gmail.com','9000000018','Mobile','Converted'),
('Deepak Yadav','deepak@gmail.com','9000000019','Laptop','Contacted'),
('Nisha Roy','nisha@gmail.com','9000000020','Tablet','Converted'),

('Aditya Kulkarni','aditya@gmail.com','9000000021','Laptop','Converted'),
('Zoya Ali','zoya@gmail.com','9000000022','Mobile','Converted'),
('Manish Pandey','manish@gmail.com','9000000023','Smart Watch','Contacted'),
('Priya Iyer','priya@gmail.com','9000000024','Tablet','Converted'),
('Karan Arora','karan@gmail.com','9000000025','Laptop','Converted'),
('Ishita Bose','ishita@gmail.com','9000000026','Camera','New'),
('Suresh Rao','suresh@gmail.com','9000000027','Printer','Converted'),
('Ananya Das','ananya@gmail.com','9000000028','Mobile','Converted'),
('Vikram Choudhary','vikram@gmail.com','9000000029','Router','Lost'),
('Salman Khan','salman@gmail.com','9000000030','Laptop','Converted'),

('Tanya Mathur','tanya@gmail.com','9000000031','Tablet','Contacted'),
('Rakesh Singh','rakesh@gmail.com','9000000032','Smart TV','Converted'),
('Farhan Akhtar','farhan@gmail.com','9000000033','Mobile','Converted'),
('Shweta Tiwari','shweta@gmail.com','9000000034','Laptop','Contacted'),
('Nitin Bansal','nitin@gmail.com','9000000035','Router','Converted'),
('Aditi Malhotra','aditi@gmail.com','9000000036','Tablet','New'),
('Mohit Agarwal','mohit@gmail.com','9000000037','Camera','Converted'),
('Payal Jain','payal@gmail.com','9000000038','Mobile','Converted'),
('Harsh Vardhan','harsh@gmail.com','9000000039','Laptop','Lost'),
('Reema Sethi','reema@gmail.com','9000000040','Printer','Converted'),

('Yash Patel','yash@gmail.com','9000000041','Laptop','Converted'),
('Kritika Arora','kritika@gmail.com','9000000042','Mobile','Converted'),
('Ashwin Iyer','ashwin@gmail.com','9000000043','Tablet','Contacted'),
('Noor Fatima','noor@gmail.com','9000000044','Smart Watch','Converted'),
('Ritu Saxena','ritu@gmail.com','9000000045','Laptop','Converted'),
('Sameer Qureshi','sameer@gmail.com','9000000046','Camera','New'),
('Aman Goel','aman@gmail.com','9000000047','Router','Converted'),
('Divya Khanna','divya@gmail.com','9000000048','Mobile','Converted'),
('Lokesh Rana','lokesh@gmail.com','9000000049','Laptop','Contacted'),
('Meena Pillai','meena@gmail.com','9000000050','Tablet','Converted');


INSERT INTO sales (lead_id, sale_date, total_amount, payment_mode, sale_status) VALUES
(1,'2026-01-05',55000,'UPI','Completed'),
(2,'2026-01-06',24000,'Card','Completed'),
(4,'2026-01-06',18000,'Cash','Completed'),
(6,'2026-01-07',32000,'UPI','Completed'),
(8,'2026-01-07',22000,'Card','Completed'),
(9,'2026-01-08',60000,'UPI','Completed'),
(11,'2026-01-08',45000,'Card','Completed'),
(13,'2026-01-09',58000,'UPI','Completed'),
(14,'2026-01-09',75000,'Bank Transfer','Completed'),
(17,'2026-01-10',15000,'Cash','Completed'),

(18,'2026-01-10',23000,'UPI','Completed'),
(20,'2026-01-11',21000,'Card','Completed'),
(21,'2026-01-11',56000,'UPI','Completed'),
(22,'2026-01-12',26000,'Cash','Completed'),
(24,'2026-01-12',20000,'Card','Completed'),
(25,'2026-01-13',59000,'UPI','Completed'),
(27,'2026-01-13',17000,'Cash','Completed'),
(28,'2026-01-14',24000,'Card','Completed'),
(30,'2026-01-14',61000,'UPI','Completed'),
(32,'2026-01-15',78000,'Bank Transfer','Completed'),

(33,'2026-01-15',26000,'Card','Completed'),
(35,'2026-01-16',14000,'Cash','Completed'),
(37,'2026-01-16',35000,'UPI','Completed'),
(38,'2026-01-17',23000,'Card','Completed'),
(40,'2026-01-17',19000,'Cash','Completed'),
(41,'2026-01-18',60000,'UPI','Completed'),
(42,'2026-01-18',27000,'Card','Completed'),
(44,'2026-01-19',16000,'Cash','Completed'),
(45,'2026-01-19',58000,'UPI','Completed'),
(47,'2026-01-20',22000,'Card','Completed');


INSERT INTO invoices (sale_id, invoice_number, invoice_date, amount, tax) VALUES
(1,'INV-2001','2026-01-05',55000,9900),
(2,'INV-2002','2026-01-06',24000,4320),
(3,'INV-2003','2026-01-06',18000,3240),
(4,'INV-2004','2026-01-07',32000,5760),
(5,'INV-2005','2026-01-07',22000,3960),

(6,'INV-2006','2026-01-08',60000,10800),
(7,'INV-2007','2026-01-08',45000,8100),
(8,'INV-2008','2026-01-09',58000,10440),
(9,'INV-2009','2026-01-09',75000,13500),
(10,'INV-2010','2026-01-10',15000,2700),

(11,'INV-2011','2026-01-10',23000,4140),
(12,'INV-2012','2026-01-11',21000,3780),
(13,'INV-2013','2026-01-11',56000,10080),
(14,'INV-2014','2026-01-12',26000,4680),
(15,'INV-2015','2026-01-12',20000,3600),

(16,'INV-2016','2026-01-13',59000,10620),
(17,'INV-2017','2026-01-13',17000,3060),
(18,'INV-2018','2026-01-14',24000,4320),
(19,'INV-2019','2026-01-14',61000,10980),
(20,'INV-2020','2026-01-15',78000,14040),

(21,'INV-2021','2026-01-15',26000,4680),
(22,'INV-2022','2026-01-16',14000,2520),
(23,'INV-2023','2026-01-16',35000,6300),
(24,'INV-2024','2026-01-17',23000,4140),
(25,'INV-2025','2026-01-17',19000,3420);

