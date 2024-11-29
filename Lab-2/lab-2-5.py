a= int(input("Enter the value a : "))
b= int(input("Enter the value b : "))
c= int(input("Enter the value c : "))

d = int((b**2)-(4*a*c))

if d==0 :
    r1  = int((-b)/(2*a))
    print(r1)
    
elif d>0 :
    r1 =int(((-b)+(d**(1/2))) /(2*a) )
    r2 = int(((-b)-(d**(1/2))) /(2*a))
    print(r1," and ",  r2 )

elif d<0 : 
    real_part = int((-b)/(2*a))    
    im_part = int(((-d)**(1/2))/(2*a))
    print(real_part, " and " , im_part)