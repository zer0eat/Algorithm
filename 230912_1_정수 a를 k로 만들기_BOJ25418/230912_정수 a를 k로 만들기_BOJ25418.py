# 정수 a를 k로 만들기_BOJ25418

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
A, K = map(int, input().split())        # A 시작 정수 / K 도착 정수를 input 받고
lst = deque([[K, 0]])                   # deque에 [도착정수, 연산 횟수]를 넣어 생성한다
while 1:                                # break가 나올 때까지 반복해서
    num, cnt = lst.popleft()            # 연산할 정수와 연산 횟수를 popleft하고
    if num == A:                        # 연산 후 A가 되었다면
        print(cnt)                      # 연산 횟수를 출력하고
        break                           # while문을 break한다
    if num % 2 == 0 and num >= A*2:     # 2로 나누어 떨어지고 도착 정수의 2배보다 큰 상황이라면
        lst.append([num//2, cnt+1])     # 연산할정수에서 2를 나누고 연산 횟수를 1 더한 후 리스트를 append한다
    else:                               # 2로 나눌 수 없는 상황에는
        lst.append([num-1, cnt+1])      # 연산할 정수에서 1을 빼고 연산 횟수를 1 더한 후 리스트를 append한다