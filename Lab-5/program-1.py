import math
p1  = (1,2,3)
p2 =  (5,6,7)

for i, j in zip(p1,p2):
    ans = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
    
print(f"Euclidean distance is : {ans}") 

    
