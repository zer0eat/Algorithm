# 왜 맘대로 예약하냐고_BOJ32941

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T, X = map(int, input().split())                # 교시의 수와 예약한 교시를 input 받고
N = int(input())                                # 사람을 input 받고
for n in range(N):                              # 사람을 반복해서
    K = int(input())                            # 들어올 수 있는 수업의 수를 input 받고
    classK = list(map(int, input().split()))    # 수업의 정보를 리스트로 input 받는다
    if X in classK:                             # X 교시에 참여할 수 있다면
        pass                                    # pass하고
    else:                                       # X 교시에 참여할 수 없다면
        print('NO')                             # NO를 출력하고
        quit()                                  # 종료한다
print('YES')                                    # 모두 출석할 수 있다면 YES를 출력한다다