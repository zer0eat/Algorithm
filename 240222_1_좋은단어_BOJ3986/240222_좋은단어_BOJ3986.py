# 좋은단어_BOJ3986

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 단어의 수를 input 받고
ans = 0                         # 정답을 저장할 변수를 생성하고
for n in range(N):              # 단어의 수를 반복해서
    stack = []                  # 스택을 생성하고
    S = input().strip()         # 문자열을 input 받은 후
    for s in S:                 # 문자를 반복한다
        if stack == []:         # 스택이 비어있다면
            stack.append(s)     # 문자를 append하고
        elif stack[-1] == s:    # 스택의 맨 마지막과 현재 문자가 같다면
            stack.pop()         # 마지막 문자를 pop하고
        else:                   # 스택의 맨 마지막과 현재 문자가 다르다면
            stack.append(s)     # 문자를 append한다
    if stack == []:             # 문자열을 모두 탐색한 후 스택이 비어있다면
        ans += 1                # 그 단어는 좋은 단어로 정답을 1 추가한다
print(ans)                      # 좋은 단어의 수를 출력한다