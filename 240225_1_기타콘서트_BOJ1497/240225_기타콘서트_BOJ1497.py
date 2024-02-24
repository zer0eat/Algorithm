# 기타콘서트_BOJ1497

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                    # N 기타의 수 / M 곡의 수를 input 받고
guitar = [list(input().split()) for _ in range(N)]  # 기타 이름과 칠 수있는 노래 목록을 리스트로 input 받는다
song = 0                                            # 연주할 수 있는 노래의 수를 저장할 변수를 생성하고
ans = 1e9                                           # 필요한 기타의 수를 저장할 변수를 생성한다

def recur(dep, need):
    global song, ans                                # song, and를 글로벌 변수로 선언하고
    if dep == N:                                    # dep이 기타의 수와 같다면
        visited = [0]*M                             # 연주할 수 있는 노래를 저장할 리스트를 생성하고
        for n in need:                              # 필요한 기타의 목록을 반복해서
            for i in range(M):                      # 기타별 연주가능한 노래를 반복해서
                if guitar[n][1][i] == 'Y':          # i번째 노래가 연주 가능하다면
                    visited[i] = 1                  # i번째 노래를 연주할 수 있다고 표시한다
        if sum(visited) >= song:                    # song보다 현재 기타로 연주할 수 있는 노래가 같거나 많다면
            song = sum(visited)                     # song을 현재 기타로 연주할 수 있는 수로 저장하고
            ans = min(ans, len(need))               # 필요한 기타의 최소값을 저장한 후
        return                                      # return한다
    need.append(dep)                                # dep번째 기타를 append하고
    recur(dep+1, need)                              # 깊이 dep+1부터 필요한 기타의 수를 탐색한다
    need.pop()                                      # dep번째 기타를 pop하고
    recur(dep+1, need)                              # 깊이 dep+1부터 필요한 기타의 수를 탐색한다

recur(0, [])                                        # 깊이 0부터 필요한 기타의 수를 탐색한다
if ans:                                             # 정답이 0이 아니라면
    print(ans)                                      # 필요한 기타의 수를 출력한다
else:                                               # 정답이 0이라면
    print(-1)                                       # 연주할 수 있는 곡이 없으므로 -1을 출력한다