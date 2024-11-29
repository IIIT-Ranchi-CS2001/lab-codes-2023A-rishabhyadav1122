point1 = tuple([float(x) for x in input("Enter coordinates of the first point (x1, y1) separated by space: ").split()])
point2 = tuple([float(x) for x in input("Enter coordinates of the second point (x2, y2) separated by space: ").split()])

x1, y1 = point1
x2, y2 = point2

if y1 != y2:
    m = (x1 - x2) / (y1 - y2)
    print(f"The equation of the line is: (x - {x1}) = {m}(y - {y1})")
else:
    print(f"The equation of the line is a horizontal line: y = {y1}")