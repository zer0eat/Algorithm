# LCM_BOJ5347

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def gcd(a,b):                           # 유클리드 호제법으로 gcd를 구하기 위한 함수
    while b > 0:                        # b가 0이 될때까지 반복해서
        a, b = b, a%b                   # a를 b로 b를 a를 b로 나눈 나머지로 저장한다
    return a                            # b가 0일때 a를 리턴한다

T = int(input())                        # 테스트 케이스 수를 input 받고
for t in range(T):                      # 테스트 케이스를 반복해서
    a, b = map(int, input().split())    # 최소 공배수를 구할 두 수를 input 받고
    gcd_num = gcd(a,b)                  # 두 수의 최대 공약수를 구한 후
    print(a*b//gcd_num)                 # 두수를 곱한 후 최대 공약수로 나눠 최소 공배수를 출력한다