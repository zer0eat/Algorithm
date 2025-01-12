# 鉛筆 2 (Pencils 2)_BOJ33161

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
money = int(input())    # 돈을 입력받고
print(money//5)         # 돈으로 살 수 있는 최대 연필 수를 출력한다