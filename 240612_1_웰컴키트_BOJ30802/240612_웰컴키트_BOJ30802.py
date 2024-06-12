# 웰컴키트_BOJ30802

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 사람의 수를 input 받고
size = list(map(int, input().split()))  # 사이즈별 수량을 리스트로 input 받고
T, P = map(int, input().split())        # 티셔츠와 펜의 묶음을 input 받고
ans = 0                                 # 티셔츠 묶음을 저장할 변수를 생성하고
for s in size:                          # 사이즈별 수량을 반복해서
    ans += (s-1)//T + 1                 # 사이즈별 묶음을 ans에 다한 후
print(ans)                              # 주문해야하는 T셔츠 묶음을 출력하고
print(N//P, N%P)                        # 주문해야하는 펜의 묶음과 나머지를 출력한다