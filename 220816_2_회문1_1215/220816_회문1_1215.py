# 회문1_1215

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10
for t in range(T):
    N = int(input()) # 찾을 회문의 길이
    arr = [list(input()) for _ in range(8)] # 회문이 들어있는 행렬

    # 길이가 N인 회문 찾기(가로)
    cnt = 0
    lst = []
    for i in range(8):
        for j in range(8 - N + 1):
            str = ''
            for k in range(N):
                str += (arr[i][j + k])
            else:
                lst.append(str)

    # 길이가 N인 회문 찾기(세로)
    for i in range(8):
        for j in range(8 - N + 1):
            str = ''
            for k in range(N):
                str += (arr[j + k][i])
            else:
                lst.append(str)
    # 문자열 뒤집기
    lst_reverse = []
    for l in lst:
        reverse_str = ''
        for r in l:
            reverse_str = r + reverse_str
        else:
            lst_reverse.append(reverse_str)
    # 회문 찾기
    for a in range(len(lst)):
        if lst[a] == lst_reverse[a]:
            cnt += 1
    print(f'#{t+1} ', cnt)

