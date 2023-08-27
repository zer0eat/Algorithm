# 배부른 마라토너_BOJ10546

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 참가자 수를 input 받고
name = dict()                           # 완주여부를 저장할 딕셔너리를 생성한다
for i in range(2*N-1):                  # N-1명의 참가 완주 기록과 한명의 참가기록을 반복해서
    marathon = input().strip()          # 이름을 input 받는다
    if name.get(marathon) == None:      # 이름이 명단에 없는 경우
        name[marathon] = 1              # 이름을 key로 1을 value로 추가하고
    else:                               # 이름이 명단에 있는 경우
        del name[marathon]              # 완주 기록이므로 삭제한다
print(*name.keys())                     # 이름이 남아 완주하지 못한 사람의 이름을 출력한다