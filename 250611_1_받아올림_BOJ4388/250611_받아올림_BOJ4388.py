# 받아올림_BOJ4388

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                                        # break가 나올때까지 반복해서
    ans = 0                                     # 정답을 저장할 변수를 생성하고
    a, b = input().split()                      # 두 수를 input받고
    if a == '0' and b == '0':                   # 두 수가 모두 0이라면
        break                                   # while문을 종료한다
    tmp = 0                                     # 올림을 저장할 변수를 생성하고
    a = (10-len(a))*'0' + a                     # a를 열자리로 만들고
    b = (10-len(b))*'0' + b                     # b를 열자리로 만들고
    for n in range(1, 11):                      # 1부터 10까지 반복해서
        if int(a[-n]) + int(b[-n]) + tmp > 9:   # 각 자리수의 합이 올림이 된다면
            ans += 1                            # 정답에 1을 추가하고
            tmp = 1                             # 올림을 표시한다
        else:                                   # 각 자리수의 합이 올림이 안된다면
            tmp = 0                             # 올림을 표시하지 않는다
    print(ans)                                  # 정답을 출력한다