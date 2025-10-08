import unittest

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

class unitTesting(unittest.TestCase):

    #Add Testing

    #any function doing testing must begin with test
    def test_add_positive_test(self):
        self.assertEqual(add(5, 3), 8)
    
    def test_add_negative_test(self):
        self.assertEqual(add(-3,-5),-8)
    
    #Subract Testing

    def test_subract_positive_test(self):
        self.assertEqual(subtract(5, 3), 2)
    
    def test_subract_negative_test(self):
        self.assertEqual(subtract(-3,-5),2)

    #Multiply Testing

    def test_multiply_positive_test(self):
        self.assertEqual(multiply(5,1),5)
    
    def test_multiply_negative_test(self):
        self.assertEqual(multiply(-5,-5),25)
    
    #Divide Testing

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_fractional_result(self):
        self.assertEqual(divide(7, 2), 3.5)

if __name__ == "__main__":
    unittest.main()

