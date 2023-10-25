# 스타트와 링크_BOJ14889

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# input 받기
N = int(input())                                                # 축구에 참여하는 사람의 수를 input 받고
ability = [list(map(int, input().split())) for _ in range(N)]   # 능력치를 행렬로 input 받아 저장한다

def swap01(lst):
    swaplst = [1 if i == 0 else 0 for i in lst]                 # lst의 원소가 1이면 0으로 0이면 1로 바꿔 swaplst에 저장한 후
    return swaplst                                              # swaplst를 return한다

def score(team):
    global ans                                                  # 두 팀의 능력치의 차이를 저장할 변수를 global로 선언하고
    t1 = 0                                                      # 팀1의 능력치를 저장할 변수를 생성하고
    t2 = 0                                                      # 팀2의 능력치를 저장할 변수를 생성한다
    for i in range(N):                                          # N명의 선수를 반복하고
        for j in range(N):                                      # N명의 선수를 반복해서
            if team[i] == team[j] and team[i] == 0:             # i와 j가 같은 팀이고 0을 배정 받았다면
                t1 += ability[i][j]                             # t1에 능력치를 더하고
            elif team[i] == team[j] and team[i] == 1:           # i와 j가 같은 팀이고 1을 배정 받았다면
                t2 += ability[i][j]                             # t2에 능력치를 더하고
    else:                                                       # 모든 선수를 탐색했다면
        ans = min(ans, abs(t1-t2))                              # 두팀의 전력차와 현재 저장된 전력차 중 더 작은 값을 ans에 저장하고
        return                                                  # return한다

def dfs(n):
    if sum(team) == N//2:                                       # team의 절반이 1번으로 배정받았다면
        if visited.get(str(team)) == None:                      # 현재 구성팀이 전에 구성된 적이 없을 경우에
            visited[str(team)] = 1                              # 현재 구성팀을 방문표시하고
            visited[str(swap01(team))] = 1                      # 상대팀도 방문표시한 후
            score(team)                                         # 두 팀의 전력차를 계산한다
    else:                                                       # team이 반으로 나누어지지 않았다면
        for i in range(n+1, N):                                 # n번 이후 선수를 반복해서
            team[i] = 1                                         # i번째 선수를 1번팀에 넣고
            dfs(i)                                              # dfs 탐색을 한다
            team[i] = 0                                         # 탐색하고 나왔다면 i번째 선수를 원래대로 돌려 놓는다
    return                                                      # return한다

ans = 100 * N                                                   # 두 팀의 능력치의 차이를 저장할 변수를 생성하고
visited = dict()                                                # 구성된 팀을 저장할 딕셔너리를 생성한 후
team = [0]*N                                                    # 팀구성을 할 리스트를 생성한다
team[0] = 1                                                     # 0번째 선수를 1번팀에 넣고
dfs(0)                                                          # dfs 탐색을 한다
print(ans)                                                      # 두 팀의 능력치의 차이의 최솟값을 출력한다