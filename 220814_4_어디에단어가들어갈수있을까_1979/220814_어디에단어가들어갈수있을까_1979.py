# 어디에 단어가 들어갈 수 있을까_1979

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N, K = input().split()
    N = int(N) # 퍼즐의 행렬의 크기
    K = int(K) # 퍼즐 안에 들어가는 단어 중 찾아야 할 길이
    arr = [list(map(int, input().split())) for _ in range(N)] # 퍼즐 그리기 / 1 = 입력 칸 / 0 = 막힌 칸

    # K의 길이를 같는 칸 찾기
    cnt = 0 # 길이가 K인 칸의 수
    blank = 0
    # 가로로 찾기
    for i in range(N):
        for j in range(N):
            # 1이 들어 있으면 빈칸을 하나씩 센다
            if arr[i][j] == 1:
                blank += 1
            # 0이 나왔을 때 앞서 나온 1의 개수가 K개면 1을 더하고 blank를 0으로 초기화한다
            elif arr[i][j] == 0:
                if blank == K:
                    cnt += 1
                blank = 0
        # 한 행을 다 돌렸을 때 1의 개수가 K개면 1을 더하고 blank를 0으로 초기화한다
        else:
            if blank == K:
                cnt += 1
            blank = 0

    # 세로로 찾기
    for i in range(N):
        for j in range(N):
            # 1이 들어 있으면 빈칸을 하나씩 센다
            if arr[j][i] == 1:
                blank += 1
            # 0이 나왔을 때 앞서 나온 1의 개수가 K개면 1을 더하고 blank를 0으로 초기화한다
            elif arr[j][i] == 0:
                if blank == K:
                    cnt += 1
                blank = 0
        # 한 열을 다 돌렸을 때 1의 개수가 K개면 1을 더하고 blank를 0으로 초기화한다
        else:
            if blank == K:
                cnt += 1
            blank = 0
    print(f'#{t + 1}', cnt)

