# 문자 인식_BOJ3448

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 테스트 케이스를 input 받고
for n in range(N):                                  # 테스트 케이스를 반복해서
    word = ''                                       # input 받을 단어를 저장할 변수를 생성하고
    while 1:                                        # break가 나올 때까지 반복해서
        tmp = input().strip()                       # 단어를 input 받고
        if tmp != '':                               # 빈칸이 아니라면
            word += tmp                             # word에 추가하고
        else:                                       # 빈칸이라면
            break                                   # while문을 종료한다
    t, f = 0, 0                                     # 아는 문자와 모르는 문자를 저장할 변수를 생성하고
    for w in word:                                  # 단어를 반복해서
        if w == '#':                                # 모르는 문자면
            f += 1                                  # f를 추가하고
        else:                                       # 아는 문자면
            t += 1                                  # t를 추가한다
    ans = round(t/(t+f)*100, 1)                     # 아는 문자의 퍼센트를 구하고
    if ans.is_integer():                            # 소수점 이하가 없다면
        print(f'Efficiency ratio is {int(ans)}%.')  # 소수점 이하 없이 정답을 출력하고
    else:                                           # 소수점 이하가 있다면
        print(f'Efficiency ratio is {ans}%.')       # 소수점 이하 1자리까지 출력한다
