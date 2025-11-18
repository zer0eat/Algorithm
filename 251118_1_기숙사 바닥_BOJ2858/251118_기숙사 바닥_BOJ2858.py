# 기숙사 바닥_BOJ2858

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
R, B = map(int, input().split())            # 빨간색 타일과 갈색 타일을 input받고
ans = R + B                                 # 전체 넓이를 구한다
for w in range(3, ans + 1):                 # 너비를 3부터 전체 넓이까지 반복하면서
    if ans % w == 0:                        # 전체 넓이가 너비로 나누어 떨어지면
        h = ans // w                        # 높이를 구하고
        if (w - 2) * (h - 2) == B:          # (너비-2)*(높이-2)가 갈색 타일 개수와 같으면
            print(h, w)                     # 너비와 높이를 출력하고 
            break                           # for문을 종료한다