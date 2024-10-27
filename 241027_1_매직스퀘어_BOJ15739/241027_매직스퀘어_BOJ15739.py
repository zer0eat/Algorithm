# 매직스퀘어_BOJ15739

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 마방진의 길이를 input 받고
matrix = [list(map(int, input().split())) for _ in range(N)]    # 마방진을 input 받는다
ans = N*(N**2+1)//2                 # 한 줄의 합을 저장하고
lst = [0] * (N**2+1)                # 모든 원소가 나왔는지 체크할 리스트를 생성한다
for n in range(N):                  # 행을 반복하고
    r, c = 0, 0                     # 한 줄의 합을 저장할 변수를 생성해서
    for m in range(N):              # 열을 반복하고
        lst[matrix[n][m]] = 1       # 나온 원소를 저장한다
        r += matrix[n][m]           # 행의 합을 더해주고
        c += matrix[m][n]           # 열을 합을 더해준다
    else:                           # 한 줄의 합이 구해지면
        if r != ans or c != ans:    # 한 줄의 합이 ans와 다르다면
            print('FALSE')          # FALSE를 출력하고
            quit()                  # 종료한다
if sum(lst) != N**2:                # 모든 원소가 나오지 않았다면
    print('FALSE')                  # FALSE를 출력하고
    quit()                          # 종료한다
x, y = 0, 0                         # 대각선의 합을 저장할 변수를 생성하고
for n in range(N):                  # 한 행을 반복해서
    x += matrix[n][N-n-1]           # 대각선의 합을 더해주고
    y += matrix[n][n]               # 반대 대각선의 합을 더해준다
else:                               # 대각선의 합이 구해지면
    if x != ans or y != ans:        # 대각선의 합이 ans와 다르다면
        print('FALSE')              # FALSE를 출력하고
        quit()                      # 종료한다
print('TRUE')                       # TRUE를 출력한다