# solvedac_BOJ18110

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

def round(num):
    if num - math.floor(num) >= 0.5:    # num에서 정수를 뺀 값이 0.5 이상이면
        num = math.floor(num) + 1       # num을 소수 첫번째에서 반올림한 수로 저장
    else:                               # num에서 정수를 뺀 값이 0.5 미만이면
        num = math.floor(num)           # num을 소수 첫번째에서 버림한 수로 저장 
    return num                          # num을 return

# input 받기
N = int(input())                        # 의견의 수를 input받고
if N == 0:                              # 의견의 수가 0이라면
    print(0)                            # 0을 출력하고
    quit()                              # 종료한다
ans = []                                # 의견을 저장할 리스트를 생성하고
for i in range(N):                      # 의견의 수를 반복해서
    ans.append(int(input()))            # ans에 의견을 append
ans.sort()                              # 의견을 오름차순으로 정렬해서
for i in range(round(N*0.15)):          # 30% 절사평균을 위해 상위 15% 반올림해서 
    ans.pop()                           # 해당하는 의견을 삭제한다
ans.sort(reverse=True)                  # 의견을 내림차순으로 정렬해서
for i in range(round(N*0.15)):          # 30% 절사평균을 위해 하위 15% 반올림해서
    ans.pop()                           # 해당하는 의견을 삭제한다
print(round(sum(ans)/len(ans)))         # 난이도를 출력한다