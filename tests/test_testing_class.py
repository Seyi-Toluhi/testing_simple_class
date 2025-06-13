from lib.testing_class import *

"""
test that class initiates an object with 
value_first and value_second attributes
"""
def test_high_value_initiation():
    high_value = HighValue(1, 2)
    actual = high_value.value_first
    assert actual 
"""
test that when we call get_highest method 
value_first is returned if its the highest value
"""

def test_get_value_first_if_highest():
    high_value = HighValue(10,8)
    actual = high_value.get_highest()
    assert actual == 'First value is higher'

"""
test that when we call get_highest method 
value_second is returned if its the highest value
"""
def test_get_value_second_if_highest():
    high_value = HighValue(3, 520)
    actual = high_value.get_highest()
    assert actual == 'Second value is higher'

"""
test that when we call get_highest method 
"values are equal" is returned if equal
"""

def test_get_value_if_values_equal():
    high_value = HighValue(3, 3)
    actual = high_value.get_highest()
    assert actual == 'Values are equal'

"""
test that when we call add method 
value_first is returned if we increment it to make it higher
"""

def test_add_method_returns_first_value_when_incremented():
    high_value = HighValue(3, 3)
    high_value.add(2,'first')
    actual = high_value.get_highest()
    assert actual == 'First value is higher'

"""
test that when we call add method 
value_second is returned if we increment it to make it higher
"""

def test_add_method_returns_second_value_when_incremented():
    high_value = HighValue(3, 3)
    high_value.add(5,'second')
    actual = high_value.get_highest()
    assert actual == 'Second value is higher'
