# 체스판다시칠하기_BOJ1018

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())                       # N 보드의 행의 길이 / M 보드의 열의 길이
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]       # arr 보드를 리스트형태로 input

maxc = N*M                                                          # 색을 바꿔 칠할 최소 개수를 저장할 변수를 생성
for k in range(N-7):                                                # 왼쪽상단을 시작점으로 시작하기 위해 행을 반복하고
    for h in range(M-7):                                            # 열을 반복할 때
        cnt = 0                                                     # 바꿔칠할 숫자를 셀 변수를 생성하고
        for i in range(8):                                          # 행을 8칸
            for j in range(8):                                      # 열을 8칸 반복해서
                if i % 2 == 0:                                      # 인덱스가 짝수행일 때
                    if j % 2 == 0:                                  # 짝수번째 열이
                        if arr[k + i][h + j] != 'W':                # 흰색이 아니면
                            cnt += 1                                # cnt를 하나 추가
                    elif j % 2 == 1:                                # 홀수번째 열이
                        if arr[k + i][h + j] != 'B':                # 검은색이 아니면
                            cnt += 1                                # cnt를 하나 추가
                elif i % 2 == 1:                                    # 인덱스가 홀수행일 때
                    if j % 2 == 0:                                  # 짝수번째 열이
                        if arr[k + i][h + j] != 'B':                # 검은색이 아니면
                            cnt += 1                                # cnt를 하나 추가
                    elif j % 2 == 1:                                # 홀수번째 열이
                        if arr[k + i][h + j] != 'W':                # 흰색이 아니면
                            cnt += 1                                # cnt를 하나 추가
        else:                                                       # 반복을 마쳤을 때
            if cnt < maxc:                                          # cnt가 maxc보다 작은 값이면
                maxc = cnt                                          # maxc를 cnt로 저장한다

        cnt = 0                                                     # 위와 같은 방법으로 왼쪽상단의 시작점이 B일때 검사
        for i in range(8):                                          
            for j in range(8):
                if i % 2 == 1:
                    if j % 2 == 0:
                        if arr[k + i][h + j] != 'W':
                            cnt += 1
                    elif j % 2 == 1:
                        if arr[k + i][h + j] != 'B':
                            cnt += 1
                elif i % 2 == 0:
                    if j % 2 == 0:
                        if arr[k + i][h + j] != 'B':
                            cnt += 1
                    elif j % 2 == 1:
                        if arr[k + i][h + j] != 'W':
                            cnt += 1
        else:
            if cnt < maxc:
                maxc = cnt

print(maxc)

