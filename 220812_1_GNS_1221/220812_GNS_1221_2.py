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
    new_arr = []

    # 숫자로 바꾸기
    for a in arr:
        if a == 'ZRO':
            new_arr.append(0)
        elif a == 'ONE':
            new_arr.append(1)
        elif a == 'TWO':
            new_arr.append(2)
        elif a == 'THR':
            new_arr.append(3)
        elif a == 'FOR':
            new_arr.append(4)
        elif a == 'FIV':
            new_arr.append(5)
        elif a == 'SIX':
            new_arr.append(6)
        elif a == 'SVN':
            new_arr.append(7)
        elif a == 'EGT':
            new_arr.append(8)
        elif a == 'NIN':
            new_arr.append(9)

    # 작은 수 부터 정리하기
    ascending_arr = []
    num = 0
    while num < 10:
        for w in new_arr:
            if w == num:
                ascending_arr.append(w)
        else:
            num += 1

    # 문자로 바꾸기
    back_arr = []
    for r in ascending_arr:
        if r == 0:
            back_arr.append('ZRO')
        elif r == 1:
            back_arr.append('ONE')
        elif r == 2:
            back_arr.append('TWO')
        elif r == 3:
            back_arr.append('THR')
        elif r == 4:
            back_arr.append('FOR')
        elif r == 5:
            back_arr.append('FIV')
        elif r == 6:
            back_arr.append('SIX')
        elif r == 7:
            back_arr.append('SVN')
        elif r == 8:
            back_arr.append('EGT')
        elif r == 9:
            back_arr.append('NIN')
    print(len(back_arr))
    print(f'{case} ', *back_arr)
