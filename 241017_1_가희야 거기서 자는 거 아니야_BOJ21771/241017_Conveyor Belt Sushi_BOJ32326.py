# Conveyor Belt Sushi_BOJ32326.py

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                     # 총 가격을 저장할 변수를 생성하고
for n in range(3, 6):       # 접시의 가격을 반복해서
    ans += int(input())*n   # 접시별 먹은 가격을 더해준다
print(ans)                  # 총 가격을 출력한다