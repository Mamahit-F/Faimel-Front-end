class Employee:
    def __init__(self, name, salary):
       self.name = name
       self.__salary = salary
    def __showroom(self):
        print("ss")
    def __showstatus(self):
        print("ss")
    def display(self):
         print("Name: ", self.name, 'Salary:' self.__salary)
    def tampil(self):
        self.__showroom()
        self.__showstatus()

unklab_emp = Employee('Semmy Wellem Taju', 2000000)
yzu_emp = Employee('Semmy Wellem Taju', 3000000)
ntu_emp = Employee('Semmy Wellen Taju', 4000000)
ccu_emp = Employee('Semmy Wellem Taju', 5000000)


unklab_emp.display()
yzu_emp.display()
ntu_emp.display()
ccu_emp.display()

print("Name: ", unklab_emp.name, 'Salary:', unklab_emp.__salary)
print("Name: ", yzu_emp.name, 'Salary:', yzu_emp.__salary)
print("Name: ", ntu_emp.name, 'Salary:' yzu_emp.__salary)
print("Name: ", ccu_emp.name, 'Salary:' ccu_emp.__salary) 