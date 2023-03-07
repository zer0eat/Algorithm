# 카우버거_BOJ15720

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
B, C, D = map(int, input().split())                 # B 주문한 버거의 수 / C 주문한 사이드의 수 / D 주문한 음료의 수
burger = list(map(int, input().split()))            # 주문한 버거의 가격을 리스트로 받고
side = list(map(int, input().split()))              # 주문한 사이드의 가격을 리스트로 받고
beverage = list(map(int, input().split()))          # 주문한 음료의 가격을 리스트로 받는다

A = min(B,C,D)                                      # 세트의 수를 A에 저장한다
burger.sort(reverse=True)                           # 주문한 버거의 가격을 내림차순으로 정렬하고
side.sort(reverse=True)                             # 주문한 사이드의 가격을 내림차순으로 정렬하고
beverage.sort(reverse=True)                         # 주문한 음료의 가격을 내림차순으로 정렬한다

discount = 0                                        # 할인 금액을 저장할 변수를 생성하고
for a in range(A):                                  # 세트의 수를 반복해서
    discount += burger[a] // 10                     # 버거의 가격의 10퍼센트를 discount에 더하고
    discount += side[a] // 10                       # 사이드의 가격의 10퍼센트를 discount에 더하고
    discount += beverage[a] // 10                   # 음료의 가격의 10퍼센트를 discount에 더한다

total = sum(burger) + sum(side) + sum(beverage)     # total에 총 금액을 저장한다

print(total)                                        # 할인 전 총 금액을 출력하고
print(total-discount)                               # 할인 후 총 금액을 출력한다