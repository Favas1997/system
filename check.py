a=[1,3,4,56,6]
c=[]
n=int(input("enter running"))
b=a.copy()
for i in range(n):
    large=0
    for i in b:
        if i>large:
            large=i
    c.append(large)
    b.remove(large)
print(c)
print(a)