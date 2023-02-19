# 키큰사람_BOJ11292

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                                            # N이 0이 나올 때 까지 반복해서
    N = int(sys.stdin.readline().strip())                           # 학생의 수를 N으로 input 받고
    if N == 0:                                                      # N이 0이면
        quit()                                                      # 종료한다
    ans = []                                                        # 키 큰 학생을 저장할 빈 리스트를 생성하고
    height = 0                                                      # 키 큰 학생의 키를 저장할 변수를 생성한다
    for _ in range(N):                                              # 학생의 수를 반복해서
        person = list(sys.stdin.readline().strip().split(' '))      # 학생의 이름과 키를 리스트로 input 받고
        if float(person[1]) > height:                               # person의 키가 현재 가장 큰 학생보다 크다면
            height = float(person[1])                               # 현재 가장 큰 학생의 키를 person의 키로 바꾸고
            ans = [person[0]]                                       # ans에 person의 이름으로 교체한다
        elif float(person[1]) == height:                            # person의 키가 현재 가장 큰 학생보다 같다면
            ans.append(person[0])                                   # ans에 person의 이름을 append 한다
    else:                                                           # 모든 학생을 반복했다면
        print(*ans)                                                 # ans를 출력한다
