# 바이러스_BOJ2606

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def virus(V):                                       # 바이러스 걸린 컴퓨터를 찾는 함수를 
    if visited[V] == 0:                             # 방문하지 않은 컴퓨터라면
        visited[V] = 1                              # 방문표시를 하고
        for i in Network[V]:                        # 연결된 컴퓨터를 찾아
            virus(i)                                # 바이러스 걸린 컴퓨터를 찾는 함수를 실행한다

#input 받기
C = int(sys.stdin.readline())                       # 컴퓨터의 대수
N = int(sys.stdin.readline())                       # 연결된 네트워크 간선의 수

Network = [[] for _ in range(C+1)]                  # 컴퓨터 마다 연결된 컴퓨터를 저장하기 위한 리스트
visited = [0]*(C+1)                                 # 바이러스 감염 여부를 표시할 리스트

for _ in range(N):                                  # 간선을 모두 반복해서
    a, b = map(int, sys.stdin.readline().split())   # a, b에 컴퓨터를 각각 입력받고
    Network[a].append(b)                            # a를 인덱스로 하는곳에 b를 append 하고
    Network[b].append(a)                            # b를 인덱스로 하는곳에 a를 append 한다

virus(1)                                            # 1번 컴퓨터부터 virus 감염을 조사해서

print(sum(visited)-1)                               # 1번에 의해 걸린 컴퓨터의 대수를 출력한다

