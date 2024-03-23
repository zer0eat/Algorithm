# 숫자고르기_BOJ2668

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 정수의 개수를 input 받고
dic = dict()                                    # 카드순서와 번호를 저장할 딕셔너리를 생성한다
cnt = 1                                         # 카드번호를 나타낼 변수를 생성하고
for _ in range(N):                              # 카드의 개수를 반복해서
    dic[cnt] = int(input())                     # cnt번 카드에 적혀있는 번호를 딕셔너리 원소로 생성하고
    cnt += 1                                    # 다음번 카드로 넘어간다
ans = []                                        # 정답을 저장할 리스트를 생성한다

def dfs(s, e):
    visited[s] = True                           # s번 카드를 방문표시하고
    if visited[dic[s]] == 0:                    # s번에 적힌 번호가 방문 전이라면
        dfs(dic[s], e)                          # s번의 적힌 번호의 카드 안에 e가 적혀있는지 탐색한다
    elif visited[dic[s]] and dic[s] == e:       # s번에 적힌 번호가 방문했고 s번의 적힌 카드가 e와 같다면
        ans.append(e)                           # 사이클이 돌 수 있으므로 e를 정답에 append한다

for i in range(1, N+1):                         # 카드번호를 반복해서
    visited = [0]*(N+1)                         # 방문표시를 할 리스트를 생성하고
    dfs(i, i)                                   # i번째 카드가 사이클이 도는지 탐색한다
print(len(ans))                                 # 정답의 개수를 출력하고
for a in ans:                                   # 정답의 원소를 반복해서
    print(a)                                    # 뽑힌 카드원소를 하나씩 출력한다