# Zadanie próbne_BOJ8545

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
word = input().strip()  # 단어를 input 받고
print(word[::-1])       # 단어를 뒤집어서 출력한다