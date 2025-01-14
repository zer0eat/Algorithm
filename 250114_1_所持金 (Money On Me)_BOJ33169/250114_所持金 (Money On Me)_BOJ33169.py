# 所持金 (Money On Me)_BOJ33169

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())        # 1000원 지폐의 수를 input 받고
B = int(input())        # 10000원 지폐의 수를 input 받고
print(A*1000+B*10000)   # 가지고 있는 돈을 출력한다