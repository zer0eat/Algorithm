# Inspiration_BOJ16715

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def calculation(N, i):
    ans = 0                     # 정답을 저장할 변수를 생성하고
    while N > 0:                # N이 0이 될때까지 반복해서
        ans += N % i            # 정답에 N을 i로 나눈 나머지를 더하고
        N //= i                 # N을 i로 나눈 몫만 저장한다
    return ans                  # N을 i진법으로 바꿨을 때 숫자의 합을 리턴한다

def find(N):
    max_sum = 0                 # 숫자의 합을 저장할 변수를 생성하고
    best_base = 2               # 진법을 저장할 변수를 생성한다
    for i in range(2, N+1):     # 2부터 N까지 반복해서
        tmp = calculation(N, i) # N을 i진법으로 바꿨을 때 숫자의 합을 저장하고
        if tmp > max_sum:       # 숫자의 합이 최대라면
            max_sum = tmp       # 최대값을 저장하고
            best_base = i       # 그때 진법의 수를 저장한다
    return max_sum, best_base   # 자릿수 합의 최대값과 진법 수를 리턴한다

N = int(input())                # 최대 진법을 input 받고
max_sum, best_base = find(N)    # 각 자리의 합이 최대가 되는 수를 구해서
print(max_sum, best_base)       # 자릿수 합의 최댓값 / 진법 수를 출력한다