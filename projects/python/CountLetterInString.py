
str1 = ''' He said, "What's there?" '''
#or
str2 = ' He said, "What\'s there?" '
#or
str3 = " He said, \"What's there?\" "
print(str1)
print(str2)
print(str3)


#1.
#count total letters in string
x = 'Companion'
count = 0
for i in x:
    count+=1
print(f"Number of Letter in {x} is {count}")
    


#2.
#count the given particular letter in string
st = "Competition"
count = 0
for i in st:
    if i == "t":
        count += 1

print(f"Count of Letter t in {st} is {count}")



#or
#count the given particular letter in string by taking user input
x = input("Your string Here: " )
y = input("A letter to be counted in that string type that letter here: " )
count = 0
for i in x:
    if i == y:
        count+=1

print(f"Count of Letter {y} in {x} is {count}")











str3 = "A Warm $%#!!! Congratulations 0099999 to you"
py = [a,b,c,d,e,f,g,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
letter = 0
number = 0
special = 0
for i in str3:
    if i in py:
        letter+=1
       
    elif i in range(0,10):
        number+=1
        
    else:
        special+=1
       

print(f" letters in {str3} is {letter}")
print(f"Numbers in {str3} is {number}")
print(f"Specials in {str3} is {special}")
