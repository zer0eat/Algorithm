# 미역은 식물 아닌데요_BOJ30502

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                # 생물의 수와 관찰 횟수를 inputqkerh
plant = [2]*N                                   # 식물을 표시할 리스트를 생성하고
animal = [2]*N                                  # 동물을 표시할 리스트를 생성하고
for m in range(M):                              # 관찰횟수를 반복해서
    a,b,c = input().split()                     # 관찰결과를 input받고
    if b == 'P':                                # 식물결과라면
        plant[int(a)-1] =int(c)                 # 식물리스트에 정보를 업데이트하고
    else:                                       # 동물결과라면
        animal[int(a)-1] =int(c)                # 동물리스트에 정보를 업데이트하고
mi, ma = 0, 0                                   # 최소 최대값을 저장할 변수를 생성하고
for m in range(N):                              # 생물의 수를 반복해서
    if plant[m] == 1 and animal[m] == 0:        # 식물이 확실하다면
        mi += 1                                 # 최소값을 추가하고
    if plant[m] != 0 and animal[m] != 1:        # 식물일 경우의 수가 있다면
        ma += 1                                 # 최대값을 추가하고
print(mi, ma)                                   # 정답을 출력한다