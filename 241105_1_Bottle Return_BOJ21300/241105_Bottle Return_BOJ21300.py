# Bottle Return_BOJ21300

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
bottle = list(map(int, input().split()))    # 빈 용기의 수를 input 받고
print(sum(bottle)*5)                        # 보증금의 총액을 출력한다