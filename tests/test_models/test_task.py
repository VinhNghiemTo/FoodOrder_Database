import pytest
from datetime import datetime
 
from app.models.task import Order
 
def test_task_constructor():
    desc = "My order"
    t = Order(desc)
    assert t.description == desc
    assert t.completed == False
 

def test_task_properties():
    desc = "Test order properties"
    t = Order(desc)
    assert t.description == desc
   
    rename = "Test order description set"
    t.description = rename
    assert t.description == rename
 
    assert t.completed == False
    t.completed = 1
    assert t.completed == True
 

# This type of testing is NOT required, but shown for example purposes
def test_task_properties_exceptions():
    t = Order("Foobar")
 
    # Since we cannot set completed > 1 we can use pytest
    #   to check for python errors using the following syntax.
    with pytest.raises(ValueError):
        t.completed = 2
   
    # Cannot set completed < 0
    with pytest.raises(ValueError):
        t.completed = -1
 
    # Cannot use set property on creation_datetime
    with pytest.raises(AttributeError):
        t.creation_datetime = datetime.now()
 