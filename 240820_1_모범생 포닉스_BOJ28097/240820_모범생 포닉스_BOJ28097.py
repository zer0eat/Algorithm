# 모범생 포닉스_BOJ28097

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 공부 계획 수를 input 받고
T = list(map(int, input().split())) # 공부 시간을 리스트로 input 받는다
ans = sum(T) + 8*(N-1)              # 공부 시간의 합과 쉬는 시간의 합을 더해서
print(ans//24, ans%24)              # 계획을 마친 후 소요 시간을 일과 시간으로 출력한다