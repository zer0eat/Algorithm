# 팀명 정하기_BOJ28114

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
lst1 = []                       # 푼 문제의 수와 성을 저장할 리스트를 생성하고
lst2 = []                       # 학번을 저장할 리스트를 생성한다
for n in range(3):              # 3명의 학생을 반복해서
    P, Y, S = input().split()   # P 푼 문제 / Y 학번 / S 성을 input 받고
    lst1.append([int(P), S])    # 푼문제를 int로 바꾸고 성과 리스트에 넣어 lst1에 append하고
    lst2.append(int(Y))         # 학번을 int로 lst2에 append한다
lst2.sort()                     # 학번을 담은 리스트를 오름차순 정렬하고
for l in lst2:                  # 학번 정렬순으로 반복해서
    print(str(l)[2:], end='')   # 학번의 뒷자리만 출력한다
print()                         # 한줄 띄어쓰고
lst1.sort(reverse=True)         # 푼 문제의 수를 담은 리스트를 내림차순 정렬하고
for l in lst1:                  # 푼 문제 정렬순으로 반복해서
    print(l[1][0], end='')      # 성의 첫글자만 출력한다