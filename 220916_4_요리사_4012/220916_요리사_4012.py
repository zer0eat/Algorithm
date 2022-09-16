# 요리사_4012

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 식재료를 반으로 나눠줄 함수
def half(a):                            #
    global food                         # 식재료를 반으로 나눈 부분집합을 저장할 빈 리스트를 불러오고
    if a == N:                          # 모든 요소에 대해 비트를 결정했을 때
        if sum(bit) == N//2:            # 부분집합 중 식재료 반으로 나눠져 있는 경우만
            food.append(bit[:])         # food에 저장한다
        return
    bit[a] = 0                          # 비트를 0으로 저장하고
    half(a+1)                           # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다
    bit[a] = 1                          # 비트를 0으로 부분집합을 구하고 나왔다면 이번에는 비트를 1로 저장하고
    half(a+1)                           # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다

# input 받기
T = int(input())                        # 테스트 케이스
for t in range(T):                      # 테스트 케이스를 반복할 때
    N = int(input())                    # 식재료의 개수
    arr = [list(map(int,input().split())) for _ in range(N)]    # 식재료의 조화를 행렬형태로 받는다

    bit = [0] * N                       # 식재료를 반으로 나눌 때 필요한 비트를 식재료 만큼 생성
    food = []                           # 식재료를 반으로 나눈 부분집합을 저장할 빈 리스트
    ind = []                            # 식재료의 인덱스를 저장하기 위한 빈 리스트
    for i in range(N):                  # 식재료의 수만큼 반복하면서
        ind.append(i)                   # ind에 식재료의 인덱스를 저장해준다

    half(0)                             # 식재료를 반으로 나누는 함수를 돌린다

    ans = 1000000                       # 두 음식의 시너지의 차를 저장할 변수
    while food:                         # food 리스트가 빌때까지 반복해서
        t1 = []                         # 식재료를 반으로 나눈 인덱스를 저장할 팀 1과
        t2 = []                         # 식재료를 반으로 나눈 인덱스를 저장할 팀 2를 생성한다
        A = food.pop(0)                 # 부분집합에서 식재료를 반으로 나눈 경우를 하나 꺼내
        for a in range(N):              # 반으로 나눈 경우를 살펴볼 때때
            if A[a] == 1:               # 만약 1이 나왔다면
                t1.append(ind[a])       # 팀 1에 인덱스를 넣고
            elif A[a] == 0:             # 만약 0이 나왔다면
                t2.append(ind[a])       # 팀 2에 인덱스를 넣는다
        else:                           # 식재료 배분이 끝났다면
            tmp1 = 0                    # 팀 1의 시너지의 합을 저장할 변수
            for q1 in t1:               # 팀 1의 인덱스를 반복해서
                for q2 in t1:           # 팀 1의 다른 재료와 조합할 때
                    if q1 != q2:        # 같은 재료가 아니라면
                        tmp1 += arr[q1][q2] # 같은 식재료가 아니라면 tmp1에 추가

            tmp2 = 0                    # 팀 2의 시너지의 합을 저장할 변수
            for w1 in t2:               # 팀 2의 인덱스를 반복해서
                for w2 in t2:           # 팀 2의 다른 재료와 조합할 때
                    if w1 != w2:        # 같은 재료가 아니라면
                        tmp2 += arr[w1][w2] # 같은 식재료가 아니라면 tmp2에 추가

            if ans > abs(tmp1-tmp2):    # ans가 두 값의 차의 절대값보다 작다면
                ans = abs(tmp1 - tmp2)  # ans에 새로운 값을 저장한다
            if ans == 0:                # 0 보다 작은 값이 나올 수 없으므로 0이 나온다면
                print(f'#{t + 1}', ans) # ans를 출력하고
                break                   # 반복문을 종료한다
    else:                               # while문 반복이 끝나면
        print(f'#{t+1}', ans)           # ans를 출력한다