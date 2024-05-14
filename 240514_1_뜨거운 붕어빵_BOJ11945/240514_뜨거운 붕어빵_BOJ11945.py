# 뜨거운 붕어빵_BOJ11945

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # 붕어빵의 행과 열을 input 받고
for n in range(N):                  # 붕어빵의 행을 반복해서
    m = input().strip()             # 한 행을 input 받고
    print(m[::-1])                  # 좌우를 뒤집어서 출력한다