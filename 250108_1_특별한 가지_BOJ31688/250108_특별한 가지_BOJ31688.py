# 특별한 가지_BOJ31688

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 파묻튀 하나의 무게를 input 받고
M = int(input())    # 파묻튀 재료의 무게를 input 받고
K = int(input())    # 파묻튀밥 하나의 밥 무게를 input 받고
print(K*(M//N))     # 필요한 밥 무게를 출력한다