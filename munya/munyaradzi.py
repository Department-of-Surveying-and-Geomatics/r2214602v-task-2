import csv
import matplotlib.pyplot as plt
from random import random


class Point:
    """
    This class represents a simple point in 2D space with x and y coordinates.
    """

    def _init_(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        """
        Returns the x-coordinate of the point.
        """
        return self.x

    def get_y(self):
        """
        Returns the y-coordinate of the point.
        """
        return self.y

    def translate(self, dx, dy):
        """
        Moves (translates) the point by the specified offsets.

        Args:
            dx (float): X-axis offset.
            dy (float): Y-axis offset.
        """
        self.x += dx
        self.y += dy

    def _str_(self):
        """
        Returns a string representation of the point in the format "(x, y)".
        """
        return f"({self.x}, {self.y})"


def main():
    # Read data from CSV file
    points = []
    with open("data.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            points.append(Point(float(row[0]), float(row[1])))

    # Create plot
    fig, ax = plt.subplots()
    x, y = zip(*[(point.get_x(), point.get_y()) for point in points])
    plt.scatter(x, y)
    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")
    plt.title("Interactive Point Plot")
    plt.grid(True)

    # Move points by random offsets
    for point in points:
        point.translate(random() - 0.5, random() - 0.5)  # Random offset between -0.5 and 0.5

    # Replot points in a different color (red)
    x, y = zip(*[(point.get_x(), point.get_y()) for point in points])
    plt.scatter(x, y, color='red')

    plt.show()


if _name_ == "_main_":
    main()