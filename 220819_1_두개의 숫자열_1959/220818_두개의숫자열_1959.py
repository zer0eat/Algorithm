# 두개의 숫자열_1959

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())         # 테스트 케이스
for t in range(T):
    N, M = map(int, input().split())

    # Ai에 항상 길이가 짧은 리스트를 입력하고 Bj에는 길이가 긴 리스트를 입력한다.
    if N < M:
        Ai = list(map(int, input().split()))
        Bj = list(map(int, input().split()))
    elif N > M:
        Bj = list(map(int, input().split()))
        Ai = list(map(int, input().split()))

    sum_all = []                                # 마주보는 숫자를 곱한 값의 합을 저장할 빈리스트
    for k in range(len(Bj)-len(Ai) + 1):        # 짧은 리스트가 긴 리스트에 한칸씩 이동할 수 있는 수 만큼 반복
        sum_a = 0                               # 짧은 리스트의 길이만큼 마주보는 숫자를 곱한 값의 합을 저장하는 변수
        for i in range(len(Ai)):                # 짧은 리스트의 길이 만큼 반복할 때
            sum_a += Ai[i] * Bj[i + k]          # 마주 보는 숫자를 곱해서 sum_a에 더해준다
        else:                                   # 반복이 끝나면
            sum_all.append(sum_a)               # 마주 보는 숫자를 곱한 값의 합을 sum_all에 append

    big = 0                                     # 마주보는 숫자를 곱한 값의 합 중 가장 큰 수를 저장하기 위한 변수
    for s in sum_all:                           # 마주보는 숫자를 곱한 값의 합의 리스트를 반복할 때
        if s > big:                             # 리스트의 요소가 big 보다 크면
            big = s                             # big을 그 요소로 바꿔준다

    print(f'#{t+1}', big)                       # 가장 큰수를 출력