t=(20, 10, 30, 70, 60, 80, 10)
a=t[2]
print(a)
print(type(a))
print(type(t))

l=len(t) 
print(l)
for a in range(l):
    print(t[a])

max=max(t)
print(max)

min=min(t)
print(min)

count=t.count(10)
print(count)

i=t.index(80)
print(i)

sum=sum(t)
print(sum)