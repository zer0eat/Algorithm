# 1로만들기_BOJ1463

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())       # 구하고자 하는 숫자를 input 받고

ans = [0,0,1,1]                     # 0부터 3까지 걸리는 횟수를 저장한 리스트를 생성하고

for i in range(4, N+1):             # 4부터 N까지 반복해서
    c = ans[i - 1] + 1              # c = i보다 1 작은 수가 걸리는 횟수 + 1을 뺀 횟수(1)
    if i % 3 == 0:                  # i를 3으로 나눠 떨어진다면
        a = ans[i//3] + 1           # a = i을 3으로 나눈 수가 걸리는 횟수 + 3으로 나눈 횟수(1)
        if a < c:                   # a보다 c가 크다면
            c = a                   # c를 a로 바꿔준다
    if i % 2 == 0:                  # i를 2로 나눠 떨어진다면
        b = ans[i//2] + 1           # b = i을 2로 나눈 수가 걸리는 횟수 + 2로 나눈 횟수(1)
        if c > b:                   # b보다 c가 크다면
            c = b                   # c를 b로 바꿔준다
    ans.append(c)                   # c를 append해 i번째 인덱스에 i의 횟수가 저장되도록 한다

print(ans[N])                       # N의 횟수를 출력한다
