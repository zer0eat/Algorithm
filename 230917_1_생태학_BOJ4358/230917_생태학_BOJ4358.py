# 생태학_BOJ4358

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from decimal import Decimal

# input 받기
woods = dict()                                                  # 나무의 숫자를 저장할 딕셔너리를 생성하고
tmp = 0                                                         # 전체 나무의 수를 저장할 변수를 생성한다
while 1:                                                        # break가 나올때까지 반복해서
    wood = input().strip()                                      # 나무의 종 이름을 저장하고
    if wood == '':                                              # 나무의 이름이 없다면
        break                                                   # while문을 break한다
    elif woods.get(wood) == None:                               # 나무의 이름이 딕셔너리에 없다면
        woods[wood] = 1                                         # 나무의 수를 1로 저장하고
        tmp += 1                                                # 전체 나무의 수를 1 더한다
    else:                                                       # 나무의 이름이 딕셔너리에 있다면
        woods[wood] += 1                                        # 나무의 수를 value에 1 더하고
        tmp += 1                                                # 전체 나무의 수를 1 더한다
woods = sorted(woods.items(), key=lambda x: x)                  # 딕셔너리의 key value를 items로 불러와서 나무의 이름순으로 정렬한후
for wood in woods:                                              # 정렬된 리스트를 반복해서
    print(wood[0], round(Decimal(wood[1]/tmp * 100), 4))        # 나무의 이름과 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력한다
