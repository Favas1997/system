def maximum(n):
    l=len(n)
    for i in range(l-1):
        for j in range(i+1,l):
            if n[i]>n[j]:
                max=n[i]
            else:
                max=n[j]
    print("the largest number is " + str(max))
limit = int(input("Enter the size of the list "))
n = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:limit]
maximum(n)


