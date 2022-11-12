# 절댓값힙_BOJ11286

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
            A = heappop(hQ)         # root를 pop하여 input 받은 원소 중 가장 작은 값을 A에 저장하고
            if A[1] == True:        # A의 1번째 인덱스 값이 True 라면
                print(A[0])         # A의 0번째 인덱스 값을 출력한다
            elif A[1] == False:     # A의 1번째 인덱스 값이 False 라면
                print(-A[0])        # A의 0번째 인덱스 값에 -를 붙여 출력한다

    elif h != 0:                    # input 받은 숫자가 0이 아니라면
        if h > 0:                   # input 받은 숫자가 양수일 때
            heappush(hQ, [h, True]) # [input받은 숫자, True] 리스트를 heapq에 넣는다
        elif h < 0:                 # input 받은 숫자가 음수일 때
            heappush(hQ, [-h, False])   # [input받은 숫자에 -를 붙이고, -표시를 해줬다고 False로 표시해준 후] 리스트를 heapq에 넣는다