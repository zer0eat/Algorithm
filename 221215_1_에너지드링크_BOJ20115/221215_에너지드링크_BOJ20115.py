# 에너지드링크_BOJ20115

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                           # 에너지드링크 재료 종류의 수
energy = list(map(int, sys.stdin.readline().split()))   # 에너지드링크 재료의 양을 리스트로 input

E1 = max(energy)                                        # 가장 큰 재료의 양
sumE = sum(energy)                                      # 모든 재료의 합

print((sumE-E1)/2 + E1)                                 # 만들 수 있는 에너지드링크의 양을 출력
