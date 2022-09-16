# 직사각형에서 탈출_BOJ2920

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
x, y, w, h = map(int, input().split())

mini = [x, w-x, y, h-y]

print(min(mini))