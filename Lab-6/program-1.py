def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("All lists must have the same length when 'strct=True'.")
    else:
        min_length = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_length)]

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = ['C001', 'C002']
shopping_points = [120, 250, 90]

try:
    print("Strict zipping (strct=True):")
    print(my_zip(customer_names, customer_ids, shopping_points, strct=True))
except ValueError as e:
    print(e)

print("\nNon-strict zipping (strct=False):")
print(my_zip(customer_names, customer_ids, shopping_points, strct=False))