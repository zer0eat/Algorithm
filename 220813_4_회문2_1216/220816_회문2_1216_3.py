# 회문2_1216_slicing 없이 풀기

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10 # 테스트 수
for t in range(T):
    N = int(input()) # 테스트 케이스
    arr = [list(input()) for _ in range(100)] # 회문이 포함된 100x100 판

    # 가로 회문 찾기
    N = 100  # 찾을 회문의 길이
    maxL = 0  # 최대 회문의 길이
    a = True
    while N > 0:
        for i in range(100):
            for j in range(100 - N + 1):
                for k in range(N):
                    if arr[i][j + k] == arr[i][(N-1) + j - k]:
                        pass
                    else:
                        break
                else:
                    maxL = N
                    a = False
                    break
            if a == False:
                break
        if a == False:
            break
        else:
            N -= 1

    # 세로 회문 찾기
    N = 100  # 찾을 회문의 길이
    maxR = 0 # 최대 회문의 길이
    a = True
    while N > 0:
        for i in range(100):
            for j in range(100 - N + 1):
                for k in range(N):
                    if arr[j + k][i] == arr[(N - 1) + j - k][i]:
                        pass
                    else:
                        break
                else:
                    maxR = N
                    a = False
                    break
            if a == False:
                break
        if a == False:
            break
        else:
            N -= 1

    if maxL <= maxR:
        print(f'#{t+1}', maxR)
    elif maxL > maxR:
        print(f'#{t+1}', maxL)
