# Since 1973_BOJ28135

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 숫자를 input 받고
ans = 0                 # 정답을 저장할 변수를 생성해서
for n in range(N):      # 숫자를 반복해서
    if '50' in str(n):  # 50이 포함되어 있으면
        ans += 2        # 2번세고
    else:               # 50이 없으면
        ans += 1        # 1번센다
print(ans)              # 카운트 한 수를 출력한다