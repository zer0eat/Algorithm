# 단순한 문제 (Small)_BOJ25494

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스를 input 받고
for t in range(T):                      # 테스트 케이스를 반복해서
    a, b, c = map(int, input().split()) # 세 숫자를 input 받고
    print(min(a,b,c))                   # a, b, c 중 가장 작은값을 출력한다