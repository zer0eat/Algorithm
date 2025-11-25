# OO0OO_BOJ34161

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
for n in range(10000):  # 10000개의 튜플을 반복해서
    print(-1)           # 답을 구할 수 없으므로 -1을 출력한다