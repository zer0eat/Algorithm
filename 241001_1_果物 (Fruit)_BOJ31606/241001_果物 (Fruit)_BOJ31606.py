# 果物 (Fruit)_BOJ31606

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X = int(input())    # 사과의 수를 input 받고
Y = int(input())    # 귤의 수를 input 받고
print(X+Y+3)        # 사과와 귤과 바나나의 수를 출력한다