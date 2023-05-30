# 트리플소트_BOJ20309

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 배열의 크기를 input
lst = list(map(int, input().split()))   # 배열의 원소를 리스트로 input

for i in range(1, N+1):                 # 배열의 크기를 반복해서
    if i % 2 == 0:                      # 짝수번째 나오는 원소라면
        if lst[i-1] % 2 == 0:           # 원소도 짝수일 때는
            pass                        # pass
        else:                           # 원소는 홀수라면
            print('NO')                 # No를 출력하고
            break                       # break
    else:                               # 홀수번째 나오는 원소라면
        if lst[i-1] % 2 == 1:           # 원소도 홀수일 때는
            pass                        # pass
        else:                           # 원소는 짝수라면
            print('NO')                 # No를 출력하고
            break                       # break
else:                                   # 모든반복을 마쳤다면
    print('YES')                        # YES를 출력한다