D = {'name' : 'Craftsman Mentality', 'age' : 30, 'hobby' : 'coding'}

# print(D.keys()) # list x
# print(D.values()) # list x
# print(D.itmes()) # list x

print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))

D['name'] = 'juhoon'
D['gender'] = 'M' # dict 추가
del D['hobby'] # dict 삭제
print(D)

# Dictionary key 수정 불가

C = {}
print(C)

C[(1,2,3)] = 'value1'

print(C)

C[(4,5,6)] = 'value2'

x = 1; y = 2; z = 3
print(C[x,y,z])



