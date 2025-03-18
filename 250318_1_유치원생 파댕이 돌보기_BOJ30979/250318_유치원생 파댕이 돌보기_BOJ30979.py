# 유치원생 파댕이 돌보기_BOJ30979

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                    # 돌봐야하는 시간을 input 받고
N = int(input())                    # 사탕의 수를 input 받는다
F = list(map(int, input().split())) # 사탕의 맛을 리스트로 input 받고
if T <= sum(F):                     # 돌봐야하는 시간동안 사탕을 줄 수 있다면
    print('Padaeng_i Happy')        # Happy를 출력하고
else:                               # 돌봐야하는 시간동안 사탕이 모자라면
    print('Padaeng_i Cry')          # cry를 출력한다