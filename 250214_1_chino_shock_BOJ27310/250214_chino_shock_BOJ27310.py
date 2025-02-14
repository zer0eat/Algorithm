# chino_shock_BOJ27310

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
emoji = list(input().strip())   # 이모지를 input 받고
u, c = 0, 0                     # 개수를 셀 변수를 생성하고
for e in emoji:                 # 이모지를 반복해서
    if e == ':':                # 콜론이 나오면
        c += 1                  # 콜론의 수를 더하고
    elif e == '_':              # 언더바가 나오면
        u += 1                  # 언더바의 수를 더하고
print(len(emoji)+c+(u*5))       # 이모지 난이도를 출력한다