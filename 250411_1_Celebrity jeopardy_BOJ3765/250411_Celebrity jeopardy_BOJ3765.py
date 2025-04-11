# Celebrity jeopardy_BOJ3765

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                    # break가 나올 때까지 반복해서
    try:                    # input이 있다면
        s = input().strip() # 방정식을 input 받고
    except:                 # input이 없다면
        break               # while문을 break한다
    print(s)                # 방정식을 출력한다