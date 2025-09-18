#Overloading
class Student:
    def displayinfo(self,name=' '):
        print("Good Morning "+ name)

obj=Student()
obj.displayinfo()
obj.displayinfo('Children')