# 색칠하기_4836

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                # 테스트 케이스
for t in range(T):                                              # 테스트 케이스 수만큼 반복
    N = int(input())                                            # N = 칠할 영역의 개수
    arr = [list(map(int, input().split())) for _ in range(N)]   # 칠할 영역을 arr 리스트에 받음
    visited = [[''] * 10 for _ in range(10)]                    # 칠할 영역을 칠 할 빈 도화지

    for a in range(len(arr)):                                   # 칠할 영역의 수만큼 반복할 때
        for i in range(arr[a][0], arr[a][2] + 1):               # i는 칠할 행의 길이
            for j in range(arr[a][1], arr[a][3] + 1):           # j는 칠할 열의 길이
                if arr[a][4] == 1:                              # 칠할 영역에 표시해야할 것이 color 1이라면
                    visited[i][j] += 'R'                        # 도화지에 R로 표시
                elif arr[a][4] == 2:                            # 칠할 영역에 표시해야할 것이 color 2이라면
                    visited[i][j] += 'B'                        # 도화지에 B로 표시

    cnt = 0                                                     # 겹친 곳의 숫자를 저장할 변수
    for i in range(10):                                         # visited의 행렬의 행의 길이 만큼 반복
        for j in range(10):                                     # visited의 행렬의 열의 길이 만큼 반복
            if 'R' in visited[i][j]:
                if 'B' in visited[i][j]:                        # 'R', 'B'로 칠해진 곳이 나오면
                    cnt += 1                                    # 카운트를 하나 센다

    print(f'#{t+1}', cnt)                                       # 카운트를 출력