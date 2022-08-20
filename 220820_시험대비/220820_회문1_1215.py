import sys
sys.stdin = open('회문1_input.txt')

T = 10                                                              # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스 만큼 반복
    N = int(input())                                                # 찾아야하는 회문의 길이
    arr = [list(input()) for _ in range(8)]                         # 행렬 받기

    cnt = 0                                                         # 회문의 수를 저장할 변수
    for i in range(8):                                              # 행의 길이만큼 반복할 때
        for j in range(8-N+1):                                      # 회문의 시작점이 되는 요소를 반복할 때
            for k in range(N):                                      # 회문의 길이만큼 반복하여
                if arr[i][j+k] == arr[i][N+j-k-1]:                  # 만약 회문이면 pass
                    pass
                elif arr[i][j + k] != arr[i][N + j - k - 1]:        # 회문이 아니라면 break
                    break
            else:                                                   # for문을 모두 pass하여 회문으로 판정되면
                cnt += 1                                            # cnt를 하나 추가

    for i in range(8):                                              # 위와 같은 방법으로 세로도 검증
        for j in range(8-N+1):
            for k in range(N):
                if arr[j+k][i] == arr[N+j-k-1][i]:
                    pass
                elif arr[j + k][i] != arr[N + j - k - 1][i]:
                    break
            else:
                cnt += 1

    print(f'#{t+1}', cnt)