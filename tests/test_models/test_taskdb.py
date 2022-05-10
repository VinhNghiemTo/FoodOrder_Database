from app.models.task import Order, OrderDB
 
# By using the parameter db_test_client, we automatically get access to our test
#   database provided by the pytest fixture in conftest.py
#   (note the parameter name matches the name of the fixture function).
def test_task_insert(db_test_client):
    # The test fixture only setups the
    conn, cursor = db_test_client
    orderdb = OrderDB(conn, cursor)
 
    orderdb.insert_task(Order("Hi there"))
   
    result = orderdb.select_task_by_id(1)[0]
    assert result['description'] == "Hi there"
    conn.commit()
 

def test_task_delete(db_test_client):
    conn, cursor = db_test_client
    orderdb = OrderDB(conn, cursor)
   
    orderdb.insert_task(Order("Delete Me!"))
 
    result = orderdb.select_task_by_id(2)[0]
    assert result['description'] == "Delete Me!"
 
    orderdb.delete_task_by_id(2)
    result = orderdb.select_task_by_id(2)
    assert len(result) == 0
    conn.commit()