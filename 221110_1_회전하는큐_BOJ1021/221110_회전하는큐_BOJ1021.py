# 회전하는큐_BOJ1021

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
N, K = map(int, sys.stdin.readline().split())           # N 순환 큐 내의 원소의 수 / K 뽑고 싶은 원소의 수
lst = list(map(int, sys.stdin.readline().split()))      # 뽑고 싶은 원소의 리스트
Q = deque([_ for _ in range(1, N+1)])                   # Q에 원소의 수 만큼 넣은 deque 생성

cnt = 0                                                 # 순환하는 횟수를 셀 변수 생성
for l in lst:                                           # 뽑고 싶은 원소의 리스트를 반복해서
    while 1:                                            # break가 나올 때까지 반복
        if Q.index(l) == 0:                             # 찾고자하는 원소의 index가 0이라면
            Q.popleft()                                 # popleft로 제거하고 while문 break
            break
        else:                                           # 찾고자하는 원소의 index가 0이 아니라면
            if Q.index(l) <= len(Q)-Q.index(l):         # 찾고자하는 원소의 인덱스가 전체길이에서 찾고자하는 인덱스를 뺀수보다 작다면 왼쪽으로 이동하는 것이 빠르므로
                A = Q.popleft()                         # A에 0번째 원소를 pop해서 저장하고
                Q.append(A)                             # Q의 맨 뒤에 append 한다
                cnt += 1                                # 순환 횟수를 1 추가한다
            else:                                       # 찾고자하는 원소의 인덱스가 전체길이에서 찾고자하는 인덱스를 뺀수보다 크다면 오른쪽으로 이동하는 것이 빠르므로
                A = Q.pop()                             # A에 마지막 원소를 pop해서 저장하고
                Q.appendleft(A)                         # Q의 맨 앞에 append 한다
                cnt += 1                                # 순환 횟수를 1 추가한다
print(cnt)                                              # 순환한 횟수를 출력한다