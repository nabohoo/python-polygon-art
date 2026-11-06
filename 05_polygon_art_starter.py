"""Static Polygon Artwork using the Polygon class."""
import turtle
import random
from polygon_shape import Polygon

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Static Polygon Art - Milestone 1")
screen.bgcolor("black")
screen.tracer(0)  # Draw entire scene before refreshing window

colors = [
    "cyan", "turquoise", "orange", "yellowgreen", "deepskyblue",
    "salmon", "plum", "lightgreen", "gold", "pink", "white"
]
rng = random.Random(12)

polygons = []
# Create and draw 20 overlapping polygons (at least 15 required)
for _ in range(20):
    sides = rng.randint(3, 7)
    side_length = rng.randint(35, 120)
    x = rng.randint(-350, 260)
    y = rng.randint(-225, 180)
    color = rng.choice(colors)
    pen_size = rng.randint(1, 7)
    angle = rng.randint(0, 359)

    polygon = Polygon(x, y, sides, side_length, color, pen_size, angle)
    polygon.draw()
    polygons.append(polygon)

screen.update()
screen.mainloop()