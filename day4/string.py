print('가' in '가나다라')
print('가다' in '가나다라')
print('나다' in '가나다라')

S = '가나다라'
print(S[0])
print(S[-1])
print(S[-4])

A = '가나다라마바사'

print(A[0:2])
print(A[1:])
print(A[:-1]) # 마지막꺼빼고 다출력
print(A[2:5]) # 다라마
print(A[::2])
print(A[::-1])
print(A[1:-1:2]) # 첫번쨰 idx 부터 마지막 idx까지 2칸씩 출력
