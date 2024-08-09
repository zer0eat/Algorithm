# Sort 마스터 배지훈_BOJ17263

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 원소의 개수를 input 받고
A = list(map(int, input().split())) # 원소를 리스트로 input 받는다
A.sort()                            # 오름차순으로 정렬해서
print(A[-1])                        # 가장 큰 수를 출력한다