# List: A List is a collection which is ordered and unchangeable. It is written in square brackets[].

list=["Apple", "banana", "pear", "mango"]
print(list)


#Change the Item Value:
list[2]="guava"
print(list)

#We can access list items by index number.
print(list[1])

#Negative Indexing: Indexing begins from the end but it starts form -1 and refers to the last element.
print(list[-2]) 

#List stores multiple items in a single variable and it is one of the 4 built-in data types in Python used to store collection of data.
#List allow duplicate values.
list=["eyes", "hair", "nose", "nail", "eyes"]
print(list)

#length func [len()]: used by the list to determine number of items in the list.
print(len(list))

#type() func: it defines type of a function
print(type(list))

#Range of idexex: specify a number by specifying where to start and where to end the range.
print(list[1:5])
print(list[:3])
print(list[1:])
print(list[-5:-2])


#Determine if the specified item is in the list.
my_list=["Cat", "Dog", "ELephant", "Lion", "Buffalo"]
if "Dog" in my_list:
    print("yes, it is.")
else:
    print("Nope!")


n=[13, 11, 20, 55, 'Heloo']
print(type(n))