# Hello Judge_BOJ9316

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 테스트 케이스를 input 받고
for n in range(1, N+1):                 # 테스트 케이스를 반복해서
    print(f'Hello World, Judge {n}!')   #  Hello World, Judge n! 를 출력한다