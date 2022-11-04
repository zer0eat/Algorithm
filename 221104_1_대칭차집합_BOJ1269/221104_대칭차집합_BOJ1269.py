# 대칭차집합_BOJ1269

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
A, B = map(int, sys.stdin.readline().split())           # A 집합 A의 개수 / B 집합 B의 개수
Alst = list(map(int, sys.stdin.readline().split()))     # 집합 A의 모든 원소
Blst = list(map(int, sys.stdin.readline().split()))     # 집합 B의 모든 원소

Alst = set(Alst)                                        # input 받은 리스트를 set으로 변경한 후
Blst = set(Blst)

Acnt = len(Alst - Blst)                                 # 차집합의 개수를 저장하고
Bcnt = len(Blst - Alst)

print(Acnt + Bcnt)                                      # 두 차집합의 개수의 합을 출력한다