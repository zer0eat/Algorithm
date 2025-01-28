# Dog Treats_BOJ19602

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                     # 정답을 저장할 변수를 생성하고
for n in range(1,4):        # 1부터 3까지 반복해서
    ans += n*int(input())   # 간식의 만족감을 더해준다
if ans >= 10:               # 만족감이 10 이상이면
    print('happy')          # happy를 출력하고
else:                       # 10 미만이면
    print('sad')            # sad를 출력한다