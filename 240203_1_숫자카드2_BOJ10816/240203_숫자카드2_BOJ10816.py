# 숫자 카드 2_BOJ10816

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 상근이가 가지고 있는 카드의 수를 input 받고
lstN = list(map(int, input().split()))  # 상근이가 가지고 있는 카드를 input 받는다
M = int(input())                        # 가지고 있는지 확인할 카드의 수를 input 받고
lstM = list(map(int, input().split()))  # 가지고 있는지 확인할 카드를 input 받는다
ans = dict()                            # 카드를 저장할 딕셔너리를 생성하고
for m in lstM:                          # 가지고 있는지 확인할 카드를 반복해서
    ans[m] = 0                          # 카드를 key로 원소를 생성하고
for n in lstN:                          # 상근이가 가지고 있는 카드를 반복해서
    if ans.get(n) != None:              # 딕셔너리에 해당 카드가 있다면
        ans[n] += 1                     # 해당 카드의 value를 1 추가한다
for a in lstM:                          # 가지고 있는지 확인할 카드를 반복해서
    print(ans[a], end=' ')              # 카드의 숫자를 출력한다