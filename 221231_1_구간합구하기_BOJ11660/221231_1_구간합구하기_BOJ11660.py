# 구간합구하기_BOJ11660

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())                           # N 행렬의 길이 / M 찾고자하는 구간합의 수
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 행렬을 lst에 저장하고

for i in range(N):                                                      # 행을 반복하고
    tmp = 0                                                             # 변수 tmp를 0으로 생성해서
    for j in range(N):                                                  # 열을 반복한 후
        tmp += lst[i][j]                                                # tmp에 해당 요소를 더하고
        lst[i][j] = tmp                                                 # 요소를 tmp의 값으로 바꿔주어 요소를 해당 열까지의 합으로 바꿔준다

for m in range(M):                                                      # 찾고자하는 구간합의 수를 반복해서
    find = list(map(int, sys.stdin.readline().split()))                 # 시작점과 끝점을 리스트로 input받고
    ans = 0                                                             # 정답을 저장할 변수를 생성한다
    for i in range(find[0]-1, find[2]):                                 # 행의 시작점부터 끝점까지 반복해서
        if find[1] == 1:                                                # 시작점의 열이 첫번째라면
            ans += lst[i][find[3]-1]                                    # ans에 끝점의 열까지 전부 더한다
        else:                                                           # 시작점의 열이 첫번째가 아니라면
            ans += (lst[i][find[3]-1] - lst[i][find[1]-2])              # 미리 더해둔 끝점의 열에서 시작점 이전의 합을 빼서 ans에 더한다
    else:                                                               # 반복을 마쳤다면
        print(ans)                                                      # 정답을 출력한다

