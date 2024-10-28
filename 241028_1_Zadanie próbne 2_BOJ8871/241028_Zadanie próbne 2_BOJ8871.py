# Zadanie próbne 2_BOJ8871

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 라운드를 input 받고
print(2*(N+1), 3*(N+1)) # 최소 득점수와 최대 득점수를 출력한다