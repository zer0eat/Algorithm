# 試験 (Exam)_BOJ18411

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
exam = list(map(int, input().split()))  # 시험점수를 input 받고
exam.sort()                             # 시험점수를 정렬해서
print(exam[-1]+exam[-2])                # 가장 높은 점수와 다음 점수의 합을 출력한다