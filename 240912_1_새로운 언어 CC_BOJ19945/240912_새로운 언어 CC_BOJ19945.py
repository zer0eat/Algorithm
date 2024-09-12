# 새로운 언어 CC_BOJ19945

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # cc의 수를 input 받고
if N < 0:               # cc가 음수라면
    print(32)           # 32를 출력하고
    quit()              # 종료한다
n = 2                   # 변수를 생성하고
for i in range(1, 33):  # 비트의 수를 반복해서
    if N <= n**i:       # cc의 수가 비트보다 작거나 같다면
        print(i)        # 비트의 수를 출력하고
        quit()          # 종료한다