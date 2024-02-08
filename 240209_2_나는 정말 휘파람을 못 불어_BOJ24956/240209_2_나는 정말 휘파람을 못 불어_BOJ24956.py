# 나는 정말 휘파람을 못 불어_BOJ24956

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                        # 문자열의 길이를 input 받고
S = list(input().strip())                                               # 문자열을 input 받는다
dic = dict()                                                            # 딕셔너리를 생성하고
dic['W'] = 0                                                            # W가 나온 수를 저장할 원소를 생성하고
dic['H'] = 0                                                            # H가 나온 수를 저장할 원소를 생성하고
dic['E1'] = 0                                                           # E가 나온 수를 저장할 원소를 생성하고
dic['E2'] = 0                                                           # 두번째 E가 나온 수를 저장할 원소를 생성한다
for s in S:                                                             # 문자열을 반복해서
    if s == 'W':                                                        # W가 나오면
        dic['W'] = (dic['W']+1) % 1000000007                            # W에 수를 1 추가하고
    elif s == 'H':                                                      # H가 나오면
        dic['H'] = (dic['H'] + dic['W']) % 1000000007                   # W의 수만큼 H에 추가한다
    elif s == 'E':                                                      # E가 나오면
        dic['E2'] = (dic['E2'] + dic['E2'] + dic['E1']) % 1000000007    # E2에 E1과 E2의 수만큼 추가하고
        dic['E1'] = (dic['E1'] + dic['H']) % 1000000007                 # E1에 H의 수만큼 추가한다
print(dic['E2'])                                                        # WHEE가 만들어지는 개수를 출력한다