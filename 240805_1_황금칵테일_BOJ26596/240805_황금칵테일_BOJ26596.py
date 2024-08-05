# 황금칵테일_BOJ26596

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
M = int(input())                    # 칵테일에 넣은 재료의 수를 input 받고
shaker = dict()                     # 칵테일의 넣은 재료를 저장할 딕셔너리를 생성한다
for m in range(M):                  # 칵테일에 넣은 재료의 수를 반복해서
    name, vol = input().split()     # 칵테일에 넣은 재료와 양을 input 받고
    if shaker.get(name):            # 이 재료를 넣은 적이 있다면
        shaker[name] += int(vol)    # 재료의 양을 더해주고
    else:                           # 이 재료를 넣은 적이 없다면
        shaker[name] = int(vol)     # 재료의 양을 저장한다
for s in shaker:                    # 칵테일에 넣은 재료를 반복하고
    for h in shaker:                # 칵테일에 넣은 재료를 반복해서
        if s == h:                  # 같은 재료라면
            continue                # 건너 뛰고
        if int(min(shaker[s], shaker[h])*1.618) == int(max(shaker[s], shaker[h])):  # 다른재료이면서 황금비율이라면
            print('Delicious!')     # 맛있다!를 출력하고
            quit()                  # 종료한다
else:                               # 황금비율이 나오지 않았다면
    print('Not Delicious...')       # 맛없다...를 출력한다