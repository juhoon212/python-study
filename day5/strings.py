
# join
a1 = ['안녕', '내', '이름은', '윤주훈', '입니다']
s1 = ' '.join(a1)
print(s1)

# replace
email1 = 'ws5501@google.com'
email2 = email1.replace('google', 'naver')
print(email2)

# split
result = email1.split('@')
print(result) 

result2 = '@'.join(result)
print(result2)

name = 'ws5501'
symbol = '@'
email = 'google.com'

print(f'{name}{symbol}{email}')
print('{}{}{}'.format(name, symbol, email))



