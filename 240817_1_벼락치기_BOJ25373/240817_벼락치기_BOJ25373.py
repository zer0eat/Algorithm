# 벼락치기_BOJ25373

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

# input 받기
N = int(input())            # 뵈야하는 video의 수를 input 받고
if N >= 28:                 # 비디오가 28개 이상이라면
    video = N // 7          # 7일간 나눠볼 비디오의 수를 저장하고
    if N % 7:               # 7일간 볼 비디오가 나눠떨어지지 않는다면
        video += 1          # 한개를 더 추가한다
    print(video+3)          # 첫날 볼 비디오의 수를 출력한다
else:                       # 비디오가 28개 보다 작다면
    video = 0               # 볼 수 있는 비디오를 저장할 변수를 생성하고
    for n in range(1, 8):   # 1부터 7까지 비디오를 반복해서
        video += n          # 볼 수 있는 비디오의 수를 더한다
        if video >= N:      # 봐야할 비디오보다 볼 수 있는 비디오의 수가 더 커졌다면
            print(n)        # 첫날 볼 비디오의 수를 출력하고
            break           # for문을 break 한다