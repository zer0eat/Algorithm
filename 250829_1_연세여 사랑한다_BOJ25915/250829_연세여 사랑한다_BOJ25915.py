# 연세여 사랑한다_BOJ25915

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
c = input().strip()             # 시작 발판의 문자를 input받고
print(abs(ord(c)-ord('I'))+84)  # 움직여야하는 횟수를 출력한다