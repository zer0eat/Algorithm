# 가희와 교통 요금_BOJ34655

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = input().split() # 내린 곳을 input받고
B = input().split() # 재탑승한 곳을 input받고
if A == B:          # 두 곳이 같다면
    print(0)        # 환승 요금을 받지 않고
else:               # 두 곳이 다르다면
    print(1550)     # 환승 요금을 1550 출력한다