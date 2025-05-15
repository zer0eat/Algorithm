# 줄 세기_BOJ4806

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
ans = 0                     # 정답을 저장할 변수를 생성하고
while 1:                    # break가 나올때까지 반복해서
    try:                    # input이 있다면
        w = input().strip() # 한줄을 input받고
        ans += 1            # 줄의 수를 추가한다
    except:                 # input이 없다면
        print(ans)          # 전체 줄을 출력하고
        break               # while문을 종료한다