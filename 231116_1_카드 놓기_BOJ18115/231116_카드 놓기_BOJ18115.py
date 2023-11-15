# 카드 놓기_BOJ18115

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                    # 카드의 수를 input 받고
A = list(map(int, input().split())) # 기술의 종류를 리스트로 input 받는다
card = deque([1])                   # 정답을 저장할 deque를 생성하고
for i in range(N-2, -1, -1):        # 기술의 종류를 뒤에서부터 반복해서
    if A[i] == 1:                   # 1번 기술을 사용했다면
        card.appendleft(N-i)        # 카드의 맨 위에 N-i번 카드를 넣는다
    elif A[i] == 2:                 # 2번 기술을 사용했다면
        tmp = card.popleft()        # 맨 위에 있는 카드를 빼놓았다가
        card.appendleft(N-i)        # 카드의 위에서 두번째에 N-i번 카드를 넣고
        card.appendleft(tmp)        # 맨 위에 있던 카드를 다시 넣는다
    else:                           # 3번 기술을 사용했다면
        card.append(N-i)            # 카드의 맨 밑에 N-i번 카드를 넣는다
print(*card)                        # 초기 카드의 상태를 위에서부터 순서대로 출력한다