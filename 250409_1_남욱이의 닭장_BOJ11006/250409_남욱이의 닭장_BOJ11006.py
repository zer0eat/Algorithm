# 남욱이의 닭장_BOJ11006

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스를 input 받고
for t in range(T):                      # 테스트 케이스를 반복해서
    N, M = map(int, input().split())    # 닭 다리 수와 닭의 수를 input 받고
    print(2*M-N, N-M)                   # 다리가 하나인 닭과 두개인 닭을 출력한다