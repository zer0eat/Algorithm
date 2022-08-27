# 색종이_BOJ10163

# input.txt 열기
import sys
sys.stdin = open('input3.txt')

# input 받기
N = int(input())                                    # 붙일 색종이의 수

dohwaji = [[0]*1001 for _ in range(1001)]           # 색종이를 붙일 도화지

for n in range(N):                                  # 색종이의 수만큼 반복 할 때
    paper = list(map(int, input().split()))         # 색종이의 정보를 paper에 input 받고
    x, y, L, H = paper                              # x(x좌표) = 0번 인덱스 / y(y좌표) = 1번 인덱스 / L(가로의 길이) = 2번 인덱스 / H(세로의 길이) = 3번 인덱스
    for i in range(x, x + L):                       # 행을 x좌표 부터 L만큼 반복할 때
        for j in range(y, y + H):                   # 열을 y좌표 부터 H만큼 반복할 때
            dohwaji[i][j] = n + 1                   # 해당 부분을 색종이 순서 번호로 표시한다

p = 1                                               # p의 번호를 가진 색종이를 찾기 위해
while p <= N:                                       # 색종이의 모든 번호를 찾을 때까지 반복하고
    cnt = 0                                         # 개수를 저장할 변수를 만든다
    for d in dohwaji:                               # 도화지의 행마다
        for s in d:                                 # 열로 움직이며 요소를 살펴 볼때
            if s == p:                              # p의 번호로 표시된 영역이 나오면
                cnt += 1                            # cnt에 1 추가한다
    else:                                           # 도화지 탐색이 끝나면
        print(cnt)                                  # 개수를 출력하고
        p += 1                                      # 다음 도화지로 넘어간다
