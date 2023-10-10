# 전깃줄_BOJ2565

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import bisect

# input 받기
N = int(input())                                            # 전깃줄의 수를 input받고
wire = [list(map(int, input().split())) for _ in range(N)]  # A전봇대와 B전봇대가 이어진 정보를 input 받아 리스트로 저장한 후
wire.sort()                                                 # A전봇대를 기준으로 오름차순 정렬한다
ans = [wire[0][1]]                                          # A의 맨 앞 전봇대와 이어진 B전봇대의 위치를 넣은 리스트를 생성하고
for n in range(1, N):                                       # 1부터 N-1까지 반복해서
    if ans[-1] < wire[n][1]:                                # ans의 맨 뒤에 저장된 B의 위치보다 n번째 B의 위치가 더 크다면
        ans.append(wire[n][1])                              # ans에 n번째 B의 위치를 append하고
    else:                                                   # ans의 맨 뒤에 저장된 B의 위치보다 n번째 B의 위치가 더 작다면
        idx = bisect.bisect_left(ans, wire[n][1])           # n번째 B보다 처음으로 같거나 큰 원소를 ans에서 찾아 idx에 인덱스를 저장한 후
        ans[idx] = wire[n][1]                               # 해당 원소를 n번째 B의 위치로 저장한다
print(N-len(ans))                                           # 전체 전깃줄 중 증가하는 최대수열을 빼서 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다