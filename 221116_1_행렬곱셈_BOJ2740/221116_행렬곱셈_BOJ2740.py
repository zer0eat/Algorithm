# 행렬곱셈_BOJ2740

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
Na, Ma = map(int, sys.stdin.readline().split())                             # A의 행N 열M
A = [list(map(int, sys.stdin.readline().split())) for _ in range(Na)]       # N*M 행렬 A를 리스트로 input 받음
Nb, Mb = map(int, sys.stdin.readline().split())                             # B의 행N 열M
B = [list(map(int, sys.stdin.readline().split())) for _ in range(Nb)]       # N*M 행렬 B를 리스트로 input 받음

ans = []                                                                    # 행렬 곱셈의 결과를 저장할 리스트를 생성하고
for a in range(Na):                                                         # A 행렬의 행을 반복하고
    tmplst = []                                                             # 곱셈 연산의 한 행의 결과를 저장할 리스트 생성
    for b in range(Mb):                                                     # B 행렬의 열을 반복해서
        tmp = 0                                                             # 행렬연산의 값을 저장할 변수를 생성하고
        for m in range(Ma):                                                 # A 행렬의 열을 반복해서
            tmp += A[a][m]*B[m][b]                                          # A의 a번째 행과 B의 b번째 열을 곱셈의 결과를 tmp에 더하고
        else:                                                               # 연산을 모두 마쳤다면
            tmplst.append(tmp)                                              # tmplst에 곱셈결과를 append 한다
    else:                                                                   # 곱셈 연산으로 한 행의 결과가 모두 완성되었다면
        ans.append(tmplst)                                                  # ans에 tmplst를 append 한다

for a in ans:                                                               # ans를 반복해서
    print(*a)                                                               # 한 행씩 출력한다