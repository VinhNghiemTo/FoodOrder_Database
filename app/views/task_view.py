from encodings import search_function
from flask import Blueprint, request, redirect
from flask import render_template, g, Blueprint
from api.task_api import Customer, CustomerDB

task_list_blueprint = Blueprint('task_list_blueprint', __name__)

@task_list_blueprint.route('/', methods=["GET", "POST"])
def index():
    database = CustomerDB(g.mysql_db, g.mysql_cursor)

    if request.method == "POST":
        task_ids = request.form.getlist("task_item")
        for id in task_ids:
            database.add_customer()

    return render_template('index.html', todo_list=database.select_all_customers())    

#eventually will render a list of all our active customers
@task_list_blueprint.route('/')
def active_customers():
   return render_template("task-entry.html")

#renders our webpage for entering new customers
@task_list_blueprint.route('/new-customer')
def new_customer():
    return render_template('add-customer.html')

#adds our new customer to the database
@task_list_blueprint.route('/add-customer', methods=["POST"])
def add_customer():
    name = request.form.get("name")
    email = request.form.get("email")
    orderID = request.form.get("orderID")
    
    newCustomer = Customer(name= name, orderID = orderID, email=email)
    database = CustomerDB(g.mysql_db, g.mysql_cursor)

    database.add_customer(newCustomer)

    return redirect('/')

@task_list_blueprint.route('/delete-customer')
def delete_customer():
    return render_template('delete-customer.html')

@task_list_blueprint.route('/delete-customer', methods=["DELETE"])
def delete_customer_by_ID():
    orderID = request.form.get("orderID")
    
    database = CustomerDB(g.mysql_db, g.mysql_cursor)

    ID_to_delete = database.select_all_customers_by_orderID(orderID=orderID)

    database.delete_customer(ID_to_delete)

    return redirect('/')