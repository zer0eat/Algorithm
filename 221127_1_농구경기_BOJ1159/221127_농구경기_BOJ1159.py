# 농구경기_BOJ1159

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                # 출전할 수 있는 선수의 수
basket = dict()                 # 선수의 명단을 저장할 딕셔너리 생성
for t in range(T):              # 선수의 수만큼 반복해서
    A = input()[0]              # 이름의 첫글짜를 A에 저장한다
    try:                        # basket[A]가 딕셔너리에 저장되어 있다면
        basket[A] += 1          # value에 1을 추가하고
    except:                     # basket[A]이 딕셔너리에 없다면
        basket[A] = 1           # basket[A]의 값을 1로 저장한다

ans = []                        # 빈 리스트를 생성하고
for b in basket:                # 딕셔너리를 반복해서
    if basket[b] >= 5:          # value가 5 이상인 경우에
        ans.append(b)           # ans에 추가한다

ans.sort()                      # ans를 오름차순으로 정렬하고
player = ''                     # 출전할 수 있는 선수의 첫글자를 저장할 변수를 생성한다

if len(ans):                    # ans가 비어있지 않아 출전할 사람이 있다면
    for a in ans:               # 출전 가능한 명단을 반복해서
        player += a             # player에 선수이름의 맨 앞글자를 추가하고
    else:                       # 반복을 마치면
        print(player)           # player를 출력한다
else:                           # 선발 출전할 사람이 없다면
    print('PREDAJA')            # PREDAJA를 출력하여 기권한다



