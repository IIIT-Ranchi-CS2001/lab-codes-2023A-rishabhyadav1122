s = input("Enter the String : ")
char = input("Enter the character whose count you want to print : ")
count = 0
for i in s:
    if i == char:
        count+=1
print(count)        