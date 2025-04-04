# 조합 0의 개수_BOJ2004

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # 조합을 할 두 정수를 input 받는다
N2, NM2, M2 = 0, 0, 0               # N2 : N! / NM2 : (N-M)! / M2 : M! 에서 2로 나눌 수 있는 개수를 저장할 변수를 각각 생성하고
N5, NM5, M5 = 0, 0, 0               # N5 : N! / NM5 : (N-M)! / M5 : M! 에서 5로 나눌 수 있는 개수를 저장할 변수를 각각 생성한다
k = 1                               # 지수로 사용할 변수를 생성하고
while 2**k <= N:                    # 2의 k제곱이 N보다 커질때까지 반복해서
    N2 += N//(2**k)                 # 2의 k제곱으로 N을 나눌 수 있는 수만큼 N2에 더하고
    NM2 += (N-M)//(2**k)            # 2의 k제곱으로 (N-M)을 나눌 수 있는 수만큼 NM2에 더하고
    M2 += M // (2**k)               # 2의 k제곱으로 M을 나눌 수 있는 수만큼 M2에 더하고
    N5 += N//(5**k)                 # 5의 k제곱으로 N을 나눌 수 있는 수만큼 N5에 더하고
    NM5 += (N-M)//(5**k)            # 5의 k제곱으로 (N-M)을 나눌 수 있는 수만큼 NM5에 더하고
    M5 += M//(5**k)                 # 5의 k제곱으로 M을 나눌 수 있는 수만큼 M5에 더하고
    k += 1                          # 지수를 1 추가한다
print(min(N2-NM2-M2, N5-NM5-M5))    # N,M 조합에서 2의 개수와 5의 개수 중 더 작은 값을 출력해서 끝자리 0의 개수를 출력한다