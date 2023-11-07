# 가로수_BOJ2485

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 가로수의 수를 input 받고
wood = [int(input()) for _ in range(N)]     # 가로수의 위치를 리스트로 input 받는다
interval = []                               # 가로수의 간격을 저장할 리스트를 생성하고
for w in range(1, N):                       # 2번째 가로수부터 마지막까지 반복해서
    interval.append(wood[w]-wood[w-1])      # 가로수의 간격을 interval에 append한다

def gcd(x,y):                               # 뉴클리드 호제법
    while y != 0:                           # y가 0이 될때까지 반복해서
        x, y = y, x % y                     # x에 y를 저장하고 y에 x를 y로 나눈 나머지를 저장한다
    return x                                # y가 0이라면 x의 값이 최대 공약수가 되므로 return한다

tmp = interval[0]                           # 가로수의 간격 중 맨 앞의 값을 tmp에 저장하고
for i in range(1, N-1):                     # 가로수의 간격의 두번째부터 마지막까지 반복해서
    tmp = gcd(tmp, interval[i])             # 두 간격의 최대 공약수를 구해서 tmp에 저장한다
need = (wood[-1]-wood[0])//tmp+1            # 같은 간격으로 심기위해 필요한 모든 가로수의 숫자를 구하고
print(need-N)                               # 모든 가로수에서 이미 심어져있는 가로수를 빼서 필요한 가로수의 숫자를 출력한다