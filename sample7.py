
def breakdown(amt,denominations):
    x=denominations.keys() 
    for i in x:
        if(amt%i==0):
            dict[i]=amt//i
            denominations[i] -= amt//i
            return dict
        else:
            if(amt//i==0):
                continue
            else:
                dict[i]=amt//i
                denominations[i] -= amt//i
                amt=amt%i
    return dict
amt=int(input("enter amount"))
dict={}
denominations = {2000:10,500:10,100:20,50:0,20:10,10:5,5:10,2:10,1:10}   
result=breakdown(amt,denominations)
print(result)
print(denominations)
        
