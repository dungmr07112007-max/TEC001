import random

def approximate_pi(num_points):
    inside = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x*x + y*y < 1:
            inside += 1

    return 4 * inside / num_points


points = int(input("Nhập số lượng điểm random: "))
pi_value = approximate_pi(points)

print("Giá trị pi xấp xỉ là:", pi_value)