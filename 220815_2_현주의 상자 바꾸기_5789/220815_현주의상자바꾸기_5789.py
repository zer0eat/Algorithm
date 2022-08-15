# 현주의 상자 바꾸기_5789

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N, Q = input().split()
    N = int(N) # N = 박스의 개수
    Q = int(Q) # Q = 박스의 숫자를 바꿀 조건의 수
    # 0으로 적힌 박스가 담긴 리스트 만들기
    box = [0] * N
    # 조건을 돌릴 때
    for q in range(Q):
        L, R = input().split()
        L = int(L) # 숫자를 바꿀 첫 박스
        R = int(R) # 숫자를 바꿀 마지막 박스
        for b in range(L - 1, R): # 박스가 0이 아닌 1부터 시작하므로 시작을 한칸 당겨준다
            box[b] = q + 1 # 박스에 조건 번호에 맞는 숫자를 입력한다

    print(f'#{t + 1}', *box)
