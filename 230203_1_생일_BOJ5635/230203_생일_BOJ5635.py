# 생일_BOJ5635

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())                               # 생일을 측정하기 위한 사람의 수
birthday = [list(sys.stdin.readline().split()) for _ in range(N)]   # [이름, 일, 월, 년]을 리스트형태로 input 받아 리스트에 저장

young = birthday[0]                                                 # 가장 어린 사람을 저장하기 위한 변수 생성
old = birthday[0]                                                   # 가장 나이가 많은 사람을 저장하기 위한 변수 생성

for i in range(1, N):                                               # 1부터 N-1의 인덱스를 반복해서
    if int(birthday[i][3]) > int(young[3]):                         # i번째 사람과 young에 저장된 사람의 태어난 해를 비교해서 i번째 사람이 더 늦게 태어났다면
        young = birthday[i]                                         # young을 i번째 사람의 정보로 바꾼다
    elif int(birthday[i][3]) == int(young[3]):                      # i번째 사람과 young에 저장된 사람이 같은 해에 태어났다면
        if int(birthday[i][2]) > int(young[2]):                     # i번째 사람과 young에 저장된 사람의 태어난 월을 비교해서 i번째 사람이 더 늦게 태어났다면
            young = birthday[i]                                     # young을 i번째 사람의 정보로 바꾼다
        elif int(birthday[i][2]) == int(young[2]):                  # i번째 사람과 young에 저장된 사람이 같은 월에 태어났다면
            if int(birthday[i][1]) > int(young[1]):                 # i번째 사람과 young에 저장된 사람의 태어난 일을 비교해서 i번째 사람이 더 늦게 태어났다면
                young = birthday[i]                                 # young을 i번째 사람의 정보로 바꾼다

    if int(birthday[i][3]) < int(old[3]):                           # i번째 사람과 old에 저장된 사람의 태어난 해를 비교해서 i번째 사람이 더 일찍 태어났다면
        old = birthday[i]                                           # old를 i번째 사람의 정보로 바꾼다
    elif int(birthday[i][3]) == int(old[3]):                        # i번째 사람과 old에 저장된 사람이 같은 해에 태어났다면
        if int(birthday[i][2]) < int(old[2]):                       # i번째 사람과 old에 저장된 사람의 태어난 월을 비교해서 i번째 사람이 더 일찍 태어났다면
            old = birthday[i]                                       # old를 i번째 사람의 정보로 바꾼다
        elif int(birthday[i][2]) == int(old[2]):                    # i번째 사람과 old에 저장된 사람이 같은 월에 태어났다면
            if int(birthday[i][1]) < int(old[1]):                   # i번째 사람과 old에 저장된 사람의 태어난 일을 비교해서 i번째 사람이 더 일찍 태어났다면
                old = birthday[i]                                   # old를 i번째 사람의 정보로 바꾼다

print(young[0])                                                     # 가장 어린사람의 이름을 출력하고
print(old[0])                                                       # 가장 나이든 사람의 이름을 출력한다