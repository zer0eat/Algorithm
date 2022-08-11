# 부분집합의 합_13631

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 원소의 합을 구하는 함수
def sum1(list):
    sum_all = 0
    for l in list:
        sum_all += l
    return sum_all


# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    # N = 부분집합의 원소의 수 / # K = 부분 집합 원소의 합
    N, K = map(int, input().split())
    # A = 1부터 12의 원소를 갖는 부분집합
    A = list(range(1, 13))

    # 모든 부분 집합 만들기
    subset_all = []
    for i in range(1<<len(A)):
        subset_element = []
        for j in range(len(A)):
            if i & (1<<j):
                subset_element.append(A[j])
        subset_all.append(subset_element)

    # 원소의 개수가 N개인 부분집합 중 합이 K인 것만 추출하기
    subset_N = []
    for a in subset_all:
        if len(a) == N:
            if sum1(a) == K:
                subset_N.append(a)

    print(f'#{t+1} {len(subset_N)}')



