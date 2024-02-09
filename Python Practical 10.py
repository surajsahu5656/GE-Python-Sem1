'''WAP to define a class Point with coordinates x and y as attributes. Create relevant methods and
print the objects. Also define a method distance to calculate the distance between any two point
objects.'''

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"Point: ({self.x}, {self.y})")

    @staticmethod
    def distance(point1, point2):
        # Calculate the distance between two points using the Euclidean distance formula
        dx = point1.x - point2.x
        dy = point1.y - point2.y
        return math.sqrt(dx**2 + dy**2)

# Create two Point objects
point1 = Point(2, 3)
point2 = Point(4, 5)

# Print the Point objects
point1.print_point()
point2.print_point()

# Calculate and print the distance between the two points
distance = Point.distance(point1, point2)
print(f"Distance between point1 and point2: {distance:.2f}")
