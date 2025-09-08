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


