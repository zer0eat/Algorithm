# 거스름돈_BOJ14916

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 거스름돈의 액수를 input 받고
A = N//5                    # A에 5원짜리로 줄 수 있는 최대 금액을 저장한다
for i in range(A, -1, -1):  # A부터 0까지 반복해서
    ans = 0                 # 거스름돈의 개수를 저장할 변수를 생성하고
    change = N              # 거스름돈의 액수를 change에 저장한다
    change -= 5*i           # 5원짜리 i개로 거스름돈을 준만큼 change에서 금액을 빼주고
    ans += i                # ans에 5원짜리 거스름돈의 수를 더해준다
    if change % 2 == 0:     # 남은 돈을 2원짜리로 줄 수 있다면
        ans += change//2    # 2원짜리 거스름돈의 개수를 ans에 더한 후
        print(ans)          # 거스름돈의 개수를 출력하고
        quit()              # 종료한다
else:                       # 거스름돈을 줄 수 없는 경우에는
    print(-1)               # -1을 출력한다다