# OlympiadPizza_BOJ15235

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

# input 받기
N = int(input())                            # N 참가자의 수
lst = list(map(int, input().split()))       # 각 참가자가 먹어야하는 피자의 수를 list로 input 받음

pizza = deque()                             # deque을 생성하고
for i in range(N):                          # 먹어야하는 피자의 수를 반복해서
    pizza.append([lst[i], i])               # [피자의수, 인덱스] 형태로 deque에 append

visited = [0]*N                             # 피자를 다 먹었을 때 걸린 시간을 저장할 리스트를 생성하고
cnt = 1                                     # 시간을 저장할 변수를 생성한다

while pizza:                                # deque이 빌 때까지 반복해서
    A = pizza.popleft()                     # deque에서 맨 앞의 원소를 꺼내 A에 저장하고
    A[0] -= 1                               # 먹어야하는 피자의 수를 1 감소시킨다
    if A[0] == 0:                           # 만약 먹어야하는 피자의 수가 0이 되었다면
       visited[A[1]] = cnt                  # visited 리스트에 A에 저장되어 있는 인덱스와 같은 위치에 다 먹은 시간을 저장한다 
    else:                                   # 만약 다 먹지 못했다면
        pizza.append(A)                     # 다시 맨 뒤에 줄을 서도록 deque에 append한다
    cnt += 1                                # 시간을 1 증가시킨다

print(*visited)                             # 모든 참가자가 피자를 다 먹었다면 참가자마다 다먹은 시간을 출력한다