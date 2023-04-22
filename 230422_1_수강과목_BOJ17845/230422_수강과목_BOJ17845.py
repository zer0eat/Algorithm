# 수강과목_BOJ17845

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                # N 최대공부시간 / K 과목수
visited = [[0] * (N+1) for _ in range(M)]       # 행을 과목수 만큼 열의 인덱스 최대가 최대 공부시간이 되도록 행렬을 생성

I, T = map(int, input().split())                # I 중요도, T 공부시간을 input 받아
for v in range(N+1):                            # 최대공부시간까지 반복한다
    if v >= T:                                  # v가 해당과목을 공부할 수 있는 시간 이상이 된다면
        visited[0][v] = I                       # visited의 v인덱스에 중요도 I를 저장한다

for m in range(1, M):                           # 두번째 행부터 반복해서
    I, T = map(int, input().split())            # I 중요도, T 공부시간을 input 받아
    for v in range(N+1):                        # 최대공부시간까지 반복한다
        if v >= T:                              # v가 해당과목을 공부할 수 있는 시간 이상이 된다면
            visited[m][v] = max(visited[m-1][v-T]+I, visited[m-1][v])   # 해당과목을 공부할 때 중요도와 해당과목을 공부하고 남은 시간만큼의 중요도를 더한값, 이전 행의 v시간만큼 공부했을 때 중요도 중 더 큰값을 저장한다
        else:                                   # v가 해당과목을 공부할 수 있는 시간 미만이라면
            visited[m][v] = visited[m-1][v]     # 이전 행의 v시간만큼 공부했을 때 중요도를 저장한다
print(visited[m][-1])                           # 모든 반복이 끝났다면 마지막행 마지막열 원소를 출력해 최대 중요도를 출력한다
