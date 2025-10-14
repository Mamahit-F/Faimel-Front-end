class Employee:
    def Name(self):
        print("")
        print("")
        print("Name   : Semi Taju")

    def Age(self):
        print("Age    : 30")
    
    def Show(self):
        return 

class PermanentEmployee(Employee):
    def Name(self):
        print("Name   : Edwin Padu")

    def Age(self):
        print("Age    : 26")
    
    def Show(self):
        print("Salary : Rp.3000")


class ContractEmployee(Employee):
    def Name(self):
        print("Name   : Reza Haeres")

    def Age(self):
        print("Age    : 35")
    
    def Show(self):
        print("HourlyPay : Rp.5000")
        print("")
        print("")


obj_Employee = Employee()
obj_PermanentEmployee = PermanentEmployee()
obj_ContractEmployee = ContractEmployee()

obj_Employee.Name()
obj_Employee.Age()
obj_Employee.Show()

obj_PermanentEmployee.Name()
obj_PermanentEmployee.Age()
obj_PermanentEmployee.Show()

obj_ContractEmployee.Name()
obj_ContractEmployee.Age()
obj_ContractEmployee.Show()