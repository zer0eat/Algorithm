# 5의 수난_BOJ23037

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = input().strip()     # 숫자를 input받고
ans = 0                 # 정답을 저장할 변수를 생성하고
for n in N:             # 숫자의 각 자리수를 반복해서
    ans += int(n)**5    # 각 자리수의 5제곱을 더해서
print(ans)              # 그 합을 출력한다