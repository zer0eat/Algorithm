# Acquiring SW-IT Corn_BOJ34529

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X, Y, Z = map(int, input().split())     # 아이스크림의 단가를 input받고
U, V, W = map(int, input().split())     # 사야하는 아이스크림의 무게를 input받고
print(int(X*(U/100)+Y*(V/50)+Z*(W/20))) # 비용을 출력한다