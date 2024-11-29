n= int(input("Enter the Number : "))
sum = 0
x = n
while(n):
    digit = n%10
    sum+=digit
    n = n//10
print(f"The sum of digits of {x} is {sum}")

