l=[]
l1=[]
l2=[]
try:
    n=int(input("How many elements you want to enter into a list\n"))
    print("Enter your elements")
    for i in range(0,n):
        x=int(input())
        l.append(x)
    print("The given elements are ",l)
    for a in l:
        if l.count(a)>1:
            l1.append(a)
            if l1.count(a)>1:
                 l1.remove(a)
    for a in l:
        if l.count(a)==1:
            for c in l:
                if c not in l1 and c not in l2:
                    l2.append(c)
    print("The duplicate elements are ",l1)
    print("The unique elements are ",l2)
except ValueError as e:
    print(e)

