# 거꾸로 구구단_BOJ13410

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())    # 구구단의 단과 개수를 input받고
ans = []                            # 거꾸로 구구단을 저장할 리스트를 생성하고
for n in range(1, K+1):             # 구구단의 개수를 반복해서
    tmp = str(n*N)                  # 구구단을 계산하고
    ans.append(int(tmp[::-1]))      # 숫자를 반대로 뒤집어서 리스트에 append한다
print(max(ans))                     # 가장 큰 수를 출력한다