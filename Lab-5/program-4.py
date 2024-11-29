customer_names = [input("Enter customer name: ") for _ in range(3)]
customer_ids = [input("Enter customer ID: ") for _ in range(3)]
shopping_points = [int(input("Enter shopping points: ")) for _ in range(3)]

# Construct a list of tuples using zip()
customer_data = list(zip(customer_names, customer_ids, shopping_points))

print("Customer data using zip():")
print(customer_data)

# Construct a list of tuples without using zip()
customer_data_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(3)]

print("Customer data without using zip():")
print(customer_data_manual)