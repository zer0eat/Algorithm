# 회문2_1216_slicing 없이 풀기

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10 # 테스트 수
for t in range(T):
    N = int(input()) # 테스트 케이스
    arr = [list(input()) for _ in range(100)] # 회문이 포함된 100x100 판
    arr_reverse = [[arr[j][i] for j in range(100)] for i in range(100)]


    # 회문 찾기
    N = 100  # 찾을 회문의 길이
    maxL = 0  # 최대 회문의 길이
    while N > 0:
        for i in range(100):
            for j in range(100 - N + 1):
                str = ''
                str_c = ''
                str_r = ''
                str_c_r = ''
                for k in range(N):
                    str += arr[i][j + k]
                    str_r = arr[i][j + k] + str_r
                    str_c += arr[j + k][i]
                    str_c_r = arr[j + k][i] + str_c_r
                else:
                    if str == str_r or str_c == str_c_r:
                        maxL = N
                        print(f'#{t+1}', maxL)
                        break
            if maxL == N:
                break
        if maxL == N:
            break
        else:
            N -= 1
