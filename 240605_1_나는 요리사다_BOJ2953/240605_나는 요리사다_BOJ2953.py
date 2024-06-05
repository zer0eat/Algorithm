# 나는 요리사다_BOJ2953

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = [0, 0]                                # 정답을 저장할 리스트를 생성하고
for n in range(1, 6):                       # 1번부터 5번 참가자를 반복해서
    num = sum(map(int, input().split()))    # 참가자의 점수를 input 받아 모두 더한 후
    if num > ans[1]:                        # 참가자의 점수가 역대 최고점이라면
        ans[0] = n                          # 참가자의 번호를 저장하고
        ans[1] = num                        # 참가자의 점수를 저장한다
print(*ans)                                 # 최고점을 받은 참가자의 번호와 점수를 출력한다