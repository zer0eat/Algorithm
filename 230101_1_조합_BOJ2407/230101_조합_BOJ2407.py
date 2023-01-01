# 조합_BOJ2407

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 열기
n, m = map(int, sys.stdin.readline().split())   # n 원소의 수 / m 선택할 개수
ans = 1                                         # 정답을 저장할 변수를 생성한다
for q in range(n, n-m, -1):                     # n부터 n-m+1까지 반복해서
    ans *= q                                    # ans에 q를 곱해준다

for p in range(1, m+1):                         # 1부터 m까지 반복해서
    ans //= p                                   # ans에서 p를 나눠준다

print(ans)                                      # 정답을 출력한다
