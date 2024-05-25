# 윷놀이_BOJ2490

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
for n in range(3):                              # 윷을 세번 던져서
    yoot = sum(list(map(int, input().split()))) # 윷의 등의 개수를 센 후
    if yoot == 0:                               # 윷의 등이 0개라면
        print('D')                              # D(윷)를 출력한다
    elif yoot == 1:                             # 윷의 등이 1개라면
        print('C')                              # C(걸)를 출력한다
    elif yoot == 2:                             # 윷의 등이 2개라면
        print('B')                              # B(개)를 출력한다
    elif yoot == 3:                             # 윷의 등이 3개라면
        print('A')                              # A(도)를 출력한다
    elif yoot == 4:                             # 윷의 등이 4개라면
        print('E')                              # E(모)를 출력한다