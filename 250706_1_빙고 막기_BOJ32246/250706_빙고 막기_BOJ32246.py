# 빙고 막기_BOJ32246

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 빙고판의 길이를 input받고
if N == 2:          # 빙고판의 길이가 2라면
    print(3)        # 3칸을 막는 것으로 출력하고
else:               # 빙고판의 길이가 2가 아니라면
    print(N)        # N칸을 막는 것으로 출력한다