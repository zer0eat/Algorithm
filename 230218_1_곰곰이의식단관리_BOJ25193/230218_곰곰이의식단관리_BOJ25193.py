# 곰곰이의식단관리_BOJ25193

# input.txt 열기
import sys
sys.stdin = open('input.txt')
import math

# input 받기
N = int(sys.stdin.readline().strip())   # 음식을 먹는 날짜
S = sys.stdin.readline().strip()        # N일간 먹을 음식리스트

chicken = 0                             # 치킨을 먹을 날을 저장할 변수
food = 1                                # 다른음식을 먹을 날을 저장할 변수
for c in S:                             # 음식리스트를 반복해서
    if c == 'C':                        # C가 나오면
        chicken += 1                    # 치킨먹는날을 1 증가시키고
    else:                               # 다른 문자가 나오면
        food += 1                       # 다른음식 먹는 날을 1증가시킨 후

print(math.ceil(chicken/food))          # 치킨먹는날에서 다른음식먹는날을 나눠준 후 올림한다
