#list
a = [1, 2, 3, 4]

#dictionary
# key 값은 string, numbers, tuples 만 가능하다.
# key 중복 x : 어떤 값을 가져올지 모르기 때문.
b = {'a': 1, 'b': 2}
print(b.__class__)

c = {
    'age' : 30,
    'age' : 31,
    'hobby' : ['최강야구 보기', '스타크래프트']
}

print(c['age'])

# HashTable : key => hash() => memory address => value

# Tuple

d = (1, 2, 3)
# e = ('안녕하세요')

# print(isinstance(e, tuple)) false 왜? 튜플은 뒤에 콤마를 찍어줘야지 튜플로 인식한다.
e = ('안녕하세요', )
print(isinstance(e, tuple))

# Set

ab = {1,2,3,4,5}

print(isinstance(ab, set))

# None

cd = None
print(cd.__class__)









 