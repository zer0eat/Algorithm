# 가장 큰 감소 부분 수열_BOJ17216

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 수열의 크기를 input 받고
lst = list(map(int, input().split()))           # 수열의 원소를 리스트로 input 받는다
ans = [0]*N                                     # 정답을 저장할 리스트를 생성하고
for i in range(N):                              # 수열을 반복하고
    ans[i] = lst[i]                             # 해당 수열의 값을 ans에 저장한 후
    for j in range(i):                          # i보다 작은 인덱스를 반복해서
        if lst[i] < lst[j]:                     # 수열i보다 수열j가 크다면
            ans[i] = max(ans[i], ans[j]+lst[i]) # ans에 현재 저장된 가장 큰 수와 j까지 가장 큰 수와 i번째 수열의 합 중 더 큰 값으로 저장한다
print(max(ans))                                 # 수열의 합이 가장 큰 감소 부분 수열의 합을 출력한다

