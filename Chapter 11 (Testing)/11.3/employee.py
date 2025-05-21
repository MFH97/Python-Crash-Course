class Employee():

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_salary=5000):

        """Give raise to employee. Default is $5000."""
        self.annual_salary += raise_salary 
        return self.annual_salary
       
    def get_name(self):

        #self.first_name = input("First name: ")
        #self.last_name = input("Last name: ")
        print(self.first_name + " " + self.last_name)

#emp object
emp1 = Employee( "Dick",'Lee',10000)
emp2 = Employee( "fname",'lname',0)
#testing
emp1.get_name()
print( '$' + str(emp1.give_raise(333)))

"""
emp2.get_name()
emp2.give_raise()
"""