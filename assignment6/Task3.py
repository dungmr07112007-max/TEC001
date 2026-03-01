names = set()

while True:
    name = input("Nhập tên (Enter để thoát): ")
    
    if name == "":
        break
    
    if name in names:
        print("Tên đã tồn tại")
    else:
        print("Tên mới")
        names.add(name)

print("\nDanh sách các tên đã nhập:")
for name in names:
    print(name)