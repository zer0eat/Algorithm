# 알파벳블록_BOJ27497

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                # 버튼을 누른 횟수를 input 받고
block = deque()                 # 버튼 누른 결과를 저장할 deque를 생성한다
flag = []                       # 마지막 버튼의 정보를 저장할 리스트를 생성하고
for n in range(N):              # 버튼을 누른 횟수를 반복해서
    a = list(input().split())   # 버튼 정보를 input 받고
    if a[0] == '1':             # 1번 버튼이라면
        flag.append(1)          # flag에 1번 버튼을 저장하고
        block.append(a[1])      # block의 맨 뒤에 문자를 추가한다
    elif a[0] == '2':           # 2번 버튼이라면
        flag.append(2)          # flag에 2번 버튼을 저장하고
        block.appendleft(a[1])  # block의 맨 앞에 문자를 추가한다
    else:                       # 3번 버튼이라면
        if block:               # block이 비어있지 않을 때
            if flag[-1] == 1:   # 맨 마지막에 누른 버튼이 1이라면
                block.pop()     # block의 맨뒤에서 문자를 지우고
                flag.pop()      # flag 기록을 지운다
            else:               # 맨 마지막에 누른 버튼이 2라면
                block.popleft() # block의 맨앞에서 문자를 지우고
                flag.pop()      # flag 기록을 지운다
if block:                       # 블록이 비어있지 않다면
    for b in block:             # block의 문자를 반복해서
        print(b, end='')        # 문자를 한줄로 출력한다
else:                           # 블록이 비어있다면
    print(0)                    # 0을 출력한다