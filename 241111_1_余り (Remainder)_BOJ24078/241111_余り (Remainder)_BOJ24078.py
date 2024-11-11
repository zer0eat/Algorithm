# 余り (Remainder)_BOJ24078

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X = int(input())    # X를 input 받고
print(X%21)         # X를 21로 나눈 나머지를 출력한다