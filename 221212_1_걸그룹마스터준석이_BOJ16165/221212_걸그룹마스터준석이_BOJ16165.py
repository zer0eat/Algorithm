# 걸그룹마스터준석이_BOJ16165

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())   # N 입력받을 걸그룹의 수 / M 맞혀야할 문제의 수
kpopname = dict()                               # 사람의 이름을 key 그룹의 이름을 value로 저장할 딕셔너리생성
kpopgroup = dict()                              # 그룹의 이름을 key 사람의 이름을 value로 저장할 딕셔너리생성

for n in range(N):                              # 입력받을 걸그룹의 수만큼 반복해서
    group = sys.stdin.readline().rstrip()       # 그룹 이름 input 받고
    kpopgroup[group] = []                       # 그룹의 이름이 key가 되고 value가 빈 리스트인 딕셔너리를 생성한다
    Q = int(sys.stdin.readline())               # 그룹의 수를 input 받는다
    for q in range(Q):                          # 그룹의 수만큼 반복해서
        name = sys.stdin.readline().rstrip()    # 사람의 이름을 input 받아서
        kpopname[name] = group                  # 사람의 이름을 key 그룹의 이름을 value인 딕셔너리를 생성한다
        kpopgroup[group].append(name)           # 그룹의 이름이 key인 딕셔너리의 value에 append 한다

for m in range(M):                              # 맞혀야할 문제의 수만큼 반복해서
    question = sys.stdin.readline().rstrip()    # 질문을 input 받고
    num = int(sys.stdin.readline())             # 질문의 유형을 input 받아서
    if num:                                     # 유형이 1번이면
        print(kpopname[question])               # 해당 걸그룹 멤버의 그룹명을 출력하고
    else:                                       # 유형이 0번이면
        ans = sorted(kpopgroup[question])       # 해당 걸그룹 멤버를 오름차순으로 ans에 저장해서
        for a in ans:                           # ans를 반복하며
            print(a)                            # 한명씩 출력한다
