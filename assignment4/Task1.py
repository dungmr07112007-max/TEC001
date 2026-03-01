import re

def is_valid_course_code(code):
    pattern = r'^[A-Z]{3}[0-9]{3}$'
    return bool(re.match(pattern, code))

code = input("Enter course code: ")
result = is_valid_course_code(code)
print("Result:", result)