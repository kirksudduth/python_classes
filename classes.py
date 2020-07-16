# Blueprint / machine / recipe / template for making instance objects
class Employee:
    # defining a method on a class
    # we don't execute this dunder method (double underscore)
    # Python does that for us
    # ^^self^^ is a keyword that references the instance
    # first param is ALWAYS ^^self^^ in class methods
    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def payEmployee(self):
        print(f'Yahhhh! Now {self.name} can pay rent')

    # string method that prints defined string when instance is initialized
    def __str__(self):
        return f"This is an employee named {self.name}"


# An instance is a combo of predictable/repeated properties with unique values
fred = Employee("Fred", "receptionist", "09/10/1999")
# fred's value is an object ** can use DOT NOTATION **
fred.name = "Fred"
print(fred.title)

linda = Employee("Linda", "boss", "01/02/1997")
print(linda.title)
linda.payEmployee()
print(fred)


class Company:

    def __init__(self, name, date, product):
        self.name = name
        self.date_founded = date
        self.product = product
        self.employees = []

    def addEmployees(self, employees):
        self.employees.extend(employees)

    def __str__(self):
        return f'{self.name} makes {self.product}!'


widget_co = Company("Widget Co", "07/16/2020", "the finest widgets")
print(widget_co)

widget_co.addEmployees([fred])
print(widget_co.employees)
