import math

# Function to calculate the distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Main program
# Input coordinates for the two points
x1, y1 = map(float, input("Enter coordinates of the first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of the second point (x2 y2): ").split())

# Calculate the distance
distance = calculate_distance(x1, y1, x2, y2)

# Output the result
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
