# BFS와DFS_BOJ1260

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M, V = map(int, sys.stdin.readline().split())        # N 노드의 개수 / M 간선의 개수 / V 시작점

road = [[] for _ in range(N+1)]                         # 간선을 저장할 리스트를 노드의 번호가 인덱스가 되도록 만들고

for _ in range(M):                                      # 간선의 개수만큼 반복해서
    a, b = map(int, sys.stdin.readline().split())       #
    road[a].append(b)                                   #
    road[b].append(a)                                   #
else:                                                   #
    for a in range(len(road)):                          #
        road[a].sort()                                  #

DDD = []                                                #
BBB = []                                                #

# DFS
def DFS(V):                                             #
    DDD.append(V)                                       #
    if len(DDD) == N:                                   #
        return                                          #
    for v in road[V]:                                   #
        if v not in DDD:                                #
            DFS(v)                                      #
DFS(V)                                                  #
print(*DDD)                                             #

# BFS                                                   #
def BFS(V):                                             #
    BBB.append(V)                                       #
    q = [V]                                             #
    while q:                                            #
        if len(BBB) == N:                               #
            return                                      #
        A = q.pop(0)                                    #
        for a in road[A]:                               #
            if a not in BBB:                            #
                BBB.append(a)                           #
                q.append(a)                             #
BFS(V)                                                  #
print(*BBB)                                             #