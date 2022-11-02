# 숫자카드_BOJ10815

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                           # 가지고 있는 카드의 개수
Nlst = list(map(int, sys.stdin.readline().split()))     # 가지고 있는 카드의 숫자를 리스트로 input 받음
M = int(sys.stdin.readline())                           # 카드의 유무를 확인할 개수
Mlst = list(map(int, sys.stdin.readline().split()))     # 카드의 유무를 확인할 숫자를 리스트로 input 받음

ans = dict()                                            # 가지고 있는 카드를 저장할 딕셔너리를 생성하고
for n in Nlst:                                          # 가지고 있는 카드를 반복해서
    ans[n] = True                                       # 카드의 숫자를 key로 가지고 있다는 표시인 True를 value로 딕셔너리에 추가한다

card = []                                               # 카드의 유무를 저장할 리스트를 생성하고
for m in Mlst:                                          # 유무를 확인할 숫자를 반복해서
    if ans.get(m) == True:                              # 해당 숫자가 딕셔너리 내에 있어 True가 나온다면
        card.append(1)                                  # card 리스트에 1을 append
    else:                                               # 해당 숫자가 딕셔너리 내에 없다면
        card.append(0)                                  # card 리스트에 0을 append

print(*card)