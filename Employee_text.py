class Employee():

    def __init__(self,name):
    
        self.name=name

    def set_salary(self,salary):

        self.salary = salary

    def future_salary(self,years):

        future_salary=(1.03**years)*self.salary

        print(f'{self.name} Salary in {years} years: £{future_salary:,.2f} ')

        return future_salary


Jill = Employee('Jill')
Jill.set_salary(30_000)
Jill.future_salary(2)
Jill.future_salary(5)


Joe = Employee('Joe')
Joe.set_salary(28_000)
Joe.future_salary(2)
Joe.future_salary(5)





