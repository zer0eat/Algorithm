# 점프점프_BOJ11060

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 미로의 길이를 input 받고
lst = list(map(int, input().split()))           # 점프할 수 있는 칸을 저장한 미로를 리스트를 input 받는다
dp = [1000] * N                                 # 점프 횟수를 저장할 dp를 생성하고
dp[0] = 0                                       # 시작점을 0으로 저장한다
for i in range(N):                              # 미로의 칸수를 반복해서
    for j in range(1, lst[i]+1):                # 해당 미로에서 점프할 수 있는 칸을 반복한다
        if i+j < N:                             # 점프하는 곳이 미로 내라면
            dp[i+j] = min(dp[i] + 1, dp[i+j])   # 점프하는 곳에 저장된 점프 횟수 + 1과 착지 지점의 저장된 점프 횟수 중 작은 수로 저장한다
if dp[-1] >= 1000:                              # 오른쪽 끝 칸까지 갈 수 없다면
    print(-1)                                   # -1을 출력하고
else:                                           # 오른쪽 끝 칸까지 도달했다면
    print(dp[-1])                               # 점프한 횟수를 출력한다