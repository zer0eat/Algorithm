# 신용카드 판별_BOJ14726

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트 케이스를 반복해서
    credit = list(input().strip())          # 신용카드 번호를 input 받고
    for n in range(0, 16, 2):               # 홀수번째 수만 반복해서
        tmp = int(credit[n])                # 해당 숫자를 저장한 후
        tmp *= 2                            # 숫자를 두배로 하고
        if tmp > 9:                         # 두자리수 수라면
            tmp = list(str(tmp))            # 리스트로 변환해서
            tmp = int(tmp[0]) + int(tmp[1]) # 십의자리와 일의자리를 더해준 후
        credit[n] = tmp                     # 해당 자리에 저장한다
    ans = 0                                 # 정답을 저장할 변수를 생성해서
    for c in credit:                        # 신용카드 번호를 반복해서
        ans += int(c)                       # 더해준 후
    if ans % 10:                            # 신용카드 번호의 합이 10으로 나눠떨어지지 않는다면
        print('F')                          # F를 출력하고
    else:                                   # 신용카드 번호의 합이 10으로 나눠떨어진다면
        print('T')                          # T를 출력한다