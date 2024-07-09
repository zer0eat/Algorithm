# 팀 나누기_BOJ13866

# input.txt
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a, b, c, d = map(int, input().split())  # 4명의 선수의 실력을 input 받고
print(abs(a+d-b-c))                     # 두팀으로 나누었을 때 실력차가 가장 낮은 값을 출력한다