# 신기한 수_BOJ17618 

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 숫자를 input받고
ans = 0                     # 정답을 저장할 변수를 생성한다
for n in range(1, N+1):     # 숫자를 반복해서
    tmp = 0                 # 각자리의 합을 저장할 변수를 생성하고
    for m in str(n):        # 각자리의 수를 반복해서
        tmp += int(m)       # 각자리의 수를 더해주고
    if n % tmp == 0:        # 각자리의 합이 원래 숫자의 약수라면
        ans += 1            # 정답에 1을 추가한다
print(ans)                  # 신기한 수를 출력한다