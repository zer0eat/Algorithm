# 이중 우선순위 큐_BOJ7662

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
T = int(input())                                        # T 테스트 케이스
for t in range(T):                                      # 테스트 케이스를 반복해서
    N = int(input())                                    # N 연산의 개수
    Q1 = []                                             # 최소 힙을 저장할 리스트 생성
    Q2 = []                                             # 최대 힙을 저장할 리스트 생성
    cnt = 0                                             # 리스트에 있는 원소의 수를 저장할 변수 생성
    visited = dict()                                    # 원소의 처리 여부를 저장할 딕셔너리 생성
    for n in range(N):                                  # 연산의 수를 반복해서
        cal, num = input().split()                      # cal 연산 상태 / num 연산할 숫자를 input받고
        if cal == 'I':                                  # 연산이 I인 경우에는
            heapq.heappush(Q1, int(num))                # 최소 힙을 저장할 리스트에 num을 heappush
            heapq.heappush(Q2, -int(num))               # 최대 힙을 저장할 리스트에 -num을 heappush
            cnt += 1                                    # 리스트 안의 원소의 수를 1 추가하고
            if visited.get(int(num)):                   # num이 key인 딕셔너리 원소가 있다면
                visited[int(num)] += 1                  # value를 1 추가하고
            else:                                       # 없다면
                visited[int(num)] = 1                   # value를 1로 원소를 생성한다
        elif cal == 'D':                                # 연산이 D인 경우에는
            cnt -= 1                                    # 리스트 안의 원소의 수를 1 감소하고
            if cnt > 0:                                 # cnt가 양수인 경우에는
                if num == '1':                          # 연산할 숫자가 1이라면
                    while 1:                            # break가 나올때까지 반복해서
                        delnum = -heapq.heappop(Q2)     # 최대힙 리스트에서 heappop해서 delnum에 가장 큰 원소를 저장한 후
                        if visited[delnum]:             # delnum이 key인 원소의 value가 양수라면
                            visited[delnum] -= 1        # value를 1 빼준 후
                            break                       # while문을 break
                elif num == '-1':                       # 연산할 숫자가 -1이라면
                    while 1:                            # break가 나올때까지 반복해서
                        delnum = heapq.heappop(Q1)      # 최소힙 리스트에서 heappop해서 delnum에 가장 작은 원소를 저장한 후
                        if visited[delnum]:             # delnum이 key인 원소의 value가 양수라면
                            visited[delnum] -= 1        # value를 1 빼준 후
                            break                       # while문을 break
            else:                                       # cnt가 0이하인 경우에는
                Q1 = []                                 # 최소힙 리스트를 초기화하고
                Q2 = []                                 # 최대힙 리스트를 초기화한다
                cnt = 0                                 # 리스트 내 원소의 수를 저장할 변수도 초기화하고
                visited = dict()                        # 원소의 처리여부를 나타낼 딕셔너리도 초기화한다

    Q2 = [-q for q in Q2]                               # 최대힙 리스트의 양수 음수 부호를 반대로 바꿔준 후
    intersection = set(Q1) & set(Q2)                    # intersection에 최대힙과 최소힙의 교집합을 저장한다
    if intersection:                                    # intersection 셋의 원소가 있다면
        print(max(intersection), min(intersection))     # 최댓값과 최솟값을 출력하고
    else:                                               # intersection 셋이 비어있다면
        print('EMPTY')                                  # EMPTY를 출력한다