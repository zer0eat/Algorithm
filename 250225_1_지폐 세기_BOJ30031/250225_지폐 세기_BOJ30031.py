# 지폐 세기_BOJ30031

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 지폐의 수를 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성한다
for n in range(N):                      # 지폐의 수를 반복해서
    n, m = map(int, input().split())    # 가로 세로 길이를 input 받고
    if n == 136:                        # 가로가 136이면
        ans += 1000                     # 1000원을 추가하고
    elif n == 142:                      # 가로가 142이면
        ans += 5000                     # 5000원을 추가하고
    elif n == 148:                      # 가로가 148이면
        ans +=  10000                   # 10000원을 추가하고
    elif n == 154:                      # 가로가 154이면
        ans += 50000                    # 50000원을 추가하고
print(ans)                              # 지폐의 총액을 출력한다