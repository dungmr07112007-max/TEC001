import re

def is_valid_hex_color(color):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, color))

color = input("Enter hex color: ")
result = is_valid_hex_color(color)
print("Result:", result)