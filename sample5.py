
def ffindstring(fname,s):
    flag = 0
    for line in fname:
        if s in line:	
            flag = 1
            break
    if flag != 0:
        return True	
    fname.close()

fname = open("any.txt", "r")
s = 'any'
ffindstring(fname,s)
