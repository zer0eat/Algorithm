# 소트인사이드_BOJ1427

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = list(input())           # 숫자를 input 받고

ans = []                    # 빈 리스트를 생성한 후
for n in N:                 # input 받은 숫자를 반복해서
    ans.append(int(n))      # int형태로 변환하여 ans에 append 한다

ans.sort(reverse=True)      # 내림차순으로 정렬하고

p = ''                      # str 변수에
for a in ans:               # ans를 반복해서
    p += str(a)             # str 타입으로 하나씩 더한 후

print(p)                    # 출력한다