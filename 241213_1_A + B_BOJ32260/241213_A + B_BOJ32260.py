# A + B_BOJ32260

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def sum(a, b):          # 함수를 정의하고
    return a + b        # a+b를 return 한다
result = sum(a, b)      # 함수에 숫자를 넣은 후
print(result)           # 결과를 출력한다