# 2022년이 아름다웠던 이유_BOJ27065

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def func(x):                        # 약수 리스트를 구할 함수를 생성하고
    L = []                          # 리스트를 생성해서
    for n in range(1, x+1):         # 1부터 x까지 반복해서
        if x % n == 0:              # n이 x의 약수라면
            L.append(n)             # 리스트에 append하고
    return L                        # 약수 리스트를 return한다

T = int(input())                    # 테스트 케이스를 Input받고
for t in range(T):                  # 테스트 케이스를 반복해서
    N = int(input())                # 숫자를 Input받고
    num = func(N)                   # 약수 리스트를 구해서
    if sum(num) - N > N:            # N이 과잉수라면
        for n in range(len(num)-1): # 약수 리스트를 반복해서
            if sum(func(num[n])) - num[n] > num[n]: # 약수가 과잉수라면
                print('BOJ 2022')   # BOJ 2022를 출력한다
                break               # for문을 종료한다
        else:                       # 모든 약수가 과잉수가 아니라면
            print('Good Bye')       # Good Bye를 출력한다
    else:                           # N이 과잉수가 아니라면
        print('BOJ 2022')           # BOJ 2022를 출력한다
