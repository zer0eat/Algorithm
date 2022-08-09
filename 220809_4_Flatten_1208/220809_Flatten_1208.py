# Flatten_1208

#input.txt 열기
import sys
sys.stdin = open('input.txt')

# 최대값 최소값 인덱스 구하는 함수 만들기
def Maxi(list):
    maxi = 0
    maxidx = 0
    for i in range(len(list)):
        if list[i] > maxi:
            maxi = list[i]
            maxidx = i
        else:
            pass
    return maxidx

def Mini(list):
    mini = 100
    minidx = 0
    for i in range(len(list)):
        if list[i] < mini:
            mini = list[i]
            minidx = i
        else:
            pass
    return minidx

#input 리스트로 받기
N = 10
for n in range(N):
    Dump = int(input())
    lst = list(map(int, input().split()))
    
    #Dump
    for d in range(Dump):
        if d < Dump:
            lst[Maxi(lst)] -= 1
            lst[Mini(lst)] += 1
        else:
            pass
    print(f'#{n+1} {lst[Maxi(lst)] - lst[Mini(lst)]}')

