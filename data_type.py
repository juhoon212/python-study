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