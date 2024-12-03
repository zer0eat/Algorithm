# An Easy-Peasy Problem_BOJ30214.py

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
s1, s2 = map(int, input().split())  # s1 트레비스가 푼 문제, s2 전체 문제를 input 받고
if s1 == 0:                         # 푼 문제가 없으면
    print('H')                      # H를 출력하고
elif s2/s1 > 2:                     # 반보다 못풀었다면
    print('H')                      # H를 출력하고
else:                               # 반 이상 풀었다면
    print('E')                      # E를 출력한다