# РАВЕНСТВО_BOJ24309

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a = int(input())    # a를 input 받고
b = int(input())    # b를 input 받고
c = int(input())    # c를 input 받고
print((b-c)//a)     # a*x = b-c를 만족하는 미지수 x를 출력한다