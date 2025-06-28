# 레퓨닛의 덧셈_BOJ33964

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X, Y = map(int, input().split())    # 두 수를 input받고
print(int('1'*X)+int('1'*Y))        # 두 수만큼의 레퓨닛수의 합을 출력한다