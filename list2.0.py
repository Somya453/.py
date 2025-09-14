my_list=["Cat", "Dog", "ELephant", "Lion", "Buffalo"]

#Change the values 
# my_list=[ ]


#Print all the items in list, one by one:
for x in my_list:
    print(x)


#Append Item: we use append method() to add an item to the end of the list.
lists=["gogo", "pinku", "honey", "henry", "wow"]
lists.append("sara")
print(lists)

#Insert method(): to insert a new list item, without replacing any of the existing values, we can use the insert() method.
#It will not remove the value just replace it and takes that place.
lists.insert(2, "kiki")
print(lists)

#Extend List: used to append the list to the current lsit.
# The element will be added to the end of the list.
list1=["cars", "vehicles", "Vahan"]
list2=["BMW", "Toyota", "Mercedes"]
list1.extend(list2)
print(list1)

m=[10, 20, 30, 40, 50]
t=len(m)
for a in range(t):
    print(m[a])

# del()
# pop()
# clear()-->blanks full list
# remove()
# append()-->adds on value at the end
# insert()-->insert any value
# extends()-->extends or add a value
# Update()--> updates the full list
# count()
# max()
# min()


#Creating a list
num=[h for h in range(1, 51)]
print(num)

j=num.count(10)
print(j)

max=max(num)
print(max)

