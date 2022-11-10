# 최대힙_BOJ11279

# import.txt 열기
import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

# input 받기
N = int(sys.stdin.readline())       # 연산의 개수
hQ = []                             # heapq를 저장할 리스트 생성
for n in range(N):                  # 연산의 개수만큼 반복해서
    h = int(sys.stdin.readline())   # h에 숫자를 input 받고
    if h == 0:                      # input 받은 숫자가 0이라면
        if len(hQ) == 0:            # hQ가 비어있을 땐
            print(0)                # 0을 출력하고
        else:                       # hQ가 비어있지 않을 땐
            print(-heappop(hQ))     # root를 pop하고 음수를 붙여 input 받은 원소 중 가장 큰 값을 출력한다
    elif h != 0:                    # input 받은 숫자가 0이 아니라면
        heappush(hQ, -h)            # 최대 힙을 위해 음수 값으로 넣어 가장 큰 input 값이 root 가 되도록한다