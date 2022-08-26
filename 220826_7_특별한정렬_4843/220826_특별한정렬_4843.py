# 특별한 정렬_4843

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                            # 테스트 케이스
for t in range(T):                                          # 테스트 케이스만큼 반복할 때
    N = int(input())                                        # N = 정수의 개수
    ai = list(map(int, input().split()))                    # ai = 정수를 저장한 리스트

    # 버블 솔트                                              # 맨앞이 가장 큰 수로 정렬
    for n in range(N - 1):                                  # 원소의 개수보다 하나 적게 반복하고
        for m in range(N - n - 1):                          # 정렬되지 않은 원소만큼 반복
            if ai[m] < ai[m + 1]:                           # 만약 앞의 요소가 뒤의 요소보다 작을 때
                ai[m], ai[m + 1] = ai[m + 1], ai[m]         # 앞 뒤를 바꿔준다

    # 특별한 정렬
    special = []                                            # 특별한 정렬을 한 것을 저장해줄 리스트
    for i in range(10):                                     # 10개까지 반복할 때
        if i % 2 == 0:                                      # 짝수번째 인덱스에서는
            special.append(ai.pop(0))                       # ai의 맨 앞에서 pop해서 append한다(리스트에서 가장 큰수)
        else:                                               # 홀수번째 인덱스에서는
            special.append(ai.pop())                        # ai의 맨 뒤에서 pop해서 append한다(리스트에서 가장 작은수)

    print(f'#{t+1}', *special)
