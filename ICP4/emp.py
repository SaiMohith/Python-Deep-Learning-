class Employee:
    empCount = 0
    wholesalary = 0

    def __init__(self, n, s, f, d):
        self.name = n
        self.salary = s
        self.age = f
        self.dep = d
        Employee.empCount += 1
        Employee.wholesalary = Employee.wholesalary + s

    def displayEmpDetails(self):
        print("Employee Name : ", self.name, ", Salary: ", self.salary, ", No of Family Members: ", self.age, ", Department: ", self.dep)

    def avgsal(totalsal,empCount):
        avgsalary = totalsal/empCount
        return avgsalary

    def withbonus(self, bonus):
        self.salary += bonus
        print(self.salary)


class Fullemp(Employee):
    def init(self,fname,sal,ffam, fdep):
        Employee.__init__(self,fname,sal,ffam,fdep)

emp1=Employee("Vamsi Krishna Challa",45000,4,"CSE")
emp2=Employee("Mohith Chagam Reddy",20000,3,"EEE")
emp3=Employee("Sravani Konjula",23000,2,"IT")
emp1.displayEmpDetails()
emp2.displayEmpDetails()
emp3.displayEmpDetails()
print("The Total number of Employees are: %d" % Employee.empCount)
print("The average salary", Employee.avgsal(Employee.wholesalary, Employee.empCount))

bonus = int(input("Enter the amount you want add as bonus:"))
emp1.withbonus(bonus)
emp2.withbonus(bonus)
emp3.withbonus(bonus)