dict = {'name' : '윤주훈', 'age' : 20}

print(dict['name'])

## java map.getOrDefault(key, defaultValue)와 같은 기능
print(dict.get(5, None))

print('age' in dict)
print('age1' in dict)
# 같은 key값을 가지면 덮어씌워진다.

dict['name'] = 'hi'
print(dict)



