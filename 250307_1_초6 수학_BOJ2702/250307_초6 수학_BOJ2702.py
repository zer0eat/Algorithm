# 초6 수학_BOJ2702

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def GCD(x, y):                          # 최대 공약수를 구하는 함수를 선언하고
    while y:                            # y가 0이 될때까지 반복해서
        x,y = y, x%y                    # x를 y y를 x를 y로 나눈 값으로 저장하고
    return x                            # y가 0일때 x의 값을 return 한다

def LCM(x, y):                          # 최소 공배수를 구하는 함수를 선언하고
    return x*y//GCD(x,y)                # 두수의 곱에서 최대 공약수를 나눈 값을 return한다

T = int(input())                        # 테스트 케이스를 input 받고
for t in range(T):                      # 테스트 케이스를 반복해서
    a, b = map(int, input().split())    # 두 수를 input 받고
    print(LCM(a,b), GCD(a,b))           # 두 수의 최소 공배수와 최대 공약수를 출력한다