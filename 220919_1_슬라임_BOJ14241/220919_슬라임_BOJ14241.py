# 슬라임_BOJ14241

# input.txt
import sys
sys.stdin = open('input4.txt')

# input 받기
N = int(input())                            # 슬라임의 개수
slime = list(map(int, input().split()))     # 슬라임의 크기를 리스트에 담아서 저장

cnt = 0                                     # 점수를 저장할 변수
for i in range(N):                          # 슬라임의 종류를 반복
    for j in range(N):                      # 슬라임의 종류를 반복
        if i < j:                           # i의 인덱스가 j보다 작을 때만
            cnt += slime[i] * slime[j]      # 두 수를 곱한 점수를 cnt에 더함

print(cnt)

''' 어떤 순서로 더하든 모든 종류를 한번씩 곱한 수의 합이 점수가 되기 때문에 
서로 다른 인덱스를 갖는 요소를 곱해서 더해준 값이 정답이된다.'''