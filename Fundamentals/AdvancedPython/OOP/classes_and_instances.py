# Python Object Oriented Programming

class Employee:
    #creating a class variable
    raise_amt = 2
    employees = 0

    def __init__(self,first_name, last_name, salary) :
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name+'.'+last_name+'@gmail.com'
        self.fullname = first_name + " " + last_name

        Employee.employees += 1
    
    def __str__(self):
        return f'{self.fullname} -> {self.email}'

    def printFullName(self):
        print(self.first_name +" "+self.last_name)
    
    def hikeSalary(self):
        self.salary = self.salary + (self.raise_amt*self.salary)/100.0

    #Classmethods
    @classmethod
    def set_raise_percent(cls, amount): #cls takes class, cant use cls as it is reserved
        cls.raise_amt = amount

    # Dunder method -> basically pre defined special methods for every object type (they can be modified)
    def __repr__(self):
        return f'Employee: {self.fullname} , {self.salary}'
     
    # creating a hypothetical add method that is gonna take 2 employees and add their salaries
    def __add__(self,other):
        return self.salary + other.salary

    #Getter and setter method alternatives -> Property decorator
    

#Inheritence
class Developer(Employee): # () is the alternative for extends
    
    def __init__(self, first_name, last_name, salary, programming_language):
        super().__init__(first_name, last_name, salary)
        self.programming_language = programming_language

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def addEmployee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def removeEmployee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmployees(self):
        print(self.first_name + " manages : ")
        for emp in self.employees:
            print(emp.fullname)

# -------------------------------------------------------------------------------------------------------------------------------------------- #

# Creating instances of the class
e1 = Employee("Rohan","Dey",95000)
e2 = Employee("Hideyoshi","Nagachika",59000)

print(f'{e1.first_name} earns {e1.salary}')
print(f'{e2.first_name} earns {e2.salary}')
# e1.printFullName()
# e2.printFullName()
Employee.set_raise_percent(2.5)
e1.hikeSalary()
e2.hikeSalary()
print(f'{e1.first_name} earns {e1.salary}')
print(f'{e2.first_name} earns {e2.salary}')
print(Employee.employees)
devin = Developer("Devin","AI",1000000,'python')
print(f'{devin.first_name} earns {devin.salary} and codes in {devin.programming_language}')

m1 = Manager('John','Doe',12000, [devin,e1,e2])
m1.printEmployees()
print(e1+e2)