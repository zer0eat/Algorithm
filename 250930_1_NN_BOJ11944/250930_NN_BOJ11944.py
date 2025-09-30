# NN_BOJ11944

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # 두 숫자를 input받고
ans = str(N)*N                      # N의 숫자를 N번 반복해서
print(ans[:M])                      # M 자리까지 출력한다