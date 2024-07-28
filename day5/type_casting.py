# print('100' + 300) TypeError

print(int('100') + 300)

print('100' + str(300)) # 100300

# strings => 불변 객체

S = '가나다라마바사'
# S[0] = '캐' # TypeError
S = '캐' + S[1:]
print(S)

# S = '가' + S[1:]
S = S.replace('캐', '가')
print(S)




