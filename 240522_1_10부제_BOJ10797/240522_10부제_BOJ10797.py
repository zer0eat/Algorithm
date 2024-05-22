# 10부제_BOJ10797

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
day = int(input())                          # 날짜의 일의 자리 숫자를 input 받고
ans = 0                                     # 정답을 저장할 변수를 생성한 후
for n in list(map(int, input().split())):   # 5대의 차량을 리스트로 input 받아 반복해서
    if n == day:                            # 날짜와 차량번호가 같다면
        ans += 1                            # 정답에 1을 추가한다
print(ans)                                  # 주어진 날짜와 자동차의 일의 자리 숫자를 보고 10부제를 위반하는 차량의 대수를 출력한다