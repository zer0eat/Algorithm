# 선형 회귀는 너무 쉬워 1_BOJ27295

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from math import gcd

# input 받기
n, b = map(int, input().split())        # 테스트 케이스와 y절편을 input받고
X, Y = 0, 0                             # 데이터의 x, y의 합을 저장할 변수를 생성한다
for a in range(n):                      # 테스트 케이스를 반복해서
    x, y = map(int, input().split())    # x, y값을 input받고
    X += x                              # x의 값을 합쳐주고
    Y += y                              # y의 값을 합쳐준다
if X == 0:                              # x의 합이 0이라면
    print('EZPZ')                       # EZPZ를 출력하고
else:                                   # x의 합이 0이 아니라면
    p = Y - n*b                         # a 값을 구할때 분자를 계산하고
    q = X                               # a 값을 구할때 분모를 계산하고
    k = gcd(abs(p), abs(q))             # 분자와 분모의 최대 공약수를 구한다
    if p%q:                             # 분자가 분모로 나눠 떨어지지 않는다면
        p //= k                         # 분자에서 최대 공약수로 나누고
        q //= k                         # 분모에서 최대 공약수로 나누고
        if p < 0 and q < 0:             # 둘 다 음수라면
            p, q = abs(p), abs(q)       # 둘 다 양수로 바꿔주고
        elif p > 0 and q < 0:           # 분자가 양수 분모가 음수라면
            p, q = -p, abs(q)           # 두 수의 부호를 바꿔준다
        print(f'{p}/{q}')               # 분수를 계산해서 출력한다
    else:                               # 분자가 분모로 나눠 떨어진다면
        print(p//q)                     # 정수를 계산해서 출력한다