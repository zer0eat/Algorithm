# 보물_BOJ1026

# input.txt
import sys
sys.stdin = open('input3.txt')

# input 받기
N = int(input())                                    # 숫자열의 길이
A = list(map(int, input().split()))                 # 첫번째 숫자열을 A에 저장
B = list(map(int, input().split()))                 # 두번째 숫자열을 B에 저장

# A를 오름차순으로 버블솔트
for i in range(N-1):
    for j in range(N-i-1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

# B를 내림차순으로 버블솔트
for i in range(N - 1):
    for j in range(N - i - 1):
        if B[j] < B[j + 1]:
            B[j], B[j + 1] = B[j + 1], B[j]

ans = 0                                             # 최소값을 저장할 변수를 만들고
for z in range(N):                                  # 숫자열을 반복하면서
    ans += A[z] * B[z]                              # ans에  A[0] × B[0] + ... + A[N-1] × B[N-1] 값을 저장

print(ans)