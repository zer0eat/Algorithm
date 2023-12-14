# 순열 사이클_BOJ10451

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def dfs(N):
    if visited[N] == 0:                     # N이 방문 전이라면
        visited[N] = 1                      # 방문표시를 하고
        dfs(lst[N]-1)                       # N과 연결된 순열로 dfs 탐색한다
    return                                  # N이 방문한 원소라면 return 한다

T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트 케이스를 반복해서
    N = int(input())                        # 순열의 크기를 input 받고
    lst = list(map(int, input().split()))   # 순열을 input받는다
    visited = [0]*N                         # 방문표시를 할 리스트를 생성하고
    ans = 0                                 # 사이클의 개수를 저장할 변수를 생성한다
    for i in range(N):                      # 순열의 크기를 반복해서
        if visited[i] == 0:                 # i번이 아직 방문 전이라면
            dfs(i)                          # dfs 함수로 탐색을 시작한다
            ans += 1                        # 탐색을 마쳤다면 사이클 하나를 추가한다
    print(ans)                              # 모든 순열을 탐색했다면 사이클의 수를 출력한다