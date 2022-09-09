# 럭비클럽_BOJ2083.py

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                    # break가 나올 때까지 반복할 때
    people = list(input().split())          # people에 input 받을 것을 리스트 형태로 저장
    if people[0] == '#':                    # 만약 리스트의 맨 앞 요소가 #일 때
        break                               # break
    else:                                   # 그렇지 않으면
        if 17 >= int(people[1]):            # 17살 이하면서
            if 80 > int(people[2]):         # 80kg 미만이면
                print(people[0], 'Junior')  # 사람이름과 junior를 출력한다
            else:                           # 80 이상이면
                print(people[0], 'Senior')  # 사람이름과 senior를 출력한다
        else:                               # 17 초과이면
            print(people[0], 'Senior')      # 사람이름과 senior를 출력한다