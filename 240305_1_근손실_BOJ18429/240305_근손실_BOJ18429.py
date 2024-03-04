# 근손실_BOJ18429

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())            # N 운동의 종류 / K 중량이 감소하는 무게를 input 받고
A = list(map(int, input().split()))         # 운동별 늘어나는 무게를 리스트로 input 받고
ans = 0                                     # 정답을 저장할 변수를 생성하고
visited = [0]*N                             # 방문표시를 할 리스트를 생성ㅎ나다

def recur(dep, weight):
    global ans                              # ans를 global로 선언하고
    if dep == N:                            # 모든 운동을 하면서 500 밑으로 내려간 적이 없다면
        ans += 1                            # 정답에 1을 추가한다
    for i in range(N):                      # 운동을 반복해서
        if visited[i]:                      # 이미 한 운동이라면
            continue                        # continue로 넘어간다
        if weight-K+A[i] >= 500:            # i 운동을 했을 때 중량이 500 이상이라면
            visited[i] = 1                  # i를 운동 표시하고
            recur(dep+1, weight-K+A[i])     # dep+1 깊이로 탐색한다
            visited[i] = 0                  # i를 운동 표시 해제한다

recur(0, 500)                               # 0 깊이로 탐색한다
print(ans)                                  # 운동 기간동안 항상 중량이 500 이상이 되도록 하는 경우의 수를 출력한다