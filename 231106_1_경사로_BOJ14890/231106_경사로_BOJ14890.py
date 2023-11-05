# 경사로_BOJ14890

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, L = map(int, input().split())                                        # N 지도의 크기 / L 경사로의 길이를 input 받고
jido = [list(map(int, input().split())) for _ in range(N)]              # 각 칸의 높이를 행렬로 input 받는다

def raw_road(i):
    global L, ans                                                       # L, ans를 global 변수로 선언하고
    visited = [0] * N                                                   # 경사로 설치 여부를 저장할 리스트를 생성한다
    for j in range(N - L):                                              # 내리막길을 설치할 수 있는 길을 앞에서부터 반복해서
        start = jido[i][j]                                              # 현재 위치의 높이를 start에 저장하고
        if start - jido[i][j + 1] < 1:                                  # 다음 칸이 같거나 높다면 내리막길을 설치할 필요가 없으므로
            pass                                                        # pass한다
        elif start - jido[i][j + 1] == 1:                               # 다음 칸이 현재칸보다 1칸 낮다면
            visited[j + 1] = 1                                          # 내리막 경사로 설치 표시를 하고
            for t in range(2, L + 1):                                   # L개의 칸에 연속으로 설치해야하기 때문에 L번칸까지 반복해서
                if start - jido[i][j + t] == 1:                         # 해당칸도 현재칸보다 1칸 낮다면
                    visited[j + t] = 1                                  # 내리막 경사로 설치 표시를 하고
                else:                                                   # 1칸 차이가 아니라면
                    return                                              # 통행할 수 없는 길이므로 return 한다
        else:                                                           # 2칸 이상 차이가 난다면
            return                                                      # 통행할 수 없는 길이므로 return 한다

    for j in range(N - L, N - 1):                                       # 내리막길을 설치할 수 없는 길을 앞에서부터 반복해서
        start = jido[i][j]                                              # 현재 위치의 높이를 start에 저장하고
        if start - jido[i][j + 1] < 1:                                  # 다음 칸이 같거나 높다면 내리막길을 설치할 필요가 없으므로
            pass                                                        # pass한다
        else:                                                           # 내리막길이라면
            return                                                      # 통행할 수 없는 길이므로 return 한다

    for j in range(N - 1, L - 1, -1):                                   # 내리막길을 설치할 수 있는 길을 뒤에서부터 반복해서
        start = jido[i][j]                                              # 현재 위치의 높이를 start에 저장하고
        if start - jido[i][j - 1] < 1:                                  # 다음 칸이 같거나 높다면 내리막길을 설치할 필요가 없으므로
            pass                                                        # pass한다
        elif start - jido[i][j - 1] == 1 and visited[j - 1] == 0:       # 다음 칸이 현재칸보다 1칸 낮고 내리막길이 설치되지 않은 길이라면
            for t in range(2, L + 1):                                   # L개의 칸에 연속으로 설치해야하기 때문에 L번칸까지 반복해서
                if start - jido[i][j - t] == 1 and visited[j - t] == 0: # 해당칸도 현재칸보다 1칸 낮고 내리막길이 설치되지 않은 길이라면
                    pass                                                # pass한다
                else:                                                   # 1칸 차이가 아니거나 내리막길이 이미 설치가 되어있다면
                    return                                              # 통행할 수 없는 길이므로 return 한다
        else:                                                           # 2칸 이상 차이난다면
            return                                                      # 통행할 수 없는 길이므로 return 한다

    for j in range(L - 1, 0, -1):                                       # 내리막길을 설치할 수 없는 길을 뒤에서부터 반복해서
        start = jido[i][j]                                              # 현재 위치의 높이를 start에 저장하고
        if start - jido[i][j - 1] < 1:                                  # 다음 칸이 같거나 높다면 내리막길을 설치할 필요가 없으므로
            pass                                                        # pass한다
        else:                                                           # 내리막길이라면
            return                                                      # 통행할 수 없는 길이므로 return 한다
    ans += 1                                                            # 통행할 수 있는 길이므로 1 추가한다

