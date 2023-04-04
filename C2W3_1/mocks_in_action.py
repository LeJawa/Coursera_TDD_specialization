from unittest.mock import Mock
from unittest.mock import create_autospec

# Question 1

m1 = Mock()

# preconfigure m1 so it has a method called 'run' that returns 5

configuration = {"run.return_value": 5}
m1.configure_mock(**configuration)

# Question 2
# call m1.run() with 1, 3, 5, 7
# call m1.run () with 2, 4, 6
# What's the results?

# m1.run(X) always returns 5, no matter the input

# Question 3
# pass m1 to the dir() function.
# which attribute verifies how many times m1 is called?

# m1.mock_calls

# Question 4
# update m1.run() so it now returns [1, 2, 3]
# use return_value attribute for this

configuration = {"run.return_value": [1, 2, 3]}
m1.configure_mock(**configuration)

# Question 5
# Test that you re-configured m1 correctly. Call m1.run()

# Question 6
# Use dir(m1) to see the functionality of the mock object again
# call assert_called and assert_called_once
# What's the output? Keep notes of this

# AssertionError: Expected 'mock' to have been called.
# AssertionError: Expected 'mock' to have been called once. Called 0 times.

# Question 7

def function(a, b, c):
    return a + b + c  

m2 = Mock()
m2.side_effect = function

# Use unittest.mock to ensure that the mock object is called correctly
# I.e, the following should product an error
# >>> m1(1)
# >>> m1(5, 10)
# The following should NOT
# >>> m1(1, 2, 3)
# If stuck, read: https://docs.python.org/3/library/unittest.mock.html 
