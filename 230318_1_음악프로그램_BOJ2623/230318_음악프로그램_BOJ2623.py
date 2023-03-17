# 음악프로그램_BOJ2623

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N, M = map(int, input().split())                    # N 가수의 수 / M 보조 PD의 수

line = dict()                                       # 가수의 순서를 저장할 딕셔너리 생성
for _ in range(M):                                  # 보조PD의 수를 반복해서
    singer = list(map(int, input().split()))        # 보조PD가 담당한 가수의 수와 순서를 list로 input 받고
    for a in range(1, singer[0]):                   # 보조PD가 담당한 가수를 반복해서
        if line.get(singer[a]) == None:             # a번째 가수의 순서가 미정이라면
            line[singer[a]] = [singer[a+1]]         # a를 key로 a+1을 value로 딕셔너리를 생성하고
        else:                                       # a번째 가수의 순서가 정해져 있다면
            line[singer[a]].append(singer[a+1])     # a 뒤에 나올 가수로 a+1번째 가수를 append한다

def dfs(x):
    visited[x] = 1                                  # x 가수를 줄을 섰다고 표시해 준 후
    stack.append(x)                                 # 순서를 임시 저장할 stack에 append
    if line.get(x) == None:                         # x 가수 뒤에 올 가수가 없다면
        ans.appendleft(stack.pop())                 # ans의 맨 앞에 append 하고
        return                                      # return
    else:                                           # x 가수 뒤에 올 가수가 있다면
        for j in line[x]:                           # x 뒤에 오는 가수를 반복해서
            if j in stack:                          # 뒤에 올 가수가 stack에 이미 있다면 cycle이 생겨 줄을 세울 수 없으므로
                print(0)                            # 0을 출력하고
                quit()                              # 종료힌다
            if visited[j] == 0:                     # 뒤에 올 가수가 줄을 서지 않았다면
                dfs(j)                              # dfs를 통해 순서를 정하고
    ans.appendleft(stack.pop())                     # x 뒤에 올 가수의 순서가 모두 정해졌다면 stack에서 x를 꺼내 ans의 맨 앞에 넣는다

ans = deque()                                       # 정답을 저장할 deque 생성
stack = []                                          # 순서를 임시로 저장할 stack 생성
visited = [0]*(N+1)                                 # 순서를 정했는지 여부를 체크할 리스트 생성

for i in range(N):                                  # 가수의 수만큼 반복해서
    if visited[i+1] == 0:                           # 해당 가수가 아직 순서가 정해지지 않았다면
        dfs(i+1)                                    # dfs를 통해 순서를 정하고

for a in ans:                                       # 순서가 모두 정해졌다면 순서를 반복해서
    print(a)                                        # 출연가수를 하나씩 출력한다