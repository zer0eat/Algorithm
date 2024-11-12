# Correct_BOJ26307

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
HH, MM = map(int, input().split())  # 시와 분을 input 받고
print((HH-9)*60 + MM)               # 걸린 시간을 출력한다