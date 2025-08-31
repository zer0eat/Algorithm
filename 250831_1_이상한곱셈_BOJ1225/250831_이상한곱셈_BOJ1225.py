# 이상한곱셈_BOJ1225

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = input().split()          # 두 수를 input받고
ans = 0                         # 정답을 저장할 변수를 생성한다
for a in A:                     # 한 수를 순서대로 반복하고
    for b in B:                 # 다른 수를 순서대로 반복해서
        ans += int(a)*int(b)    # 두 수의 곱을 정답을 저장할 변수에 더해준다
print(ans)                      # 곱셈의 결과를 출력한다