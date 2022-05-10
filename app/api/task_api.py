"""
task_api.py

Routes for the API and logic for managing Tasks.
"""

from flask import g, request, jsonify, Blueprint

from models.task import Customer, CustomerDB, Order, OrderDB, OrderItem, OrderItemDB, Address, AddressDB

# Establish the blueprint to link it to the flask app file (main_app.py)
#   Need to do this before you create your routes
task_api_blueprint = Blueprint("task_api_blueprint", __name__)


# Define routes for the API
#   Note that we can stack the decorators to associate similar routes to the same function.
#   In the case below we can optionally add the id number for a task to the end of the url
#   so we can retrieve a specific task or the entire list of tasks as a JSON object
@task_api_blueprint.route('/api/v1/orders/', defaults={'customerID':None}, methods=["GET"])
def get_customers(customerID):
    """
    get_tasks can take urls in a variety of forms:
        * /api/v1/task/ - get all tasks
        * /api/v1/task/1 - get the task with id 1 (or any other valid id)
        * /api/v1/task/?search="eggs" - find all tasks with the string "eggs" anywhere in the description
            * The ? means we have a query string which is essentially a list of key, value pairs
                where the ? indicates the start of the query string parameters and the pairs are separated
                by ampersands like so:
                ?id=10&name=Sarah&job=developer
            * The query string is optional 
    """

    # To access a query string, we need to get the arguments from our web request object
    args = request.args
    
    # setup the TaskDB object with the mysql connection and cursor objects
    customerdb = CustomerDB(g.mysql_db, g.mysql_cursor)

    result = None
    
    # If an ID for the task is not supplied then we are either returning all
    #   tasks or any tasks that match the search query string.
    if customerID is None:
        # Logic to find all or multiple tasks

        # Since the args for the query string are in the form of a dictionary, we can
        #   simply check if the key is in the dictionary. If not, the web request simply
        #   did not supply this information.
        if not 'search' in args:
            result = customerdb.select_all_tasks()
        # All tasks matching the query string "search"
        else:
            result = customerdb.select_all_tasks_by_description(args['search'])
    
    else:
        # Logic to request a specific task
        # We get a specific tasks based on the provided task ID
        result = customerdb.select_task_by_id(customerID)

    # Sending a response of JSON including a human readable status message,
    #   list of the tasks found, and a HTTP status code (200 OK).
    return jsonify({"status": "success", "tasks": result}), 200


@task_api_blueprint.route('/api/v1/customers/', methods=["POST"])
def add_customer():
    customerdb = CustomerDB(g.mysql_db, g.mysql_cursor)
        
    customer = Customer(request.json['name'])
    result = customerdb.add_customer()
    
    return jsonify({"status": "success", "customers": result}), 200


"""@task_api_blueprint.route('/api/v1/tasks/<int:task_id>/', methods=["PUT"])
def update_task(task_id):
    taskdb = TaskDB(g.mysql_db, g.mysql_cursor)

    task = Task(request.json['description'])
    taskdb.update_task(task_id, task)
    
    return jsonify({"status": "success", "id": task_id}), 200 """


@task_api_blueprint.route('/api/v1/tasks/<int:task_id>/', methods=["DELETE"])
def delete_customer(customerID):
    customerdb = CustomerDB(g.mysql_db, g.mysql_cursor)

    customerdb.delete_task_by_id(customerID)
        
    return jsonify({"status": "success", "id": customerID}), 200
