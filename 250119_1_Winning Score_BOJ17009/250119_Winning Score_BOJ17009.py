# Winning Score_BOJ17009

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = 0, 0             # 점수를 저장할 변수를 생성하고
for a in range(3,0,-1): # 점수를 반복해서
    A += a*int(input()) # A가 득점한 점수에 추가한다
for b in range(3,0,-1): # 점수를 반복해서
    B += b*int(input()) # B가 득점한 점수에 추가한다
if A > B:               # A가 더 많이 득점했다면
    print('A')          # A를 출력하고
elif A < B:             # B가 더 많이 득점했다면
    print('B')          # B를 출력하고
else:                   # 동점이라면
    print('T')          # T를 출력한다