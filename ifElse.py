# Determine if the specified item is in the list.
my_list=["Cat", "Dog", "ELephant", "Lion", "Buffalo"]
if "Cow" in my_list:
    print("yes, it is.")
else:
    print("Nope!")

#Example 0.2:
my_list1=["Cat", "Dog", "ELephant", "Lion", "Buffalo"]
if "ELephant" in my_list:
    print("yes, it is.")
else:
    print("Nope!")


#Example 0.3: 
a=int(input("Enter your age: "))
if (a>=18):
    print("You can vote!")
else:
    print("You cannot vote!")


#Example 0.4: if-elif-else statement
a=int(input("Enter your age: "))
if (a>=18):
    print("You can vote!")
elif (a>=16):
    print("You can drive!")
else:
    print("You cannot vote or drive!")
