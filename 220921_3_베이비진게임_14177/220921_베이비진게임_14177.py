# 베이비진게임_14177

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                # 테스트케이스
for t in range(T):                              # 테스트케이스를 반복할 때
    card = list(map(int, input().split()))      # card에 나눠줄 카드를 input 받고
    A = [0]*10                                  # A가 가진 카드 숫자를 인덱스로 카드의 개수를 저장할 리스트를 만들고
    B = [0]*10                                  # B도 똑같이 만들어준다
    flag = False                                # 베이비진게임의 승리조건을 달성했을 때 반복문을 종료하기 위한 변수를 생성하고
    ans = []                                    # 정답을 저장할 리스트를 만든다
    while card:                                 # 카드를 모두 나눠줄 때까지 반복해서
        if flag == True:                        # 승리조건을 달성한 사람이 있다면 반복문을 종료하고
            break
        if len(card) % 2 == 0:                  # 짝수번째 차례에는
            a = card.pop(0)                     # 카드를 뽑아
            A[a] += 1                           # A에게 나눠준다
        elif len(card) % 2 == 1:                # 홀수번째 차례에는
            b = card.pop(0)                     # 카드를 뽑아
            B[b] += 1                           # B에게 나눠준다
        if len(card) >= 7:                      # 카드의 개수가 모자라 승리조건을 달성하지 못하면 패스한다
            pass
        else:                                   # 한사람이 3장이상 카드를 받아 승리조건을 달성할 경우가 생길 경우에는
            for c in range(len(A)):             # A를 순서대로 살펴보며
                if A[c] >= 3:                   # 한종류의 카드를 3개이상 가지고 있다면
                    ans.append(1)               # 정답에 1을 저장하고
                    flag = True                 # while 반복문 종료 신호를 보낸 후 반복문을 종료한다
                    break
                elif A[c] >= 1:                 # 한장의 카드를 가지고 있을 때
                    try:                        # 시도가 가능 하다면
                        if A[c+1] >= 1 and A[c+2] >= 1:     # 그 다음장과 다다음장의 카드가 모두 존재할 때
                            ans.append(1)       # 정답에 1을 저장하고
                            flag = True         # while 반복문 종료 신호를 보낸 후 반복문을 종료한다
                            break
                    except:                     # 3장연속 살펴볼 수 없다면 패스한다
                        pass

            for d in range(len(B)):             # B를 순서대로 살펴보며
                if B[d] >= 3:                   # 한종류의 카드를 3개이상 가지고 있다면
                    ans.append(2)               # 정답에 2를 저장하고
                    flag = True                 # while 반복문 종료 신호를 보낸 후 반복문을 종료한다
                    break
                elif B[d] >= 1:                 # 한장의 카드를 가지고 있을 때
                    try:                        # 시도가 가능 하다면
                        if B[d+1] >= 1 and B[d+2] >= 1:     # 그 다음장과 다다음장의 카드가 모두 존재할 때
                            ans.append(2)       # 정답에 2를 저장하고
                            flag = True         # while 반복문 종료 신호를 보낸 후 반복문을 종료한다
                            break
                    except:                     # 3장연속 살펴볼 수 없다면 패스한다
                        pass

    if len(ans) == 1:                           # ans에 정답이 담겨 있으면 정답을 출력하고
        print(f'#{t+1}',*ans)
    else:                                       # 그렇지 않으면 무승부로 0을 출력한다
        print(f'#{t+1}', 0)

