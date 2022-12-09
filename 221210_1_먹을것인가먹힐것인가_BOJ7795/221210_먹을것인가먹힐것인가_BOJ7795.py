# 먹을것인가먹힐것인가_BOJ7795

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                               # 테스트 케이스
for t in range(T):                                          # 테스트 케이스를 반복해서
    A, B = map(int, sys.stdin.readline().split())           # A 생명체의 수 / B 생명체의 수
    Alst = list(map(int, sys.stdin.readline().split()))     # Alst A 생명체의 크기를 리스트로 input
    Blst = list(map(int, sys.stdin.readline().split()))     # Blst B 생명체의 크기를 리스트로 input
    Aeat = dict()                                           # A 생명체가 먹을 수 있는 B 생명체의 수를 딕셔너리 형태로 저장하기 위해 빈 딕셔너리 생성

    Alst.sort()                                             # Alst 오름차순으로 정렬
    Blst.sort()                                             # Blst 오름차순으로 정렬

    end = 0                                                 # A 생명체가 잡아먹지 못한 B 생명체의 인덱스를 저장하기 위한 변수
    cnt = 0                                                 # 잡아먹은 B 생명체의 수를 저장하기 위한 변수

    for a in Alst:                                          # Alst를 반복해서
        if Aeat.get(a):                                     # Aeat에 잡아먹은 정보가 저장되어 있다면
            pass                                            # pass
        else:                                               # 그렇지 않다면
            for b in range(end, len(Blst)):                 # end부터 Blst 끝까지 반복해서
                if a > Blst[b]:                             # A 생명체보다 B 생명체가 작으면
                    cnt += 1                                # cnt에 1을 추가
                else:                                       # 그렇지 않다면
                    Aeat[a] = cnt                           # A 생명체를 key로 잡아먹은 숫자를 value로 딕셔너리 생성
                    end = b                                 # end를 잡아먹지 못한 마지막 B 인덱스로 저장
                    break                                   # for문 break
            else:                                           # B 생명체를 모두 잡아먹었다면
                Aeat[a] = cnt                               # A 생명체를 key로 잡아먹은 숫자를 value로 딕셔너리 생성
                end = b+1                                   # end를 Blst의 수로 저장

    ans = 0                                                 # 총 잡아먹은 수를 저장할 변수 생성
    for a in Alst:                                          # Alst를 반복해서
        ans += Aeat[a]                                      # ans에 잡아먹은 숫자를 더한 후
    else:                                                   # 반복이 끝났다면
        print(ans)                                          # ans를 출력한다
