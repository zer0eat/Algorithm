import sys
sys.stdin = open('파리퇴치_input.txt')

T = int(input())                                                    # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스 만큼 반복
    N, M = input().split()                                          # 행렬의 길이를 N 파리채의 크기를 M으로 받는다
    N = int(N)                                                      # int로 바꿔줌
    M = int(M)                                                      # int로 바꿔줌
    fly = [list(map(int, input().split())) for n in range(N)]       # fly에 행렬 저장

    flapper = []                                                    # 파리채로 잡은 파리의 수를 저장할 빈 리스트 만들기
    for i in range(N-M+1):                                          # 파리채의 왼쪽 위를 좌표를 기준으로 이동할 수 있을 만큼 반복
        for j in range(N-M+1):
            lst = 0                                                 # 잡은 파리의 수를 저장할 변수를 설정하고
            for k in range(M):                                      # 파리채의 범위 만큼 반복을 해서
                for h in range(M):                                  #
                    lst += fly[i+k][j+h]                            # 잡은 파리를 lst에 저장하고
            else:                                                   # 파리채의 크기만큼 반복이 끝나면
                flapper.append(lst)                                 # 잡은 파리를 flapper에 저장

    morefly = 0                                                     # 가장 많이 잡은 파리의 수를 저장할 변수를 만들고
    for f in flapper:                                               # flapper를 반복하면서
        if f > morefly:                                             # 현재 가장 많은 파리의 수보다 더 큰수가 나오면
            morefly = f                                             # 바꿔준다

    print(f'#{t+1}', morefly)
