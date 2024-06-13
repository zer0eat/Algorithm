# 과자_BOJ10156

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
K, N, M = map(int, input().split()) # K 과자 한개의 가격 / N 과자의 개수 / M 동수가 가진 돈을 input 받고
ans = (K * N) - M                   # 사려는 가격에서 가진돈을 빼준 후
if ans > 0:                         # 돈이 모자라다면
    print(ans)                      # 모자란 액수를 출력하고
else:                               # 돈이 모자라지 않는다면
    print(0)                        # 0을 출력한다