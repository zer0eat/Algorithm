# 身長 (Height)_BOJ24086

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())    # A의 키를 input 받고
B = int(input())    # B의 키를 input 받아서
print(abs(A-B))     # 두사람의 키 차이를 출력한다