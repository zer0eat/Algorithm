# 간단한369게임_1926

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                                        # 369 게임의 마지막 숫자를 input 받는다

ThreeSixNine = []                                       # 369 게임을 저장할 빈 리스트를 만들고
for n in range(1, N + 1):                               # 1부터 N까지 반복할 때
    n = str(n)                                          # n을 string으로 바꿔 준 후
    if '3' in n or '6' in n or '9' in n:                # 만약 n에 3, 6, 9가 있다면
        tmp = ''                                        # 박수를 담을 빈 변수에
        for m in n:                                     # 3, 6, 9가 있는 n을 하나씩 검사하여
            if m == '3' or m == '6' or m == '9':        # 3, 6, 9가 있을 때마다
                tmp += '-'                              # tmp에 박수를 - 형태로 하나씩 저장한다
        else:                                           # n의 모든 자리를 확인 했다면
            ThreeSixNine.append(tmp)                    # 박수의 숫자를 ThreeSixNine 리스트에 저장한다
    else:                                               # 3, 6, 9가 없는 숫자는
        ThreeSixNine.append(n)                          # 숫자 그대로 저장한다

print(*ThreeSixNine)