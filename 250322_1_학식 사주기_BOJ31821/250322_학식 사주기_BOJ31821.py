# 학식 사주기_BOJ31821

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 메뉴의 수를 input 받고
menu = []                       # 메뉴를 저장할 리스트를 생성하고
for n in range(N):              # 메뉴의 수를 반복해서
    menu.append(int(input()))   # 메뉴의 가격을 append한다
M = int(input())                # 학생의 수를 input 받고
ans = 0                         # 정답을 저장할 변수를 생성해서
for m in range(M):              # 학생의 수를 반복해서
    ans += menu[int(input())-1] # 학식의 가격을 추가하고
print(ans)                      # 정답을 출력한다