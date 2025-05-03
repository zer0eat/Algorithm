# 특별한 작은 분수_BOJ27890

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
x, N = map(int, input().split())    # 분수 높이의 시작값과 횟수를 input 받고
for n in range(N):                  # 횟수를 반복해서
    if x % 2 == 0:                  # 높이가 짝수라면
        x = int(x/2)^6              # 다음 높이를 계산하고
    else:                           # 높이가 분수라면
        x = int(2*x)^6              # 다음 높이를 계산해서
print(x)                            # N초 후 높이를 출력한다