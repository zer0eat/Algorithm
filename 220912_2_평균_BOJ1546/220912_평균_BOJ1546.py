# 평균_BOJ1546

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                        # 성적표의 성적의 수
arr = list(map(int, input().split()))   # 성적표를 리스트로 받음

M = max(arr)                            # 가장 높은 성적을 M으로 저장
ans = 0                                 # 조작 후 평균 성적을 저장할 변수

for t in range(T):                      # 성적표의 모든 성적을 반복하며
    ans += (arr[t]/M*100)               # 각 과목의 성적을 최고성적으로 나눈 후 100을 곱한 숫자로 조작

print(ans/T)

