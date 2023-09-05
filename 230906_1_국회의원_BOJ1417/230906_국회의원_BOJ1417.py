# 국회의원_BOJ1417

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 후보의 수를 input 받고
precident = int(input())                    # 다솜이의 득표수를 저장할 변수를 생성한다
if N == 1:                                  # 후보가 1이라면 무조건 다솜이가 당선이므로
    print(0)                                # 매수해야하는 사람을 0으로 출력하고
    quit()                                  # 종료한다
lst = [int(input()) for _ in range(N-1)]    # 다솜이를 제외한 후보의 득표수를 input 받아 리스트에 저장하고
lst.sort(reverse=True)                      # 리스트를 내림차순으로 정렬한다
cnt = 0                                     # 매수해야하는 사람의 수를 저장할 변수를 생성하고
while precident <= lst[0]:                  # 다솜이의 득표수가 나머지 최다 득표자보다 커질때까지 반복해서
    lst[0] -= 1                             # 최다득표자의 표를 하나 감소하나
    precident += 1                          # 다솜이의 표를 하나 증가 시킨 후
    cnt += 1                                # 매수자의 수를 하나 추가한다
    lst.sort(reverse=True)                  # 후보자 리스트를 내림차순 정렬한다
print(cnt)                                  # 다솜이가 매수해야 하는 사람의 최솟값을 출력한다