def col_road(j):
    global L, ans                                                       # L, ans를 global 변수로 선언하고
    visited = [0] * N                                                   # 경사로 설치 여부를 저장할 리스트를 생성한다
    for i in range(N - L):                                              # 내리막길을 설치할 수 있는 길을 앞에서부터 반복해서
        start = jido[i][j]                                              # 현재 위치의 높이를 start에 저장하고
        if start - jido[i + 1][j] < 1:                                  # 다음 칸이 같거나 높다면 내리막길을 설치할 필요가 없으므로
            pass                                                        # pass한다
        elif start - jido[i + 1][j] == 1:                               # 다음 칸이 현재칸보다 1칸 낮다면
            visited[i + 1] = 1                                          # 내리막 경사로 설치 표시를 하고
            for t in range(2, L + 1):                                   # L개의 칸에 연속으로 설치해야하기 때문에 L번칸까지 반복해서
                if start - jido[i + t][j] == 1:                         # 해당칸도 현재칸보다 1칸 낮다면
                    visited[i + t] = 1                                  # 내리막 경사로 설치 표시를 하고
                else:                                                   # 1칸 차이가 아니라면
                    return                                              # 통행할 수 없는 길이므로 return 한다
        else:                                                           # 2칸 이상 차이가 난다면
            return                                                      # 통행할 수 없는 길이므로 return 한다

    for i in range(N - L, N - 1):                                       # 내리막길을 설치할 수 없는 길을 앞에서부터 반복해서
        start = jido[i][j]                                              # 현재 위치의 높이를 start에 저장하고
        if start - jido[i + 1][j] < 1:                                  # 다음 칸이 같거나 높다면 내리막길을 설치할 필요가 없으므로
            pass                                                        # pass한다
        else:                                                           # 내리막길이라면
            return                                                      # 통행할 수 없는 길이므로 return 한다

    for i in range(N - 1, L - 1, -1):                                   # 내리막길을 설치할 수 있는 길을 뒤에서부터 반복해서
        start = jido[i][j]                                              # 현재 위치의 높이를 start에 저장하고
        if start - jido[i - 1][j] < 1:                                  # 다음 칸이 같거나 높다면 내리막길을 설치할 필요가 없으므로
            pass                                                        # pass한다
        elif start - jido[i - 1][j] == 1 and visited[i - 1] == 0:       # 다음 칸이 현재칸보다 1칸 낮고 내리막길이 설치되지 않은 길이라면
            for t in range(2, L + 1):                                   # L개의 칸에 연속으로 설치해야하기 때문에 L번칸까지 반복해서
                if start - jido[i - t][j] == 1 and visited[i - t] == 0: # 해당칸도 현재칸보다 1칸 낮고 내리막길이 설치되지 않은 길이라면
                    pass                                                # pass한다
                else:                                                   # 1칸 차이가 아니거나 내리막길이 이미 설치가 되어있다면
                    return                                              # 통행할 수 없는 길이므로 return 한다
        else:                                                           # 2칸 이상 차이난다면
            return                                                      # 통행할 수 없는 길이므로 return 한다

    for i in range(L - 1, 0, -1):                                       # 내리막길을 설치할 수 없는 길을 뒤에서부터 반복해서
        start = jido[i][j]                                              # 현재 위치의 높이를 start에 저장하고
        if start - jido[i - 1][j] < 1:                                  # 다음 칸이 같거나 높다면 내리막길을 설치할 필요가 없으므로
            pass                                                        # pass한다
        else:                                                           # 내리막길이라면
            return                                                      # 통행할 수 없는 길이므로 return 한다
    ans += 1                                                            # 통행할 수 있는 길이므로 1 추가한다

ans = 0                                                                 # 통행가능한 길의 수를 저장할 변수를 생성하고
for i in range(N):                                                      # 지도의 크기를 반복해서
    raw_road(i)                                                         # i행의 통행여부를 확인하고
    col_road(i)                                                         # i열의 통행여부를 확인한다
print(ans)                                                              # 지나갈 수 있는 길의 개수를 출력한다