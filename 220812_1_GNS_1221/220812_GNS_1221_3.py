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
    Dic_Num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    new_arr = []

    # arr 문자를 숫자로 바꾸기
    for a in arr:
        new_arr.append(Dic_Num[a])

    # 오름차순 정렬
    ascending_arr = []
    num = 0
    while num < 10:
        for w in new_arr:
            if w == num:
                ascending_arr.append(w)
        else:
            num += 1

    # 딕셔너리 뒤집기
    convert_Dic_Num = {v: k for k, v in Dic_Num.items()}

    # 숫자를 문자로 바꾸기
    result = []
    for s in ascending_arr:
        result.append(convert_Dic_Num[s])

    print(f'{case} ', *result)
