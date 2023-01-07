# 가장긴증가하는부분수열_BOJ11053

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())               # 수열의 원소의 개수
lst = list(map(int, sys.stdin.readline().split()))  # 수열을 list로 input 받음
ans = [1] * N                                       # 수열의 인덱스마다 최대 수열이 되는 값을 저장할 리스트 생성

for i in range(1, N):                               # 인덱스를 1부터 N-1까지 반복해서
    for j in range(i):                              # 인덱스를 0부터 i-1까지 반복한 후
        if lst[j] < lst[i]:                         # i번째 원소가 i보다 작은 인덱스의 원소보다 큰 경우
            if ans[i] < ans[j] + 1:                 # 현재 저장된 i번째의 최대 수열의 길이가 j의 최대 수열의 길이 +1보다 작다면
                ans[i] = ans[j] + 1                 # i의 최대 수열의 길이를 j의 최대 수열의 길이 +1로 저장한다
print(max(ans))                                     # 모든 반복을 마치면 최대 수열의 길이를 출력한다
