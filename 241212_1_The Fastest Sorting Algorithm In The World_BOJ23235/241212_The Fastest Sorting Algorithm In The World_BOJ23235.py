# The Fastest Sorting Algorithm In The World_BOJ23235

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
cnt = 1                                     # 케이스를 셀 변 수를 생성하고
while 1:                                    # break가 나올 때까지 반복해서
    a = input()                             # 숫자를 input 받고
    if a == '0':                            # 0이 나오면
        break                               # while문을 break한다
    print(f'Case {cnt}: Sorting... done!')  # 케이스와 문장을 출력하고
    cnt += 1                                # 케이스를 1 더해준다