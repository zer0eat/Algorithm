# 치킨댄스를 추는 곰곰이를 본 임스 2_BOJ26068

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 기프티콘의 수를 input 받고
ans = 0                         # 사용할 기프티콘의 수를 저장할 변수를 생성한다
for n in range(N):              # 기프티콘의 수를 반복해서
    a, day = input().split('-') # 남은 기간을 input 받고
    if int(day) <= 90:          # 남은 기간이 90일 이하라면
        ans += 1                # 사용할 기프티콘을 1 추가하고
print(ans)                      # 사용한 기프티콘의 수를 출력한다