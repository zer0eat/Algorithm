# 거스름돈_BOJ5585

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
money = 1000-int(input())       # 1000원을 내고 남은 돈을 저장하고
ans = 0                         # 정답을 저장할 변수를 생성한다
lst = [500, 100, 50, 10, 5, 1]  # 거스름돈의 종류를 리스트로 생성하고
for m in lst:                   # 거스름돈의 종류를 반복해서
    ans += money//m             # m원으로 줄 수 있는 거스름돈의 개수를 ans에 더하고
    money = money%m             # 주고 남은 돈을 money에 저장한다
print(ans)                      # 잔돈에 포함된 매수를 출력한다