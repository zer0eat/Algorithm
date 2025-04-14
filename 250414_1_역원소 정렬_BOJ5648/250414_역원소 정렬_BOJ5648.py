# 역원소 정렬_BOJ5648

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
num = []                            # 숫자를 저장할 리스트를 생성하고
while 1:                            # 숫자를 더 이상 input 하지 못할 때까지 반복해서
    try:                            # 숫자가 있다면
        tmp = list(input().split()) # 숫자를 리스트로 input받고
        num += tmp                  # num리스트에 더해준다
    except:                         # 숫자가 없다면
        break                       # while문을 종료한다
N = num.pop(0)                      # 숫자의 개수를 리스트에서 빼서 저장하고
ans = []                            # 정답을 저장할 리스트를 생성해서
for n in range(int(N)):             # 숫자의 수를 반복해서
    A = num[n][::-1]                # 숫자를 뒤집고
    ans.append(int(A))              # ans에 append한다
ans.sort()                          # 오름차순으로 정렬하고
for a in ans:                       # ans의 원소를 반복해서
    print(a)                        # 원소를 하나씩 출력한다