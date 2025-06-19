# 얼마?_BOJ9325

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())            # 테스트 케이스를 input받고
for t in range(T):          # 테스트 케이스를 반복해서
    s = int(input())        # 자동차의 가격을 input받고
    n = int(input())        # 옵션의 수를 input받고
    for m in range(n):      # 옵션의 수를 반복해서
        q, p = map(int, input().split())    # 옵션의 수와 가격을 input받고
        s += q*p            # 차가격에 추가한다
    else:                   # 계산이 끝났다면
        print(s)            # 차 가격을 출력한다