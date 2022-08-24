# 배열최소합_13882

def f(i, r):
    if i==r:
        print(bit[:r])
        return
    for n in range(N):
        if n not in bit[0:i]:
            bit[i] = n
            f(i+1,r)




# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                # 테스트 케이스
for t in range(T):                                              # 테스트 케이스 수만큼 반복
    N = int(input())                                            # 행렬의 길이를 N으로 input
    arr = [list(map(int, input().split())) for n in range(N)]   # 길이가 N인 행렬을 arr에 input

    # 부분집합의 합
    arr_sum = []

    bit = [0] * N
    f(0, N)



