class Employee:
    def __init__(self,Name,Salary) -> None:
        self.Name=Name
        self.Salary=Salary

emp1=Employee('Prem',23000)
emp2=Employee('Sasi',65000)
emp3=Employee('Nalini',89000)
emp4=Employee('Preethi',36000)
emp5=Employee('Indhu',76000)

# Use  any sorting method to sort
Employee=[emp1,emp2,emp3,emp4,emp5]
for i in range(len(Employee)):
    minpos=i
    for j in range(i,len(Employee)):
        if Employee[j].Salary > Employee[minpos].Salary:
            minpos=j
    Employee[i],Employee[minpos]=Employee[minpos],Employee[i]


for i in Employee:
    print(i.Salary,i.Name)
