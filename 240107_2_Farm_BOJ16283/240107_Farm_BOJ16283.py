# Farm_BOJ16283

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a, b, n, w = map(int, input().split())  # a 양이 먹는 사료 / b 염소가 먹는 사료 / n 양과 염소의 수 / w 소비한 사료의 양
ans = []                                # 정답을 저장할 리스트를 생성하고
for i in range(1, n):                   # 양의 수를 반복해서
    if a*i + b*(n-i) == w:              # 양과 염소가 먹은 사료가 정확히 w가 된다면
        ans.append([i, n-i])            # 양과 염소의 수를 ans에 append한다
if len(ans) == 1:                       # 정답에 가능한 경우가 1가지만 있다면
    print(*ans[0])                      # 양과 염소의 수를 출력하고
else:                                   # 1가지가 아니라면
    print(-1)                           # -1을 출력한다