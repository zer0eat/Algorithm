# 당구 좀 치자 제발_BOJ32642

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 날짜를 input 받고
W = list(map(int, input().split())) # 비오는 날을 input 받고
ans = 0                             # 분노를 저장할 변수를 생성하고
all = []                            # 분노 상태를 저장할 리스트를 생성한다
for n in range(N):                  # 날짜를 반복해서
    if W[n] == 0:                   # 비가 안오면
        ans -= 1                    # 분노를 줄이고
    else:                           # 비가 오면
        ans += 1                    # 분노를 높인다
    all.append(ans)                 # n+1일째 분노를 리스트에 append한다
print(sum(all))                     # n일간 분노의 합을 출력한다