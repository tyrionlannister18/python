rows = 5
for i in range(1,rows+1):
    print("*" *i)
    


#second approach
row=5
for i in range(0,row):
    for j in range(0,i+1):
        print("*",end=" ")
        print("\r")
    


...