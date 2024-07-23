# 특식 배부_BOJ27110

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 치킨의 수를 input 받고
chicken = list(map(int, input().split()))   # 치킨별 좋아하는 사람의 수를 input 받고
ans = 0                                     # 정답을 저장할 변수를 생성해서
for c in chicken:                           # 선호하는 치킨을 반복해서
    if c < N:                               # 치킨 수보다 선호하는 사람이 적다면
        ans += c                            # 선호하는 사람만큼 정답에 더하고
    else:                                   # 치킨 수보다 선호하는 사람이 많다면
        ans += N                            # 치킨 수만큼 정답에 더해서
print(ans)                                  # 좋아하는 치킨을 받을 수 있는 사람의 수를 출력한다