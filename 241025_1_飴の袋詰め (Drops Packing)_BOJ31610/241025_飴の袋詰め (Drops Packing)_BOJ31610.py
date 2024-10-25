# 飴の袋詰め (Drops Packing)_BOJ31610

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())    # 사탕의 가격을 input 받고
B = int(input())    # 사탕의 수를 input 받고 
C = int(input())    # 봉투의 가격을 input 받고
print(A*B+C)        # 총 금액을 출력한다