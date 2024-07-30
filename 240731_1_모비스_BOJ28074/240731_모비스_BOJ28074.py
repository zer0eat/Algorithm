# 모비스_BOJ28074

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
d = dict()              # 딕셔너리를 생성하고
d['M'] = 0              # M을 키로 원소를 생성하고
d['O'] = 0              # O를 키로 원소를 생성하고
d['B'] = 0              # B를 키로 원소를 생성하고
d['I'] = 0              # I를 키로 원소를 생성하고
d['S'] = 0              # S를 키로 원소를 생성한다
N = input().strip()     # 문자열을 input 받고
for n in N:             # 문자열을 반복해서
    d[n] = 1            # n이 키인 원소를 1로 저장한다
for m in d:             # 딕셔너리를 반복해서
    if d[m]:            # 밸류가 1이면
        pass            # pass로 넘어가고
    else:               # 밸류가 0인 원소가 나오면
        print('NO')     # NO를 출력하고
        break           # for문을 break한다
else:                   # for문을 마쳤다면
    print('YES')        # YES를 출력한다