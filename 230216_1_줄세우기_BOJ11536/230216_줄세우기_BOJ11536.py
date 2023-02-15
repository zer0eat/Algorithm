# 줄세우기_BOJ11536

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())                       # input 받을 사람의 수를 input 받고
name = [sys.stdin.readline().strip() for _ in range(N)]     # 사람 이름을 받아서 리스트를 만든다
copy = name[:]                                              # 사람 이름이 담긴 리스트를 복사한 후

name.sort()                                                 # 사람 이름을 오름차순으로 정렬한다
if name == copy:                                            # 오름차순 정렬한 것과 input 받은 리스트가 같다면
    print('INCREASING')                                     # INCREASING을 출력하고
    quit()                                                  # 종료한다
name.sort(reverse=True)                                     # 사람 이름을 내림차순으로 정렬하고
if name == copy:                                            # 내림차순 정렬한 것과 input 받은 리스트가 같다면
    print('DECREASING')                                     # DECREASING을 출력하고
    quit()                                                  # 종료한다
print('NEITHER')                                            # 모두 아니라면 NEITHER를 출력한다