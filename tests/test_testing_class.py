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
"""
test that when we call get_highest method 
value_second is returned if its the highest value
"""
"""
test that when we call get_highest method 
"values are equal" is returned if equal
"""
"""
test that when we call add method 
value_first is returned if we increment it to make it higher
"""
"""
test that when we call add method 
value_second is returned if we increment it to make it higher
"""