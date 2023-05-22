# Word Tree_BOJ25777

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, K = map(int, input().split())                            # N 단어의 수 / K 단어의 길이
road = [[] for _ in range(N)]                               # 단어의 길을 저장할 리스트 생성
word = []                                                   # 단어를 저장할 리스트 생성

for i in range(N):                                          # 단어의 수를 반복해서
    A = input().strip()                                     # A에 단어를 input 받는다
    B = []                                                  # 빈 리스트를 하나 생성하고
    for k in range(K):                                      # 단어의 길이를 반복해서
        B.append(ord(A[k]))                                 # 단어를 숫자로 바꿔 B에 append

    for j in enumerate(word):                               # word 단어를 enumerate로 반복해서
        cost = 0                                            # 비용을 저장할 변수를 생성한다
        for k in range(K):                                  # 단어의 길이를 반복해서
            cost += abs(B[k] - j[1][k])                     # B에 저장된 단어와 j번째 단어의 알파벳을 비교해서 그 차를 cost에 더한다
        else:                                               # 모든 알파벳을 반복했다면
            road[i].append([cost, j[0]])                    # road의 i번째에 [비용, 연결 단어]를 append
            road[j[0]].append([cost, i])                    # road의 j번째에 [비용, 연결 단어]를 append
    else:                                                   # word의 단어를 마쳤다면
        word.append(B)                                      # word에 B를 append

ans = 0                                                     # 최소 비용을 저장할 변수를 생성
tmp = [[0, 0]]                                              # 시작점을 넣고 tmp 리스트 생성
visited = [0] * N                                           # 방문 기록을 저장할 리스트 생성
minCost = [1e9] * N                                         # 최소 비용을 저장할 리스트 생성
cnt = 0                                                     # 방문한 노드의 수를 저장할 변수를 생성
while cnt < N:                                              # cnt가 N이 될때까지 반복해서
    cost, node = heapq.heappop(tmp)                         # tmp에서 cost와 node를 heappop
    if visited[node] == 0:                                  # node가 방문 전이라면
        if ans < cost:                                      # ans가 cost보다 작을 경우에
            ans = cost                                      # ans를 cost로 바꿔 저장하고
        visited[node] = 1                                   # node를 방문표시한다
        cnt += 1                                            # N에 1을 더한다
        for r in road[node]:                                # node와 연결된 단어를 반복해서
            if visited[r[1]] == 0 and minCost[r[1]] > r[0]: # 해당 단어가 방문 전이고 저장된 최소 비용이 현재 비용보다 크다면
                minCost[r[1]] = r[0]                        # 최소비용을 현재비용으로 바꿔 저장하고
                heapq.heappush(tmp, r)                      # tmp에 heappush한다
print(ans)                                                  # ans를 출력한다