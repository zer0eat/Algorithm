# 카드1_BOJ2161

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
N = int(sys.stdin.readline())               # 카드의 숫자 중 가장 큰 숫자를 input 받고
card = deque([i for i in range(1, N+1)])    # card 리스트를 만들고 1부터 N까지 카드를 순서대로 저장한다

ans = []                                    # 정답을 저장할 리스트를 생성하고
while card:                                 # card가 빌 때까지 반복해서
    ans.append(card.popleft())              # card에서 가장 왼쪽에 있는 카드를 빼서 ans에 넣고
    if card:                                # card 리스트가 비어있지 않다면
        card.append(card.popleft())         # 맨앞의 카드를 맨 뒤로 옮겨준다
else:                                       # while문이 끝났다면
    print(*ans)                             # 정답을 출력한다