# 수학은 비대면강의입니다_BOJ19532

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a, b, c, d, e, f = map(int, input().split())    # a x의 계수 / b y의 계수 / c 상수 / d x의 계수 / e y의 계수 / f 상수
for x in range(-999, 1000):                     # x가 될 수 있는 -999부터 999까지 반복하고
    for y in range(-999, 1000):                 # y가 될 수 있는 -999부터 999까지 반복해서
        if a*x + b*y == c:                      # a*x + b*y = c를 만족하고
            if d*x + e*y == f:                  # d*x + e*y = f를 만족하여
                print(x, y)                     # 두 직선이 만나는 점의 좌표를 출력하고
                quit()                          # 종료한다