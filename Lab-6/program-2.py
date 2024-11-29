def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("All lists must have the same length when 'strct=True'.")
    else:
        min_length = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_length)]
    
    
def my_sort(data, key=0):
    n = len(data)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
    
    return data

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = ['C001', 'C002', 'C003']
shopping_points = [120, 250, 90]

customer_data = my_zip(customer_names, customer_ids, shopping_points, strct=False)

print("Sorted by customer name (key = 0):")
print(my_sort(customer_data, key=0))

print("\nSorted by customer ID (key = 1):")
print(my_sort(customer_data, key=1))

print("\nSorted by shopping points (key = 2):")
print(my_sort(customer_data, key=2))