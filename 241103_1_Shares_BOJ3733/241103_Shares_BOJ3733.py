# Shares_BOJ3733

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                    # break가 나올 때까지 반복해서
    try:                                    # input이 있다면
        N, S = map(int, input().split())    # 그룹 인원과 주식의 수를 input 받고
        print(S // (N + 1))                 # 주식을 나눠 받을 수 있는 숫자를 출력한다
    except:                                 # 더이상 input이 없다면
        break    		                    # while문을 종료한다