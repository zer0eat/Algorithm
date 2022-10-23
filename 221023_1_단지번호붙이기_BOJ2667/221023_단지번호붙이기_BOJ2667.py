# 단지번호붙이기_BOJ2667

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def color(i, j, cnt):                               # 단지내 동에 단지번호를 부여하는 함수
    global tmp                                      # tmp를 불러와서
    arr[i][j] = cnt                                 # 해당 동에 단지번호를 부여하고
    tmp += 1                                        # 동의 수를 1 올려준다
    for k in range(4):                              # 델타탐색 해서
        if 0 <= i+dx[k] < N and 0 <= j+dy[k] < N:   # 지도 내에 있는 곳에서
            if arr[i+dx[k]][j+dy[k]] == 1:          # 1이 표시된 동이 있다면
                color(i+dx[k], j+dy[k], cnt)        # 그 동의 좌표로 다시 color 함수를 돌린 후
    return tmp                                      # tmp를 return 한다

# input 받기
N = int(sys.stdin.readline())                       # 지도의 크기
arr = [list(map(int, input())) for _ in range(N)]   # arr에 지도를 행렬형태로 저장

dx = [-1, 0, 1, 0]                                  # 델타탐색 행 이동을 위한 리스트 (상우하좌)
dy = [0, 1, 0, -1]                                  # 데타탐색 열 이동을 위한 리스트 (상우하좌)

cnt = 1                                             # 단지 번호로 사용할 변수
ans = []                                            # 단지 안의 동수를 저장할 리스트 생성
for i in range(N):                                  # 행을 반복하고
    for j in range(N):                              # 열을 반복해서
        if arr[i][j] == 1:                          # 집이 있는 1이 나오면
            tmp = 0                                 # 동의 개수를 저장할 변수를 생성하고
            cnt += 1                                # 단지번호를 하나 올린 뒤
            ans.append(color(i, j, cnt))            # 함수를 돌려 같은 단지 안에 있는 집에 단지번호를 부여하고 단지 내 집 개수를 ans에 append

print(cnt-1)                                        # 단지의 수를 출력하고
ans.sort()                                          # 단지내 동의 수를 오름차순정렬해서
for a in ans:                                       # 동의 수를 반복해서
    print(a)                                        # 출력한다