# 노드의거리_13974

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 거리를 찾는 함수
def find_road(S, G):                                    # 노드의 시작(S)과 끝(G)점이 주어졌을 때 거리를 구하는 함수
    q = []                                              # 큐를 만들어주고
    q.append(S)                                         # 시작점을 q에 넣어준다
    visited[S] = 1                                      # 시작점을 출발점 1로 표시해준다
    while q:                                            # q가 빌 때까지 반복해주면
        node = q.pop(0)                                 # 가장 먼저 넣은 노드를 빼서 node에 저장해주고
        for s in road[node]:                            # 노드가 갈 수 있는 점들을 반복한다
            if s == G:                                  # 만약 갈 수 있는 점이 도착지라면
                visited[s] = visited[node] + 1          # 현재까지 이동거리를 방문지에 기록하고
                return                                  # 함수를 종료한다
            elif visited[s] == 0:                       # 만약 방문하지 않은 지점이라면(방문지는 패스한다)
                q.append(s)                             # q에 append하고
                visited[s] = visited[node] + 1          # visited에 현재까지 이동거리를 기록한다.
    else:                                               # q가 빌 때까지 반복이 끝나면
        return                                          # 함수를 종료한다

# input 받기
T = int(input())                                        # 테스트 케이스
for t in range(T):                                      # 테스트 케이스 수 만큼 반복할 때
    V, E = input().split()                              # V = 노드의 개수 / E = 간선 정보의 개수
    V = int(V)                                          # int로 바꾸어 저장
    E = int(E)                                          # int로 바꾸어 저장
    road = [[] for _ in range(V+1)]                     # 빈 road 리스트 안에 노드의 번호가 인덱스가 될 수 있게 리스트를 생성해준 후
    for e in range(E):                                  # 간선의 개수만큼 반복해서 간선의 정보를 받는다
        A, B = input().split()                          # A, B = 간선의 양 끝 노드
        A = int(A)                                      # int로 바꾸어 저장
        B = int(B)                                      # int로 바꾸어 저장
        road[A].append(B)                               # 양 방향으로 움직일 수 있으므로 출발점을 인덱스 도착점이 요소가 되도록 append
        road[B].append(A)
    S, G = input().split()                              # S = 출발노드 / G = 도착노드
    S = int(S)                                          # int로 바꾸어 저장
    G = int(G)                                          # int로 바꾸어 저장

    # 길찾기
    visited = [0] * (V+1)                               # 노드의 번호가 인덱스가 될 수 있게 요소가 0인 방문지를 만들어 준다
    find_road(S, G)                                     # 거리를 찾는 함수에 (S = 출발노드 / G = 도착노드)를 넣고 돌린 후
    if visited[G] == 0:                                 # 방문지의 값이 0이면 도달할 수 없으므로
        print(f'#{t + 1}', visited[G])                  # 0을 출력
    else:                                               # 0이 아니라면 도달한 값이므로
        print(f'#{t+1}', visited[G] - 1)                # 간선의 개수인 (노드의 수 -1)을 해서 출력한다




