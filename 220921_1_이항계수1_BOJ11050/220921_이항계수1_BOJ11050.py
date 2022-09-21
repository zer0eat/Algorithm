# 이항계수1_BOJ11050

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, K = map(int, input().split())    # N = 뽑을 수 있는 종류 / K = 뽑을 개수
a = 1                               # 분자로 사용할 변수
b = 1                               # 분모로 사용할 변수
for p in range(K):                  # K만큼 반복할 때
    a *= (N-p)                      # 분자에 N에서 1씩 빼며 K개를 곱함
    b *= (K-p)                      # 분모에 N에서 1씩 빼며 K개를 곱함

print(a//b)