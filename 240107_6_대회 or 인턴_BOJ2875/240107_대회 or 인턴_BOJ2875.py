# 대회 or 인턴_BOJ2875

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, K = map(int, input().split()) # N 여학생의 수 / M 남학생의 수 / K 인턴쉽에 참여해야 학생의 수
while K > 0:                        # 인턴쉽에 참여해야하는 학생의 수가 0이하가 될때까지 반복해서
    if M*2 < N:                     # 팀을 구성하고 여학생이 남는다면
        N -= 2                      # 여학생 두명을 빼서
        K -= 2                      # 인턴쉽에 참여시키고
    elif M*2 > N:                   # 팀을 구성하고 남학생이 남는다면
        M -= 1                      # 남학생 한명을 빼서
        K -= 1                      # 인턴쉽에 참여시킨다
    else:                           # 남여 비율이 딱 맞다면
        M -= 1                      # 남학생 한명과
        N -= 2                      # 여학생 두명을 빼서
        K -= 3                      # 인턴쉽에 참여시킨다
print(min(N//2, M))                 # 인턴쉽에 참여하고 남는 학생이 팀을 구성할 수 있는 최대값을 출력한다