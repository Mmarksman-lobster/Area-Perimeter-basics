#ask user for width and height
#assume they put in valid data
width = float(input("width: "))
height = float(input("height: "))

#calculate area and perimeter
area = width * height
perimeter = 2 * (width + height)
#output the area and perimeter
print()
print(f"area: {area} units")
print()
print(f"perimeter: {perimeter} square units")