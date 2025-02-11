# 2 番目に大きい整数 (The Second Largest Integer)_BOJ20976

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
num = list(map(int, input().split()))   # 숫자를 리스트로 input 받고
num.sort()                              # 오름차순으로 정렬해서
print(num[1])                           # 2번째로 큰 수를 출력한다