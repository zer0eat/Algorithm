# 선로에 마네킹이야_BOJ15920

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 문자열의 길이를 input 받고
S = input().strip()             # 문자열을 반복해서
step = 0                        # 기차의 위치를 저장할 변수를 생성하고
lever = True                    # 레버의 위치를 저장할 변수를 생성하고
multi = 0                       # 멀티 드래프팅을 저장할 변수를 생성한다
for n in range(N):              # 문자열의 길이를 반복해서
    if S[n] == 'P':             # 레버를 당기는 행위가 나오면
        if step == 1:           # B단계인 경우
            multi = 1           # 멀티 드래프팅 표시를 하고
        if step == 0:           # A단계인 경우
            lever = not lever   # 레버의 위치를 변경한다
    else:                       # 기다리는 행위가 나오면
        step += 1               # 단계를 더해준다
if step >= 2:                   # C단계까지 간경우
    if multi:                   # 멀티 드래프팅이 일어났으면
        print(6)                # 6을 출력하고
    else:                       # 멀티 드래프팅이 일어나지 않았으면
        if lever:               # 레버의 위치가 처음과 같다면
            print(5)            # 5를 출력하고
        else:                   # 레버의 위치가 처음과 다르다면
            print(1)            # 1을 출력하고
else:                           # C단계까지 가지 않았다면
    print(0)                    # 0을 출력한다