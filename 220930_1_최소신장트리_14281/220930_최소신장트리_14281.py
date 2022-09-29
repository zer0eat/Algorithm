# 최소신장트리_14281

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def prim(a):
    visited = [0] * (V + 1)                         # 방문을 한 노드임을 표시하기 위한 리스트를 생성하고 방문시 0을 1로 바꿔준다
    min_cost = [10000000] * (V + 1)                 # 해당 인덱스의 노드로 이동하기 위한 가장 적은 cost를 저장하기 위한 리스트를 생성
    parent = [-1] * (V + 1)                         # 해당 인덱스의 부모의 노드가 어떤 노드인지 표시하기 위한 리스트 생성

    min_cost[a] = 0                                 # 출발 노드에서 출발 노드로 이동할 때 드는 비용을 0으로 저장하고 시작한다

    for _ in range(V + 1):                          # 모든 노드를 탐색할 때
        # 출발점 찾기
        val = 10000000                              # 최소비용의 출발점을 찾기 위한 변수 생성
        for i in range(V + 1):                      # 모든 노드를 탐색할 때
            if visited[i] == 0 and min_cost[i] < val:       # 해당 노드에 방문한 적이 없고 / 최소 비용 val 보다 작은 값을 가지고 있을 때
                s = i                               # 출발점 s에 노드 i를 저장하고
                val = min_cost[i]                   # 최소 비용 val에 그 값을 저장하고
        visited[s] = 1                              # 모든 노드의 탐색이 끝났다면 방문표시를 한다
        # 도착점 비용 계산
        for e in range(V + 1):                      # 모든 노드를 탐색할 때
            if visited[e] == 0 and cost[s][e] > 0:  # 해당 노드에 방문한 적이 없고 / 이동 비용이 있어 간선이 있다고 판단된 경우에
                if min_cost[e] > cost[s][e]:        # 현재 저장되어 있는 e 노드로 이동하는 최저 비용보다 / s에서 e로 이동할 때 이동 비용이 더 적다면
                    min_cost[e] = cost[s][e]        # e 노드로 이동하는 최저 비용을 s에서 e로 이동할 때 드는 비용으로 교체한다
                    parent[e] = s                   # 교체한 후, parent리스트 e인덱스에 부모의 값을 요소로 저장한다
    return sum(min_cost)                            # 최저 비용의 합을 리턴한다

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복할 때
    V, E = map(int, input().split())                # V 노드의 개수 / E 간선의 수

    cost = [[0] * (V + 1) for _ in range(V + 1)]    # 출발점과 도착점을 행과 열의 인덱스로 잡았을 때 요소에 드는 비용을 저장하기 위한 행렬을 만든다

    for _ in range(E):                              # 간선의 수를 반복해서
        s, e, w = map(int, input().split())         # s에 시작점 / e에 도착점 / w에 비용을 저장한다

        cost[s][e] = w                              # 행렬의 인덱스를 출발점과 도착점으로 잡고 해당 영역에 비용을 저장한다
        cost[e][s] = w

    print(f'#{t+1}', prim(0))                       # prim 함수를 돌려 최소 비용을 출력한다