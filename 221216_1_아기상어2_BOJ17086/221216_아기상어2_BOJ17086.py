# 아기상어2_BOJ17086

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())                       # N 행의 길이 / M 열의 길이
shark = []                                                          # 상어가 있는 행렬을 저장할 빈 리스트 생성
visited = [[0]*M for _ in range(N)]                                 # 안전지역을 표시할 행렬을 N*M의 크기로 생성

for _ in range(N):                                                  # 행의 길이만큼 반복해서
    shark.append(list(map(int, sys.stdin.readline().split())))      # input받은 리스트를 shark 리스트에 append 한다

dx = [0, 1, 0, -1]                                                  # 우/하/좌/상 순으로 행의 이동
dy = [1, 0, -1, 0]                                                  # 우/하/좌/상 순으로 열의 이동

if N > M:                                                           # 행이 열보다 길면
    big = N                                                         # big에 N의 길이를 저장
else:                                                               # 열이 행보다 길면
    big = M                                                         # big에 M의 길이를 저장

for i in range(N):                                                  # 행을 반복하고
    for j in range(M):                                              # 열을 반복해서
        if shark[i][j] == 0:                                        # 상어가 없는 구역이면
            flag = False                                            # flag를 False로 설정하고
            for q in range(2, big*2, 2):                            # 2의 배수로 행렬 중 더 긴 길이의 2배까지 2칸 씩 증가하도록 반복해서
                if flag == True:                                    # flag가 True이면
                    break                                           # for문을 종료한다
                for k in range(4):                                  # 우/하/좌/상 순으로 반복해서
                    if flag == True:                                # flag가 True이면
                        break                                       # for문을 종료한다
                    if k == 0:                                      # k가 0일 때
                        for p in range(1, q+1):                     # 1부터 q까지 반복해서
                            if 0 <= i-(q//2)+dx[k]*p < N and 0 <= j-(q//2)+dy[k]*p < M: # 중심 위치에서 왼쪽 위 대각선부터 오른쪽으로 이동할 때 행렬 내라면
                                if shark[i-(q//2)+dx[k]*p][j-(q//2)+dy[k]*p] == 0:      # 그 지역에 상어가 없으면
                                    pass                            # 패스
                                else:                               # 상어가 있다면
                                    visited[i][j] = q//2            # 안전지역의 길이를 q//2의 값으로 저장하고
                                    flag = True                     # flag를 True로 바꾸고
                                    break                           # for문을 종료한다
                    elif k == 1:                                    # k가 1일 때
                        for p in range(1, q+1):                     # 1부터 q까지 반복해서
                            if 0 <= i-(q//2)+dx[k]*p < N and 0 <= j+(q//2)+dy[k]*p < M: # 중심 위치에서 오른쪽 위 대각선부터 아래쪽으로 이동할 때 행렬 내라면
                                if shark[i-(q//2)+dx[k]*p][j+(q//2)+dy[k]*p] == 0:      # 그 지역에 상어가 없으면
                                    pass                            # 패스
                                else:                               # 상어가 있다면
                                    visited[i][j] = q//2            # 안전지역의 길이를 q//2의 값으로 저장하고
                                    flag = True                     # flag를 True로 바꾸고
                                    break                           # for문을 종료한다
                    elif k == 2:                                    # k가 2일 때
                        for p in range(1, q+1):                     # 1부터 q까지 반복해서
                            if 0 <= i+(q//2)+dx[k]*p < N and 0 <= j+(q//2)+dy[k]*p < M: # 중심 위치에서 오른쪽 아래 대각선부터 왼쪽으로 이동할 때 행렬 내라면
                                if shark[i+(q//2)+dx[k]*p][j+(q//2)+dy[k]*p] == 0:      # 그 지역에 상어가 없으면
                                    pass                            # 패스
                                else:                               # 상어가 있다면
                                    visited[i][j] = q//2            # 안전지역의 길이를 q//2의 값으로 저장하고
                                    flag = True                     # flag를 True로 바꾸고
                                    break                           # for문을 종료한다
                    elif k == 3:                                    # k가 3일 때
                        for p in range(1, q+1):                     # 1부터 q까지 반복해서
                            if 0 <= i+(q//2)+dx[k]*p < N and 0 <= j-(q//2)+dy[k]*p < M: # 중심 위치에서 왼쪽 아래 대각선부터 위쪽으로 이동할 때 행렬 내라면
                                if shark[i+(q//2)+dx[k]*p][j-(q//2)+dy[k]*p] == 0:      # 그 지역에 상어가 없으면
                                    pass                            # 패스
                                else:                               # 상어가 있다면
                                    visited[i][j] = q//2            # 안전지역의 길이를 q//2의 값으로 저장하고
                                    flag = True                     # flag를 True로 바꾸고
                                    break                           # for문을 종료한다

ans = 0                                                             # 정답을 저장할 변수를 생성하고
for i in range(N):                                                  # 행을 반복하고
    for j in range(M):                                              # 열을 반복해서
        if visited[i][j] > ans:                                     # 안전지역이 ans보다 더 크다면
            ans = visited[i][j]                                     # ans를 더 넓은 안전지역 값으로 바꾸고
print(ans)                                                          # 정답을 출력한다
