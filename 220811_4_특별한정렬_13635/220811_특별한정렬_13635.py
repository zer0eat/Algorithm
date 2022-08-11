# 특별한 정렬_13635

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 가장 큰 수와 가장 작은 수 찾는 함수 만들기
def Big(list):
    big1 = 0
    for l in list:
        if l > big1:
            big1 = l
    return big1

def Small(list):
    small1 = 101
    for s in list:
        if s < small1:
            small1 = s
    return small1

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N = int(input()) # 정수의 개수
    A = list(map(int, input().split())) # A = N개의 원소를 갖는 리스트
    B = []

    # A를 특별한 정렬 10개까지만 하기
    for i in range(10):
        # 홀수 번째 정렬은 제일 큰 값 찾기
        if i % 2 == 0:
            B.append(Big(A))
            A.remove(Big(A))
        # 짝수 번째 정렬은 제일 작은 값 찾기
        elif i % 2 == 1:
            B.append(Small(A))
            A.remove(Small(A))

    print(f'#{t+1} ', end='')
    print(*B)