# 5와 6의 차이_BOJ2864

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 두 정수를 input 받고
mina, maxa = A+B, A+B               # 정답을 저장할 변수를 생성한다
A, B = str(A), str(B)               # 두 정수를 문자열로 저장하고
tmpA, tmpB = '', ''                 # 최소값을 저장할 변수를 생성하고
for a in range(len(A)):             # A를 반복해서
    if A[a] == '6':                 # a번째 숫자가 6이라면
        tmpA += '5'                 # tmpA에 5를 추가하고
    else:                           # a번째 숫자가 6이 아니라면
        tmpA += A[a]                # tmpA에 a번째 숫자를 더한다
for b in range(len(B)):             # B를 반복해서
    if B[b] == '6':                 # b번째 숫자가 6이라면
        tmpB += '5'                 # tmpB에 5를 추가하고
    else:                           # b번째 숫자가 6이 아니라면
        tmpB += B[b]                # tmpB에 b번째 숫자를 더한다
mina = int(tmpA) + int(tmpB)        # 최소값을 저장한다
tmpA, tmpB = '', ''                 # 최대값을 저장할 변수를 생성하고
for a in range(len(A)):             # A를 반복해서
    if A[a] == '5':                 # a번째 숫자가 5이라면
        tmpA += '6'                 # tmpA에 6을 추가하고
    else:                           # a번째 숫자가 5가 아니라면
        tmpA += A[a]                # tmpA에 a번째 숫자를 더한다
for b in range(len(B)):             # B를 반복해서
    if B[b] == '5':                 # b번째 숫자가 5이라면
        tmpB += '6'                 # tmpB에 6을 추가하고
    else:                           # b번째 숫자가 5가 아니라면
        tmpB += B[b]                # tmpB에 b번째 숫자를 더한다
maxa = int(tmpA) + int(tmpB)        # 최댓값을 저장한다
print(mina, maxa)                   # 두 수의 합 중 최솟값과 최댓값을 출력한다