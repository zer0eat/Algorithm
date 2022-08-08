# Flatten_1208

#input.txt 열기
import sys
sys.stdin = open('input.txt')

#input 리스트로 받기
N = 10
for n in range(N):
    Dump = int(input())
    lst = list(map(int, input().split()))
