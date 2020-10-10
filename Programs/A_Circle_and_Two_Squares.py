inputR = 7
# Calculate Long Diagonal of Square (also circle diameter)
CircleDiameter = inputR * 2
# Calculate Length of Side of Square
SquareLength = (CircleDiameter**2 / 2)**(1/2)
# Calculate Area
Area = SquareLength**2
print(int(Area))