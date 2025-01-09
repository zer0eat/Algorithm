# 부호_BOJ1247

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
for t in range(3):          # 테스트 케이스를 반복해서
    N = int(input())        # 숫자를 input 받고
    ans = 0                 # 정답을 저장할 변수를 생성한다
    for n in range(N):      # 숫자를 반복해서
        ans += int(input()) # N개의 숫자를 더해서
    if ans < 0:             # 음수면
        print('-')          # -를 출력하고
    elif ans > 0:           # 양수면
        print('+')          # +를 출력하고
    else:                   # 그렇지 않으면
        print(0)            # 0을 출력한다