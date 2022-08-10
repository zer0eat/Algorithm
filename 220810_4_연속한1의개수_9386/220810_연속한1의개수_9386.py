# 연속한1의개수_9386

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input()))

    # 연속된 1 찾기
    cnt = 0 # 연속 된 1개수
    biggest = []
    for l in lst:
        if l == 1:
            cnt += 1
        else:
            biggest.append(cnt)
            cnt = 0
    else:
        biggest.append(cnt)

    big1 = 0
    for b in biggest:
        if b > big1:
            big1 = b

    print(f'#{t+1} {big1}')
