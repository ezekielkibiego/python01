import math

def calculate_area(radius):
    area = math.pi * (radius ** 2)
    return area

result = calculate_area(7)
print(f'{result:.2f}')