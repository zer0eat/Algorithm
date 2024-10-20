# Rats_BOJ18301

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
n1, n2, n12 = map(int, input().split()) # 쥐의 수를 input 받고
ans = (n1+1)*(n2+1)/(n12+1)-1           # 쥐의 총 추정량을 계산해서
print(int(ans))                         # 쥐의 총 추정량을 툴력한다