# 등교_BOJ31962

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, X = map(int, input().split())        # 버스의 대수와 도착시간을 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성한다
for n in range(N):                      # 버스의 대수를 반복해서
    S, T = map(int, input().split())    # 출발시간과 걸리는 시간을 input 받고
    if S + T <= X:                      # 시간내 도착할 수 있다면
        ans = max(ans, S)               # 출발시간의 최대값을 저장한다
if ans:                                 # 탈 수 있는 버스가 있다면
    print(ans)                          # 가장 늦게 출발하는 시간을 출력하고
else:                                   # 탈 수 있는 버스가 없다면
    print(-1)                           # -1을 출력한다