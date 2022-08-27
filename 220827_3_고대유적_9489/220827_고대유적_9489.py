# 고대유적_9489

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                    # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스만큼 반복할 때
    N, M = map(int, input().split())                                # N = 행의 값 / M = 열의 값
    picture = [list(map(int, input().split())) for _ in range(N)]   # 사진의 데이터가 담기 행렬을 저장

    # 유적의 길이 측정하기
    # 가로 유적 측정
    ruins = []                                                      # 유적의 길이를 저장할 리스트
    for i in range(N):                                              # 행의 길이만큼 반복
        cnt = 0                                                     # 길이를 저장할 변수
        for j in range(M):                                          # 열의 길이만큼 반복
            if picture[i][j] == 1:                                  # 행렬을 탐색하며 1이 나오면
                cnt += 1                                            # cnt에 1을 더함
            elif picture[i][j] == 0:                                # 행렬을 탐색하며 0이 나오면
                if cnt > 0:                                         # cnt에 저장된 길이가 0이 아니면
                    ruins.append(cnt)                               # ruins 리스트에 저장된 유적의 길이를 append
                    cnt = 0                                         # cnt 초기화
                else:                                               # 만약 저장된 길이가 0일땐
                    pass                                            # 패스
        else:                                                       # 유적을 찍은 사진의 행을 모두 탐색했다면
            if cnt > 0:                                             # cnt에 저장된 길이가 0이 아니면
                ruins.append(cnt)                                   # ruins 리스트에 저장된 유적의 길이를 append
                cnt = 0                                             # cnt 초기화
            else:                                                   # 만약 저장된 길이가 0일땐
                pass                                                # 패스

    # 세로 유적 측정
    for j in range(M):                                              # 열의 길이만큼 반복
        cnt = 0                                                     # 길이를 저장할 변수
        for i in range(N):                                          # 행의 길이만큼 반복
            if picture[i][j] == 1:                                  # 행렬을 탐색하며 1이 나오면
                cnt += 1                                            # cnt에 1을 더함
            elif picture[i][j] == 0:                                # 행렬을 탐색하며 0이 나오면
                if cnt > 0:                                         # cnt에 저장된 길이가 0이 아니면
                    ruins.append(cnt)                               # ruins 리스트에 저장된 유적의 길이를 append
                    cnt = 0                                         # cnt 초기화
                else:                                               # 만약 저장된 길이가 0일땐
                    pass                                            # 패스
        else:                                                       # 유적을 찍은 사진의 행을 모두 탐색했다면
            if cnt > 0:                                             # cnt에 저장된 길이가 0이 아니면
                ruins.append(cnt)                                   # ruins 리스트에 저장된 유적의 길이를 append
                cnt = 0                                             # cnt 초기화
            else:                                                   # 만약 저장된 길이가 0일땐
                pass                                                # 패스

    # 최대 길이 유적 찾기
    maxL = 0                                                        # 유적의 최대 길이를 저장할 변수
    for r in ruins:                                                 # 저장된 유적을 반복할때
        if r > maxL:                                                # 최대 길이보다 긴 유적이 나오면
            maxL = r                                                # maxL 변수에 가장 긴 유적으로 바꿔준다
    print(f'#{t+1}', maxL)
