# JOI와IOI_BOJ5586

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = list(input().strip())                   # 문자를 리스트로 input받고
J, I = 0, 0                                 # 문자열의 수를 저장할 변수를 생성한다
for a in range(len(A)-2):                   # 문자 리스트를 반복해서
    if A[a] == 'J':                         # 시작이 J라면
        if A[a:a+3] == ['J', 'O', 'I']:     # 해당문자부터 JOI가 나오면
            J += 1                          # 변수에 1을 추가하고
    elif A[a] == 'I':                       # 시작이 I라면
        if A[a:a+3] == ['I', 'O', 'I']:     # 해당문자부터 IOI가 나오면
            I += 1                          # 변수에 1을 추가한다
print(J)                                    # JOI의 수를 출력하고
print(I)                                    # IOI의 수를 출력한다