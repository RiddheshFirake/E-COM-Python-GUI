CREATE DATABASE StormZ;

USE StormZ;

CREATE TABLE User (
    UserId INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Gender VARCHAR(10),
    Products INT NOT NULL,
    TotalProductPrice DECIMAL(10, 2)
);
select * from User;

CREATE DATABASE StormZ;

USE StormZ;

CREATE TABLE IF NOT EXISTS selected_products (
    Product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name varchar(28) not null,
    product_price INT NOT NULL
    /*action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP*/
);

SELECT * FROM selected_products;

drop table User;
drop table selected_products;


CREATE TABLE Admin (
    UserId INT PRIMARY KEY AUTO_INCREMENT,
    AdminName VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL
);

SELECT * FROM Admin;
drop table Admin;
