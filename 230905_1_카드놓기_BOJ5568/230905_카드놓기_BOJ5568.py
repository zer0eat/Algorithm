# 카드놓기_BOJ5568

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import permutations

# input 받기
N = int(input())                            # 카드의 개수를 input 받고
K = int(input())                            # 뽑을 카드의 수를 input 받는다
card = [int(input()) for i in range(N)]     # card를 input 받아 리스트에 저장하고
ans = set()                                 # 뽑은 카드로 정수를 만들어 저장할 set을 생성한다
for i in permutations(card, K):             # card 리스트에서 K개를 순열로 뽑아서
    tmp = ''                                # 뽑은 카드로 숫자를 만들 변수를 생성하고
    for j in i:                             # 순열로 뽑은 카드를 반복해서
        tmp += str(j)                       # tmp에 카드 숫자를 더한다
    else:                                   # 순열로 뽑은 카드를 모두 반복했으면
        ans.add(tmp)                        # 만들어진 숫자를 set에 add한다
print(len(ans))                             # 모든 순열을 반복한 후 ans에 저장된 정수의 수를 출력한다