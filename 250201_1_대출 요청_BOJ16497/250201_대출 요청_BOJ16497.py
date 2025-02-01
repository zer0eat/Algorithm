# 대출 요청_BOJ16497

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 대출자를 input 받고
book = [0]*101                      # 대출일자를 저장할 리스트를 생성한다
for n in range(N):                  # 대출자를 반복해서
    s,e = map(int, input().split()) # 대출 시작일과 끝일을 input 받고
    for b in range(s,e):            # 시작부터 끝까지 반복해서
        book[b] += 1                # 대출한 책의 수를 1 더한다
ans = int(input())                  # 책의 최대수를 input 받고
if max(book) <= ans:                # 책이 제일 많이 나간날보다 책이 많다면
    print(1)                        # 1을 출력하고
else:                               # 책이 부족하다면
    print(0)                        # 0을 출력한다