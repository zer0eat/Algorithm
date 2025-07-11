# 첨탑 밀어서 부수기_BOJ28014

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 첨탑의 수를 input받고
H = list(map(int, input().split()))     # 첨탑의 높이를 input받고
ans = 1                                 # 정답을 저장할 변수를 생성한다
for n in range(N-1):                    # 첨탑의 수를 반복해서
    if H[n] <= H[n+1]:                  # 다음 첨탑이 더 높다면
        ans += 1                        # 횟수를 1 추가하고
print(ans)                              # 첨탑을 미는 횟수를 출력한다