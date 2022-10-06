# 숫자카드2_BOJ10816

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                           # N 카드의 개수
cardn = list(map(int, sys.stdin.readline().split()))    # 카드의 숫자를 리스트로 input
M = int(sys.stdin.readline())                           # M 확인해야할 숫자의 수
cardm = list(map(int, sys.stdin.readline().split()))    # 확인해야할 숫자를 리스트로 input

ans = dict()                                            # 빈 딕셔너리 생성

for m in cardm:                                         # 확인해야할 숫자 리스트를 반복해서
    ans[m] = 0                                          # 확인해야할 숫자를 키값으로 밸류가 0인 딕셔너리 생성

for n in cardn:                                         # 가지고 있는 카드를 반복해서
    if ans.get(n) != None:                              # 딕셔너리에 key 값이 존재하면
        ans[n] = ans.get(n) + 1                         # 밸류에 1을 더한 값을 저장한다

ans2 = []                                               # 정답을 출력하기 위한 빈 리스트를 생성하고
for a in cardm:                                         # 확인해야할 숫자 리스트를 반복해서
    ans2.append(ans.get(a))                             # 확인해야할 숫자의 밸류 값을 ans2에 append하고

print(*ans2)                                            # 출력한다