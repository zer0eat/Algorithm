# 달팽이는올라가고싶다_BOJ2869

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
A, B, V = map(int, sys.stdin.readline().split())    # A 올라가는 거리 B 미끄러지는 거리 V 나무의 높이

N = (V - B) / (A - B)                               # N 올라가는 시간
N2 = (V - B) // (A - B)                             # N2 올라가는 시간 중 정수부분
# V = A*N - B*(N-1)
# V = A*N - B*N + B
# V + B = N(A-B)

if N - N2 > 0:                                      # 올라가는 시간에 소수부분이 있다면
    N2 += 1                                         # 올림한 값을 N2에 저장

print(N2)