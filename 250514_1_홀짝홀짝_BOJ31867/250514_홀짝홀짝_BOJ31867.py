# 홀짝홀짝_BOJ31867

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 자리수를 input받고
K = input().strip() # 숫자를 input받아서
E, O = 0,0          # 짝수와 홀수를 저장할 변수를 생성하고
for k in K:         # 숫자의 자리수를 반복해서
    if int(k) % 2:  # 홀수라면
        O += 1      # 홀수의 수를 추가하고
    else:           # 짝수라면
        E += 1      # 짝수의 수를 추가하고
if E > O:           # 짝짝수라면
    print(0)        # 0을 출력하고
elif E < O:         # 홀홀수라면
    print(1)        # 1을 출력하고
else:               # 짝수와 홀수의 수가 같다면
    print(-1)       # -1을 출력한다