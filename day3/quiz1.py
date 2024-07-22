X = [100, 200, 300]
Y = [100, 200, 300]

Z = Y

# X와 Y는 다른 객체입니다. 왜그럴까요?
print(X is Y)

## X Y 는 list 이고 list는 서로 다른 주소값을 가지고 있다.

print(X == Y)

print(Z is Y)
