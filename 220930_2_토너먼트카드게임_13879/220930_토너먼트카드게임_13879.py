# 토너먼트카드게임_13879

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def half(card):

    if len(card) == 1:                          # card의 요소가 1개 일 때
        return card                             # card를 return

    else:                                       # 1개 이상일 때
        group1 = card[:((len(card)-1)//2)+1]    # (len(card)-1)//2)을 포함하며 이보다 작은 인덱스를 갖는 그룹과
        group2 = card[((len(card)-1)//2)+1:]    # (len(card)-1)//2)보다 큰 인덱스를 갖는 그룹으로 나눈다
        if len(group1) != 1:                    # 나눈 왼쪽 그룹의 길이가 1이 아니라면
            group1 = half(group1)               # 왼쪽 그룹을 다시 half 함수로 돌린다
        if len(group2) != 1:                    # 나눈 오른쪽 그룹의 길이가 1이 아니라면
             group2 = half(group2)              # 오른쪽 그룹을 다시 half 함수로 돌린다

        # 승자 뽑기
        if group1[0][0] >= group2[0][0]:        # 왼쪽이 같은값이나 큰 값일 경우에
            if group1[0][0] == 3 and group2[0][0] == 1:     # 왼쪽이 3일 경우에 오른쪽이 1인 경우에만
                return group2                   # 오른쪽이 승리하고
            else:                               # 그렇지 않으면
                return group1                   # 왼쪽이 승리한다
        else:                                   # 오른쪽이 더 큰값일 경우에
            if group1[0][0] == 1 and group2[0][0] == 3:     # 왼쪽이 1일 경우에 오른쪽이 3인 경우에만
                return group1                   # 왼쪽이 승리하고
            else:                               # 그렇지 않으면
                return group2                   # 오른쪽이 승리한다

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복할 때
    N = int(input())                            # 토너먼트에 참여한 사람의 수
    arr = list(map(int, input().split()))       # 참여한 사람에게 나눠줄 카드를 리스트로 받음

    card = []                                   # 카드번호와 참가번호를 저장할 빈 리스트 생성
    cnt = 1                                     # 참가번호를 입력하기 위해 사용할 변수
    for a in arr:                               # 카드를 반복해서
        card.append([a, cnt])                   # [카드번호, 참가번호]를 card 리스트에 append
        cnt += 1                                # 참가번호를 다음으로 넘겨준다

    print(f'#{t+1}', half(card)[0][1])          # 우승자의 참가번호를 출력한다