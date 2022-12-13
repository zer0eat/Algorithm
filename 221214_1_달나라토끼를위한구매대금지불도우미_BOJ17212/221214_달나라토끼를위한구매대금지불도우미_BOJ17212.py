# 달나라토끼를위한구매대금지불도우미_BOJ17212

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())               # 지불해야하는 금액
rabbit = [0] * (N+1)                        # 지불해야하는 금액별 내야하는 동전의 개수를 저장하기 위한 리스트 생성

for n in range(1, N+1):                     # 1부터 N까지 반복해서
    if n in [1,2,5,7]:                      # n이 1,2,5,7이라면
        rabbit[n] = 1                       # 동전을 한개만 제출하면 되므로 n인 index에 1을 저장한다
    else:                                   # 그렇지 않으면
        cnt = []                            # 빈 리스트를 생성하고
        if rabbit[n - 1]:                   # n보다 1원 적게 낸 경우가 있다면
            cnt.append(rabbit[n - 1] + 1)   # cnt에 1원 적게낸 경우에 1원짜리 동전을 하나 더낸 개수를 append
        if rabbit[n - 2]:                   # n보다 2원 적게 낸 경우가 있다면
            cnt.append(rabbit[n - 2] + 1)   # cnt에 2원 적게낸 경우에 2원짜리 동전을 하나 더낸 개수를 append
        if rabbit[n - 5]:                   # n보다 5원 적게 낸 경우가 있다면
            cnt.append(rabbit[n - 5] + 1)   # cnt에 5원 적게낸 경우에 5원짜리 동전을 하나 더낸 개수를 append
        if rabbit[n - 7]:                   # n보다 7원 적게 낸 경우가 있다면
            cnt.append(rabbit[n - 7] + 1)   # cnt에 7원 적게낸 경우에 7원짜리 동전을 하나 더낸 개수를 append
        rabbit[n] = min(cnt)                # n을 인덱스로 갖는 자리에 cnt에 저장된 값 중 가장 적게 내도 되는 경우를 저장한다

print(rabbit[N])                            # N일때 최소 동전의 개수를 출력한다
