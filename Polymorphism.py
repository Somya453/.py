#Polymorphism:

# 1. Overloading
class Student:
    def displayinfo(self,name=' '):
        print("Good Morning "+ name)

obj=Student()
obj.displayinfo()
obj.displayinfo('Children')


# 2. Overriding the function
class Student:
    def displayinfo(self,name=' '):
        print("Good Morning "+ name)

class Stud:
    def displayinfo(self):
        print("Heyyyy")

# obj=Student()
obj=Stud()
obj.displayinfo()
# obj.displayinfo('Children')

#Example:
class Area:
    def find_area(self, x=None, y=None):
        
    if x!=None and y!=None:
        print(x*y)

    elif x!=None:
        print(x*x)
    
    else:
        print("NA")

obj1=Area()
obj1.find_area()
obj1.find_area(20)
obj1.find_area(20, 30)