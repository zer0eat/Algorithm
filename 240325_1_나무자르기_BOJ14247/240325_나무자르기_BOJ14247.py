# 나무자르기_BOJ14247

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 나무의 개수를 input 받고
woods = list(map(int, input().split()))     # 초기의 나무를 리스트로 input 받고
growth = list(map(int, input().split()))    # 나무의 성장치를 리스트로 input 받는다
ans = sum(woods)                            # 초기 나무의 길이의 합을 저장한 변수를 생성하고
growth.sort()                               # 성장치를 오름차순으로 정렬한다
for i in range(N):                          # 나무의 성장치를 반복해서
    ans += growth[i]*i                      # i번째 성장치가 i일 동안 성장한 만큼 나무의 양에 더해준다
print(ans)                                  # 나무를 잘라서 구할 수 있는 최대 양을 출력한다