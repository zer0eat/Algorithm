# 가희와 4시간의 벽 2_BOJ32776

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = int(input())                        # 기차의 이동 시간을 input 받고
Ma, F, Mb = map(int, input().split())   # 비행기의 이동 시간을 input 받고
if S > Ma + F + Mb and S > 240:         # 비행기 이동시간이 짧고 기차 이동 시간이 4시간보다 오래걸리면
    print('flight')                     # 비행을 하고
else:                                   # 기차 이동이 4시간 이하이거나 기차 이동시간이 짧으면
    print('high speed rail')            # 기차로 이동한다