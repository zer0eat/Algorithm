# 노드의거리_13974

# def find_road(S):




# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    V, E = input().split()
    V = int(V)
    E = int(E)
    road = [[] for _ in range(V+1)]
    for e in range(E):
        A, B = input().split()
        A = int(A)
        B = int(B)
        road[A].append(B)
        road[B].append(A)
    S, G = input().split()
    S = int(S)
    G = int(G)
    print(road)

    # 길찾기




