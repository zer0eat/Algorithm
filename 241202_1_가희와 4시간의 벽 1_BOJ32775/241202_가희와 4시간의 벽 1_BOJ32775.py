# 가희와 4시간의 벽 1_BOJ32775

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = int(input())                # 철도 이동 인구를 input받고
F = int(input())                # 비행기 이동 인구를 input받고
if S <= F:                      # 비행기의 이동 인구가 더 많으면
    print('high speed rail')    # high speed rail를 출력한다
else:                           # 철도 이동 인구가 더 많으면
    print('flight')             # flight를 출력한다