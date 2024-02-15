# N과 M (1)_BOJ15649

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # N 자연수의 수 / M 수열의 길이
ans = [0]*M                         # 수열의 길이 만큼 리스트를 생성하고
visited = [0]*(N+1)                 # 자연수 유무를 표시할 리스트를 생성한다

def recur(dep):
    if dep == M:                    # M 깊이가 되었다면
        print(*ans)                 # 수열을 출력하고
        return                      # return해서 종료한다
    for i in range(1, N+1):         # 자연수를 반복해서
        if visited[i]:              # i가 수열안에 있다면
            continue                # 건너뛴다
        visited[i] = True           # i를 방문표시하고
        ans[dep] = i                # dep깊이에 자연수 i를 저장하고
        recur(dep+1)                # dep를 하나 늘려 recur 함수를 진행한다
        visited[i] = False          # i를 방문표시를 삭제한다

recur(0)                            # 0의 깊이 부터 반복해서