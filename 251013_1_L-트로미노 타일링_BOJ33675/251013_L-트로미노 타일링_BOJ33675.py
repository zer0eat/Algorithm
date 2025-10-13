# L-트로미노 타일링_BOJ33675

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())            # 테스트 케이스를 input받고
for t in range(T):          # 테스트 케이스를 반복해서
    N = int(input())        # 타일의 길이를 input받고
    if N % 2 == 0:          # 타일의 길이가 짝수라면
        print(2**(N//2))    # 경우의 수를 출력하고
    else:                   # 타일의 길이가 홀수라면
        print(0)            # 0을 출력한다