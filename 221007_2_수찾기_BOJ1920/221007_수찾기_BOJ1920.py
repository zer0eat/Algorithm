# 수찾기_BOJ1920

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                           # N 가지고 있는 정수의 개수
cardn = list(map(int, sys.stdin.readline().split()))    # 정수를 리스트 형태로 input
M = int(sys.stdin.readline())                           # M 확인해야할 숫자의 개수
cardm = list(map(int, sys.stdin.readline().split()))    # 확인해야할 숫자를 리스트 형태로 input

ans = dict()                                            # 빈 딕셔너리를 생성
for m in cardm:                                         # 확인해할 숫자를 반복해서
    ans[m] = 0                                          # 확인해야할 숫자를 키값으로 밸류가 0인 요소를 딕셔너리에 추가한다

for n in cardn:                                         # 가지고 있는 정수 리스트를 반복해서
    if ans.get(n) == 0:                                 # 가지고 있는 정수의 키값이 존재하면
        ans[n] = 1                                      # 밸류값을 1로 변경

for a in cardm:                                         # 확인해야할 숫자를 반복해서
    if ans.get(a):                                      # 밸류값이 존재하면
        print(ans.get(a))                               # 밸류값을 출력하고
    else:                                               # 존재하지 않으면
        print(0)                                        # 0을 출력한다