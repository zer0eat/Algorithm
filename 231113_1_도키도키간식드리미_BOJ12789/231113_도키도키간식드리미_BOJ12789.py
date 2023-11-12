# 도키도키간식드리미_BOJ12789
# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                                # 학생의 수를 input 받고
student = deque(map(int, input().split()))      # 줄선 학생의 번호를 덱으로 input 받는다
ready = []                                      # 대기열을 리스트로 생성하고
cnt = 1                                         # 순번을 확인할 변수를 생성한다
while cnt < N:                                  # cnt가 학생의 수와 같아질 때까지 반복해서
    if len(ready):                              # 대기열에 사람이 있다면
        if ready[-1] == cnt:                    # 대기열의 맨 마지막 사람이 현재 순번이라면
            ready.pop()                         # 대기열에서 빼내 간식을 준 후
            cnt += 1                            # 순번을 1 추가하고
            continue                            # continue로 다음 while문으로 들어간다
    if len(student):                            # 대기열에 현재 순번이 없고 줄선 학생이 남아 있다면
        A = student.popleft()                   # 맨 앞에 서있는 학생을 pop해서
        if A == cnt:                            # 맨 앞에 있는 학생이 현재 순번이라면
            cnt += 1                            # 순번을 1 추가한다
        else:                                   # 맨 앞에 있는 학생이 현재 순번이 아니라면
            if len(ready) and ready[-1] < A:    # 대기열의 맨 마지막 사람보다 A가 큰 경우 간식배부가 불가능 하므로
                print('Sad')                    # Sad를 출력하고
                quit()                          # 종료한다
            else:                               # 대기열이 비어있거나 대기열의 맨 마지막 사람보다 A가 더 작은 경우
                ready.append(A)                 # A를 대기열 맨 뒷줄에 append한다
print('Nice')                                   # 모두 간식을 받을 수 있다면 Nice를 출력한다