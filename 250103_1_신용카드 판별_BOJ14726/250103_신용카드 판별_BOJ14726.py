# 신용카드 판별_BOJ14726

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())
for t in range(T):
    credit = list(input().strip())
    for n in range(1, 16, 2):
        tmp = int(credit[n])
        tmp *= 2
        if tmp > 9:
            tmp = list(str(tmp))
            tmp = int(tmp[0]) + int(tmp[1])
        credit[n] = tmp
    ans = 0
    for c in credit:
        ans += int(c)
    print(credit)
    print(ans)
    if ans % 10:
        print('T')
    else:
        print('F')
