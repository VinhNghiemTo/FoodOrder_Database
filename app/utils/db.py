"""
Collection of functions to help establish the database
"""
import mysql.connector


# Connect to MySQL and the task database
def connect_db(config):
    conn = mysql.connector.connect(
        host=config["DBHOST"],
        user=config["DBUSERNAME"],
        password=config["DBPASSWORD"],
        database=config["DATABASE"]
    )
    return conn


# Setup for the Database
#   Will erase the database if it exists
def init_db(config):
    conn = mysql.connector.connect(
        host=config["DBHOST"],
        user=config["DBUSERNAME"],
        password=config["DBPASSWORD"]
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"DROP DATABASE IF EXISTS {config['DATABASE']};")
    cursor.execute(f"CREATE DATABASE {config['DATABASE']};")
    cursor.execute(f"use {config['DATABASE']};")
    cursor.execute(
        f"""
        CREATE TABLE Customers (

            customerID INT AUTO_INCREMENT,

            name VARCHAR(50),

            orderID INT,

            email VARCHAR(50),

            CONSTRAINT pk_customer PRIMARY KEY (customerID)

        );



        CREATE TABLE Orders (

            orderID INT,

            customerID INT,

            orderDate TIMESTAMP,

            shippedDate TIMESTAMP,

            orderStatus VARCHAR,

            totalPrice FLOAT,

            CONSTRAINT pk_order PRIMARY KEY (orderID),

            FOREIGN KEY (customerID) REFERENCES Customers (customerID)

        );



        CREATE TABLE Address (

            customerID INT,

            streetAdress VARCHAR,

            unitNumber VARCHAR(10),

            city VARCHAR,

            state VARCHAR(2),

            zipcode INT(5),

            CONSTRAINT pk_address PRIMARY KEY (streetAddress, unitNumber, zipcode),

            FOREIGN KEY (customerID) REFERENCES Customers (customerID)

        );



        CREATE TABLE OrderItem (

            itemID INT,

            name VARCHAR(50),

            irderID INT,

            unitPrice FLOAT,

            quantity TINYINT,

            CONSTRAINT pk_item PRIMARY KEY (itemID),

            FOREIGN KEY (orderID) REFERENCES Orders (orderID)

        );
        """
    )
    cursor.close()
    conn.close()
