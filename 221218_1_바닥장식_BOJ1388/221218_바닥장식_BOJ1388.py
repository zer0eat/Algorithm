# 바닥장식_BOJ1388

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())               # N 행의 길이 / M 열의 길이
visited = [[0]*M for _ in range(N)]                         # N*M 행렬이 모두 0인 리스트 생성
floor = []                                                  # 바닥장식을 저장할 빈 리스트 생성

for _ in range(N):                                          # 행을 반복해서
    floor.append(list(sys.stdin.readline().strip()))        # floor에 바닥장식의 한 행 input 받아 append 한다

cnt = 0                                                     # 바닥장식의 개수를 저장할 변수를 생성하고
for i in range(N):                                          # 행을 반복하고
    for j in range(M):                                      # 열을 반복해서
        if visited[i][j] == 0:                              # 확인하지 않은 바닥장식이라면
            visited[i][j] = 1                               # 확인 표시를 하고
            cnt += 1                                        # 바닥장식의 개수를 1 증가시킨다
            if floor[i][j] == '-':                          # 확인한 바닥장식이 - 라면
                q = j                                       # q에 열의 위치를 저장하고
                while 1:                                    # break가 나올때까지 반복해서
                    q += 1                                  # 한 열씩 이동하면서
                    if q < M and floor[i][q] == '-':        # 열이 M보다 작고 - 인 경우에만
                        visited[i][q] = 1                   # 확인표시를 하고
                    else:                                   # 나머지는
                        break                               # while문을 break한다
            elif floor[i][j] == '|':                        # 확인한 바닥장식이 | 라면
                p = i                                       # p에 행의 위치를 저장하고
                while 1:                                    # break가 나올때까지 반복해서
                    p += 1                                  # 한 행씩 이동하면서
                    if p < N and floor[p][j] == '|':        # 행이 N보다 작고 | 인 경우에만
                        visited[p][j] = 1                   # 확인표시를 하고
                    else:                                   # 나머지는
                        break                               # while문을 break한다

print(cnt)                                                  # 바닥장식의 개수를 출력한다