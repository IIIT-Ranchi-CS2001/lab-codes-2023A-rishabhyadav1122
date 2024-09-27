input_count  = int(input("Enter count of numbers in list : "))

input_list = []
for i in range(input_count):
    input_value = int(input(f"Enter value {i + 1}: "))
    input_list.append(input_value)

print(input_list)

mean = sum(input_list) / len(input_list)

print(f"Mean is {mean}")

input_list.sort()
median = 0
if(input_count % 2 == 0):
    median  += (input_list[(input_count//2)-1]+input_list[(input_count//2)])//2
else:
    median += input_list[((input_count+1)//2)-1]    
print(f"Median is {median}")    


    
