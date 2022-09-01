# 의석이의세로로말해요_5356.py

# input.txt 열기
import sys
sys.stdin = open('input.txt')

#  input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스 반복
    arr = [list(input()) for n in range(5)]         # 5줄을 문자열을 arr에 받음

    long = 0                                        # 가장 긴 길이를 저장할 변수를 만들고
    for a in arr:                                   # 한줄씩 반복해서
        if len(a) > long:                           # 가장 long보다 긴줄이 나오면
            long = len(a)                           # 긴줄의 길이를 long에 저장

    for b in range(len(arr)):                       # 한줄씩 반복해서
        if len(arr[b]) < long:                      # long보다 짧은 줄에는
            for c in range(long-len(arr[b])):       # 부족한 만큼 반복하여
                arr[b].append('')                   # '' 를추가한다

    new = []                                        # 새로운 리스트를 만들고
    for i in range(long):                           # 열을 반복하고
        for j in range(5):                          # 행을 반복하여
            new.append(arr[j][i])                   # 세로로 new에 append

    print(f'#{t+1} ', end= '')                      # 한줄로 띄어쓰기 없이 출력
    print(*new, sep='')
