# 점화식_BOJ13699

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 구하려는 수열의 N번째 수를 input 받고
t = [1]                             # N이 0일 때 값인 1을 넣은 리스트를 생성한다
for i in range(1, N+1):             # 1부터 N까지 반복해서
    tmp = 0                         # 변수 tmp를 생성하고
    for j in range(i):              # i까지 반복해서
        tmp += t[j] * t[i-j-1]      # tmp에 점화식을 통한 값을 더한 후
    else:                           # i까지 반복을 완료하면
        t.append(tmp)               # tmp를 t에 append한다
print(t[N])                         # N번재 점화식을 출력한다