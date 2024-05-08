# 저작권_BOJ2914
# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, I = map(int, input().split())    # A 앨범에 수록된 곡의 개수 / I 평균값을 input 받고
print(A*(I-1)+1)                    # 저작권이 있는 멜로디의 최소개수를 출력한다