# 立方体 (Cube)_BOJ24082

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
x = int(input())    # 한 변을 input 받고
print(x**3)         # 입방체의 부피를 출력한다