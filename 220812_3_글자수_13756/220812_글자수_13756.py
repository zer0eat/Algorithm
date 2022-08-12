# 글자수_13756

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N = list(input())
    M = list(input())
    countDic = {}

    # N 값 딕셔너리로 만들기
    for n in N:
        countDic[n] = 0

    # N값이 M안에 있으면 하나씩 세기
    for m in M:
        if m in countDic:
            countDic[m] += 1

    # countDic에서 value 값이 가장 큰 것 추출하기
    maxV = 0
    for c in countDic:
        if countDic[c] > maxV:
            maxV = countDic[c]

    print(f'#{t+1} {maxV}')


