import json
d={
    'name': 'Lotus',
    'age' : 20
}

f=json.dumps(d)
print(type(f))
print(f)


d='{"name": "Lotus", "age" : 20, "gender" : "Female"}'
    
l=json.loads(d)
print(type(l))
print(l)


for a in l:
    print(a, l[a])

#Example 
file=open("posts.json", "r") #read the file
x=file.read()
finaalData=json.loads(x)
print(finaalData)