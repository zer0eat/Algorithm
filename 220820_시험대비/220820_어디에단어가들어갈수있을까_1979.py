import sys
sys.stdin = open('어디에단어가들어갈수있을까_input.txt')

T = int(input())                                                    # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스 만큼 반복
    N, K = input().split()                                          # 행렬의 길이를 N 답의 길이를 K로 받음
    N = int(N)                                                      # int로 바꿈
    K = int(K)                                                      # int로 바꿈
    arr = []                                                        # 행렬을 담을 빈 리스트
    # input 방법 1
    # for n in range(N):
    #     arr.append(list(map(int, input().split())))

    # input 방법 2
    arr = [list(map(int, input().split())) for n in range(N)]       # arr에 행렬 받기

    cnt = 0                                                         # 빈칸의 개수를 세기 위한 변수
    answer = 0                                                      # K 만큼의 크기를 갖는 빈칸을 세기 위한 변수
    for i in range(N):                                              # 행의 길이 만큼 반복할 때
        for j in range(N):                                          # 열의 길이 만큼 반복할 때
            if arr[i][j] == 1:                                      # 요소의 값이 1이면
                cnt += 1                                            # cnt에 1 추가
            elif arr[i][j] == 0:                                    # 요소의 값이 0이면
                if cnt == K:                                        # cnt가 K만큼 일 땐
                    answer += 1                                     # answer에 1 추가
                cnt = 0                                             # cnt 0으로 초기화
        else:                                                       # 반복이 끝나면
            if cnt == K:                                            # cnt가 K만큼 일 땐
                answer += 1                                         # answer에 1 추가
            cnt = 0                                                 # cnt 0으로 초기화

    for i in range(N):                                              # 위와 같은 방법으로 세로로 찾음
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            elif arr[j][i] == 0:
                if cnt == K:
                    answer += 1
                cnt = 0
        else:
            if cnt == K:
                answer += 1
            cnt = 0


    print(f'#{t+1}', answer)
