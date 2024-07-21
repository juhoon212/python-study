import math

print(math.pi)

print(4 ** 4) # 4의 4제곱

print(2 * 2 ** 2) # 연산자 우선순위는 ** 거듭제곱이 제일 높다.

radius = float(input("Enter the radius: "))
answer = math.pi * radius ** 2
print("반지름이 5인 원의 넓이는: ", answer, "입니다.") # 