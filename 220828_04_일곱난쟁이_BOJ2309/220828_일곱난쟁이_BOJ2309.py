# 일곱난쟁이_BOJ2309

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
dwarf = []                                                      # 난쟁이의 키를 저장할 리스트
for _ in range(9):                                              # 9명의 난쟁이를 반복하여
    dwarf.append(int(input()))                                  # dwarf에 키를 append 한다

# 버블 정렬
for i in range(8):                                              # 버블솔트하여 키를 오름차순으로 정렬해준다
    for j in range(8-i):
        if dwarf[j] > dwarf[j + 1]:
            dwarf[j], dwarf[j + 1] = dwarf[j + 1], dwarf[j]

witch = []                                                      # 마녀의 가짜 난쟁이의 인덱스를 저장하기 위한 리스트
for i in range(len(dwarf)):                                     # dwarf에 저장된 난쟁이의 수 만큼 반복할 때
    for j in range(len(dwarf)):                                 # dwarf에 저장된 난쟁이의 수 만큼 반복할 때
        if i != j:                                              # i와 j가 같은 난쟁이가 아니면
            if sum(dwarf) - dwarf[i] - dwarf[j] == 100:         # 두명의 난쟁이를 제외한 키의 합이 100일 때
                witch.append(j)                                 # 마녀의 가짜 난쟁이를 witch 리스트에 인덱스를 저장(뒤에 있는 난쟁이 부터 저장해서 인덱스가 꼬이지 않게)
                witch.append(i)                                 # 마녀의 가짜 난쟁이를 witch 리스트에 인덱스를 저장
                break                                           # 색출 완료했으니 반복문 종료
    if len(witch) != 0:                                         # 가짜 난쟁이를 찾으면 반복문 종료
        break

dwarf.pop(witch[0])                                             # dwarf 리스트에서 가짜 난쟁이 제외(뒤에 있는 난쟁이 부터 제거해서 인덱스가 꼬이지 않게)
dwarf.pop(witch[1])                                             # dwarf 리스트에서 가짜 난쟁이 제외

for i in dwarf:
    print(i)