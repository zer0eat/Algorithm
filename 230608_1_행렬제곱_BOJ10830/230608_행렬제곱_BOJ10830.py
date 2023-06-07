# 행렬제곱_BOJ10830

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, B = map(int, input().split())                            # N 행렬의 크기 / B 거듭제곱의 지수
A = [list(map(int, input().split())) for _ in range(N)]     # 행렬 A를 input 받는다
B = bin(B)[2:][::-1]                                        # 지수를 이진수로 바꾼후 뒤집는다
ans = [[0]*N for _ in range(N)]                             # 정답을 저장할 행렬을 생성하고
for i in range(N):                                          # 행렬의 크기를 반복해서
    ans[i][i] = 1                                           # 행과 열이 같은 곳에 1을 저장해서 항등행렬을 만든다

for b in B:                                                 # 지수를 이진수로 바꾼 수를 반복해서
    if b == '1':                                            # 이진수의 해당 자리가 1인 경우
        tmp = [[0] * N for _ in range(N)]                   # 빈 행렬을 생성하고
        for i in range(N):                                  # 행의 크기를 반복하고
            for j in range(N):                              # 열의 크기를 반복해서
                tmpNum = 0                                  # 행렬의 곱을 저장할 변수를 생성한다
                for k in range(N):                          # i행 j열의 값을 구하기 위해 행렬의 크기만큼 반복해서
                    tmpNum += ans[k][j] * A[i][k]           # tmpNum에 ans와 A행렬의 곱을 더하고
                else:                                       # 모든 반복이 끝났으면
                    tmp[i][j] = tmpNum % 1000               # tmp의 i행 j열의 값에 tmpNum을 1000으로 나눈 나머지를 저장한다
        else:                                               # 모든 행렬의 곱을 마쳤다면
            ans = tmp[:]                                    # ans에 tmp를 저장한다

    tmp = [[0] * N for _ in range(N)]                       # 빈 행렬을 생성하고
    for i in range(N):                                      # 행의 크기를 반복하고
        for j in range(N):                                  # 열의 크기를 반복해서
            tmpNum = 0                                      # 행렬의 곱을 저장할 변수를 생성한다
            for k in range(N):                              # i행 j열의 값을 구하기 위해 행렬의 크기만큼 반복해서
                tmpNum += A[k][j] * A[i][k]                 # tmpNum에 A와 A행렬의 곱을 더하고
            else:                                           # 모든 반복이 끝났으면
                tmp[i][j] = tmpNum % 1000                   # tmp의 i행 j열의 값에 tmpNum을 1000으로 나눈 나머지를 저장한다
    else:                                                   # 모든 행렬의 곱을 마쳤다면
        A = tmp[:]                                          # A에 tmp를 저장한다
for a in ans:                                               # ans를 반복해서
    print(*a)                                               # 한 행씩 출력한다