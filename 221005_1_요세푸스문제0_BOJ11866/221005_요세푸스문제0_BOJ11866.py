# 요세푸스문제0_BOJ11866

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
N, K = map(int, sys.stdin.readline().split())       # N 사람의 수 / K 제거할 사람의 순서

people = [i for i in range(1, N+1)]                 # people 리스트에 N명의 사람을 순서대로 저장한다
people = deque(people)                              # people을 deque로 만듬

ans = []                                            # 정답을 저장할 빈 리스트 생성

while people:                                       # people 리스트가 빌때까지 반복해서
    for k in range(K):                              # K번을 반복해서
        a = people.popleft()                        # 맨 앞에서 사람을 뺀 후
        if k == K-1:                                # K번째면
            ans.append(a)                           # ans에 append
        else:                                       # 그렇지 않으면
            people.append(a)                        # people에 append

pp = '<'                                            # 출력 형식을 맞추기 위해 <를 저장한 변수 생성
for a in range(len(ans)):                           # ans를 반복해서
    if a == len(ans)-1:                             # 맨 뒤라면
        pp += str(ans[a])                           # 요소만 저장
    else:                                           # 맨 뒤가 아니라면
        pp += str(ans[a])                           # 요소를 저장하고
        pp += ', '                                  # 뒤에 ,와 띄어쓰기를 저장
else:                                               # 반복을 마쳤다면
    pp += '>'                                       # >를 저장
print(pp)