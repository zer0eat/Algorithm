# 할인이 필요해_BOJ34323

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, S = map(int, input().split()) # 할인 퍼센트, 1개를 더주는 기준수, 개당 가격을 input받고
ans1 = M*S                          # M+1개를 샀을 때 가격을 저장하고
ans2 = int((M+1)*S*(100-N)//100)    # 무인 할인을 받아 샀을 때 가격을 저장하고
print(min(ans1, ans2))              # 두 값중 더 작은 값을 출력한다