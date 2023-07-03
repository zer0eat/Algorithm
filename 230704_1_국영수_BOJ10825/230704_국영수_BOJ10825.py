# 국영수_BOJ10825

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # 학생의 수
lst = []                                                        # 학생의 이름과 성적을 저장할 리스트 생성
for n in range(N):                                              # 학생의 수를 반복해서
    a, b, c, d = input().split()                                # a 이름 / b 국어 / c 영어 / d 수학 점수를 input받고
    tmp = [int(b), int(c), int(d), a]                           # tmp 리스트에 국영수 점수와 이름을 순서대로 저장한 후
    lst.append(tmp)                                             # lst에 append
lst = sorted(lst, key = lambda x : (-x[0], x[1], -x[2], x[3]))  # 국어 점수가 감소하는 순서로 / 국어 점수가 같으면 영어 점수가 증가하는 순서로 / 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로 / 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 정렬한 후
for l in lst:                                                   # lst를 반복해서
    print(l[3])                                                 # 정렬된 이름을 출력한다