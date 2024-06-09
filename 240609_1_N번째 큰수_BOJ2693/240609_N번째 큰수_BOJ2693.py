# N번째 큰수_BOJ2693

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스를 input 받고
for t in range(T):                      # 테스트 케이스를 반복해서
    A = list(map(int, input().split())) # 10개의 숫자를 input 받고
    A.sort()                            # 오름차순으로 정렬한 후
    print(A[-3])                        # 3번째 큰 값을 출력한다