Problem 1: Shape Area Calculator
Scenario:

You are developing a shape calculator that calculates the area of different shapes.

Initially, the application supports:
- Circle
- Rectangle
Later, the business wants to introduce Triangle and Square.

Your tasks:
1. Create an abstract class Shape.
2. Define an abstract method calculate_area().
3. Implement separate classes for Circle, Rectangle and Triangle.
4. Create a function print_area() that accepts any shape object.
5. Demonstrate how a new shape can be added without modifying existing classes.
Expected output:
Circle Area: 78.5
Rectangle Area: 50
Triangle Area: 25


Edge cases:
- Circle radius is zero.
- Rectangle has a negative length.
- Triangle has invalid dimensions.