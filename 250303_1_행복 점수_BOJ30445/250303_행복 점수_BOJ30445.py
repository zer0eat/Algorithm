# 행복 점수_BOJ30445

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from decimal import Decimal, ROUND_HALF_UP

# input 받기
H, S = 0, 0                             # 행복, 슬픔지수를 저장할 변수를 생성하고
N = list(input().strip())               # 문자를 input 받아서
HG = {'H', 'A', 'P', 'Y'}               # 행복 지수를 비교할 그룹을 생성하고
SG = {'S', 'A', 'D'}                    # 슬픔 지수를 비교할 그룹을 생성하다
for n in N:                             # 문자를 반복해서
    if n in HG:                         # 행복 그룹의 단어라면
        H += 1                          # 행복 지수를 추가하고
    if n in SG:                         # 슬픔 그룹의 단어라면
        S += 1                          # 슬픔 지수를 추가하고
if H == 0 and S == 0:                   # 모두 0이라면
    print('50.00')                      # 50.00을 출력하고
else:                                   # 모두 0이 아니라면
    ans = Decimal((H/(H+S))*100)        # 행복 점수를 계산하고
    ans = ans.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) # 2자리수로 반올림해서
    print(ans)                          # 행복 점수를 출력한다