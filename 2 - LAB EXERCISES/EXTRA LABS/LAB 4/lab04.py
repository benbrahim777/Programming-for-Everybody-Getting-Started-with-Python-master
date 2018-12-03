"""
A test script to test the module funcs.py

<YOUR NAME HERE>
<DATE HERE>
"""

import cornell      # For assert_equals and assert_true
import funcs        # This is what we are testing

# TEST PROCEDURE
def test_asserts():
    """
    This is a simple test procedure to help you understand how assert works
    """
    print('Testing the cornell asserts')
    cornell.assert_equals('b c', 'ab cd'[1:4])
    #cornell.assert_equals('b c', 'ab cd'[1:3])     # UNCOMMENT ONLY WHEN DIRECTED
    
    cornell.assert_true(3 < 4)
    cornell.assert_equals(3, 1+2)
    
    cornell.assert_equals(3.0, 1.0+2.0)
    cornell.assert_floats_equal(6.3, 3.1+3.2)
    #cornell.assert_equals(6.3, 3.1+3.2)            # UNCOMMENT ONLY WHEN DIRECTED


# SCRIPT CODE (Call Test Procedures here)
test_asserts()
print('Module funcs is working correctly')