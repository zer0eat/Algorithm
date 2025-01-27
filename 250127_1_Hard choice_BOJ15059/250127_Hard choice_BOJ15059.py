# Hard choice_BOJ15059 

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
menu = list(map(int, input().split()))      # 메뉴의 준비 수를 input 받고
people = list(map(int, input().split()))    # 메뉴의 요청 수를 input 받고
ans = 0                                     # 정답을 저장할 변수를 생성한다
for n in range(3):                          # 메뉴를 반복해서
    if people[n] - menu[n] > 0:             # 준비된 메뉴보다 요청 수가 많다면
        ans += people[n] - menu[n]          # 먹지못하는 사람을 정답에 저장하고
print(ans)                                  # 먹지 못하는 사람의 수를 출력한다