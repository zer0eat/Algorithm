# 직사각형네개의합집합의면적구하기_BOJ2669

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
square = [list(map(int, input().split())) for _ in range(4)]    # 사각형의 좌하 모서리와 우상 모서리의 x,y 좌표를 리스트로 저장

dohwaji = [[0]*101 for _ in range(101)]                         # 직사각형을 붙일 빈 도화지를 생성

for s in square:                                                # 사각형 정보를 반복할 때
    for i in range(s[0], s[2]):                                 # x 좌표의 길이를 반복하고
        for j in range(s[1], s[3]):                             # y 좌표의 길이를 반복해서
            dohwaji[i][j] = 1                                   # 해당하는 부분을 1로 표시한다

cnt = 0                                                         # 직사각형의 넓이를 세기위한 변수
for k in range(101):                                            # 도화지의 행을 반복하고
    for h in range(101):                                        # 도화지의 열을 반복해서
        if dohwaji[k][h] == 1:                                  # 1이 표시된 부분이 나오면
            cnt += 1                                            # cnt에 1을 추가한다

print(cnt)