#Composite Design Pattern

from abc import ABC, abstractmethod

class IDepartment(ABC):
    @abstractmethod
    def __init__(self, employees):
        '''implement in child classes'''

    @abstractmethod
    def printDepartment(self):
        '''Implement in chil class'''

#leaf node
class Accounting(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def printDepartment(self):
        print(f'Accounting department: {self.employees}')

#leaf node
class Development(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def printDepartment(self):
        print(f'Development department: {self.employees}')

#non leaf node   
class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.baseEmployees = employees
        self.sub_depts = []

    def add(self,dept):
        self.sub_depts.append(dept)
        self.employees+=dept.employees
    
    def printDepartment(self):
        print("Parent Department")
        print(f'Parent department base employees {self.baseEmployees}')

        for dept in  self.sub_depts:
            dept.printDepartment()
        print(f'Total number of employees: {self.employees}')



dept1 = Accounting(200)
dept2 = Development(177)
ParentDept = ParentDepartment(30)

ParentDept.add(dept1)
ParentDept.add(dept2)

ParentDept.printDepartment()

