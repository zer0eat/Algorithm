# 전자카트_14174

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def golf(i, N):                                     # order리스트에서 i 인덱스에서 부터 N개의 순열을 조합
    if i == N:                                      # i와 N이 같아 질때
        qqq.append(order[:])                        # 결과를 qqq에 넣음
    else:                                           # 같지 않을 때
        for j in range(i, N):                       # 반복문을 i부터 N 까지 돌려서
            order[i], order[j] = order[j], order[i] # i와 j를 바꾼후
            golf(i+1, N)                            # 다음 인덱스를 살펴보고
            order[i], order[j] = order[j], order[i] # i와 j를 제자리로 바꿔놓는다

# input 받기
T = int(input())                                    # 테스트케이스
for t in range(T):                                  # 테스트케이스를 반복할 때
    N = int(input())                                # 행렬의 개수
    arr = [list(map(int, input().split())) for _ in range(N)]   # 골프장의 행렬로 받음
    ans = 100 * N *2                                  # 전기량을 저장할 변수
    order = [_ for _ in range(1, N)]                # 1부터 N까지 요소가 담긴 리스트를 생성하고

    qqq = []                                        # golf 함수의 결과를 받을 리스트
    golf(0, N-1)                                    # order함수의 첫번째 리스트부터 N-1개의 순열을 뽑을 함수를 돌린다

    for q in qqq:                                   # 순찰할수 있는 경우의 수를 살펴볼 때
        o = 0                                       # 출발점의 행을 o로 저장하고
        tmp = 0                                     # 전기 소비량을 저장할 변수 tmp를 생성한다
        for j in q:                                 # 경로를 하나씩 확인하면서
            if o == j:                              # 행과 열이 같은줄에 도착하면
                break                               # 그 경로는 돌 수 없으므로 break 한다
            tmp += arr[o][j]                        # 행과열이 다른 경우에는 tmp에 해당 소비량을 저장하고
            if tmp > ans:                           # tmp가 ans보다 크다면 break
                break
            o = j                                   # 다음으로 이동하기 위해 현재 열의 인덱스를 o에 저장한다
        else:                                       # 경로를 모두 순찰했다면
            tmp += arr[o][0]                        # 사무실로 들어가기 전 마지막 소비량을 tmp에 더하고
            if ans > tmp:                           # ans보다 tmp가 작을 때
                ans = tmp                           # ans에 tmp를 저장한다

    print(f'#{t+1}', ans)

