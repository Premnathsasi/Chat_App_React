class car:
    def __init__(self,color,speed,time,tyre):
        self.color=color
        self.speed=speed
        self.time=time
        self.tyre=tyre

    def cal_speed(self):
        self.print_attri()
        print(self.speed*self.time)
    def print_attri(self):
        print(self.color)
        
        print(self.tyre)
        print(self.speed)
        print(self.time)

obj1=car('Black',120,3,10)
obj1.cal_speed()

print(id(obj1))

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print(self.name,self.roll_no)
s1=Student('John',2)
s1.display()

class Triangle:
    side1=0
    side2=0
    side3=0
    def __init__(self,side1,side2,side3) -> None:
        self.side1=side1
        self.side2=side2
        self.side3=side3

    def cal_area(self):
        print((self.side1+self.side2+self.side3)/2)
    
    def cal_perimeter(self):
        self.peri=self.side1+self.side2+self.side3
        print(float(self.peri))

tri1=Triangle(3,4,5)
tri1.cal_area()
tri1.cal_perimeter()

class Employee:
    def __init__(self,name,year_of_joining,address) -> None:
        self.name=name
        self.year_of_joining=year_of_joining
        self.address=address

    def print_details(self):
        print(self.name, self.year_of_joining,self.address)
emp1=Employee('Robert',1994,'64c-Wallstreet')
emp2=Employee('Sam',2000,'68d-Wallstreet')
emp3=Employee('John',1998,'70v-Wallstreet')

emp1.print_details()
emp2.print_details()
emp3.print_details()        

class Employee:
    def __init__(self) -> None:
        salary=0
        hours=0
    
    def getinfo(self,salary,hours):
        self.salary=salary
        self.hours=hours

    def Addsal(self):
        if self.salary<500:
            self.salary=self.salary+10
        return self.salary
    
    def Addwork(self):
        if self.hours>6:
            self.salary=self.salary+5
        return self.salary
    def print_finalsal(self):
        print('Final salary is:',self.salary)

salary=int(input('Enter salary:'))
hours=int(input('Enter Hours:'))

emp1=Employee()
emp1.getinfo(salary,hours)
emp1.Addsal()
emp1.Addwork()
emp1.print_finalsal()

class count_objects:
    count=0

    def __init__(self) -> None:
        count_objects.count+=1

obj1=count_objects()
obj2=count_objects()
obj3=count_objects()

print(count_objects.count)


class PARENT:
    def parent_method(self):
        print('This is parent class')

class CHILD(PARENT):
    def child_method(self):
        print('This is child class')

        
obj1=PARENT()
obj2=CHILD()
obj1.parent_method()
obj2.child_method()
obj2.parent_method()

#Inheritance
class Member:
    def __init__(self,Name,Age,Phone_no,Address,Salary) -> None:
        self.Name=Name
        self.Age=Age
        self.Phone_no=Phone_no
        self.Address=Address
        self.Salary=Salary

    def printSalary(self):
        print(self.Salary)

class Employee(Member):
    def __init__(self, Name, Age, Phone_no, Address, Salary,specialization) -> None:
        super().__init__(Name, Age, Phone_no, Address, Salary)
        self.specialization=specialization
        print(self.Name,self.Age,self.Phone_no, self.Address, self.Salary,self.specialization)

class Manager(Member):
    def __init__(self, Name, Age, Phone_no, Address, Salary,Department) -> None:
        super().__init__(Name, Age, Phone_no, Address, Salary)
        self.Department=Department
        print(self.Name,self.Age,self.Phone_no, self.Address, self.Salary,self.Department)


emp1=Employee('Premnath',24,7010445887,'Ranipet',40000,'commerce')
mng1=Manager('Sasi',55,9843177459,'Ranipet',70000,'Adminstraion')

emp1.printSalary()
mng1.printSalary()


class Shape:
    def printshape(self):
        print("This is shape")

class Rectangle(Shape):
    def printrec(self):
        print("This is rectangular shape")

class Circle(Shape):
    def printcir(self):
        print("This is circular shape")
class Square(Rectangle):
    def printsq(self):
        print("Square is a rectangle")

obj=Square()
obj.printshape()
obj.printrec()


