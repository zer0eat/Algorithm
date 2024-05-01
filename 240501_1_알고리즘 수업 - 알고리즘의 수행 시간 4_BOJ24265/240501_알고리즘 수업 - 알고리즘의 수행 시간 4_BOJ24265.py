# 알고리즘 수업 - 알고리즘의 수행 시간 4_BOJ24265

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 입력의 크기를 input 받고
print(N*(N-1)//2)   # MenOfPassion의 수행횟수를 출력하고
print(2)            # 수행 후 최고차항을 출력한다