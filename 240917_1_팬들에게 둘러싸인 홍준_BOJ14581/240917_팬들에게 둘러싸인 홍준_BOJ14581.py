# 팬들에게 둘러싸인 홍준_BOJ14581

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
id = input().strip()        # 아이디를 input 받고
print(':fan::fan::fan:')    # 팬들을 출력하고
print(f':fan::{id}::fan:')  # 팬에게 둘러쌓인 것을 출력하고
print(':fan::fan::fan:')    # 팬들을 출력한다