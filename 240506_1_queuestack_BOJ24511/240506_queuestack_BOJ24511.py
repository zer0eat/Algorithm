# queuestack_BOJ24511

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                    # queuestack의 길이를 input 받고
A = list(map(int, input().split())) # queuestack의 자료구조 형태를 리스트로 input 받고
B = list(map(int, input().split())) # queuestack의 원소를 리스트로 input 받고
M = int(input())                    # 삽입할 수열을 길이를 input 받고
C = list(map(int, input().split())) # 삽입할 원소를 리스트로 input 받는다
q = deque()                         # queue를 생성하고
for n in range(N):                  # queuestack의 길이를 반복해서
    if A[n] == 0:                   # queue인 원소가 나오면
        q.append(B[n])              # q에 append한다
for m in range(M):                  # 삽입할 수열을 반복해서
    q.appendleft(C[m])              # 삽입할 수열을 맨 앞에 추가하고
    print(q.pop(), end=' ')         # queue는 FIFO이므로 맨 처음 들어온 마지막 원소를 pop하고 출력한다