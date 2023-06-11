# 수 정렬하기 4_BOJ11931

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 숫자의 수를 input 받고
num = set()             # 숫자를 저장할 set 생성
for i in range(N):      # 숫자의 수를 반복해서
    a = int(input())    # a에 숫자를 input받고
    num.add(a)          # set에 a 숫자를 add 한다
num = list(num)         # set을 list로 변경하고
num.sort(reverse=True)  # list를 내림차순으로 정렬한 후
for n in num:           # 원소 하나씩 반복해서
    print(n)            # 원소를 출력한다