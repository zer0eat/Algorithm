# 탄소 화합물_BOJ1907

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a, m3 = input().strip().split('=')              # 두 분자와 화합물을 input 받고
m1, m2 = a.strip().split('+')                   # 두 분자를 각각 저장한다
m1_atom = [0]*3                                 # 첫번째 분자의 원소를 저장할 리스트를 생성하고
m2_atom = [0]*3                                 # 두번째 분자의 원소를 저장할 리스트를 생성하고
m3_atom = [0]*3                                 # 세번째 분자의 원소를 저장할 리스트를 생성한다
dic = {'C':0, 'H':1, 'O':2}                     # 탄소 수소 산소를 key로 딕셔너리를 생성한다
for m in m1:                                    # 첫번째 분자를 반복해서
    if dic.get(m) != None:                      # 원자가 나왔다면
        m1_atom[dic[m]] += 1                    # 해당 원자의 수를 1 더하고
        tmp = m                                 # 해당 원자를 저장한다
    else:                                       # 숫자가 나왔다면
        if m == '0':                            # 0일 경우
            m1_atom[dic[tmp]] += 9              # 원자의 수를 9 더하고
        else:                                   # 0이 아닐 경우
            m1_atom[dic[tmp]] += int(m)-1       # 원자의 수를 m-1개를 더한다
for m in m2:                                    # 두번째 분자를 반복해서
    if dic.get(m) != None:                      # 원자가 나왔다면
        m2_atom[dic[m]] += 1                    # 해당 원자의 수를 1 더하고
        tmp = m                                 # 해당 원자를 저장한다
    else:                                       # 숫자가 나왔다면
        if m == '0':                            # 0일 경우
            m2_atom[dic[tmp]] += 9              # 원자의 수를 9 더하고
        else:                                   # 0이 아닐 경우
            m2_atom[dic[tmp]] += int(m)-1       # 원자의 수를 m-1개를 더한다
for m in m3:                                    # 세번째 분자를 반복해서
    if dic.get(m) != None:                      # 원자가 나왔다면
        m3_atom[dic[m]] += 1                    # 해당 원자의 수를 1 더하고
        tmp = m                                 # 해당 원자를 저장한다
    else:                                       # 숫자가 나왔다면
        if m == '0':                            # 0일 경우
            m3_atom[dic[tmp]] += 9              # 원자의 수를 9 더하고
        else:                                   # 0이 아닐 경우
            m3_atom[dic[tmp]] += int(m)-1       # 원자의 수를 m-1개를 더한다
for i in range(1, 11):                          # 첫번째 분자의 수를 반복하고
    for j in range(1, 11):                      # 두번째 분자의 수를 반복하고
        for k in range(1, 11):                  # 세번째 분자의 수를 반복해서
            if m1_atom[0]*i + m2_atom[0]*j == m3_atom[0]*k:             # 탄소의 개수가 일치하고
                if m1_atom[1]*i + m2_atom[1]*j == m3_atom[1]*k:         # 수소의 개수가 일치하고
                    if m1_atom[2]*i + m2_atom[2]*j == m3_atom[2]*k:     # 산소의 개수가 일치하면
                        print(i,j,k)            # m1, m2, m3의 개수를 출력하고
                        quit()                  # 종료한다