from datetime import datetime

# Class to model Task objects
class Customer:
    def __init__(self, name, orderID, email):
        self._name = name
        self._creation_datetime = datetime.now()
        self._completed = 0
        self._email = email
        self._orderID = orderID
        #self.set_id
   
    # returns name of customer
    @property
    def name(self):
        return self._name
 
    # returns customer's order id
    @property
    def orderID(self):
        return self._orderID
 
    # returns customer's email
    @property
    def email(self):
        return self._email
    
    #returns an auto increment of the customer ID
    """@property
    def customerID(self):
        return self._customerID"""
 
    # assigns name to customer
    @name.setter
    def name(self, new_name):
        self._name = new_name
 
    # assigns order id to customer
    @orderID.setter
    def order_id(self, new_order_id):
        self._orderID = new_order_id
 
    # assigns email to customer
    @email.setter
    def email(self, new_email):
        self._email = new_email
 
    # sets a customer id
    """@customerID.setter
    def cust_id(self):
        self._customerID"""

class Address:
    def __init__(self, street_address, city, state, zip_code):
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code
 
    @property
    def street_address(self):
        return self._street_address
 
    @property
    def city(self):
        return self._city
 
    @property
    def state(self):
        return self._state
 
    @property
    def zip_code(self):
        return self._zip_code



class Order:
    def __init__(self, price):
        self.set_id
        self._id_cursor = 0
        self._price = price
        self._order_status = False
        self._order_date = datetime.now()
 
    # returns the next available id value
    @property
    def id_cursor(self):
        return self.id_cursor
 
    # returns the price of the order
    @property
    def price(self):
        return self._price
 
    # returns the order id number
    @property
    def order_id(self):
        return self._order_id
 
    # returns the order status
    # False = not shipped
    # True = shipped
    @property
    def order_status(self):
        self._order_status
 
    # returns the creation datetime of the order
    @property
    def order_date(self):
        return self._order_date
 
    # sets an id number for the order
    @order_id.setter
    def set_id(self):
        self._id_cursor = self._id_cursor + 1
        order_id = self.id_cursor
        self._order_id = order_id
 
    # changes order status to True
    @order_status.setter
    def complete_order(self):
        self._order_status = True
 
    # changes order status to False
    @order_status.setter
    def incomplete_order(self):
        self._order_status = False
 

class OrderItem:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        self.set_item_id
   
    # returns the next available id value
    @property
    def id_cursor(self):
        return self.id_cursor
 
    # returns the order id number
    @property
    def item_id(self):
        return self._item_id
 
    # returns the name of the item
    @property
    def name(self):
        return self._name
 
    # returns the price of the item
    @property
    def price(self):
        return self._price
 
    # returns the quantity of items
    @property
    def quantity(self):
        return self._quantity
 
    # returns the item id number
    @property
    def item_id(self):
        return self._item_id
 
    # sets an id number for the order
    @item_id.setter
    def set_item_id(self):
        self._id_cursor = self._id_cursor + 1
        item_id = self.id_cursor
        self._item_id = item_id



# Class to support reading/writing Task objects with the database
class CustomerDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor
    
    #READ operation
    def select_all_customers(self):
        select_all_query = """
            SELECT * from Customers;
        """
        self._cursor.execute(select_all_query)

        return self._cursor.fetchall()


    def select_all_customers_by_orderID(self, orderID):
        select_all_customers_by_orderID = """
            SELECT * from Customers WHERE orderID LIKE %s;
        """
        self._cursor.execute(select_all_customers_by_orderID, (f"%{orderID}%",))
        return self._cursor.fetchall()
    

    #CREATE operation
    def add_customer(self, Customer):
        insert_query = """
            INSERT INTO Customers (name, orderID, email)
            VALUES (%s, %s, %s);
        """

        self._cursor.execute(insert_query, (Customer.name, Customer.orderID, Customer.email))
        self._cursor.execute("SELECT LAST_INSERT_ID() orderID")
        task_id = self._cursor.fetchone()
        self._db_conn.commit()
        return task_id

    #UPDATE operation
    def update_customer(self, orderID):
        update_query = """
            UPDATE Customer
            SET orderID=%s
            WHERE orderID=%s;
        """
        self._cursor.execute(update_query, (Customer.orderID, orderID))
        self._db_conn.commit()

    #DELETE operation
    def delete_customer(self, orderID):
        delete_query = """
            DELETE from Customer
            WHERE orderID=%s;
        """
        self._cursor.execute(delete_query, (orderID,))
        self._db_conn.commit()

class OrderItemDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor
    
    #READ operation
    def select_all_orders(self):
        select_all_query = """
            SELECT * from OrderItem;
        """
        self._cursor.execute(select_all_query)

        return self._cursor.fetchall()


    def select_all_orders_by_orderID(self, orderID):
        select_all_orders_by_orderID = """
            SELECT * from OrderItems WHERE orderID LIKE %s;
        """
        self._cursor.execute(select_all_orders_by_orderID, (f"%{orderID}%",))
        return self._cursor.fetchall()
    

    #CREATE operation
    def add_item(self, name, itemID, unitPrice, quantity):
        insert_query = """
            INSERT INTO OrderItem (name, itemID, unitPrice, quantity)
            VALUES (%s, %s, %s, %s);
        """

        self._cursor.execute(insert_query, (OrderItem.name, OrderItem.itemID, OrderItem.unitPrice))
        self._cursor.execute("SELECT LAST_INSERT_ID() itemID")
        task_id = self._cursor.fetchone()
        self._db_conn.commit()
        return task_id

    #UPDATE operation
    def update_quantity(self, itemID):
        update_query = """
            UPDATE OrderItem
            SET quantity=%s
            WHERE itemID=%s;
        """
        self._cursor.execute(update_query, (OrderItem.quantity, itemID))
        self._db_conn.commit()

    #DELETE operation
    def delete_item(self, itemID):
        delete_query = """
            DELETE from OrderItem
            WHERE itemID=%s;
        """
        self._cursor.execute(delete_query, (itemID,))
        self._db_conn.commit()

class AddressDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor
    
    #READ operations
    def select_all_addresses(self):
        select_all_query = """
            SELECT * from Address;
        """
        self._cursor.execute(select_all_query)
        return self._cursor.fetchall()

    def select_by_city(self, city):
        select_all_query = """
            SELECT * from Address;
            WHERE city=%s;
        """
        self._cursor.execute(select_all_query, (f"%{city}%",))

        return self._cursor.fetchall()

    def select_by_customerID(self, customerID):
        select_all_query = """
            SELECT * from Address;
            WHERE customerID=%s;
        """
        self._cursor.execute(select_all_query, (f"%{customerID}%",))

        return self._cursor.fetchall()

    #CREATE operation
    def add_address(self, streetAddress, unitNumber, city, state, zipCode):
        insert_query = """
            INSERT INTO Address (streetAddress, unitNumber, city, state, zipCode)
            VALUES (%s, %s, %s, %s, %s);
        """

        self._cursor.execute(insert_query, (Address.streetAddress, Address.unitNumber, Address.city, Address.state, Address.zipCide))
        self._cursor.execute("SELECT LAST_INSERT_ID() streetAddress")
        task_id = self._cursor.fetchone()
        self._db_conn.commit()
        return task_id

    #UPDATE operation
    def update_street_address(self, streetAddress):
        update_query = """
            UPDATE Address
            SET streetAddress=%s
            WHERE streetAddress=%s;
        """
        self._cursor.execute(update_query, (Address.streetAddress, streetAddress))
        self._db_conn.commit()

    #DELETE operation
    def delete_address(self, customerID):
        delete_query = """
            DELETE from Address
            WHERE customerID=%s;
        """
        self._cursor.execute(delete_query, (customerID,))
        self._db_conn.commit()

class OrderDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor


    def select_all_orders(self):
        select_all_query = """
            SELECT * from orders;
        """
        self._cursor.execute(select_all_query)

        return self._cursor.fetchall()


    def select_all_orders_by_description(self, description):
        select_tasks_by_description = """
            SELECT * from Orders WHERE OrderID LIKE %s;
        """
        self._cursor.execute(select_tasks_by_description, (f"%{description}%",))
        return self._cursor.fetchall()


    def insert_order(self, Orders):
        insert_query = """
            INSERT INTO Orders (OrderID, CustomerID, OrderDate)
            VALUES (%s, %s, %s);
        """

        self._cursor.execute(insert_query, (Orders.OrderID, Orders.CustomerID, Orders.OrderDate))
        self._cursor.execute("SELECT LAST_INSERT_ID() OrderID")
        order_id = self._cursor.fetchone()
        self._db_conn.commit()
        return order_id


    def update_order_status(self, order_id, new_status):
        update_query = """
            UPDATE Orders
            SET OrderStatus=%s
            WHERE OrderID=%s;
        """
        self._cursor.execute(update_query, (new_status.OrderStatus, order_id))
        self._db_conn.commit()


    def delete_order_by_id(self, order_id):
        delete_query = """
            DELETE from Oders
            WHERE OrderID=%s;
        """
        self._cursor.execute(delete_query, (order_id,))
        self._db_conn.commit()