# 카드_BOJ1835

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())            # 카드의 개수를 input 받고
ans = deque([N])            # 마지막 카드를 넣은 deque을 생성한다
for i in range(N-1, 0, -1): # N-1번 카드부터 1번 카드까지 역으로 반복해서
    ans.appendleft(i)       # 카드를 덱 맨 앞에 넣고
    for j in range(i):      # 카드의 숫자만큼 반복해서
        a = ans.pop()       # 맨 뒤의 카드를 꺼내
        ans.appendleft(a)   # 맨 앞에 넣는 것을 반복한다
print(*ans)                 # 마술을 하기위한 카드의 초기 순서를 출력한다