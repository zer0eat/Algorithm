# 정육각형과 삼각형_BOJ14264

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
L = int(input())        # 육각형의 한변을 input받고   
print(3**0.5*L*L/2/2)   # 가장 작은 삼각형의 넓이를 출력한다