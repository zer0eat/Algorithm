# (중략)_BOJ21966

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 문장의 수를 input 받고
if N < 26:                          # 문장가 25개 이하라면
    print(input().strip())          # 문장를 그대로 출력한다
else:                               # 문장가 26이상이라면
    word = list(input())            # 문장를 리스트로 input 받고
    tmp = 0                         # 중략 안에 포함된 문장를 세기 위한 변수를 생성하고
    for n in range(11, N-12):       # 중략할 부분을 반복해서
        if word[n] == '.':          # 중략 부분에 두 문장이 포함된다면
            tmp = 1                 # 중략표시를 하고 
            break                   # for문을 종료한다
    if tmp == False:                # 한문장이 중략 된다면
        ans = ''                    # 정답을 저장할 변수를 생성하고
        for n in range(11):         # 앞부분 11글자를 반복해서
            ans += word[n]          # 정답에 저장하고
        ans += '...'                # 중략될 ...을 저장하고
        for n in range(N-11, N):    # 뒷부분 11글자를 반복해서
            ans += word[n]          # 정답에 저장하고
        print(ans)                  # 문장을 출력한다
    else:                           # 두문장이 중략 된다면
        ans = ''                    # 정답을 저장할 변수를 생성하고
        for n in range(9):          # 앞부분 9글자를 반복해서
            ans += word[n]          # 정답에 저장하고
        ans += '......'             # 중략될 ......을 저장하고
        for n in range(N-10, N):    # 뒷부분 10글자를 반복해서
            ans += word[n]          # 정답에 저장하고
        print(ans)                  # 문장을 출력한다