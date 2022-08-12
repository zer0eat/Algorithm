# GNS_1221

# input.txt 열기
import sys
sys.stdin = open('input.txt')

#input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    case, N = input().split()
    N = int(N)
    arr = list(input().split())

    # 작은 수부터 정리하기
    new_arr = []
    for a in arr:
        if a == 'ZRO':
            new_arr.append(a)
    for b in arr:
        if b == 'ONE':
            new_arr.append(b)
    for c in arr:
        if c == 'TWO':
            new_arr.append(c)
    for d in arr:
        if d == 'THR':
            new_arr.append(d)
    for e in arr:
        if e == 'FOR':
            new_arr.append(e)
    for f in arr:
        if f == 'FIV':
            new_arr.append(f)
    for g in arr:
        if g == 'SIX':
            new_arr.append(g)
    for h in arr:
        if h == 'SVN':
            new_arr.append(h)
    for i in arr:
        if i == 'EGT':
            new_arr.append(i)
    for j in arr:
        if j == 'NIN':
            new_arr.append(j)

    print(f'{case} ', *new_arr)

