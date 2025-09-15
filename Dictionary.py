#Dictionary-->Key value pairs
#Unordered Data Type
#Mutable

d={
    'name':'Python',
    'Fees' : 2500,
    'duration' : '2 Months'
}
print(type(d))
f=d['Fees']
print(f)

for a in d:
    print(d[a])

n=d.get('name')
print(n)

for a in d.items():
    print(a)


a=d.pop('Fees')
print(a)

dict=dict(name='Kajol', book='Twisting tales', price=550)
print(dict)

