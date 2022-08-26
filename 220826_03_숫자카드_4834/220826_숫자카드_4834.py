# 숫자카드_4834

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                            # 테스트 케이스
for t in range(T):                          # 테스트 케이스를 반복할 때
    N = int(input())                        # 숫자 카드의 개수
    ai = list(map(int, input()))            # 숫자 카드를 리스트 ai에 저장

    cnt = [0] * 10                          # 카드의 숫자를 저장할 빈 리스트를 만든 후
    for a in ai:                            # 숫자카드를 반복하여
        cnt[a] += 1                         # 나온 숫자를 cnt의 해당 인덱스에 +1해줌

    maxV = 0                                # 가장 많은 카드의 수
    idx = -1                                # 가장 많은 카드의 인덱스
    for c in range(len(cnt)):               # cnt의 길이만큼 반복할 때
        if cnt[c] >= maxV:                  # cnt의 해당 인덱스의 요소가 최대값보다 같거나 크면
            maxV = cnt[c]                   # cnt의 해당 인덱스의 요소를 maxV에 저장하고
            idx = c                         # idx에 인덱스를 저장한다

    print(f'#{t+1}', idx, maxV)             # 카드 번호와 최대 수를 출력한다