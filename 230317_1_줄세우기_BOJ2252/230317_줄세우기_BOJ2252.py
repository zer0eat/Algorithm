# 줄세우기_BOJ2252

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N, M = map(int, input().split())            # N 학생의 수 / M 키를 비교한 수
line = dict()                               # 
for _ in range(M):                          # 키를 비교한 수를 반복해서
    a, b = map(int, input().split())        # a, b 두 학생의 번호를 input 받고
    if line.get(a) == None:                 # a가 현재 아무도 비교하지 않은 상태라면
        line[a] = [b]                       # a를 key b를 value로 딕셔너리에 추가하고
    else:                                   # a가 비교한 기록이 있다면
        line[a].append(b)                   # value에 b를 append

def dfs(x):
    visited[x] = 1                          # x번 학생이 줄을 섰다는 표시를 하고
    if line.get(x) == None:                 # x번 뒤에 설 학생이 없다면
        ans.appendleft(x)                   # ans의 가장 앞에 줄을 서고
        return                              # return
    else:                                   # x번 뒤에 설 학생이 있다면
        for i in line[x]:                   # x번 뒤에 올 학생을 반복해서
            if visited[i] == 0:             # 학생이 아직 줄을 안섰다면
                dfs(i)                      # dfs에 학생 번호를 넣어 줄을 세운다
    ans.appendleft(x)                       # x 뒤에 설 학생을 모두 줄을 세웠다면 ans의 가장 앞에 줄을 선다

ans = deque()                               # 키 순서로 세운 번호를 저장할 deque 생성
visited = [0]*(N+1)                         # 줄을 섰는지 여부를 체크할 리스트 생성
for a in range(N):                          # 학생의 순서를 반복해서
    if visited[a+1] == 0:                   # a+1번 학생이 아직 줄을 서지 않았다면
        dfs(a+1)                            # dfs에 학생 번호를 넣어 줄을 세운다

print(*ans)                                 # 줄 선 순서대로 학생의 번호를 출력한다
