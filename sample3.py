def maximum2(n,m):
    result=[]
    a=n.copy()
    for i in range(m):
        large=0
        for i in a:
            if i>large:
                large=i
        result.append(large)
        a.remove(large)
    return result
limit = int(input("Enter the size of the list "))
m=int(input("enter the largest numbers required"))
n= list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:limit]
maximum2(n,m)