# 주사위_BOJ9295

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 테스트 케이스를 input 받고
for n in range(N):                  # 테스트 케이스를 반복해서
    a, b = map(int,input().split()) # 두 주사위의 눈을 input 받고
    print(f'Case {n+1}: {a+b}')     # 주사위의 합을 출력한다