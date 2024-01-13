# 팩토리얼 나누기_BOJ15996

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, A = map(int, input().split())    # N 음이 아닌 정수 / A N을 나눌 수를 input 받고
if N == 0:                          # N이 0이면
    N = 1                           # 0!은 1이므로 N에 1을 저장한다
ans = 0                             # 정답을 저장할 변수를 생성하고
k = 1                               # A의 지수로 사용할 k를 생성한다
while A**k <= N:                    # A의 k제곱이 N보다 커질때까지 반복해서
    ans += N//(A**k)                # A의 k제곱으로 N을 나눌 수 있는 수만큼 ans에 더하고
    k += 1                          # k를 1 추가한다
print(ans)                          # A의 k제곱으로 나누었을 때, 나머지가 0이 되는 최대의 음이 아닌 정수를 출력한다
