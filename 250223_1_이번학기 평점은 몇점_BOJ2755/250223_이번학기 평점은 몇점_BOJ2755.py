# 이번학기 평점은 몇점_BOJ2755

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from decimal import Decimal

# input 받기
N = int(input())                            # 수업의 수를 input 받고
grade, credit = 0, 0                        # 성적과 학점을 저장할 변수를 생성하고
dic = {                                     
    'A+': Decimal("4.3"), 'A0': Decimal("4.0"), 'A-': Decimal("3.7"),
    'B+': Decimal("3.3"), 'B0': Decimal("3.0"), 'B-': Decimal("2.7"),
    'C+': Decimal("2.3"), 'C0': Decimal("2.0"), 'C-': Decimal("1.7"),
    'D+': Decimal("1.3"), 'D0': Decimal("1.0"), 'D-': Decimal("0.7"),
    'F': Decimal("0"),
}                                           # 학점에 맞는 점수를 저장한다
for n in range(N):                          # 수업의 수를 반복해서
    c = input().split()                     # 수업 정보를 input 받고
    credit += Decimal(c[1])                 # 학점을 저장하고
    grade += Decimal(c[1]) * dic[c[2]]      # 성적을 저장해서
ans = (grade / credit)                      # gpa를 구한후
print(f"{ans:.2f}")                         # gpa를 소수점 2자리까지 출력한다