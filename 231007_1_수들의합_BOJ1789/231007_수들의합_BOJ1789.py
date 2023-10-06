# 수들의합_BOJ1789

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = int(input())                # 서로 다른 자연수의 합을 input받고
cnt = 0                         # 서로 다른 자연수의 개수를 저장할 변수를 생성한 후
while 1:                        # break가 나올 때까지 반복해서
    cnt += 1                    # 자연수의 개수를 1더하고
    if cnt*(cnt+1)/2 > S:       # cnt개의 자연수의 합보다 S가 작을 때
        print(cnt-1)            # cnt-1개를 출력하고
        break                   # while문을 break한다