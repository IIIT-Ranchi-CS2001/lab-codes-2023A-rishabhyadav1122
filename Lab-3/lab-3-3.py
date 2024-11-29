n= int(input("Enter the Number : "))

li = [0,1]
i = 2
while(i<n):
    sum = li[-1]+li[-2]
    
    li.insert(len(li),sum)
    i+=1
# print(li)  

for i in li :
    print(i)