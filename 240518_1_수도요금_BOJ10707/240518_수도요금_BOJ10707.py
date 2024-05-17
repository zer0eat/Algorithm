# 수도요금_BOJ10707

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())        # X사의 리터당 요금을 input받고
B = int(input())        # Y사의 기본요금을 input 받고
C = int(input())        # Y사의 기본 제공량을 input받고
D = int(input())        # Y사의 리터당 요금을 input받고
P = int(input())        # 사용량을 input 받는다
X = A*P                 # X사를 이용했을 때 수도요금을 변수에 저장하고
if P-C > 0:             # 기본 제공량보다 사용량이 많을 경우
    Y = B + D*(P-C)     # Y사를 이용했을 때 수도요금을 변수에 저장하고
else:                   # 기본 제공량보다 사용량이 적을 경우
    Y = B               # Y사의 기본요금을 변수에 저장한다
print(min(X, Y))        # X사와 Y사 중 더 싼 요금을 출력한다