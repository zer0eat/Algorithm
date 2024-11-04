# Site Score_BOJ20254

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
Ur, Tr, Uo, To = map(int, input().split())  # 푼 문제의 수를 input 받고
print(56*Ur+24*Tr+14*Uo+6*To)               # 점수를 출력한다