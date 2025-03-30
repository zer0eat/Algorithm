# 구구단표_BOJ32710

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 숫자를 input 받고
for i in range(1, 10):      # 1부터 9까지 반복하고
    for j in range(1, 10):  # 1부터 9까지 반복해서
        if i * j == N:      # 두수의 곱이 N이라면
            print(1)        # 1을 출력하고
            quit()          # 종료한다
print(0)                    # 구구단에 없는 수라면 0을 출력한다