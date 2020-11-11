## Polymorphism
'''Polymorphism means that  different types respond to the same function'''

class Person:

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def show_salary(self):
        print(f'{self.name} has a salary of: £{self.salary:,.2f}')

    def __str__(self):

        return(f'Person with name: {self.name}, aged: {self.age:d} ')

class Employee(Person):

    def __init__(self,name,age,salary):
        super().__init__(name,age)

        self._salary=salary

    @property
    def salary(self):
        return(self._salary)

    @salary.setter
    def salary(self,value):
        if value < 20_000:
            print(f'Minimum salary for {self.name} must be £20,000')
            raise ValueError('Minimum salary must be £20,000')

        self._salary=value

    def __str__(self):

        return(f'Employee with name: {self.name}, aged: {self.age:d} and with salary: £{self.salary:,.2f}')

    
    


person_1=Person('Julio',25)
print(person_1)

employee_1 = Employee(person_1.name,person_1.age,40_000)
print(employee_1)
    
employee_1.salary = 100_000
print(employee_1)
employee_1.salary=10_000
