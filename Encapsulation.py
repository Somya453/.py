class Student:
    def __init__(self):
        self.__name = " "   # private variable

    def getname(self):
        return self.__name
    
    def setname(self, name):
        self.__name = name


obj = Student()
obj.setname("Testing")
name = obj.getname()
print(name)


#Encapsulation hides variables
class Stud:
    __name="Tara"

    def __init__(self):
        print(self.__name)
        self. __displayinfo()

    def __displayinfo(self):
        print("Private Info") ##Can't access directly!

obj=Stud()
