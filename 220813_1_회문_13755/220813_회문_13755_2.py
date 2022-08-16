# 회문_13755

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N, M = map(int, input().split()) # 입력될 문장의 숫자
    lst = [list(input()) for _ in range(N)]
    lst_reverse = [[lst[j][i] for j in range(N)] for i in range(N)]

    # 회문찾기
    for n in range(N): # NxN 행렬에서 가로로 탐색을 할 때 회문을 찾아 출력한다.
        for m in range(N - M + 1):
            if lst[n][m : m + M] == lst[n][m : m + M][::-1]:
                print(f'#{t+1}', ''.join(lst[n][m : m + M]))

    for n in range(N): # NxN 행렬에서 세로로 탐색을 할 때 회문을 찾아 출력한다.
        for m in range(N - M + 1):
            if lst_reverse[n][m : m + M] == lst_reverse[n][m : m + M][::-1]:
                print(f'#{t+1}', ''.join(lst_reverse[n][m : m + M]))