numbers = []

while True:
    user_input = input("Nhập số (Enter để thoát): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except:
        print("Vui lòng nhập số hợp lệ!")

numbers.sort(reverse=True)

print("5 số lớn nhất là:")
for num in numbers[:5]:
    print(num)