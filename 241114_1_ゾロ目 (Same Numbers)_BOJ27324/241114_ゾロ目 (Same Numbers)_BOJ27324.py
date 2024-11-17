# ゾロ目 (Same Numbers)_BOJ27324

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 숫자를 input 받고
if N//10 == N%10:   # 10의자리와 1의자리가 같으면
    print(1)        # 1을 출력하고
else:               # 아니라면
    print(0)        # 0을 출력한다