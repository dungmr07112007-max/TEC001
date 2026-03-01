import re

def sum_of_numbers(text):
    numbers = re.findall(r'\d+', text)
    total = 0
    for num in numbers:
        total += int(num)
    return total

text = input("Enter paragraph: ")
result = sum_of_numbers(text)
print("Sum:", result)