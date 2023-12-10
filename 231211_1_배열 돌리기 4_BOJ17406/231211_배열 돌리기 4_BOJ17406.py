# 배열 돌리기 4_BOJ17406

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from copy import deepcopy
from itertools import permutations

# input 받기
N, M, K = map(int, input().split())                         # N 배열의 행 / M 배열의 열 / K 연산의 개수를 input 받고
lst = [list(map(int, input().split())) for _ in range(N)]   # 배열의 정보를 input 받는다
lst_o = deepcopy(lst)                                       # 배열의 정보를 lst_o에 저장해두고
rotation = []                                               # 연산을 할 정보를 저장할 리스트를 생성한다
for k in range(K):                                          # 연산의 개수를 반복해서
    r, c, s = map(int, input().split())                     # 회전 연산의 정보 r,c 중심의 행렬 / s 회전 크기를 input 받고
    rotation.append([r-1, c-1, s])                          # rotation에 연산 정보를 append 한다
ans = 1e9                                                   # 배열 A의 최소값을 저장할 변수를 생성하고
for rot in permutations(rotation, K):                       # 연산의 정보를 순열로 섞어서
    lst = deepcopy(lst_o)                                   # lst에 초기 배열 정보를 받아온다
    for ro in rot:                                          # 순열로 섞인 연산정보를 반복해서
        r, c, s = ro                                        # 연산정보에서 연산의 중심 r, c와 회전크기 s로 저장하고
        new = deepcopy(lst)                                 # 회전한 연산을 저장할 리스트를 생성한다
        for q in range(1, s+1):                             # 회전의 크기를 반복해서
            for j in range(c-q, c+q+1):                     # 회전할 열을 반복하고
                if j == c-q:                                # 첫번째 열이라면
                    new[r-q][j] = lst[r-q+1][j]             # 맨 위 행의 첫번째 열은 아래에서 가져오고
                    new[r+q][j] = lst[r+q][j+1]             # 맨 아래 행의 첫번째 열을 오른쪽에서 가져온다
                elif j == c+q:                              # 마지막 행이라면
                    new[r-q][j] = lst[r-q][j-1]             # 맨 위 행의 첫번째 열은 왼쪽에서 가져오고
                    new[r+q][j] = lst[r+q-1][j]             # 맨 아래 행의 첫번째 열을 위에서 가져온다
                else:                                       # 첫번째와 마지막 행이 아니라면
                    new[r-q][j] = lst[r-q][j-1]             # 맨 위 행의 각 열은 왼쪽에서 가져오고
                    new[r+q][j] = lst[r+q][j+1]             # 맨 아래 행의 각 열은 오른쪽에서 가져온다
            for i in range(r-q+1, r+q):                     # 회전할 행 중 첫번째와 마지막을 빼고 반복해서
                new[i][c-q] = lst[i+1][c-q]                 # 맨 왼쪽 열의 각 행은 아래에서 가져오고
                new[i][c+q] = lst[i-1][c+q]                 # 맨 오른쪽 열의 각 행은 위에서 가져온다
        else:                                               # 회전의 크기가 끝났다면
            lst = deepcopy(new)                             # lst에 회전한 배열을 저장하고
    else:                                                   # 연산정보를 모두 반복했다면
        for a in lst:                                       # 배열의 각 행을 반복해서
            ans = min(ans, sum(a))                          # ans에 각 행의 합 중 가장 작은 값을 저장한다
print(ans)                                                  # 모든 연산 정보를 순열로 조합한 후 가장 작은 값을 출력한다