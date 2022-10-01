# ACM호텔_BOJ10250

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                            # 테스트 케이스
for t in range(T):                          # 테스트 케이스를 반복할 때
    H, W, N = map(int, input().split())     # H는 호텔의 높이 / W 호텔의 호수 / N 투숙객의 수

    floor = 0                               # 방배정 시 층수로 사용할 변수
    room = 1                                # 방배정 시 호수로 사용할 변수
    ans = []                                # N번째 투숙객의 층수와 호수를 저장할 리스트
    for n in range(N):                      # N번째 투숙객까지 반복하면서 방배정할 때
        floor += 1                          # 투숙객에게 엘리베이터와 가장 가까운 방을 배정하기 위해 층수를 높여주고
        if floor <= H:                      # 꼭대기 층까지 방을 하나씩 배정해주고
            if n == N - 1:                  # 마지막 투숙객이면
                ans.append(floor)           # 층과 호수를  append 한다
                ans.append(room)            
        else:                               # 만약 꼭대기층보다 높은 층이 되었다면
            floor = 1                       # 1층으로 내려와서
            room += 1                       # 다음 호수로 배정한다
            if n == N - 1:                  # 마지막 투숙객이면
                ans.append(floor)           # 층과 호수를  append 한다
                ans.append(room)            
    else:                                   # 모든 투숙객에게 방을 배정했다면
        f = str(ans[0])                     # 층수를 str로 바꾸고
        if ans[1] < 10:                     # 호수가 10 미만이면
            s = '0'+str(ans[1])             # 앞에 0을 붙인 str로 바꾸고
        else:                               # 호수가 10 이상이면
            s = str(ans[1])                 # str로 바로 바꾼후

        print(f,s, sep = '')                # 층수와 호수를 붙인상태로 출력한다