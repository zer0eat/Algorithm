# 이전순열_BOJ10973

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # 순열의 크기를 input받고
find = list(map(int, input().split()))                          # 대상 순열을 input 받는다
for i in range(N-1, 0, -1):                                     # 순열을 뒤에서부터 반복해서
    if find[i] < find[i-1]:                                     # i번째 숫자보다 i-1번째 숫자가 더 큰 경우에
        flag = i-1                                              # i-1을 flag에 저장하고
        break                                                   # for문을 break
else:                                                           # for문을 마쳤다면
    print(-1)                                                   # 이전 순열이 없으므로 -1을 출력하고
    quit()                                                      # 종료한다
for i in range(N-1, 0, -1):                                     # 순열을 뒤에서부터 반복해서
    if find[flag] > find[i]:                                    # flag보다 작은 숫자가 나온다면
        find[flag], find[i] = find[i], find[flag]               # 두 숫자의 위치를 바꿔준 후
        break                                                   # for문을 break
find = find[:flag+1] + sorted(find[flag+1:], reverse=True)      # find를 flag인덱스까지는 그냥 두고 그 뒤로는 내림차순 정렬한다
print(*find)                                                    # flag에 저장된 이전 순열을 출력한다