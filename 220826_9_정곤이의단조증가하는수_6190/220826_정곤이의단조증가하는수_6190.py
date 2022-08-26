# 정곤이의 단조증가하는 수_6190

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                        # 테스트 케이스
for t in range(T):                                      # 테스트 케이스 수 반복
    N = int(input())                                    # N = input 받을 정수의 개수
    Ai = list(map(int, input().split()))                # Ai = input 받은 정수의 리스트

    # Ai X Aj 구하기
    monotonic = []                                      # Ai X Aj의 값을 저장할 빈리스트 생성
    for a in range(N - 1):                              # 정수의 곱셈을 할때 앞의 요소의 인덱스 만큼 반복할 때
        for b in range(a + 1, N):                       # a 보다 뒤에 나오는 요소 b를 반복하여
            monotonic.append(Ai[a] * Ai[b])             # 두 요소를 곱한 후 그 값을 monotonic에 append

    # 가장 큰 단조함수 구하기
    Big_monotonic = -1                                  # 가장 큰 단조함수를 저장할 변수를 -1 값으로 생성
    for m in monotonic:                                 # 저장한 Ai X Aj의 값을 반복할 때
        o = m                                           # monotonic의 요소를 o에 저장하고
        if o < 10:                                      # 한 자리 숫자면
            pass                                        # 패스
        elif o >= 10:                                   # 두자리 이상의 숫자일 때
            while o >= 10:                              # 한자리 숫자가 될때까지 반복
                if o >= 10:                             # 연산 값이 두자리 숫자 이상일 때
                    if o % 10 >= (o // 10) % 10:        # 1의 자리가 10의자리 숫자보다 크면
                        o = o // 10                     # o를 10로 나누고 나머지는 버린 값을 저장 후 패스
                        pass
                    elif o % 10 < (o // 10) % 10:       # 만약 1의 자리가 10의자리 숫자보다 작다면
                        break                           # 단조함수가 아니므로 break
                elif o < 10:                            # 모든 자리가 단조함수를 만족해서 한자리만 남았다면
                    pass                                # 그 숫자는 단조함수를 만족하므로 패스
            else:                                       # 반복문을 통과하여 단조함수가 검증되었으면
                if Big_monotonic < m:                   # Big_monotonic의 값과 비교하여 그 값보다 큰 경우에
                    Big_monotonic = m                   # Big_monotonic를 m으로 변경한다

    print(f'#{t+1}', Big_monotonic)                     # Ai X Aj 중 가장 큰 단조함수를 출력한다



