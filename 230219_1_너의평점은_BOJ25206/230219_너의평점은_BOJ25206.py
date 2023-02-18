# 너의평점은_BOJ25206

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
credit = 0                                                  # 이수한 학점을 저장할 변수
grade = 0                                                   # 학점과 점수를 곱한 값을 저장할 변수
for _ in range(20):                                         # 20개의 과목을 반복해서
    Q = list(sys.stdin.readline().strip().split(' '))       # Q에 과목명, 학점, 점수를 리스트로 input 받는다
    if 'A+' == Q[2]:                                        # A+를 받았다면
        grade += (float(Q[1]) * 4.5)                        # grade에 학점과 점수의 곱을 더하고
        credit += float(Q[1])                               # credit에 학점을 더한다
    elif 'A0' == Q[2]:                                      # A0를 받았다면
        grade += (float(Q[1]) * 4.0)                        # grade에 학점과 점수의 곱을 더하고
        credit += float(Q[1])                               # credit에 학점을 더한다
    elif 'B+' == Q[2]:                                      # B+를 받았다면
        grade += (float(Q[1]) * 3.5)                        # grade에 학점과 점수의 곱을 더하고
        credit += float(Q[1])                               # credit에 학점을 더한다
    elif 'B0' == Q[2]:                                      # B0를 받았다면
        grade += (float(Q[1]) * 3.0)                        # grade에 학점과 점수의 곱을 더하고
        credit += float(Q[1])                               # credit에 학점을 더한다
    elif 'C+' == Q[2]:                                      # C+를 받았다면
        grade += (float(Q[1]) * 2.5)                        # grade에 학점과 점수의 곱을 더하고
        credit += float(Q[1])                               # credit에 학점을 더한다
    elif 'C0' == Q[2]:                                      # C0를 받았다면
        grade += (float(Q[1]) * 2.0)                        # grade에 학점과 점수의 곱을 더하고
        credit += float(Q[1])                               # credit에 학점을 더한다
    elif 'D+' == Q[2]:                                      # D+를 받았다면
        grade += (float(Q[1]) * 1.5)                        # grade에 학점과 점수의 곱을 더하고
        credit += float(Q[1])                               # credit에 학점을 더한다
    elif 'D0' == Q[2]:                                      # D0를 받았다면
        grade += (float(Q[1]) * 1.0)                        # grade에 학점과 점수의 곱을 더하고
        credit += float(Q[1])                               # credit에 학점을 더한다
    elif 'F' == Q[2]:                                       # F를 받았다면
        credit += float(Q[1])                               # credit에 학점을 더한다

print(grade/credit)                                         # grade를 credit으로 나눠 평점을 출력한다