# 연결요소의개수_BOJ11724

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def line(n):                                # node를 연결하는 함수
    visited[n] = 1                          # node n을 방문표시하고
    for a in node[n]:                       # node n에서 갈수 있는 node를 반복해서
        if visited[a] == 0:                 # 아직 방문 전이라면
            line(a)                         # 연결하는 함수를 통해 연결한다

# input 받기
N, M = map(int, input().split())            # N node의 수 / M 간선의 개수

node = [[] for _ in range(N+1)]             # node에 node의 번호가 인덱스가 되도록 리스트 생성
visited = [0]*(N+1)                         # node의 번호가 인덱스가 되도록 방문여부를 확인할 리스트 생성

for _ in range(M):                          # 간선의 수 만큼 반복할 때
    a, b = map(int, input().split())        # 양 노드를 a,b에 저장하고
    node[a].append(b)                       # a를 인덱스로하는 리스트에 b를 저장하고
    node[b].append(a)                       # b를 인덱스로하는 리스트에 a를 저장한다

cnt = 0                                     # 연결요소의 개수를 셀 변수를 생성하고
for n in range(1, N+1):                     # 1부터 끝까지 node를 반복해서
    if visited[n] == 0:                     # 방문 전이라면
        line(n)                             # 연결하는 함수를 돌고
        cnt += 1                            # cnt를 하나 추가한다

print(cnt)