class DemoClass:
    a=10

    def sum(self):
        print(17+9)

demoObject=DemoClass()
print(demoObject.a)
# Calling a function
demoObject.sum()

#Methods and Constructor:

class DemoClass:
    a = 10

    def __init__(self):
        print("To be proud") #Constructor

#Method:

    def showValue(self):
        print(self.a)

    def showvalue(self, a, b):
        print("Constructor", a+b)

obj=DemoClass()
obj.showvalue(20,20)