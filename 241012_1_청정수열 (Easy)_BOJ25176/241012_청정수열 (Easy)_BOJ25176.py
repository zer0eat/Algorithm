# 청정수열 (Easy)_BOJ25176

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 정수를 input 받고
ans = 1                 # 정답을 저장할 변수를 생성한다
for n in range(1, N+1): # 1부터 N까지 반복해서
    ans *= n            # N개로 만들 수 있는 순열을 계산해서
print(ans)              # 청정수열(같은 수가 붙어있는 수열)의 개수를 출력한다