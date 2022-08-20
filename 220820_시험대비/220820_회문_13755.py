import sys
sys.stdin = open('회문_input.txt')

T = int(input())                                                    # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스 만큼 반복
    N, M = input().split()                                          # 행렬의 길이를 N 회문의 길이를 M으로 받는다
    N = int(N)                                                      # int로 변경한다
    M = int(M)                                                      # int로 변경한다
    arr = [list(input()) for _ in range(N)]                         # 행렬을 받아 arr에 저장한다

    pand = False                                                    # 회문이 없을 때 False라는 설정을 준다
    for i in range(N):                                              # 행의 길이만큼 반복할 때
        for j in range(N-M+1):                                      # 회문의 시작점이 되는 요소까지 반복
            word = ''                                               # 회문을 저장할 빈 문자열
            for k in range(M):                                      # 회문의 길이만큼 반복
                if arr[i][j+k] == arr[i][M+j-k-1]:                  # 만약 회문이라면
                    word += arr[i][j+k]                             # word에 문자를 저장
                    pass
                elif arr[i][j+k] != arr[i][M+j-k-1]:                # 아니라면 반복문 break
                    break
            else:                                                   # 회문의 길이만큼 반복이 완료되면 회문이므로
                pand = True                                         # 회문이 있으니 True로 조건을 변경하고
                print(f'#{t+1}', word)                              # 회문을 출력한다

    if pand == False:                                               # 회문이 발견되지 않았다면
        for i in range(N):                                          # 위와 같은 조건으로 세로로 탐색한다
            for j in range(N - M + 1):
                word = ''
                for k in range(M):
                    if arr[j + k][i] == arr[M + j - k - 1][i]:
                        word += arr[j + k][i]
                        pass
                    elif arr[j + k][i] != arr[M + j - k - 1][i]:
                        break
                else:
                    pand = True
                    print(f'#{t + 1}', word)
