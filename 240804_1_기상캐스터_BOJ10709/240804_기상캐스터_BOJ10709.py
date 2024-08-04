# 기상캐스터_BOJ10709

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
H, W = map(int, input().split())                        # 하늘의 가로와 세로의 길이를 input 받고
sky = [list(input().strip()) for h in range(H)]         # 하늘의 구름 상태를 리스트로 input 받는다
ans = [[-1]*W for h in range(H)]                        # 정답을 저장할 리스트를 생성하고
for w in range(W):                                      # 하늘의 가로 높이를 반복해서
    for n in range(H):                                  # 하늘의 세로를 반복하고
        for m in range(W-1, -1, -1):                    # 하늘의 가로를 뒤에서부터 반복해서
            if sky[n][m] == 'c' and ans[n][m] == -1:    # 현재 하늘에 구름이 있고 한번도 구름이 도착한 적이 없다면
                ans[n][m] = w                           # 현재 시간을 저장한다
            if m == 0:                                  # 가로의 맨 앞지점이라면
                sky[n][m] = '.'                         # 다가올 구름이 없으므로 .을 저장하고
            else:                                       # 가로의 맨 앞지점이 아니라면
                sky[n][m] = sky[n][m-1]                 # 서쪽의 구름을 현재 위치에 저장한다
for a in ans:                                           # 구름이 도착한 시간을 저장한 리스트를 반복해서
    print(*a)                                           # 구름의 도착시간을 출력한다