# 초콜릿 자르기_BOJ2163

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # 초콜릿의 가로와 세로의 크기를 input 받고
ans = N-1 + N*(M-1)                 # 초콜릿을 잘라야하는 횟수를 저장한 변수를 생성한다
print(ans)                          # 초콜릿을 잘라야하는 최소한의 횟수를 출력한다