# 카드_BOJ11908

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 카드의 숫자를 input받고
card = list(map(int, input().split()))  # 카드를 리스트로 input받고
card.sort()                             # 오름차순으로 정렬해서
print(sum(card[:-1]))                   # 가장 큰 숫자를 뺀 나머지의 합을 구한다