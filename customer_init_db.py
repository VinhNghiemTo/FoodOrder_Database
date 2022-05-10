import os
import csv

import mysql.connector


def setup_database(csvfile):
    """
    Function to initialize the MySQL database

    :param csvfile: csv datafile for customers
    """
    create_tables()
    populate_tables(csvfile)


def populate_tables(csvfile):
    """
    Put data into the Customers table

    :param csvfile: csv datafile for customers
    """
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    sql_insert = "INSERT INTO Customers (CustomerID, FirstName, LastName, Email) VALUE (%s, %s, %s, %s)"
    with open(csvfile, 'r') as csv_input:
        reader = csv.DictReader(csv_input)
        for row in reader:
            insert_values = (row["id"], int(row["first_name"]), row["last_name"], row["email"])
            cursor.execute(sql_insert, insert_values)

    conn.commit()
    cursor.close()
    conn.close()


def create_tables():
    """
    Add the tables to the MySQL database
    """
    conn = mysql.connector.connect(
        host = os.getenv("DBHOST"),
        user = os.getenv("DBUSERNAME"),
        password = os.getenv("DBPASSWORD")
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"DROP DATABASE IF EXISTS {os.getenv('DATABASE')};")
    cursor.execute(f"CREATE DATABASE {os.getenv('DATABASE')};")
    cursor.execute(f"USE {os.getenv('DATABASE')};")

    cursor.execute(
        '''
        CREATE TABLE  Customers
        (
            CustomerID INT,
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            Email VARCHAR(50),
            CONSTRAINT pk_customer PRIMARY KEY (CustomerID)
        )
        '''
    )

    cursor.close()
    conn.close()


def connect_db():
    """
    Connect to the MySQL database

    :return: Connection object to the MySQL database
    """
    conn = mysql.connector.connect(
        host = os.getenv("DBHOST"),
        user = os.getenv("DBUSERNAME"),
        password = os.getenv("DBPASSWORD"),
        database = os.getenv("DATABASE")
    )

    return conn

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    setup_database('customers_data.csv')