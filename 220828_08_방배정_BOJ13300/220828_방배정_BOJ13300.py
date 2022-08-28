# 방배정_BOJ13300

# input.txt 열기
import sys
sys.stdin = open('input2.txt')

# input 받기
N, K = map(int, input().split())            # 수학여행에 참가하는 학생 수 N / 한 방에 배정할 수 있는 최대 인원 수 K
students = [list(map(int, input().split())) for _ in range(N)]      # 학생의 성별 / 학년정보가 담긴 리스트

W1 = 0                                      # 1학년 여자의 수
M1 = 0                                      # 1학년 남자의 수
W2 = 0                                      # 2학년 여자의 수
M2 = 0                                      # 2학년 남자의 수
W3 = 0                                      # 3학년 여자의 수
M3 = 0                                      # 3학년 남자의 수
W4 = 0                                      # 4학년 여자의 수
M4 = 0                                      # 4학년 남자의 수
W5 = 0                                      # 5학년 여자의 수
M5 = 0                                      # 5학년 남자의 수
W6 = 0                                      # 6학년 여자의 수
M6 = 0                                      # 6학년 남자의 수

for s in students:                          # 학생정보를 하나씩 반복할 때
    if s[0] == 0:                           # 여학생인 경우
        if s[1] == 1:                       # 1~6학년일 때
            W1 += 1                         # 1~6학년 여자의 수에 1을 추가한다
        elif s[1] == 2:
            W2 += 1
        elif s[1] == 3:
            W3 += 1
        elif s[1] == 4:
            W4 += 1
        elif s[1] == 5:
            W5 += 1
        elif s[1] == 6:
            W6 += 1

    if s[0] == 1:                           # 남학생인 경우
        if s[1] == 1:                       # 1~6학년일 때
            M1 += 1                         # 1~6학년 남자의 수에 1을 추가한다
        elif s[1] == 2:
            M2 += 1
        elif s[1] == 3:
            M3 += 1
        elif s[1] == 4:
            M4 += 1
        elif s[1] == 5:
            M5 += 1
        elif s[1] == 6:
            M6 += 1

room = 0                                    # 필요한 방의 수를 세기 위한 변수
if W1 == 0:                                 # 한명도 없으면
    pass                                    # 방이 필요 없으므로 패스
elif W1 > 0:                                # 한명 이상이라면
    room += W1 // K                         # 최대 인원씩 방에 넣었을 때 필요한 방을 추가하고
    if W1 % K == 0:                         # 방에 넣고 남은 인원이 0명이면 패스
        pass
    else:                                   # 방에 넣고 남은 인원이 있으면 방을 한개 추가한다
        room += 1
                                            # 위와 같은 방법으로 모든 학년과 성별을 확인하며 방을 추가한다
if W2 == 0:
    pass
elif W2 > 0:
    room += W2 // K
    if W2 % K == 0:
        pass
    else:
        room += 1

if W3 == 0:
    pass
elif W3 > 0:
    room += W3 // K
    if W3 % K == 0:
        pass
    else:
        room += 1

if W4 == 0:
    pass
elif W4 > 0:
    room += W4 // K
    if W4 % K == 0:
        pass
    else:
        room += 1

if W5 == 0:
    pass
elif W5 > 0:
    room += W5 // K
    if W5 % K == 0:
        pass
    else:
        room += 1

if W6 == 0:
    pass
elif W6 > 0:
    room += W6 // K
    if W6 % K == 0:
        pass
    else:
        room += 1

if M1 == 0:
    pass
elif M1 > 0:
    room += M1 // K
    if M1 % K == 0:
        pass
    else:
        room += 1

if M2 == 0:
    pass
elif M2 > 0:
    room += M2 // K
    if M2 % K == 0:
        pass
    else:
        room += 1

if M3 == 0:
    pass
elif M3 > 0:
    room += M3 // K
    if M3 % K == 0:
        pass
    else:
        room += 1

if M4 == 0:
    pass
elif M4 > 0:
    room += M4 // K
    if M4 % K == 0:
        pass
    else:
        room += 1

if M5 == 0:
    pass
elif M5 > 0:
    room += M5 // K
    if M5 % K == 0:
        pass
    else:
        room += 1

if M6 == 0:
    pass
elif M6 > 0:
    room += M6 // K
    if M6 % K == 0:
        pass
    else:
        room += 1

print(room)