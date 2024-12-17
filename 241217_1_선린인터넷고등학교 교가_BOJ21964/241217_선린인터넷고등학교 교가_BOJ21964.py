# 선린인터넷고등학교 교가_BOJ21964

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 글자의 수를 input 받고
words = input().strip() # 글자를 input 받고
print(words[-5:])       # 마지막 5글자를 출력한다