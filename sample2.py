def maximum2(n):
    l=len(n)
    for i in range(l-1):
        for j in range(i+1,l):
            if n[i]<n[j]:
                temp=n[i]
                n[i]=n[j]
                n[j]=temp  
    for i in range(2):
        print(n[i])
limit = int(input("Enter the size of the list "))
n = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:limit]
maximum2(n)