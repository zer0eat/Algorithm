# 암호문3_1230

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10                                                          # 테스트 케이스
for t in range(10):                                             # 테스트 케이스를 반복할 때
    N = int(input())                                            # 암호문의 길이
    code = list(map(int, input().split()))                      # 암호문을 리스트로 받음
    M = int(input())                                            # 암호 변경문의 길이
    statement = list(input().split())                           # 암호변경문을 리스트로 받음

    while statement:                                            # statement가 빌때까지 반복해서
        func = statement.pop(0)                                 # 맨앞에서 꺼낸 요소가
        if func == 'I':                                         # I 이면
            Xi = int(statement.pop(0))                          # 다음 요소를 꺼내 Xi에 int로
            Yi = int(statement.pop(0))                          # 그 다음 요소를 꺼내 Yi에 int로 저장하고
            for y in range(Yi):                                 # Yi만큼 반복해서
                code.insert(Xi + y, int(statement.pop(0)))      # code에 Xi 인덱스부터 그 뒤로 statement에서 하나씩 꺼내 삽입한다
        elif func == 'D':                                       # D 이면
            Xd = int(statement.pop(0))                          # 다음 요소를 꺼내 Xd에 int로
            Yd = int(statement.pop(0))                          # 그 다음 요소를 꺼내 Yd에 int로 저장하고
            for d in range(Yd):                                 # Yd만큼 반복해서
                del code[Xd:Xd + Yd]                            # Xd부터 Yd개 삭제한다
        elif func == 'A':                                       # A 이면
            Ya = int(statement.pop(0))                          # 다음 요소를 꺼내 Ya에 int로 저장하고
            for a in range(Ya):                                 # Ya만큼 반복해서
                code.append(int(statement.pop(0)))              # code의 맨뒤에 statement에서 하나씩 꺼내 삽입한다

    print(f'#{t+1}', *code[0:10])                               # 앞에서 10개만 출력
