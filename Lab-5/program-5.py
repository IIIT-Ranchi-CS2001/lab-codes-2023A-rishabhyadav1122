customer_data = [
    ('Alice', 'C001', 120),
    ('Bob', 'C002', 250),
    ('Charlie', 'C003', 90)
]

# Sort the list of tuples based on shopping points (3rd element in the tuple)
sorted_customer_data = sorted(customer_data, key=lambda x: x[2])

print("Sorted customer data using sorted():")
print(sorted_customer_data)


# List of tuples constructed manually
customer_data_manual = [
    ('Alice', 'C001', 120),
    ('Bob', 'C002', 250),
    ('Charlie', 'C003', 90)
]

# Implement Bubble Sort to sort based on shopping points (3rd element in the tuple)
n = len(customer_data_manual)
for i in range(n):
    for j in range(0, n-i-1):
        if customer_data_manual[j][2] > customer_data_manual[j+1][2]:
            customer_data_manual[j], customer_data_manual[j+1] = customer_data_manual[j+1], customer_data_manual[j]

print("Sorted customer data without using sorted() (Bubble Sort):")
print(customer_data_manual)