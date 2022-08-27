# 스위치 켜고 끄기_1244

# input.txt 열기
import sys
sys.stdin = open('input2.txt')

# 스위치 함수
def onoff(switch, N):                                   # switch 리스트와 인덱스 N을 넣고 함수를 돌렸을 때
    if switch[N] == 1:                                  # 1일 땐 0으로
        switch[N] = 0
    elif switch[N] == 0:                                # 0일 땐 1로 바꿔준다
        switch[N] = 1

# input 받기
N = int(input())                                        # N = 스위치의 개수
switch = list(map(int, input().split()))                # switch를 리스트로 받음
students = int(input())                                 # 학생의 수를 받음

for s in range(students):                               # 학생의 수 만큼 반복할 때
    student = list(map(int, input().split()))           # 인덱스 0은 성별 인덱스 1은 카드번호인 리스트 형태 받는다

    # 남학생일 때
    if student[0] == 1:                                 # 성별이 1이라서 남학생인 경우
        M = student[1]                                  # M = 남학생의 카드 번호
        for i in range(1, N + 1):                       # 모든 스위치의 위치를 반복할 때
            if M * i <= N:                              # 카드번호의 배수가 스위치 보다 작으면
                onoff(switch, (M * i) - 1)              # 해당 번호의 스위치를 누른다

    # 여학생일 때
    if student[0] == 2:                                 # 성별이 2이라서 여학생인 경우
        F = student[1] - 1                              # 여학생의 카드번호를 인덱스 형태로 저장한다
        A = []                                          # 회문의 길이를 받기 위한 빈 리스트에
        for j in range(N):                              # 모든 스위치의 위치를 반복할 때
            if 0 <= F - j and F + 1 + j <= N:           # 회문의 인덱스가 초과하지 않을 때
                if switch[F - j: F + 1 + j] == switch[F - j: F + 1 + j][::-1]:      # 회문인 경우
                    A.append(F - j)                     # A에 회문의 시작과
                    A.append(F + 1 + j)                 # 끝을 append
                elif switch[F - j: F + 1 + j] != switch[F - j: F + 1 + j][::-1]:    # 회문이 아닌경우
                    break                               # 반복문을 멈춘다
        b = A.pop()                                     # 가장 긴 회문인 A에 마지막에 append 된 인덱스 끝 값과
        a = A.pop()                                     # 인덱스 처음 값을 꺼낸 후
        for z in range(a, b):                           # 그 범위에 있는
            onoff(switch, z)                            # 스위치를 모두 누른다

for i in range(0, N, 20):                               # 0부터 N까지 20개 단위로
    print(*switch[i:i+20])                              # 스위치를 프린트한다

