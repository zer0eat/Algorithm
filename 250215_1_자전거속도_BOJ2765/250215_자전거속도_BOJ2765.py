# 자전거속도_BOJ2765

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = 1                                                   # 순서를 저장할 변수를 생성하고
while 1:                                                # quit이 나올때까지 반복해서
    try:                                                # input을 받을 수 있으면
        r, p, m = map(float, input().split())           # 지름, 회전수, 시간을 input 받고
        pi = 3.1415927                                  # 파이를 저장한 후
        if p == 0:                                      # 회전수가 0 이면
            pass                                        # 넘어가고
        else:                                           # 회전수가 0이 아니면
            dis = (r/12/5280)* pi * p                   # 거리를 구하고
            mph = dis/(m/3600)                          # 시간당 거리를 구해서
            print(f'Trip #{N}: {dis:.2f} {mph:.2f}')    # 거리와 시간당 거리를 출력하고
            N += 1                                      # 순서를 1 더해준다
    except:                                             # input을 받을 수 없다면
        quit()                                          # 종료한다