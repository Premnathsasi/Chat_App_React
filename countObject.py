class class_count:
    count=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        class_count.count+=1

    def print_details(self):
        print(self.name ,self.age)

    def print_count(self):
        print('Total Number of Count' , class_count.count)

newCount = class_count('Premnath',24)
newCount2 = class_count('Sasi',56)

newCount.print_details()
newCount2.print_details()
newCount2.print_count()
