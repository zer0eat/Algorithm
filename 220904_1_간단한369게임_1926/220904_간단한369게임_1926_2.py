# 간단한369게임_1926

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                                        # 369 게임의 마지막 숫자를 input 받는다

ThreeSixNine = []                                       # 369 게임을 저장할 빈 리스트를 만들고
for n in range(1, N + 1):                               # 1부터 N까지 반복할 때
    tmp = ''                                            # 박수를 담을 빈 변수를 생성하고
    m = n                                               # n을 m에 저장한 후
    while m > 0:                                        # m이 0이 될때까지 반복한다
        if m % 10 == 3 or m % 10 == 6 or m % 10 == 9:   # 만약 1의 자리수가 3, 6, 9라면
            tmp += '-'                                  # tmp에 박수를 저장하고
            m = m // 10                                 # m을 10으로 나눈 몫만 m에 저장한다
        else:                                           # 만약 1의 자리수가 3, 6, 9가 아니라면
            m = m // 10                                 # m을 10으로 나눈 몫만 m에 저장한다
    else:                                               # m이 0이 될때까지 반복한 후
        if tmp == '':                                   # tmp가 비어있다면
            ThreeSixNine.append(n)                      # n을 ThreeSixNine 리스트에 저장한다
        else:                                           # tmp가 비어있지 않다면
            ThreeSixNine.append(tmp)                    # 박수의 숫자를 ThreeSixNine 리스트에 저장한다

print(*ThreeSixNine)