# 빗물_BOJ14719

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
H, W = map(int, input().split())            # H 세로의 길이 / W 가로의 길이를 input 받고
height = list(map(int, input().split()))    # 각 줄의 높이를 리스트로 input 받고
jido = [[0]*W  for _ in range(H)]           # 높이를 표시할 행렬을 만든다
for i in range(H):                          # 행을 반복하고
    for j in range(W):                      # 열을 반복해서
        if height[j] > i:                   # j열의 높이가 i보다 높다면
            jido[i][j] = 1                  # 높이 표시를 해준다
rain = 0                                    # 빗물이 고인 양을 저장할 변수를 생성하고
for i in range(H):                          # 행을 반복하고
    s = -1                                  # 시작 위치를 저장할 변수를 생성하고
    for j in range(W):                      # 열을 반복해서
        if s == -1:                         # 시작 위치가 -1일 때
            if jido[i][j] == 1:             # j열의 i행이 블록이라면
                s = j                       # 시작점으로 j열을 설정한다
        else:                               # 시작점이 설정됐다면
            if jido[i][j] == 1:             # j열의 i행이 블록이라면
                for k in range(s+1, j):     # 시작점부터 j열 사이에
                    jido[i][k] = 2          # 빗물을 채우고
                    rain += 1               # 빗물의 수를 추가한다
                else:                       # 모든 반복을 마쳤다면
                    s = j                   # 시작점을 j열로 설정한다
print(rain)                                 # 빗물의 양을 출력한다