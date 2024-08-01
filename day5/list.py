# list : mutable

print([1,2,3] + [4,5,6])

print([1,2,3] * 3)

# print([1,2,3] + 100) Type Error

print([100,200,300] in [100,200,300]) # in은 객체비교 == 은 값 비교

print(100 in [100,200,300])

L = [100, 200, 300, 400]
print(L[::2])
print(L[:-1:2])

# print(str(['a', 'b'] + 'c')) TypeError


a = (1,2,3,4,5)
b = 'abcde'
c = 100

print(list(a))
print(list(b))
# print(list(c)) # TypeError int는 iterable하지 않다.
# 해결방법
print([c])

# 2

L = ['캐', '나', '다', '라', '마', '바', '사']
# 바꾸기
L[3:6] = ['벤', '쿠', '버']
print(L)
# 넣기
L[6:6] = ['최', '고']
print(L)
# 지우기
L[0:3] = []
print(L)
L[5:6] = ['다']
print(L)

# append는 기존의 리스트에 추가하는 것이다. 생성 x
L1 = ['안녕', '내 이름은', '윤주훈', '이야']

# NONE append()는 return할 객체가 없기 때문
# L1 = L1.append('반가워') 

print(L1)

# extend()는 list등 iterable한 객체를 추가할 수 있다.
L1.extend(['정말', '반가워'])
print(L1)

# L1.sort()
# L1.reverse()

print(L1)

L2 = L1[::-1]
print(L2)

item = L2.pop()

print(item)

L1.insert(1, ['정말', '반가워'])
print(L1)


D = dict(name = 'Craftsman Mentality', age = 30)

D = dict(zip(['name', 'age'], ['Craftsman Mentality', 30]))

A = dict(zip([1,2,3], ['a', 'b', 'c']))
print(A)

print(D)








