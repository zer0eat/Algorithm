# 시그마_BOJ2355

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 두 정수를 input 받고
if A > B:                           # A가 B보다 크다면
    A, B = B, A                     # 두 정수를 바꿔준다
ans = (B*(B+1)//2) - (A*(A-1)//2)   # 0부터 절대 값 B까지의 합에서 0부터 절대 값 A까지의 합을 빼준 후
print(ans)                          # 정답을 출력한다