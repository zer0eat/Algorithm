# Covid-19_BOJ20673

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
p = int(input())            # 신규 확진자 수를 input 받고
q = int(input())            # 신규 입원자 수를 input 받는다
if q > 30:                  # 신규 입원자 수가 30명을 넘는다면
    print('Red')            # Red로 표시한다
elif p <= 50 and q <=10:    # 신규 확진자가 50명 이하이고 신규 입원자 수가 10명 이하이면
    print('White')          # White로 표시한다
else:                       # 그 외 지역은
    print('Yellow')         # Yellow로 표시한다