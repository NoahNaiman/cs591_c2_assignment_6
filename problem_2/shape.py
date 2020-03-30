import re
from math import pi


def get_input(prompt, accepted):
    inpt = ''
    pattern = re.compile(accepted)
    while not pattern.fullmatch(inpt):
        inpt = input(prompt).lower()
    return inpt


def get_circle_properties(r):
    if r <= 0:
        raise ValueError
    area = pi * r ** 2
    circumference = 2 * pi * r
    return (area, circumference)


def get_rectangle_properties(x, y):
    if x <= 0 or y <= 0:
        raise ValueError
    area = x*y
    perimeter = 2*x+2*y
    return (area, perimeter)


if __name__ == "__main__":
    shape = get_input(
        'Choose a shape: (c)ircle, (r)ectangle or (s)quare: ', '[crs]')

    if shape == 'c':
        radius = float(get_input('Radius of circle: ', '\d+'))
        area, circumference = get_circle_properties(radius)
        print('Area: %f units square\nCircumference: %f units' %
              (area, circumference))
    if shape == 'r':
        side1 = int(get_input('Length of rectangle: ', '\d+'))
        side2 = int(get_input('Height of rectangle: ', '\d+'))
        area, perimeter = get_rectangle_properties(side1, side2)
        print('Area: %d units square\nPerimeter: %d units' %
              (area, perimeter))
    if shape == 's':
        side1 = int(get_input('Side of square: ', '\d+'))
        area, perimeter = get_rectangle_properties(side1, side1)
        print('Area: %d units square\nPerimeter: %d units' %
              (area, perimeter))
