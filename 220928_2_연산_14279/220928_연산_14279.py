# 연산_14279

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# deque import
from collections import deque

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복할 때
    N, M = map(int, input().split())                # N 시작점이 되는 숫자 / M 결과가 되는 숫자

    visited = [0] * 1000000                         # 중간 과정중 겹치는 숫자를 제거해 주기 위한 방문리스트를 생성

    q = deque([[M, 0]])                             # deque를 생성해준다

    while 1:                                        # break 될때까지 반복해서
        A = q.popleft()                             # q의 가장 왼쪽에 있는 요소를 빼내 A에 저장한다

        if A[0] % 2 == 0 and (A[0] // 2) != N and visited[A[0] // 2] == 0:                          # A[0]가 짝수이고/ 나눈 숫자가 N이 아니면서 / 방문한 적이 없을 때
            q.append([A[0] // 2, A[1] + 1])         # 나눈값과 연산횟수를 리스트 형태로 q에 append
            visited[A[0] // 2] = 1                  # 연산 결과를 visited에 체크
        elif A[0] % 2 == 0 and A[0] // 2 == N:      # 만약 N에 도달 했다면
            print(f'#{t+1}', A[1] + 1)              # 연산 횟수를 출력하고 반복문을 종료한다
            break

        if (A[0] + 1) != N and A[0] + 1 < 1000000 and visited[A[0] + 1] == 0:                      # 더한 숫자가 N이 아니면서 / 1000000 보다 작은 숫자 이고 /방문한 적이 없을 때
            q.append([A[0] + 1, A[1] + 1])          # 1을 더한 값과 연산횟수를 리스트 형태로 q에 append
            visited[A[0] + 1] = 1                   # 연산 결과를 visited에 체크
        elif (A[0] + 1) == N:                       # 만약 N에 도달 했다면
            print(f'#{t+1}', A[1] + 1)              # 연산 횟수를 출력하고 반복문을 종료한다
            break

        if (A[0] - 1) != N and visited[A[0] - 1] == 0:                                              # 뺀 숫자가 N이 아니면서 / 방문한 적이 없을 때
            q.append([A[0] - 1, A[1] + 1])          # 1을 뺀 값과 연산횟수를 리스트 형태로 q에 append
            visited[A[0] - 1] = 1                   # 연산 결과를 visited에 체크
        elif (A[0] - 1) == N:                       # 만약 N에 도달 했다면
            print(f'#{t+1}', A[1] + 1)              # 연산 횟수를 출력하고 반복문을 종료한다
            break

        if (A[0] + 10) != N and A[0] + 10 < 1000000 and visited[A[0] + 10] == 0:                     # 더한 숫자가 N이 아니면서 / 1000000 보다 작은 숫자 이고 /방문한 적이 없을 때
            q.append([A[0] + 10, A[1] + 1])         # 10을 더한 값과 연산횟수를 리스트 형태로 q에 append
            visited[A[0] + 10] = 1                  # 연산 결과를 visited에 체크
        elif (A[0] + 10) == N:                      # 만약 N에 도달 했다면
            print(f'#{t+1}', A[1] + 1)              # 연산 횟수를 출력하고 반복문을 종료한다
            break