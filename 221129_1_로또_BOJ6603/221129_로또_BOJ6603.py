# 로또_BOJ6603

# import.txt 열기
import sys
sys.stdin = open('input.txt')

def lotto6(n):
    if n == N:                                              # 모든 요소에 대해 비트를 결정했을 때
        if sum(bit) == 6:                                   # bit의 합이 6인 경우에만
            ans = []                                        # 로또번호를 저장할 빈 리스트를 생성하고
            for b in range(N):                              # 비트를 반복해서
                if bit[b] == 1:                             # 해당 인덱스의 비트가 1인 경우에만
                    ans.append(lotto[b])                    # 해당 인덱스의 로또번호를 ans에 append
            else:                                           # 반복을 마쳤다면
                print(*ans)                                 # ans를 출력한다
        return
    bit[n] = 1                                              # 비트를 1로 저장하고
    lotto6(n+1)                                             # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다
    bit[n] = 0                                              # 비트를 0으로 저장하고
    lotto6(n + 1)                                           # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다

# input 받기
time = 1                                                    # 반복 횟수를 셀 변수 생성
while 1:                                                    # break가 나올 때까지 반복
    lotto = list(map(int, sys.stdin.readline().split()))    # 고른 번호의 개수와 번호를 리스트 형태로 input 받음
    N = lotto.pop(0)                                        # 맨 앞에 있는 고른 번호의 개수를 pop해서
    if N == 0:                                              # 개수가 0이라면
        break                                               # while문 종료
    if time > 1:                                            # 두번째 반복 부터
        print()                                             # 출력에서 한줄 띄어쓰고
    bit = [0]*N                                             # bit를 N개 만큼 만들어서
    lotto6(0)                                               # lotto6 함수를 돌리고
    time += 1                                               # time을 1 증가시킨다


