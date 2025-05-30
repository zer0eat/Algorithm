# 근우의 다이어리 꾸미기_BOJ16676

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 숫자를 input받고
tmp = 10                # 비교할 수를 저장할 변수를 생성하고
ans = 1                 # 정답을 저장할 변수를 생성한다
while tmp < N:          # 숫자보다 비교할 수가 작으면 반복해서
    tmp = '1'+str(tmp)  # 맨앞에 1을 붙이고
    tmp = int(tmp)      # int로 변경하고
    ans += 1            # 정답의 수를 1 추가한다
print(ans)              # 필요한 숫자팩의 수를 출력한다