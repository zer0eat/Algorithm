# 그래프경로_13808

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 방문 함수 만들기
def nod(S):
    visited[S - 1] = 1                        # 시작점을 방문 했으므로 1이라고 저장한다.(인덱스의 0자리가 1이므로 -1을 해준다)
    for M in lst[S - 1]:                      # 시작점과 연결된 곳을 반복할 때
        if visited[M - 1] == 0:               # 방문했던 곳이 아니라면
            nod(M)                            # 다시 함수를 돌려 방문한다

# input 받기
T = int(input())                              # 테스트 케이스
for t in range(T):
    V, E = map(int, input().split())          # V 노드의수 / E 간선의 수

    lst = [[] for _ in range(V)]              # 빈 리스트를 노드의 숫자만큼 만들어준다
    for e in range(E):                        # 간선 정보의 갯수만큼 반복을 돌려
        A, B = map(int, input().split())      # 간선의 시작과 끝을 A, B에 저장한 후
        lst[A-1].append(B)                    # 시작점을 lst의 인덱스로 끝나는 점을 리스트 내에 저장한다.(인덱스의 0자리가 1이므로 -1을 해준다)

    S, G = map(int, input().split())          # 알아볼 출발점과 도착점을 S, G로 저장한다

    visited = [0] * V                         # 방문 함수를 돌리기 위해 아무도 도착하지 않은 요소가 0인 리스트를 만든다.
    nod(S)                                    # 방문함수를 돌려서
    print(f'#{t+1}', visited[G-1])            # 도착지가 방문으로 체크되어있으면 1 아니면 0을 출력한다.(인덱스의 0자리가 1이므로 -1을 해준다)




