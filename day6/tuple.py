T = ('hi')
t = ('hi')

print(T)

print((1,2,3) + (4,5,6))

a = (1,2,3)
print(list(a))
print(tuple(a))

# 튜플 안에 있는 수정 가능한 객체들은 수정 가능하다.

T = (1,2,2,3,3,3,4,4,4,4)
print(T.index(4)) # 4가 몇번째 index에 있는지
print(T.index(4, 7)) # 4가 7번째 index 포함 이후에 몇번째 index에 있는지
