# 절사평균_BOJ6986

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())                                    # N 점수의 개수 / K 제외하는 점수의 수
lst = []                                                            # 점수를 저장할 리스트 생성
for i in range(N):                                                  # 점수의 개수를 반복해서
    lst.append(float(input()))                                      # lst에 점수를 append
lst.sort()                                                          # 점수를 오름차순으로 정렬한 뒤
print('{:.2f}'.format(round(sum(lst[K: N-K])/(N-2*K) + 1e-8, 2)))   # 절사평균을 출력한다
for i in range(K):                                                  # 제외하는 점수의 수를 반복해서
    lst[i] = lst[K]                                                 # 제외하는 낮은 점수를 가장 가까운 점수로 바꿔 저장한다
    lst[-i-1] = lst[-1-K]                                           # 제외하는 높은 점수를 가장 가까운 점수로 바꿔 저장한다
print('{:.2f}'.format(round(sum(lst)/N + 1e-8, 2)))                 # 보정평균을 출력한다