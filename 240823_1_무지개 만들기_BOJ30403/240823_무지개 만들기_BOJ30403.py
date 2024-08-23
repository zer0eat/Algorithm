# 무지개 만들기_BOJ30403

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 글자수를 input 받고
W = list(input().strip())                       # 글자를 리스트로 input 받는다
ans1 = [0]*7                                    # 소문자 무지개를 저장할 리스트를 생성하고
ans2 = [0]*7                                    # 대문자 무지개를 저장할 리스트를 생성한다
small = ['r', 'o', 'y', 'g', 'b', 'i', 'v']     # 소문자 무지개를 리스트에 저장하고
big = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']       # 대문자 무지개를 리스트에 저장한다
for n in range(N):                              # 글자의 수를 반복해서
    for m in range(7):                          # 무지개의 길이를 반복한 후
        if W[n] == small[m]:                    # 글자가 소문자 m번째 글자라면
            ans1[m] = 1                         # 소문자 무지개 리스트에 체크표시하고
            break                               # for문을 break한다
        elif W[n] == big[m]:                    # 글자가 대문자 m번째 글자라면
            ans2[m] = 1                         # 대문자 무지개 리스트에 체크표시하고
            break                               # for문을 break한다
if sum(ans1) == 7 and sum(ans2) == 7:           # 소문자 무지개와 대문자 무지개를 모두 만들 수 있다면
    print('YeS')                                # YeS를 출력한다
elif sum(ans1) == 7:                            # 소문자 무지개를 만들 수 있다면
    print('yes')                                # yes를 출력한다
elif sum(ans2) == 7:                            # 대문자 무지개를 만들 수 있다면
    print('YES')                                # YES를 출력한다
else:                                           # 무지개를 만들 수 없다면
    print('NO!')                                # NO!를 출력한다