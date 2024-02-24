# 다이어트_BOJ19942

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                            # 식재료의 수를 input 받고
P, L, C, V = map(int, input().split())                                      # 필요한 단백질, 지방, 탄수화물, 비타민을 input 받는다
food = [list(map(int, input().split())) for _ in range(N)]                  # 식재료별 단백질, 지방, 탄수화물, 비타민, 가격을 리스트로 input 받고
ans = 1e9                                                                   # 최소 비용을 저장할 변수를 생성하고
ans2 = []                                                                   # 그 때 음식의 인덱스를 저장할 리스트를 생성한다

def recur(dep, start, eat):
    global ans, ans2                                                        # 정답을 저장할 변수를 global 변수로 선언하고
    if dep > 0:                                                             # 식재료가 하나라도 있다면
        tmp = [0]*4                                                         # 필요한 영양성분을 저장할 리스트를 생성하고
        money = 0                                                           # 비용을 저장할 변수를 생성한다
        for e in eat:                                                       # eat에 담긴 식재료를 반복해서
            for j in range(4):                                              # 식재료별 영양소를 반복한 후
                tmp[j] += food[e][j]                                        # 들어있는 영양소를 tmp에 더해주고
            money += food[e][4]                                             # 비용을 money에 더해준다
        if tmp[0] >= P and tmp[1] >= L and tmp[2] >= C and tmp[3] >= V:     # 필요한 영양분이 eat에 모두 담겼다면
            if ans > money:                                                 # ans보다 비용이 더 작은 경우에
                ans = money                                                 # ans를 money로 저장하고
                ans2 = eat.copy()                                           # 해당 식재료의 번호를 저장한다
    if dep == N:                                                            # 모든 식재료를 탐색했다면
        return                                                              # return한다
    for i in range(start, N):                                               # start부터 식재료를 반복해서
        eat.append(i)                                                       # 식재료를 담고
        recur(dep+1, i+1, eat)                                              # 깊이 dep+1부터 i+1번 음식부터 탐색한 후
        eat.pop()                                                           # 식재료를 pop한다

recur(0, 0, [])                                                             # 깊이 0부터 0번 음식부터 탐색한다
if ans == 1e9:                                                              # 조건을 만족하는 음식 조합이 없다면
    print(-1)                                                               # -1을 출력하고
else:                                                                       # 조건을 만족하는 음식조합이 있다면
    print(ans)                                                              # 최소비용을 출력하고
    for a in ans2:                                                          # 그때 음식을 반복해서
        print(a+1, end=' ')                                                 # 음식의 번호를 출력한다