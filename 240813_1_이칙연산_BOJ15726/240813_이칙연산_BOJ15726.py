# 이칙연산_BOJ15726

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, C = map(int, input().split()) # 개 정수 A, B, C를 input 받고
print(max(A*B//C, A*C//B))          # 나올 수 있는 가장 큰 값을 출력한다