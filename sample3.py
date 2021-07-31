def maximum2(n,m):
    l=len(n)
    for i in range(l-1):
        for j in range(i+1,l):
            if n[i]<n[j]:
                temp=n[i]
                n[i]=n[j]
                n[j]=temp  
    for i in range(m):
        print(n[i])
limit = int(input("Enter the size of the list "))
m=int(input("enter the largest numbers required"))
n = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:limit]
maximum2(n,m)