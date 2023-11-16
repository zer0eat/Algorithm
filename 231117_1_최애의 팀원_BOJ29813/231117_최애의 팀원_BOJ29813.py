# 최애의 팀원_BOJ29813

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                    # 학생의 수를 input 받고
student = deque([])                 # 학생을 저장할 deque를 생성한다
for i in range(N):                  # 학생의 수를 반복해서
    a, b = input().strip().split()  # 학생의 이름과 패스할 횟수를 input 받고
    student.append([a, int(b)])     # student에 이름과 횟수를 append한다
for i in range(N//2):               # 팀이 만들어지는 횟수만큼 반복해서
    first = student.popleft()       # 첫번째 사람을 first에 저장하고
    for i in range(first[1]-1):     # first가 패스할 수보다 1명 적게 반복해서
        a = student.popleft()       # 맨 앞에 있는 사람을 빼서
        student.append(a)           # 맨 뒤로 보낸 후
    else:                           # 모두 반복했다면
        student.popleft()           # X번째 사람과 팀을 이루고 빠진다
print(student[0][0])                # 팀을 짜고 남은 팀원의 이름을 출력한다
