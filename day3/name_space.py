X = 2023
Y = X

print(hex(id(X)))
print(hex(id(Y)))

print(X is Y) # 객체 비교

print (X == Y) #value 비교

X = 2024

print(hex(id(X)))
print(hex(id(Y)))

print(X is Y)