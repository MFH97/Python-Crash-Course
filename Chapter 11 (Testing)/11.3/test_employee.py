import unittest
from employee import Employee
"""
#Testcases for employee raise only!
"""

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee("fname", "lname", 30000)  # Start with realistic salary

    def test_give_default_raise(self):
        original_salary = self.emp1.annual_salary
        self.emp1.give_raise()  # Default raise of 5000
        self.assertEqual(self.emp1.annual_salary, original_salary + 5000)
        
        
    def test_give_custom_raise(self):
        original_salary = self.emp1.annual_salary
        custom_raise = 2000
        self.emp1.give_raise(custom_raise)
        self.assertEqual(self.emp1.annual_salary, original_salary + custom_raise)
    


if __name__ == '__main__':
    unittest.main()
