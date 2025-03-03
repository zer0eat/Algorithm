# 꿍 가라사대_BOJ11094

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 가라사대의 수를 input 받고
for n in range(N):                                  # 가라사대의 수를 반복해서
    S = list(input().split())                       # 가라사대를 input 받고
    if len(S) > 2 and S[0] + S[1] == 'Simonsays':   # 앞자리 2개가 simon says라면
        print(end= ' ')                             # 한자리를 띄고
        print(*S[2:])                               # 명령어를 출력한다