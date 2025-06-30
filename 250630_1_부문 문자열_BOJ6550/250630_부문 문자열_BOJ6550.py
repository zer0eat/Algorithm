# 부문 문자열_BOJ6550

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                        # break가 나올때까지 반복해서
    try:                        # input받을 내용이 있다면
        S, T = input().split()  # 두 문자를 input받고
        ans = 0                 # 위치를 저장할 변수를 생성한다
        for t in T:             # 긴 문자를 반복해서
            if ans == len(S):   # 짧은 문자를 모두 포함했다면
                break           # for문을 종료한다
            if t == S[ans]:     # 짧은 문자가 긴 문자에 포함되어 있다면
                ans += 1        # 위치를 한칸 이동하고
        if len(S) == ans:       # 짧은 문자열이 긴 문자열에 포함되어 있다면
            print('Yes')        # 예를 출력하고
        else:                   # 아니라면
            print('No')         # 아니오를 출력한다
    except:                     # input 받을 것이 없다면
        break                   # while문을 종료한다