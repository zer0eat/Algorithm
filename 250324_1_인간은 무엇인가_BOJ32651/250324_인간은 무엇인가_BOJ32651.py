# 인간은 무엇인가_BOJ32651

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 햇수를 input 받고
if N > 100000 or N % 2024:  # 100000이 넘거나 2024의 배수가 아니라면
    print('No')     # No를 출력하고
else:               # 100000 이하의 2024의 배수라면
    print('Yes')    # Yes를 출력한다