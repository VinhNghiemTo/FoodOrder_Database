import json
 

# By using the parameter flask_test_client, we automatically get access to a "fake" version
#   of our webservice application to test our api. This is provided by the pytest fixture in conftest.py
#   (note the parameter name matches the name of the fixture function).
def test_posting_a_task(flask_test_client):
 
    # Simulate a post request that sends json data
    request = flask_test_client.post('api/v1/tasks/', json={'description': 'first order'})
 
    # Make sure we got a status code of 200
    assert request.status_code == 200
 
    # The body of the response is JSON, so we turn it from a string into a JSON
    #   object. The json object can be treated similarly to a dictionary or list
    #   based on the format of the JSON content.
    data = json.loads(request.data.decode())
 
    assert data['status'] == "success"
    assert data['id'] == 1
 
    request = flask_test_client.post('api/v1/tasks/', json={'description': 'second order'})
 
    # Make sure we got a status code of 200
    assert request.status_code == 200
 
    # The body of the response is JSON, so we turn it from a string into a JSON
    # object.
    data = json.loads(request.data.decode())
 
    assert data['id'] == 2
 

def test_get_all_tasks(flask_test_client):
   
    # Here is how to use the test client to simulate a GET request
    request = flask_test_client.get('/api/v1/tasks/')
 
    # The body of the response is JSON, so we turn it from a string into a JSON
    # object.
    data = json.loads(request.data.decode())
 
    # Make sure we got a status code of 200
    assert request.status_code == 200
 
    # Verify data
    assert len(data['orders']) == 2
 
    # When getting all the tasks, we cannot rely on the ordering because I did
    #   not enforce an ordering on the SQL query. Always be careful with
    #   assumptions about order unless you have explicity
    #   ensured that the content will be ordered
    for task in data['orders']:
        if order['id'] == 1:
            assert order['description'] == 'first order'
        elif order['id'] == 2:
            assert task['description'] == 'second order'
        else:
            # We should not get here as there are only two items inserted
            raise Exception("Unknown order found in database!")
 

def test_get_task_by_id(flask_test_client):
   
    # Here is how to use the test client to simulate a GET request
    request = flask_test_client.get('/api/v1/tasks/1/')
 
    # The body of the response is JSON, so we turn it from a string into a JSON
    # object.
    data = json.loads(request.data.decode())
 
    # Make sure we got a status code of 200
    assert request.status_code == 200
 
    assert len(data['orders']) == 1
 
    # Get the first item from the list of tasks (which should only be task id 1)
    order = data['orders'][0]
 
    # Check the id and description
    assert order['id'] == 1
    assert order['description'] == 'first order'
 

def test_get_task_by_description_search(flask_test_client):
 
    # Here is how to use the test client to simulate a GET request with a query string
    request = flask_test_client.get('/api/v1/tasks/?search=second')
 
    # The body of the response is JSON, so we turn it from a string into a JSON
    # object.
    data = json.loads(request.data.decode())
 
    # Make sure we got a status code of 200
    assert request.status_code == 200
 
    # Verify data
    assert len(data['orders']) == 1
 
    # Since I know this test should only return one value I can request
    #   the task from the list of tasks via its index
    order = data['orders'][0]
 
    assert order['id'] == 2
    assert order['description'] == 'second order'
 

def test_update_task_by_id(flask_test_client):
   
    # Add a new task to the list
    request = flask_test_client.post('/api/v1/tasks/', json={'description': 'order to be updated'})
    assert request.status_code == 200
   
    data = json.loads(request.data.decode())
    order_id = data['id']
 
    # Here is how to use the test client to simulate a PUT request
    request = flask_test_client.put(f'/api/v1/tasks/{order_id}/', json={'description': 'updated via test'})
   
    # Make sure we got a status code of 200
    assert request.status_code == 200
 
    data = json.loads(request.data.decode())
    assert order_id == data['id']
 
    request = flask_test_client.get(f'/api/v1/tasks/{order_id}/')
    data = json.loads(request.data.decode())
 
    order = data['orders'][0]
    assert order['id'] == order_id
    assert order['description'] == 'updated via test'
 