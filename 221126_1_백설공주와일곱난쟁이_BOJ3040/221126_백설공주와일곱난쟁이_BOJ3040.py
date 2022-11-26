# 백설공주와일곱난쟁이_BOJ3040

# import.txt 열기
import sys
sys.stdin = open('input.txt')

def snowwhite(n):
    if n == 9:                              # 모든 요소에 대해 비트를 결정했을 때
        if sum(bit) == 7:                   # bit의 합이 7인 경우에만
            sum100 = 0                      # 숫자의 합을 저장할 변수를 생성하고
            for b in range(len(bit)):       # 비트를 반복해서
                if bit[b]:                  # 해당 인덱스의 비트가 1인 겨웅에만
                    sum100 += dwarf[b]      # 변수에 숫자를 저장한다
            else:                           # 반복을 마친 후
                if sum100 == 100:           # 숫자의 합이 100인 경우에만
                    ans.append(bit[:])      # ans에 비트를 append 한다
        return                              
    bit[n] = 1                              # 비트를 1로 저장하고
    snowwhite(n+1)                          # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다
    bit[n] = 0                              # 비트를 0으로 저장하고
    snowwhite(n+1)                          # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다

# input 받기
dwarf = []                                  # 난쟁이의 모자를 저장한 빈 리스트 생성
for _ in range(9):                          # 9명의 난쟁이를 반복해서
    N = int(sys.stdin.readline())           # 모자에 적힌 숫자를 input 받아
    dwarf.append(N)                         # dwarf 리스트에 append

ans = []                                    # 모자의 합이 100이 되는 경우의 수를 저장할 빈 리스트
bit = [0]*9                                 # 경우의 수를 확인하기 위한 bit 생성
snowwhite(0)                                # 7명의 숫자의 합이 100이 되는 경우를 구하기 위한 함수

B = ans.pop()                               # ans에서 합이 100이 되는 경우의 bit를 pop 한 후
for b in range(len(B)):                     # bit를 반복해서
    if B[b]:                                # 해당 인덱스의 bit가 1이면
        print(dwarf[b])                     # 난쟁이의 모자의 숫자를 출력한다