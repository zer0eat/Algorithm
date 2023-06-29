# 인기투표_BOJ11637

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복해서
    N = int(input())                                # 후보자의 수
    winner = 0                                      # 최다 득표자의 번호를 저장할 변수
    total = 0                                       # 총 투표수를 저장할 변수
    maxScore = 0                                    # 최다 득표자의 득표수를 저장할 변수
    for n in range(1, N+1):                         # 후보자를 반복해서
        a = int(input())                            # 후보자의 득표수를 저장하고
        total += a                                  # 총 투표수에 득표수를 더한 후
        if maxScore < a:                            # 득표수가 현재 최대 득표수보다 크다면
            maxScore = a                            # 최다 득표수를 a로 갱신한다
            winner = n                              # 최다 득표자를 n번 후보자로 저장한다
        elif maxScore == a:                         # 득표수가 현재 최대 득표수와 같다면
            winner = 0                              # 최다 득표자를 초기화 한다
    if winner != 0:                                 # 모든 후보자의 득표수를 검사한 후 당선자가 있다면
        if maxScore / total > 0.5:                  # 최다 득표자가 과반수 초과를 받은 경우
            print(f'majority winner {winner}')      # majority winner와 당선자 번호를 출력한다
        else:                                       # 최다 득표자가 과반수 이하를 받은 경우
            print(f'minority winner {winner}')      # minority winner와 당선자 번호를 출력한다
    else:                                           # 최다 득표자가 중복인 경우
        print('no winner')                          # no winner를 출력한다