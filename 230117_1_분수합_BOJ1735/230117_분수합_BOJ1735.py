# 분수합_BOJ1735

# input.txt 열기
import sys
sys.stdin = open('input.txt')
import math

# input 받기
A, B = map(int, sys.stdin.readline().split())   # 첫번째 분수의 분자를 A 분모를 B로 input 받는다
C, D = map(int, sys.stdin.readline().split())   # 두번째 분수의 분자를 C 분모를 D로 input 받는다

Q = math.gcd(A, B)                              # A와 B의 최대공약수를 Q에 저장한 후
A = A // Q                                      # 분자를 최대공약수로 나누고
B = B // Q                                      # 분모를 최대공약수로 나누어 기약분수로 나눠준다

R = math.gcd(C, D)                              # C와 D의 최대공약수를 R에 저장한 후
C = C // R                                      # 분자를 최대공약수로 나누고
D = D // R                                      # 분모를 최대공약수로 나누어 기약분수로 나눠준다

X = A*D + B*C                                   # 두 분수의 합을 계산한 분자를 X에 저장하고
Y = B*D                                         # 두 분수의 합을 계산한 분모를 Y에 저장한 후

T = math.gcd(X, Y)                              # X와 Y의 최대공약수를 T에 저장한 후
X = X // T                                      # 분자를 최대공약수로 나누고
Y = Y // T                                      # 분모를 최대공약수로 나누어 기약분수로 나눠준다
print(X, Y)                                     # 두 분수의 합을 기약분수 형태로 출력한다


