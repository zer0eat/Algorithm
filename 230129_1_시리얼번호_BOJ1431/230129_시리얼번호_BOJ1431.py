# 시리얼번호_BOJ1431

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())                       # 기타의 개수
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    # 기타의 시리얼 넘버중 숫자를 확인하기 위한 리스트 생성
serial = []                                                 # 기타의 시리얼 넘버를 저장하기 위한 리스트 생성
info = []                                                   # 시리얼 넘버의 정보를 저장하기 위한 리스트 생성
for i in range(N):                                          # 기타의 개수를 반복해서
    A = sys.stdin.readline().strip()                        # A에 시리얼 넘버를 input 받는다
    serial.append(A)                                        # serial 리스트에 A를 append하고
    x = len(A)                                              # x에 A의 길이
    y = 0                                                   # y를 생성하고
    for a in A:                                             # 시리얼 넘버를 반복해서
        if a in num:                                        # 숫자라면
            y += int(a)                                     # 해당 숫자만큼 y에 더한다
    z = i                                                   # z에는 serial 리스트에 저장된 인덱스를 저장한 뒤
    info.append([x,y,z])                                    # info 리스트에 [길이,숫자의합,인덱스]를 append 한다
info.sort()                                                 # info를 오름차순 정렬한 뒤
cnt = 0                                                     # 길이와 합이 같은 시리얼 넘버의 수를 저장하기 위한 변수 생성
for s in range(N):                                          # 기타의 수만큼 반복해서
    if cnt > 0:                                             # 길이와 합이 같은 시러얼 넘버의 수가 있다면
        cnt -= 1                                            # cnt에서 1을 빼고
        pass                                                # 패스한다
    elif s == N-1:                                          # 마지막 info를 탐색중이면
        print(serial[info[s][2]])                           # s info에 해당하는 시리얼넘버를 출력한다
    elif info[s][0] < info[s+1][0]:                         # s info에 해당되는 시리얼 넘버가 다음 info의 시리얼 넘버보다 짧다면
        print(serial[info[s][2]])                           # s info에 해당하는 시리얼넘버를 출력한다
    else:                                                   # s info와 그 다음 info의 시리얼넘버 길이가 같다면
        if info[s][1] < info[s + 1][1]:                     # s info에 해당되는 시리얼 넘버의 합이 다음 info의 시리얼 넘버의 합보다 작다면
            print(serial[info[s][2]])                       # s info에 해당하는 시리얼넘버를 출력한다
        else:                                               # s info와 그 다음 info의 시리얼넘버 숫자의 합이 같다면
            tmp = [serial[info[s][2]], serial[info[s + 1][2]]]    # tmp라는 리스트를 s와 s+1에 해당하는 시리얼 넘버를 넣어 생성한다
            for s2 in range(s+1, N-1):                      # s+1부터 N-2까지 탐색을 해서
                if info[s2][0] < info[s2+1][0]:             # s2 info에 해당되는 시리얼 넘버가 다음 info의 시리얼 넘버보다 짧다면
                    break                                   # for문을 break
                else:                                       # s2 info와 그 다음 info의 시리얼넘버 길이가 같다면
                    if info[s2][1] < info[s2 + 1][1]:       # s2 info에 해당되는 시리얼 넘버의 합이 다음 info의 시리얼 넘버의 합보다 작다면
                        break                               # for문을 break
                    else:                                   # s2 info와 그 다음 info의 시리얼넘버 숫자의 합이 같다면
                        tmp.append(serial[info[s2+1][2]])   # tmp 리스트에 s2+1 info에 해당하는 시리얼넘버를 append한다
            tmp.sort()                                      # for문이 끝난 후에 tmp를 오름차순 정렬하여
            for t in tmp:                                   # tmp에 있는 시러얼 넘버를 반복해서
                print(t)                                    # 시리얼 넘버를 출력하고
            cnt += (len(tmp)-1)                             # 길이와 합이 같은 시리얼 넘버의 수에 tmp의 길이보다 1 작은수를 넣는다