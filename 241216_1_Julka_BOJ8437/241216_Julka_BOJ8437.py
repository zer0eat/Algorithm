# Julka_BOJ8437

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a = int(input())    # 소녀가 가진 총 사과의 개수를 input 받고
b = int(input())    # klaudia가 Natalia보다 많이 가진 사과의 개수를 input 받는다
print((a+b)//2)     # klaudia의 사과의 수를 출력하고
print((a-b)//2)     # Natalia 사과의 수를 출력한다