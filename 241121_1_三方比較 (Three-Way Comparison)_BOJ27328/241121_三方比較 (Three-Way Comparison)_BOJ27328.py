# 三方比較 (Three-Way Comparison)_BOJ27328

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())    # A를 input 받고
B = int(input())    # B를 input 받고
if A < B:           # B가 더 크다면
    print(-1)       # -1을 출력하고
elif A > B:         # A가 더 크다면
    print(1)        # 1을 출력하고
else:               # A와 B가 같다면
    print(0)        # 0을 출력한다