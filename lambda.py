from math import pi
print((lambda radius: pi * radius ** 2)(3)) # (3) => lambda 뒤의 radius(파라미터)에 매핑됨.

area_circle = lambda radius: pi * radius ** 2 # 함수를 담을 변수를 지정 후 파라미터로 값을 넣어줄 수도 있다. 
print(area_circle(3))  