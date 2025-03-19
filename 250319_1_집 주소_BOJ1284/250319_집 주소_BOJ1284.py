# 집 주소_BOJ1284

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                # 0이 나올때까지 반복해서
    N = int(input())    # 숫자를 input 받고
    if N == 0:          # 숫자가 0이라면
        quit()          # 종료한다
    ans = 1             # 정답을 저장할 변수를 생성하고
    for n in str(N):    # 숫자를 반복해서
        if n == '1':    # 1이면
            ans += 3    # 3칸을 추가하고
        elif n == '0':  # 0이면
            ans += 5    # 5칸을 추가하고
        else:           # 나머지 숫자라면
            ans += 4    # 4칸을 추가하고
    print(ans)          # 차지한 칸을 출력한다