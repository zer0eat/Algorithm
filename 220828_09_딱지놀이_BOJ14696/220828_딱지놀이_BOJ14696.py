# 딱지놀이_BOJ14696

# input.txt 열기
import sys
sys.stdin = open('input2.txt')

# input 받기
N = int(input())                                # 딱지놀이의 총 라운드 수
for n in range(N):                              # 라운드의 수만큼 반복할 때

    Acnt = [0]*4                                # A 카드의 별 동그라미 네모 세모의 개수를 입력할 리스트
    Bcnt = [0]*4                                # B 카드의 별 동그라미 네모 세모의 개수를 입력할 리스트

    A = list(map(int, input().split()))         # A 카드를 input 받음
    B = list(map(int, input().split()))         # B 카드를 input 받음

    for a in range(1, A[0]+1):                  # 딱지에 나온 그림의 총 개수만큼 반복할 때
        if A[a] == 4:                           # 4가 나왔으면
            Acnt[0] += 1                        # Acnt의 맨앞에 1을 추가
        elif A[a] == 3:                         # 3이 나왔다면
            Acnt[1] += 1                        # Acnt의 두번째에 1을 추가
        elif A[a] == 2:                         # 2가 나왔다면
            Acnt[2] += 1                        # Acnt의 세번째에 1을 추가
        elif A[a] == 1:                         # 1이 나왔다면
            Acnt[3] += 1                        # Acnt의 마지막에 1을 추가

    for b in range(1, B[0]+1):                  # 딱지에 나온 그림의 총 개수만큼 반복할 때
        if B[b] == 4:                           # 4가 나왔으면
            Bcnt[0] += 1                        # Bcnt의 맨앞에 1을 추가
        elif B[b] == 3:                         # 3이 나왔다면
            Bcnt[1] += 1                        # Bcnt의 맨앞에 1을 추가
        elif B[b] == 2:                         # 2가 나왔다면
            Bcnt[2] += 1                        # Bcnt의 맨앞에 1을 추가
        elif B[b] == 1:                         # 1이 나왔다면
            Bcnt[3] += 1                        # Bcnt의 맨앞에 1을 추가

    while Acnt:                                 # Acnt가 빌때까지 반복할 때
        Anum = Acnt.pop(0)                      # 맨앞에서 숫자를 꺼내 Anum에 저장
        Bnum = Bcnt.pop(0)                      # 맨앞에서 숫자를 꺼내 Bnum에 저장
        if Anum > Bnum:                         # Anum이 더 크면
            print('A')                          # A를 출력하고
            break                               # 반복문 종료
        elif Anum < Bnum:                       # Bnum이 더 크면
            print('B')                          # B를 출력하고
            break                               # 반복문 종료
        elif Anum == Bnum:                      # 두 수가 같다면
            pass                                # 패스
    else:                                       # 반복문을 모두 통과했다면 무승부 이므로
        print('D')                              # D를 출력한다