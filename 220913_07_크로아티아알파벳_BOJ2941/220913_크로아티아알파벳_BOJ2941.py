# 크로아티아알파벳_BOJ2941

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
num = input()                                       # 변형된 크로아티아 알파벳을 받음

ans = 0                                             # 알파벳의 개수를 셀 변수
n = 0                                               # 인덱스로 사용할 n
while n < len(num):                                 # 단어를 반복 할 때
    if num[n] == 'c':                               # c가 나오면
        if n + 1 < len(num):                        # 그 다음 글자가 단어 안일 때
            if num[n+1] == '=' or num[n+1] == '-':  # = 또는 - 이면
                ans += 1                            # 두개를 한 알파벳으로 세고
                n += 2                              # 다음으로 넘어간다
            else:                                   # 만약 다음 알파벳이 지정된 단어가 아니라면
                ans += 1                            # c만 1개의 알파벳으로 세고
                n += 1                              # 다음으로 넘어간다
        else:                                       # 만약 다음단어가 단어 범위 밖이라면
            ans += 1                                # c만 1개의 알파벳으로 세고
            n += 1                                  # 다음으로 넘어간다
    elif num[n] == 'd':                             # 위와 같은 방식으로 다음 단어들도 확인하여 단어의 개수를 센다
        if n + 1 < len(num):
            if num[n + 1] == 'z':
                if n + 2 < len(num):
                    if num[n+2] == '=':
                        ans += 1
                        n += 3
                    else:
                        ans += 1
                        n += 1
                else:
                    ans += 1
                    n += 1
            elif num[n + 1] == '-':
                ans += 1
                n += 2
            else:
                ans += 1
                n += 1
        else:
            ans += 1
            n += 1
    elif num[n] == 'l':
        if n + 1 < len(num):
            if num[n+1] == 'j':
                ans += 1
                n += 2
            else:
                ans += 1
                n += 1
        else:
            ans += 1
            n += 1
    elif num[n] == 'n':
        if n + 1 < len(num):
            if num[n + 1] == 'j':
                ans += 1
                n += 2
            else:
                ans += 1
                n += 1
        else:
            ans += 1
            n += 1
    elif num[n] == 's':
        if n + 1 < len(num):
            if num[n + 1] == '=':
                ans += 1
                n += 2
            else:
                ans += 1
                n += 1
        else:
            ans += 1
            n += 1
    elif num[n] == 'z':
        if n + 1 < len(num):
            if num[n + 1] == '=':
                ans += 1
                n += 2
            else:
                ans += 1
                n += 1
        else:
            ans += 1
            n += 1
    else:
        ans += 1
        n += 1
print(ans)