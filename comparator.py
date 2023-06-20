from functools import cmp_to_key
class Employee:
    def __init__(self,Name,Salary):
        self.Name=Name
        self.Salary=Salary


    def comparator(a,b):
        if a.Salary > b.Salary:
            return -1
        if a.Salary<b.Salary:
            return 1
        if a.Name<b.Name:
            return -1
        if a.Name>b.Name:
            return 1
        return 0

emp1=Employee('Prem',23000)
emp2=Employee('Sasi',30000)
emp3=Employee('Nalini',40000)
emp4=Employee('Preethi',27000)
emp5=Employee('Chandru',36000)

data=[emp1,emp2,emp3,emp4,emp5]
data=sorted(data,key=cmp_to_key(Employee.comparator))
for i in data:
    print(i.Name,i.Salary)
