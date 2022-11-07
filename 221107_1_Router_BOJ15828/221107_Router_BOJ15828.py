# Router_BOJ15828

# import.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
N = int(sys.stdin.readline())   # 라우터에 들어갈 패킷의 개수

que = deque()                   # 라우터를 deque 형태로 생성

while 1:                        # break가 나올 때까지 반복해서
    a = int(input())            # a에 input 받은 숫자를 저장하고
    if a == -1:                 # a가 -1일 때 while문 종료
        break
    elif a == 0:                # 0일 때는
        que.popleft()           # deque에서 popleft
    else:                       # 자연수일 때는
        if len(que) < N:        # deque내 패킷이 N보다 작을 때
            que.append(a)       # a를 deque에 append하고
        else:                   # N개만큼 차있다면
            pass                # 패킷을 버린다

if que:                         # que에 패킷이 남아있다면
    print(*que)                 # 남아있는 패킷을 출력하고
else:                           # 비어있다면
    print('empty')              # empty를 출력한다다