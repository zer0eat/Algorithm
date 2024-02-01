# 숫자카드_BOJ10815

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 상근이가 가지고 있는 카드의 수를 input 받고
lst = list(map(int, input().split()))   # 상근이가 가지고 있는 카드를 input 받는다
M = int(input())                        # 가지고 있는지 확인할 카드의 수를 input 받고
card = list(map(int, input().split()))  # 가지고 있는지 확인할 카드를 input 받는다
dic = dict()                            # 카드를 저장할 딕셔너리를 생성하고
for c in card:                          # 가지고 있는지 확인할 카드를 반복해서
    dic[c] = 0                          # 카드를 key로 원소를 생성하고
for l in lst:                           # 상근이가 가지고 있는 카드를 반복해서
    if dic.get(l) != None:              # 딕셔너리에 해당 카드가 있다면
        dic[l] = 1                      # 해당 카드의 value를 1로 저장한다
for d in dic:                           # 딕셔너리를 반복해서
    print(dic[d], end= ' ')             # 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다