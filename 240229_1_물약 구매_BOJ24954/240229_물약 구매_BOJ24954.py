# 물약 구매_BOJ24954

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 구매하려는 물약의 수를 input 받고
price = list(map(int, input().split()))             # 물약의 가격을 리스트로 input 받는다
sale = []                                           # 물약의 할인 정보를 저장할 리스트를 생성하고
for n in range(N):                                  # 물약의 개수를 반복해서
    M = int(input())                                # n번 물약을 구매했을 때 할인 되는 물약의 수를 input 받고
    tmp = []                                        # 할인 정보를 저장할 리스트를 생성한 후
    for m in range(M):                              # 할인되는 물약의 수를 반복해서
        tmp.append(list(map(int, input().split()))) # 할인되는 물약의 정보를 tmp에 append하고
    sale.append(tmp)                                # tmp를 sale에 append해서 할인 정보를 저장한다
ans = 1e9                                           # 정답을 저장할 변수를 생성하고
visited = [0]*N                                     # 구매 표시를 할 리스트틀 생성한다

def recur(dep, tmp):
    global ans                                      # ans를 global 변수로 선언하고
    if dep == N:                                    # 모든 물약을 구매했다면
        ans = min(ans, tmp)                         # ans와 tmp 중 작은 값을 저장하고
        return                                      # return 한다
    for i in range(N):                              # 물약을 반복해서
        if visited[i]:                              # i번째 물약을 이미 구매했다면
            continue                                # continue로 넘어간다
        visited[i] = 1                              # i번째 물약을 구매표시하고
        if price[i] < 1:                            # i번째 물약의 가격이 1보다 작다면
            tmp += 1                                # tmp에 1원을 추가하고
        else:                                       # i번째 물약의 가격이 1 이상이라면
            tmp += price[i]                         # tmp에 가격을 추가한다
        for s in sale[i]:                           # i번째 물약을 구매했을 때 할인정보를 반복해서
            price[s[0]-1] -= s[1]                   # 해당 물약의 가격을 할인한다
        recur(dep+1, tmp)                           # 깊이 dep+1부터 물약가격을 탐색한다
        for s in sale[i]:                           # i번째 물약을 구매했을 때 할인정보를 반복해서
            price[s[0]-1] += s[1]                   # 해당 물약의 가격을 복구하고
        if price[i] < 1:                            # i번째 물약의 가격이 1보다 작다면
            tmp -= 1                                # 구매가격을 1 감소하고
        else:                                       # i번째 물약의 가격이 1 이상이라면
            tmp -= price[i]                         # 가격만큼 감소한다
        visited[i] = 0                              # i번째 물약을 구매표시를 해제한다

recur(0, 0)                                         # 깊이 0부터 물약가격을 탐색한다
print(ans)                                          # 물약을 가장 싸게 샀을 때 필요한 동전을 출력한다