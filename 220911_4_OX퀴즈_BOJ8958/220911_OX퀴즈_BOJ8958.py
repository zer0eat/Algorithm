# OX퀴즈_BOJ8958

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())        # 테스트 케이스
for t in range(T):      # 테스트 케이스를 반복할 때
    ans = 0             # 점수를 저장할 변수
    w = 0               # 정답 시 추가할 점수
    arr = input()       # 정답과 오답을 문자열로 input
    for a in arr:       # 문자열을 반복할 때
        if a == 'O':    # O가 나왔으면
            w += 1      # 연속된 정답 시 얻을 수 있는 추가점수 계산한다 
            ans += w    # ans에 점수를 추가한다
        else:           # X가 나왔다면
            w = 0       # 추가점수를 초기화 한다
    else:               # 반복이 끝났다면 ans를 출력한다
        print(ans)
