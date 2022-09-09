# 제리와톰2_BOJ17504

# input.txt
import sys
sys.stdin = open('input.txt')
from fractions import Fraction                  # 분수를 사용할 수 있도록 import

# input 받기
T = int(input())                                # 제리가 훔쳐간 횟수
arr = list(map(int, input().split()))           # 훔쳐간 크기를 저장한 리스트
b = 0                                           # 분모를 계산할 변수
while arr:                                      # 훔쳐간 크기를 저장한 리스트를 반복
    a = arr.pop()                               # 맨 마지막에 훔쳐간 치즈의 양을 빼서
    b = Fraction(1, a + b)                      # b에 분모 형태로 저장
else:                                           # 반복이 모두 끝났다면
    ans = Fraction(1 - b)                       # ans에 정답을 저장
    print(ans.numerator, ans.denominator)       # 분자와 분모를 따로 출력