# 히스토그램_BOJ13752

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())            # 테스트 케이스를 input 받고
for t in range(T):          # 테스트 케이스를 반복해서
    print('='*int(input())) # 히스토그램의 크기 k와 동일한 수의 '='를 출력한다