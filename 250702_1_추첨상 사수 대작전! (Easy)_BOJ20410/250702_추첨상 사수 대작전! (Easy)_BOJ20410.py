# 추첨상 사수 대작전! (Easy)_BOJ20410

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
m, s, x1, x2 = map(int, input().split())            # 네 숫자를 input받고
for a in range(m):                                  # a가 될 수 있는 수를 반복하고
    for c in range(m):                              # b가 될 수 있는 수를 반복해서
        if x1 == (a*s+c)%m and x2 == (a*x1+c)%m:    # 조건을 만족한다면
            print(a, c)                             # a,c를 출력하고
            quit()                                  # 종료한다