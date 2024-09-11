a = int(input("Enter the first side : "))
b = int(input("Enter the Second side : "))
c = int(input("Enter the third side : "))

print("The perimeter of triangle is : " , a+b+c)

s = (a+b+c)/2

area   = (s*(s-a)*(s-b)*(s-c))**0.5

print("Area of triangle " , area)



