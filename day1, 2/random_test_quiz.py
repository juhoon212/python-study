from random import *

# 랜덤 날짜
# 월별 일수 28 이내
# 매월 1~3일은 스터디 준비를 해야 하므로 제외

value = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 {} 일로 선정되었습니다".format(value))