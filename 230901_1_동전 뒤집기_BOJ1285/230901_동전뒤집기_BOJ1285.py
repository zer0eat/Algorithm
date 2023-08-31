# 동전뒤집기_BOJ1285

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import copy
from itertools import product

# input 받기
N = int(sys.stdin.readline())                                       # 동전의 줄 수를 input 받고
board = [list(sys.stdin.readline().strip()) for _ in range(N)]      # 동전의 상태를 행렬로 input 받아 저장한다
rev_board = copy.deepcopy(board)                                    # 동전을 전체 뒤집은 상태를 저장할 행렬을 복사하고
for i in range(N):                                                  # 행을 반복하고
    for j in range(N):                                              # 열을 반복해서
        if rev_board[i][j] == 'T':                                  # 동전이 뒷면을 보고 있다면
            rev_board[i][j] = 'H'                                   # 앞면을 향하게 뒤집고
        else:                                                       # 동전이 앞면을 보고 있다면
            rev_board[i][j] = 'T'                                   # 뒷면을 향하게 뒤집는다
A = [0, 1]                                                          # 0과 1을 넣은 리스트를 생성하고
ans = N ** 2                                                        # 뒷면을 향하는 동전의 개수를 최댓값으로 저장한 변수를 생성한다
for b in product(A, repeat=N):                                      # 1일때 해당 행을 뒤집고 0일때 해당 행을 뒤집지 않을 때 각 행을 뒤집을지 여부를 결정하는 product를 반복해서
    tmp_board = []                                                  # 뒤집은 상태를 저장할 리스트를 생성한다
    for i in range(N):                                              # 행을 반복해서
        if b[i] == 1:                                               # product의 i번째 행이 1일 때
            tmp_board.append(rev_board[i][:])                       # 해당 행을 뒤집어서 tmp_board에 저장한다
        else:                                                       # product의 i번째 행이 0일 때
            tmp_board.append(board[i][:])                           # 해당 행을 뒤집지 않고 저장한다
    cnt = 0                                                         # 뒷면을 보고 있는 개수를 저장할 변수를 생성하고
    for i in range(N):                                              # 열을 반복하고
        tmp = 0                                                     # 해당 열의 뒷면 개수를 저장할 변수를 생성한 뒤
        for j in range(N):                                          # 행을 반복해서
            if tmp_board[j][i] == 'T':                              # 뒷면을 보고 있다면
                tmp += 1                                            # tmp를 1 증가시킨다
        cnt += min(tmp, N - tmp)                                    # 한 열을 반복한 후 현재 상태와 열을 뒤집은 상태 중 뒷면의 수가 더 적은 상태를 cnt에 더해준다
    ans = min(ans, cnt)                                             # 모든 열을 반복한 후 cnt와 ans 중 뒷면의 수가 더 적은 상태를 저장한다
print(ans)                                                          # 모든 상황을 반복한 후 뒷면의 최소 개수를 출력한다