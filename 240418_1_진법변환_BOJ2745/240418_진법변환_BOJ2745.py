# 진법변환_BOJ2745

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, B = input().split()                              # N B진법의 수 / B 진법을 input 받고
ans = 0                                             # 정답을 저장할 변수를 생성한다
for n in range(len(N)):                             # N의 길이 만큼 반복해서
    if N[-1-n].isdigit():                           # n번째 자리의 수가 숫자라면
        ans += (int(N[-1-n])) * (int(B) ** n)       # 10진법으로 변환하여 더하고
    else:                                           # n번째 자리의 수가 영어라면
        ans += (int(B) ** n) * (ord(N[-1-n]) - 55)  # 10진법으로 변환하여 더한다
print(ans)                                          # B진법 수 N을 10진법으로 바꿔 출력한다