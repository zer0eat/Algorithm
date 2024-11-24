# Call for Problems_BOJ32498

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 문제의 수를 input 받고
ans = 0                 # 정답을 저장할 변수를 생성한다
for n in range(N):      # 문제의 수를 반복해서
    d = int(input())    # 문제를 input 받고
    if d%2:             # 문제가 홀수라면
        ans += 1        # 제외할 문제를 더해주고
print(ans)              # 제외할 문제의 수를 출력한다