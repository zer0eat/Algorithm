# 체육은 수학과목 입니다_BOJ32025

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
H = int(input())    # 사각형의 높이를 input 받고
W = int(input())    # 사각형의 너비를 input 받고
r = min(H, W)       # 사각형 중 짧은 변을 저장한 후
print(r * 50)       # 해당 변에 그릴 수 있는 가장 큰 원의 반지름을 출력한다