# Tri-du_BOJ13597

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
card = list(map(int, input().split()))  # 카드를 input 받고
print(max(card))                        # 카드 중 가장 큰 카드를 출력한다