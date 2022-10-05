# 카드2_BOJ2164

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
N = int(sys.stdin.readline())           # 카드의 개수
card = [i for i in range(1, N+1)]       # card 리스트에 1번부터 N번까지 카드를 넣은 후
card = deque(card)                      # deque로 변환 한다

while len(card) > 1:                    # 한장이 남을때까지 반복하고
    card.popleft()                      # 한장은 버리고
    card.append(card.popleft())         # 한장은 맨 뒤에 넣는다

print(*card)