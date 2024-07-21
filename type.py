## type
print(type("20" + "21"))
# str
print(type(20212))
# int
print(type(2021.9))
#float

print((2021.9))

## class
x = 100
print(x.__class__.__class__) #type
print(x.__class__) # int

# isInstance
z = True
print(isinstance(z, bool)) # z가 bool인지 확인
print(isinstance(z, int)) # z가 bool인지 확인

# list
y = ['안녕하세요']
print(y.__class__)
print(type(y))

a = [0, [1,2], [3,4,5], ['안녕', ['하', '세요']]] # 객체의 메모리 주소 하나하나를 왼쪽에서 오른쪽으로 차례대로 저장된다. 
print(a[0])
print(a[3][1][0])
print(len(a))




