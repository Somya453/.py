#Stack is a linear data structure (Lifo and Filo)
w=[]
while True:
    c=int(input('''
    1.Push
    2.Pop
    3.Peek
    4.Display
    5.Exit
    '''))

    if c==1:
        k=input('Enter value:');
        w.append(k)
        print(w)

    elif c==2:
        if len(w)==0:
            print('Empty Stack')
        else:
            p=w.pop()
            print(p)
            print(w)

    elif c==3:
        if len(w)==0:
            print('Empty Stack')
        else:
            print("Last Stack Value", w[-1])

    elif c==4:
        print("Display Stack:", w)

    elif c==5:
        break;

    else:
        print('Invalid Operation')
        

