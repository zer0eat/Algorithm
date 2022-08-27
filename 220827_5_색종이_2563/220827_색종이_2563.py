# 색종이_2563

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from pprint import pprint

# input 받기
N = int(input())                                                # 색종이의 수
square = [list(map(int, input().split())) for n in range(N)]    # 색종이의 왼쪽 아래의 x 좌표와 y좌표를 리스트로 저장

# 리스트의 요소를 좌표가 아닌 크기가 1인 정사각형으로 표시
dohwaji = [[0] * 100 for _ in range(100)]                       # 색종이를 붙일 빈 도화지를 행렬로 만듬 / 좌표를 x 축을 대칭으로 뒤집은 형태

# 색종이의 넓이 구하기
while square:                                                   # square에 저장된 색종이를 다 붙일 때까지 반복
    c = square.pop(0)                                           # 색종이 하나를 꺼내서
    a, b = c                                                    # x 좌표를 a / y 좌표를 b에 저장
    for i in range(a, a+10):                                    # 한변의 길이가 10인 행을 반복하고
        for j in range(b, b+10):                                # 한변의 길이가 10인 열을 반복하여
            dohwaji[i][j] = 1                                   # 1X1 크기의 색종이를 dohwaji에 붙인다

# 칠한 영역 세기
cnt = 0                                                         # 색종이를 붙인 영역을 셀 변수
for d in dohwaji:                                               # 도화지의 각 행을 반복하며
    for z in d:                                                 # 하나하나 열을 찾아볼 때
        if z == 1:                                              # 1이 붙어있으면
            cnt += 1                                            # 하나를 카운트 한다

print(cnt)