# 피자굽기_13973_deque

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복
    N, M = map(int, input().split())            # N = 오븐에서 구울 수 있는 피자의 수 / M = 구워야할 피자의 수
    pizza = deque(map(int, input().split()))    # 피자의 치즈 양을 pizza deque에 input

    pizza_num = deque([] for _ in range(M))     # 리스트 안에 피자의 수 만큼 빈 deque를 만듬

    for m in range(M):                          # 피자의 수 만큼 반복할 때
        pizza_num[m].append(m)                  # 인덱스를 append
        pizza_num[m].append(pizza[m])           # 치즈의 양을 append

    oven = deque()                              # oven으로 쓸 deque 생성

    complite_pizza = []                         # 완성된 피자를 넣을 리스트 생성

    # 오븐에 피자 넣기
    for n in range(N):                          # 오븐의 허용 수 만큼 반복할 때
        oven.append(pizza_num.popleft())        # 오븐에 피자를 순서대로 넣는다

    # 피자 확인하기
    while oven:                                 # 오븐에 피자가 없을 때까지 반복
        cheese = oven.popleft()                 # 맨 앞의 피자를 꺼내서
        cheese[1] = cheese[1]//2                # 치즈가 반 녹았을 때(소수점 이하 절삭)
        if cheese[1] == 0:                      # 치즈가 다 녹았다면
            complite_pizza.append(cheese)       # 완성된 피자 리스트에 넣고
            if pizza_num:                       # 구워야할 피자가 남아있으면
                oven.append(pizza_num.popleft())   # 오븐에 넣는다
        elif cheese[1] != 0 :                   # 치즈가 다 녹지 않았다면
            oven.append(cheese)                 # 다시 오븐에 넣는다

    print(f'#{t+1}', complite_pizza[-1][0] + 1)     # 완성된 피자를 보고 가장 마지막에 완성된 피자의 번호(인덱스 + 1)를 출력한다
