# Inheritance:

# 1. Single Inheritance
class A:
    def displayA(self):
        print("Welcome to A")

class B(A):
    def displayB(self):
        print("Welcome to B")

obj=B()
obj.displayA()
obj.displayB()


# 2. Multi Level Inheritance
class A:
    def displayA(self):
        print("Welcome to A")

class B:
    def displayB(self):
        print("Welcome to B")

class C(B):
    def displayC(self):
        print("Welcome to C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()




# > Multiple Inheritance

class A:
    def displayA(self):
        print("Welcome to A")

class B:
    def displayB(self):
        print("Welcome to B")

class C(A,B):   # Class C inherits from A and B
    def displayC(self):
        print("Welcome to C")


obj = C()       # Create object of class C
obj.displayA()  # Inherited from A
obj.displayB()  # Inherited from B
obj.displayC()  # Defined in C
