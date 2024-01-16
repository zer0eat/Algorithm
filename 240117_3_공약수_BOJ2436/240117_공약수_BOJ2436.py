# 공약수_BOJ2436

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())                # A 최대 공약수 / B 최소공배수를 input 받고

def gcd(a, b):
    while b > 0:                                # b가 0이 될때까지 반복해서
        a, b = b, a % b                         # a에 b를 저장하고 b에 a를 b로 나눈 나머지를 저장한다
    return a                                    # b가 0일 때 최대공약수인 a를 return한다

B //= A                                         # 최대공배수에서 최대공약수를 나눠 두수의 서로소의 곱만 남기고
num = 1                                         # 서로소가 될 두 수중 하나를 num에 저장한 후
while num**2 <= B:                              # num**2이 B보다 같거나 작을때 반복해서
    if B%num == 0 and gcd(num, B//num) == 1:    # B가 num으로 나눠 떨어지고, num과 B//num이 서로소 라면
        a, b = num, B//num                      # a에는 num을 b에는 B//num을 저장한다
    num += 1                                    # num을 1 증가시킨다
print(A*a, A*b)                                 # A, B를 만족하는 두 수 중 합이 최소가 되는 수를 출력한다