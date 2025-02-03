# Time to Decompress_BOJ17010

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
L = int(input())                # 메세지의 수를 input 받고
for l in range(L):              # 메세지의 수를 반복해서
    N = list(input().split())   # 숫자와 메세지를 input 받고
    print(int(N[0])*N[1])       # 숫자만큼 메세지를 출력한다