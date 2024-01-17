# 실질적 약수_BOJ2247

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # SOD를 구하기 위한 값을 input 받고
ans = 0                     # 정답을 저장할 변수를 생성한다
for i in range(2, N//2+1):  # N의 절반까지 반복해서
    ans += (i*(N//i - 1))   # i가 약수가 되는 수의 개수에 i를 곱해서 ans에 저장하고
    ans %= 1000000          # 1000000으로 나눈 나머지만 저장한다
print(ans)                  # CSOD(n)을 1,000,000으로 나눈 나머지를 출력한다