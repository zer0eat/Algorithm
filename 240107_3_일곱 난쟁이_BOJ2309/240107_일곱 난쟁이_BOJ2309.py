# 일곱 난쟁이_BOJ2309

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
dwarf = [int(input()) for _ in range(9)]        # 난쟁이의 키를 input 받고
dwarf.sort()                                    # 난쟁이의 키를 오름차순으로 정렬한다
total = sum(dwarf)                              # 난쟁이의 키의 합을 더해주고
for i in range(8):                              # 1부터 8까지 난쟁이를 반복하고
    for j in range(i+1, 9):                     # i부터 9까지 난쟁이를 반복해서
        if total - dwarf[i] - dwarf[j] == 100:  # i와 j 난쟁이를 뺏을 때 키의 합이 100이라면
            for k in range(9):                  # 난쟁이를 반복해서
                if k != i and k != j:           # i와 j가 아닌 경우에만
                    print(dwarf[k])             # 난쟁이의 키를 출력하고
            quit()                              # 종료한다