# 스물셋_BOJ23251

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())            # 테스트 케이스를 Input받고
for t in range(T):          # 테스트 케이스를 반복해서
    print(23*int(input()))  # K번째 23의 수를 출력한다