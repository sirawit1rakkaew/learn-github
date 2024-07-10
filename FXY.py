# กำหนดช่วงของ X และ Y
x_start = 0
x_end = 10
y_start = 0
y_end = 10
precision = 0.1
Sum=0

# ฟังก์ชันตรวจสอบสมการ
def check_equation(x, y):
    result = x**2 - 2*x*y + y**2
    return abs(result - 4) < 0.01

# วนลูปผ่านค่า X และ Y
x = x_start
while x <= x_end:
    y = y_start
    while y <= y_end:
        if check_equation(x, y):
            print("X =", round(x, 1), "Y =", round(y, 1), "Result =", round(x**2 - 2*x*y + y**2, 2))
        y += precision
    x += precision
    Sum+=1
print(Sum)