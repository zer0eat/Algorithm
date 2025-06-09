# 팩토리얼_BOJ7489

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                # 테스트 케이스를 input받고
for t in range(T):              # 테스트 케이스를 반복해서
    ans = 1                     # 정답을 저장할 변수를 생성하고
    N = int(input())            # 팩토리얼의 수를 input받고
    for n in range(1, N+1):     # 1부터 N까지 반복해서
        ans *= n                # 변수에 순서대로 곱해서
        while ans % 10 == 0:    # 끝자리가 0이 아닐때 까지 반복해서
            ans //= 10          # 끝자리가 0이면 0을 제거한다
    print(ans%10)               # 0이 아닌 가장 우측에 있는 수를 출력한다