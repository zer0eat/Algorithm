# 피자굽기_13973

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int,input().split()))
    complite_pizza = []







    # while pizza:
    #     print(pizza)
    #     for p in range(len(pizza)):
    #         # pizza[p] = pizza[p]//2
    #         if pizza[p]//2 == 0:
    #             out = pizza.pop(p)
    #             complite_pizza.append(out)
    #         else:
    #             pizza[p] = pizza[p] // 2
    #
    #
    # print(complite_pizza)