seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Nhập số tháng (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Season:", seasons[0])
elif 3 <= month <= 5:
    print("Season:", seasons[1])
elif 6 <= month <= 8:
    print("Season:", seasons[2])
elif 9 <= month <= 11:
    print("Season:", seasons[3])
else:
    print("Tháng không hợp lệ!")