# 소수의 자격_BOJ6219

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, D = map(int, input().split())     # A 범위의 시작 / B 범위의 끝 / D 포함하는 숫자
prime = [0] * (B + 1)                   # 소수를 체크할 리스트를 생성하고
for i in range(2, B+1):                 # 2부터 범위의 끝까지 반복해서
    if prime[i] == 0:                   # 아직 소수판정이 안 된수가 나오면
        prime[i] = 1                    # 소수로 표시하고
        for j in range(i+i, B+1, i):    # i의 배수를 반복해서
            prime[j] = 2                # 배수는 모두 소수가 아니라고 표시한다
ans = 0                                 # 정답을 저장할 변수를 생성하고
for a in range(A, B+1):                 # 범위의 시작과 끝을 반복해서
    if prime[a] == 1:                   # 해당 숫자가 소수라면
        if str(D) in str(a):            # D가 소수에 포함된다면
            ans += 1                    # 정답의 개수를 1 추가하고
print(ans)                              # 정답의 개수를 출력한다