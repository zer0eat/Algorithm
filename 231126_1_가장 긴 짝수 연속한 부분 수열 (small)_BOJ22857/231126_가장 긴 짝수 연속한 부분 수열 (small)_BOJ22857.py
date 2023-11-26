# 가장 긴 짝수 연속한 부분 수열 (small)_BOJ22857

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N, K = map(int, input().split())        # N 수열의 길이와 / K 삭제할 수 있는 횟수를 input 받고
lst = list(map(int, input().split()))   # 수열을 리스트로 input 받는다
start = N-1                             # 시작점을 나타낼 변수를 생성하고
tmp = deque([])                         # 정답을 저장할 deque을 생성한 후
max_length = 0                          # 최대 길이를 저장할 변수를 생성한다
for i in range(N):                      # 수열의 길이를 반복해서
    if lst[i] % 2 == 0:                 # 짝수 값을 갖는 수열이 나온다면
        start = i                       # start를 해당 값의 인덱스로 저장하고
        tmp.append(lst[i])              # deque에 해당 값을 append한 후
        max_length = 1                  # 최대 길이를 1로 저장하고
        break                           # for문을 break한다
cnt = 0                                 # 홀수의 개수를 셀 변수를 생성하고
for i in range(start+1, N):             # start 다음부터 N까지 반복해서
    if lst[i] % 2:                      # i번째 값이 홀수라면
        if K <= cnt:                    # cnt가 K보다 같거나 큰 경우
            while K <= cnt:             # K가 cnt보다 작거나 같아질때 까지 반복해서
                A = tmp.popleft()       # deque의 맨 왼쪽 수를 빼고
                if A % 2:               # 해당 값이 홀수라면
                    cnt -= 1            # 홀수의 개수를 1 빼준다
        cnt += 1                        # 홀수의 개수를 1 추가하고
        tmp.append(lst[i])              # deque에 해당 값을 append한다
    else:                               # i번째 값이 짝수라면
        tmp.append(lst[i])              # deque에 해당 값을 append한다
    max_length = max(max_length, len(tmp)-cnt)  # 현재 tmp에 저장된 값 중 홀수를 뺀 나머지와 max_length 중 더 큰 값으로 저장하고
print(max_length)                       # 수열에서 최대 K개 삭제한 후 짝수로 이루어져 있는 연속한 부분 수열의 최대값을 출력한다