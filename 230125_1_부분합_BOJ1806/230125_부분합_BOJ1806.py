# 부분합_BOJ1806

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, S = map(int, sys.stdin.readline().split())           # N 수열의 길이 / S 구하려는 부분 합
lst = list(map(int, sys.stdin.readline().split()))      # lst에 수열의 원소를 list로 input 받는다
lst2 = lst[:]                                           # lst2에 lst를 복사한다

for i in range(1, N):                                   # 수열의 인덱스를 1부터 끝까지 반복해서
    lst[i] = lst[i] + lst[i-1]                          # i의 해당 원소와 그전의 원소의 합으로 바꿔준다

cnt = 100000                                            # cnt를 수열의 최대길이인 100000으로 설정하고
start = 0                                               # 투포인트의 시작점과
end = 0                                                 # 투포인트의 끝점을 설정한다
while start < N:                                        # 투포인트의 시작점이 N이 될때까지 반복해서
    if start == end:                                    # 시작점과 끝점이 같다면
        if lst2[end] >= S:                              # 인덱스 end의 원소가 S보다 크다면
            cnt = 1                                     # cnt를 1로 바꾸고
            print(cnt)                                  # cnt를 출력하고
            quit()                                      # 종료한다
        else:                                           # 인덱스 end의 원소가 S보다 작다면
            if end == N-1:                              # end가 끝에 도달했다면
                start += 1                              # start를 1 증가시키고
            else:                                       # end가 끝에 도달하지 않았다면
                end += 1                                # end를 1 증가시킨다
    else:                                               # start와 end가 다르다면
        if start == 0:                                  # start가 0일때는
            if lst[end] >= S:                           # 0부터 end까지의 합이 S보다 크다면
                if cnt > end-start:                     # cnt가 end-start보다 크다면
                    cnt = end+1                         # cnt를 end-start로 바꾼 후
                start += 1                              # start를 1 증가시킨다
            else:                                       # 0부터 end까지의 합이 S보다 작다면
                if end == N - 1:                        # end가 끝에 도달했다면
                    start += 1                          # start를 1 증가시키고
                else:                                   # end가 끝에 도달하지 않았다면
                    end += 1                            # end를 1 증가시킨다
        elif lst[end] - lst[start] >= S:                # start가 0이 아니면서 start + 1부터 end까지의 합이 S보다 크다면
            if cnt > end-start:                         # cnt가 end-start보다 크다면
                cnt = end-start                         # cnt를 end-start로 바꾼 후
            start += 1                                  # start를 1 증가시킨다
        else:                                           # S보다 작다면
            if end == N-1:                              # end가 끝에 도달했다면
                start += 1                              # start를 1 증가시키고
            else:                                       # end가 끝에 도달하지 않았다면
                end += 1                                # end를 1 증가시킨다
else:                                                   # while문의 반복이 끝났으면
    if cnt == 100000:                                   # cnt가 처음과 변동이 없는 경우에는
        print(0)                                        # 0을 출력하고
    else:                                               # cnt가 변동이 있는 경우에는
        print(cnt)                                      # cnt를 출력한다